from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ClassModel, SubjectModel, TeacherAssignment
from users.models import CustomUser

@login_required
def hod_dashboard(request):
    if request.user.role != 'HOD':
        return redirect('login')

    classes = ClassModel.objects.all()
    subjects = SubjectModel.objects.all()
    teachers = CustomUser.objects.filter(role='Teacher')
    assignments = TeacherAssignment.objects.all()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create_class':
            try:
                ClassModel.objects.create(
                    name=request.POST['name'],
                    semester=request.POST['semester'],
                    section=request.POST['section']
                )
                messages.success(request, "Class created successfully!")
            except Exception as e:
                messages.error(request, f"Error creating class: {str(e)}")

        elif action == 'create_subject':
            try:
                assigned_class = ClassModel.objects.get(id=request.POST['assigned_class'])
                SubjectModel.objects.create(
                name=request.POST['name'],
                assigned_class=assigned_class  # Correct field name
                )
                messages.success(request, "Subject created successfully!")
            except Exception as e:
                messages.error(request, f"Error creating subject: {str(e)}")

        elif action == 'assign_teacher':
            try:
                teacher = CustomUser.objects.get(id=request.POST['teacher'])
                subject = SubjectModel.objects.get(id=request.POST['subject'])
                assigned_class = ClassModel.objects.get(id=request.POST['assigned_class'])

                # Check if the assignment already exists
                if TeacherAssignment.objects.filter(teacher=teacher, subject=subject, assigned_class=assigned_class).exists():
                    messages.error(request, "This assignment already exists.")
                else:
                    TeacherAssignment.objects.create(
                    teacher=teacher,
                    subject=subject,
                    assigned_class=assigned_class
                    )
                    messages.success(request, "Teacher assigned successfully.")
            except (CustomUser.DoesNotExist, SubjectModel.DoesNotExist, ClassModel.DoesNotExist):
                messages.error(request, "Invalid data provided. Please try again.")


        return redirect('hod_dashboard')

    context = {
        'classes': classes,
        'subjects': subjects,
        'teachers': teachers,
        'assignments': assignments,
    }
    return render(request, 'hod/hod_dashboard.html', context)
