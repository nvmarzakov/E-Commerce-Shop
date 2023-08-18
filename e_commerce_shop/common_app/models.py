from django.db import models


class ContactSubmission(models.Model):
    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    subject = models.CharField(
        max_length=200,
    )

    message = models.TextField(
        blank=False,
        null=False,
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.subject} by {self.first_name} {self.last_name}'
