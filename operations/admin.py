from django.contrib import admin
from .models import Relocation, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0

    fields = (
        "sequence",
        "workflow",
        "title",
        "status",
        "due_date",
        "notes",
    )

    readonly_fields = (
        "sequence",
        "workflow",
        "title",
    )

    ordering = (
        "sequence",
    )


@admin.register(Relocation)
class RelocationAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "current_city",
        "destination_city",
        "move_date",
        "assigned_ops",
        "status",
    )

    list_filter = (
        "status",
        "current_city",
        "destination_city",
    )

    search_fields = (
        "customer_name",
        "phone",
        "assigned_ops",
    )

    fieldsets = (

        ("Customer", {
            "fields": (
                "customer_name",
                "phone",
                "email",
            )
        }),

        ("Relocation", {
            "fields": (
                "current_city",
                "destination_city",
                "move_date",
                "household_size",
                "property_type",
            )
        }),

        ("Operations", {
            "fields": (
                "assigned_ops",
                "status",
                "notes",
            )
        }),

    )

    inlines = [TaskInline]