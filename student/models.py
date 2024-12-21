from django.db import models
from teacher.models import Quiz
from users.models import CustomUser

class Attempt(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'Student'})
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answers = models.JSONField()
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    subject_id = models.IntegerField()
    class_id = models.IntegerField()
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.title
