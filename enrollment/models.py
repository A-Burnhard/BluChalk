from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Enrollment(models.Model):
    ACTIVE = 'active'
    COMPLETED = 'completed'
    DROPPED = 'dropped'
    
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (COMPLETED, 'Completed'),
        (DROPPED, 'Dropped'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    progress = models.PositiveIntegerField(default=0)  # Represented as a percentage.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    feedback = models.TextField(null=True, blank=True)  # Feedback from the student about the course.
    grade = models.FloatField(null=True, blank=True)  # Grade/Score of the student in the course.

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
