from datetime import timedelta

from django.db import models


class Relocation(models.Model):

    STATUS_CHOICES = [
        ("Planning", "Planning"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    PROPERTY_CHOICES = [
        ("1RK", "1RK"),
        ("1BHK", "1BHK"),
        ("2BHK", "2BHK"),
        ("3BHK", "3BHK"),
        ("Villa", "Villa"),
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    current_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)

    move_date = models.DateField()

    household_size = models.PositiveIntegerField(default=1)

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_CHOICES,
        default="2BHK",
    )

    assigned_ops = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Planning",
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} ({self.current_city} → {self.destination_city})"

    def create_default_tasks(self):

        # Prevent duplicate task creation
        if self.tasks.exists():
            return

        default_tasks = [

            ("Planning", "Collect Customer Requirements"),

            ("Planning", "Assign Operations Executive"),

            ("Property Search", "Apartment Search"),

            ("Property Search", "Finalize Rental Agreement"),

            ("Packers & Movers", "Book Packers & Movers"),

            ("Utilities", "Setup Utilities"),

            ("Documentation", "Address Change Documentation"),

            ("Move Day", "Coordinate Moving Day"),

            ("Post Move Support", "Verify Successful Relocation"),

            ("Closure", "Close Relocation"),

        ]

        total = len(default_tasks)

        for sequence, (workflow, title) in enumerate(default_tasks, start=1):

            Task.objects.create(
                relocation=self,
                sequence=sequence,
                workflow=workflow,
                title=title,
                status="Pending",
                due_date=self.move_date - timedelta(days=(total - sequence)),
            )


class Task(models.Model):

    WORKFLOW_CHOICES = [
        ("Planning", "Planning"),
        ("Property Search", "Property Search"),
        ("Packers & Movers", "Packers & Movers"),
        ("Utilities", "Utilities"),
        ("Documentation", "Documentation"),
        ("Move Day", "Move Day"),
        ("Post Move Support", "Post Move Support"),
        ("Closure", "Closure"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    relocation = models.ForeignKey(
        Relocation,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    sequence = models.PositiveIntegerField()

    workflow = models.CharField(
        max_length=40,
        choices=WORKFLOW_CHOICES
    )

    title = models.CharField(max_length=200)

    due_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    notes = models.TextField(blank=True)

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["sequence"]

    def __str__(self):
        return f"{self.sequence}. {self.title}"