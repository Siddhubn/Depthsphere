from django.contrib import admin
from .models import Quiz,Attempt

class QuizAdmin(admin.ModelAdmin): 
    list_display = ('title', 'subject_id', 'class_id', 'scheduled_time')
    search_fields = ('title',)
    list_filter = ('class_id', 'subject_id')

admin.site.register(Quiz, QuizAdmin)

class AttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'answers', 'score')
    search_fields = ('student',)
    list_filter = ('quiz', 'score')

admin.site.register(Attempt, AttemptAdmin)
