# teacher/models.py
from django.db import models
from hod.models import SubjectModel, ClassModel
from users.models import CustomUser

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    assigned_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.subject.name}) - {self.assigned_class.name}"


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    points = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.question_text[:50]}... (Quiz: {self.quiz.title})"


class Result(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'Student'})
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}: {self.score}"
