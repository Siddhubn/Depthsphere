from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, QuizQuestion, Result
from hod.models import SubjectModel, ClassModel, TeacherAssignment
from users.models import CustomUser


@login_required
def teacher_dashboard(request):
    if request.user.role != 'Teacher':
        return redirect('login')

    assignments = TeacherAssignment.objects.filter(teacher=request.user)
    quizzes = Quiz.objects.filter(subject__in=assignments.values_list('subject', flat=True))

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create_quiz':
            subject = SubjectModel.objects.get(id=request.POST['subject_id'])
            assigned_class = ClassModel.objects.get(id=request.POST['class_id'])
            quiz = Quiz.objects.create(
                title=request.POST['title'],
                subject=subject,
                assigned_class=assigned_class,
                scheduled_time=request.POST['scheduled_time']
            )
            messages.success(request, f"Quiz '{quiz.title}' created successfully.")

        elif action == 'view_results':
            quiz = Quiz.objects.get(id=request.POST['quiz_id'])
            results = Result.objects.filter(quiz=quiz)
            return render(request, 'teacher/view_results.html', {'results': results, 'quiz': quiz})

        elif action == 'forward_results':
            quiz = Quiz.objects.get(id=request.POST['quiz_id'])
            results = Result.objects.filter(quiz=quiz)
            # Logic for forwarding results to HOD can be implemented here
            messages.success(request, f"Results for '{quiz.title}' forwarded to HOD successfully.")

        return redirect('teacher_dashboard')

    return render(request, 'teacher/teacher_dashboard.html', {
        'assignments': assignments,
        'quizzes': quizzes
    })

@login_required
def create_question(request, quiz_id):
    if request.user.role != 'Teacher':
        return redirect('login')

    # Ensure the quiz belongs to the logged-in teacher
    quiz = get_object_or_404(Quiz, id=quiz_id, subject__teacherassignment__teacher=request.user)

    if request.method == 'POST':
        question_text = request.POST['question_text']
        option_a = request.POST['option_a']
        option_b = request.POST['option_b']
        option_c = request.POST['option_c']
        option_d = request.POST['option_d']
        correct_option = request.POST['correct_option']
        points = request.POST.get('points', 1)

        # Create the question
        QuizQuestion.objects.create(
            quiz=quiz,
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option,
            points=points
        )

        messages.success(request, "Question added successfully.")
        return redirect('create_question', quiz_id=quiz.id)

    return render(request, 'teacher/create_question.html', {'quiz': quiz})
