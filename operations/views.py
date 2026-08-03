from datetime import date, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Relocation, Task
from .forms import RelocationForm








def calculate_risk(relocation):

    tasks = list(relocation.tasks.all())
    total_tasks = len(tasks)
    completed_tasks = sum(task.status == "Completed" for task in tasks)

    pending_tasks = total_tasks - completed_tasks

    days_left = (relocation.move_date - date.today()).days

    if pending_tasks >= 6 and days_left <= 3:

        return (
            "High Risk",
            "danger",
            "Many workflow tasks are still pending and the relocation date is very close."
        )

    elif pending_tasks >= 3 or days_left <= 7:

        return (
            "Medium Risk",
            "warning",
            "Some important workflow tasks are still pending."
        )

    else:

        return (
            "Low Risk",
            "success",
            "Workflow is progressing on schedule."
        )


def attach_risk(relocation):

    risk, badge, reason = calculate_risk(relocation)

    relocation.risk = risk
    relocation.risk_badge = badge
    relocation.risk_reason = reason

    return relocation














# =====================================================
# Dashboard
# =====================================================

@login_required
def dashboard(request):

    today = date.today()

    risk_relocations = Relocation.objects.exclude(
        status="Completed"
    ).prefetch_related("tasks")

    total_risks = sum(
        calculate_risk(relocation)[0] != "Low Risk"
        for relocation in risk_relocations
    )

    recent_relocations = Relocation.objects.order_by(
        "-created_at"
    )[:5]

    for relocation in recent_relocations:
        attach_risk(relocation)

    context = {

        "total_relocations": Relocation.objects.count(),

        "active_relocations": Relocation.objects.exclude(
            status="Completed"
        ).count(),

        "completed_relocations": Relocation.objects.filter(
            status="Completed"
        ).count(),

        "pending_tasks": Task.objects.filter(
            status="Pending"
        ).count(),

        "total_risks": total_risks,

        "today_tasks": Task.objects.filter(
            due_date=today
        ).count(),

        "planning": Relocation.objects.filter(
            status="Planning"
        ).count(),

        "progress": Relocation.objects.filter(
            status="In Progress"
        ).count(),

        "completed": Relocation.objects.filter(
            status="Completed"
        ).count(),

        "recent_relocations": recent_relocations,

    }

    return render(
        request,
        "operations/dashboard.html",
        context
    )


# =====================================================
# Relocations
# =====================================================

@login_required
def relocations(request):

    relocations = Relocation.objects.order_by("-created_at")

    for relocation in relocations:
        attach_risk(relocation)

    return render(
        request,
        "operations/relocations.html",
        {
            "relocations": relocations
        }
    )


# =====================================================
# New Relocation
# =====================================================

@login_required
def new_relocation(request):

    if request.method == "POST":

        form = RelocationForm(request.POST)

        if form.is_valid():

            relocation = form.save()

            return redirect(
                "task_list",
                pk=relocation.id
            )

    else:

        form = RelocationForm()

    return render(
        request,
        "operations/new_relocation.html",
        {
            "form": form
        }
    )


# =====================================================
# Relocation Details
# =====================================================
@login_required
def relocation_detail(request, pk):

    relocation = get_object_or_404(
        Relocation,
        pk=pk
    )

    completed_tasks = relocation.tasks.filter(
        status="Completed"
    ).count()

    total_tasks = relocation.tasks.count()

    progress = 0

    if total_tasks > 0:

        progress = int(
            (completed_tasks / total_tasks) * 100
        )

    attach_risk(relocation)

    return render(
        request,
        "operations/relocation_detail.html",
        {
            "relocation": relocation,
            "completed_tasks": completed_tasks,
            "total_tasks": total_tasks,
            "progress": progress,

        }
    )

# =====================================================
# Workflow
# =====================================================

@login_required
def task_list(request, pk):

    relocation = get_object_or_404(
        Relocation,
        pk=pk
    )

    tasks = relocation.tasks.all()

    completed_tasks = tasks.filter(
        status="Completed"
    ).count()

    total_tasks = tasks.count()

    progress = 0

    if total_tasks > 0:

        progress = int(
            (completed_tasks / total_tasks) * 100
        )

    return render(
        request,
        "operations/task_list.html",
        {
            "relocation": relocation,
            "tasks": tasks,
            "completed_tasks": completed_tasks,
            "total_tasks": total_tasks,
            "progress": progress,
        }
    )


# =====================================================
# Update Task Status
# =====================================================

@login_required
@require_POST
def update_task_status(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    new_status = request.POST.get("status")

    if new_status in [

        "Pending",

        "In Progress",

        "Completed",

    ]:

        task.status = new_status
        task.save()

    return redirect(
        "task_list",
        pk=task.relocation.id
    )


# =====================================================
# Operations Queue
# =====================================================

@login_required
def operations_queue(request):

    today = date.today()

    today_relocations = Relocation.objects.filter(
        move_date=today
    ).order_by("created_at")

    upcoming_relocations = Relocation.objects.filter(
        move_date__gt=today,
        move_date__lte=today + timedelta(days=7)
    ).order_by("move_date")

    future_relocations = Relocation.objects.filter(
        move_date__gt=today + timedelta(days=7)
    ).order_by("move_date")

    for relocation in (
        list(today_relocations)
        + list(upcoming_relocations)
        + list(future_relocations)
    ):
        attach_risk(relocation)

    return render(
        request,
        "operations/operations_queue.html",
        {
            "today_relocations": today_relocations,
            "upcoming_relocations": upcoming_relocations,
            "future_relocations": future_relocations,
        }
    )


# =====================================================
# Analytics
# =====================================================

@login_required
def analytics(request):

    context = {

        "planning": Relocation.objects.filter(
            status="Planning"
        ).count(),

        "progress": Relocation.objects.filter(
            status="In Progress"
        ).count(),

        "completed": Relocation.objects.filter(
            status="Completed"
        ).count(),

        "total": Relocation.objects.count(),

    }

    return render(
        request,
        "operations/analytics.html",
        context
    )


@require_POST
def logout_user(request):
    logout(request)
    return redirect("login")
