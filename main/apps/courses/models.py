from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CoursesManager(models.Manager):
    def add(self, name, description):
        messages = []

        if len(name) < 1:
            messages.append('You must enter a course name')
        if len(description) < 1:
            messages.append('You must enter a course description')

        if len(messages) > 0:
            return False, messages
        else:
            course = Courses.coursesManager.create(name=name,description=description)
            return (True, course)

class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    coursesManager = CoursesManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
