from django.db import models
from users.models import CustomUser

class ClassModel(models.Model):
    name = models.CharField(max_length=50)  # Class names should be unique
    semester = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - Semester: {self.semester}, Section: {self.section}"


class SubjectModel(models.Model):  
    name = models.CharField(max_length=100, unique=True)  
    assigned_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return f"{self.name} ({self.assigned_class})"


class TeacherAssignment(models.Model):
    teacher = models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role': 'Teacher'}, related_name="assignments")
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, related_name="teacher_assignments")
    assigned_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name="teacher_assignments")

    class Meta:
        unique_together = ('teacher', 'subject', 'assigned_class')  # Prevent duplicate assignments

    def __str__(self):
        return f"{self.teacher.username} - {self.subject.name} ({self.assigned_class.name})"
