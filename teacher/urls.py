from django.urls import path
from . import views

urlpatterns = [
    path('teacher_dashboard/', views.teacher_dashboard, name="teacher_dashboard"),
    path('quiz/<int:quiz_id>/add-question/', views.create_question, name='create_question'),
]
