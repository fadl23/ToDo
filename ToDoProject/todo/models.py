from django.db import models
from django.contrib.auth.models import User  # Fix the import statement
from django.core.validators import MinValueValidator, MaxValueValidator

x = (('happy', 'Happy'), ('sad', 'Sad'))  # Update the choices for 'feelings'
class Todo(models.Model):
    task = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # productivity = models.ForeignKey(Productivity, on_delete=models.CASCADE, related_name='todo')

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['created']

class Productivity(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, blank=True, null=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    feelings = models.CharField(max_length=10, choices=x)  # Update the choices for 'feelings'
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='productivity')

    def __str__(self):
        return str(self.rating)

    # class Meta:
    #     ordering = ['created']


