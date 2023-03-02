from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    login = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.TextField(max_length=20, null=True, blank=True)
    corp_email = models.EmailField(max_length=40, null=True, blank=True)
    last_seen = models.DateField(null=True, blank=True)
    length_of_last_session_minute = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Login: {self.login}, Company: {self.company}, Last seen: {self.last_seen}'



class BugReport(models.Model):
    login = models.ManyToManyField(User)
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    date_of_send = models.DateField()

    def __str__(self):
        return f'Title: {self.title}, ' \
               f'description: {self.description}, ' \
               f'date: {self.date_of_send}, ' \
               f'sender: {self.login}'



class Workplace(models.Model):
    owner = models.ManyToManyField(User)
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'Owner:{self.owner}, ' \
               f'title: {self.title}, ' \
               f'description: {self.description}'

class TaskTracker(models.Model):
    DONE = "DE"
    PROGRESS = "PS"
    REVIEW = "RW "
    REJECT = "RT "
    WorkStatus = [
        (DONE, 'Done'),
        (PROGRESS, 'Progress'),
        (REVIEW, 'Review'),
        (REJECT, 'Reject'),
    ]

    owner = models.ManyToManyField(User)
    workplace_id = models.ForeignKey(Workplace, null=True, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=WorkStatus,
        default=PROGRESS,
    )
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    date_of_create = models.DateField()
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'ID: {self.id}, ' \
               f'owner: {self.owner}, ' \
               f'title: {self.title}, ' \
               f'description: {self.description}, ' \
               f'date of create: {self.date_of_create}, ' \
               f'deadline: {self.deadline} '
