from django.db import models
from django.contrib.auth.models import User

class Label(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)

    class Status(models.IntegerChoices):
        DEFAULT = 0
        ACTIVE = 1
        ARCHIVED = 2

    status = models.IntegerField(choices=Status.choices, null=False, default=Status.ACTIVE)
    description = models.CharField(max_length=150, null=True)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return "{}'s {}".format(self.user.username, self.title)


class Task(models.Model):
    title = models.CharField(max_length=100, null=False)

    class Status(models.IntegerChoices):
        ACTIVE = 1
        ARCHIVED = 2

    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    description = models.CharField(max_length=150, null=True)
    scheduled_for = models.DateTimeField(auto_now_add=False, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return "{}:{}".format(str(self.project), self.title)


class Activity(models.Model):
    start = models.DateTimeField(auto_now_add=False, null=False)
    end = models.DateTimeField(auto_now_add=False, null=True)

    notes = models.CharField(max_length=150, null=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return "{} - {}".format(str(self.task), self.start)
