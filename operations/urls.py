from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="operations/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),

    path(
        "logout/",
        views.logout_user,
        name="logout",
    ),

    # Dashboard
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    # Operations Queue
    path(
        "operations/",
        views.operations_queue,
        name="operations_queue"
    ),

    # Relocations
    path(
        "relocations/",
        views.relocations,
        name="relocations"
    ),

    # New Relocation
    path(
        "relocations/new/",
        views.new_relocation,
        name="new_relocation"
    ),

    # Relocation Details
    path(
        "relocation/<int:pk>/",
        views.relocation_detail,
        name="relocation_detail"
    ),

    # Workflow
    path(
        "relocation/<int:pk>/workflow/",
        views.task_list,
        name="task_list"
    ),

    # Update Task Status
    path(
        "task/<int:task_id>/update/",
        views.update_task_status,
        name="update_task_status"
    ),

    # Analytics
    path(
        "analytics/",
        views.analytics,
        name="analytics"
    ),

]
