from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    class Status(models.TextChoices):
        Unverified = 'Unverified', 'Unverified'
        Verified = 'Verified', 'Verified'

    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payee = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(
        max_length=16, 
        choices=Status.choices, 
        default=Status.Unverified
    )

    def __str__(self):
        return f'{self.timestamp} {self.payee} {self.amount}'