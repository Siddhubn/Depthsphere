from django.contrib import admin
from teacher.models import Quiz  # Using the shared Quiz model

class TeacherQuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'assigned_class', 'scheduled_time')
    search_fields = ('title',) 
    list_filter = ('subject', 'assigned_class', 'scheduled_time')

# You can reuse the Quiz model in the teacher context
admin.site.register(Quiz, TeacherQuizAdmin)
