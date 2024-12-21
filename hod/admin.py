from django.contrib import admin
from .models import ClassModel, SubjectModel

class ClassModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'section')
    search_fields = ('name', 'semester', 'section')
    list_filter = ('semester', 'section')

class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'assigned_class')
    search_fields = ('name',)
    list_filter = ('assigned_class',)

admin.site.register(ClassModel, ClassModelAdmin)
admin.site.register(SubjectModel, SubjectModelAdmin)
