from django.db import models
from User.models import Users

class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True)
    category_id = models.IntegerField(unique=True, serialize=True, primary_key=True)

    def __str__(self):
        return f'{self.category_name}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return f'{self.tag_name}'


class Task(models.Model):
    Task_id = models.IntegerField(unique=True, primary_key=True, serialize=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_expire_time = models.TimeField(null=False, blank=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=100, null=False)
    task_description = models.TextField(null=False, blank=False)
    task_status = models.BooleanField(default=True)
    tag_id = models.ManyToManyField(Tag, blank=True, related_name='tag')

    def __str__(self):
        return f'{self.task_title} - {self.task_description[:15]}... -{self.category_id.category_name}'
