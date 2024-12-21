from django.shortcuts import render, redirect
from .models import Attempt
from teacher.models import Quiz

def student_dashboard(request):
    if request.user.role != 'Student':
        return redirect('login')

    quizzes = Quiz.objects.filter(assigned_class__in=request.user.class_set.all())
    attempts = Attempt.objects.filter(student=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'attempt_quiz':
             quiz = Quiz.objects.get(id=request.POST['quiz_id'])
             answers = {int(k): v for k, v in request.POST.items() if k.startswith('question_')}
             score = calculate_score(answers)
             Attempt.objects.create(
                  student=request.user,
                  quiz=quiz,
                  answers=answers,  # Save the answers for review if needed
                  score=score
                  )
             return redirect('student_dashboard')

    return render(request, 'student/student_dashboard.html', {'quizzes': quizzes, 'attempts': attempts})

from teacher.models import QuizQuestion

def calculate_score(answers):
    """
    Calculates the score for a quiz based on submitted answers.

    :param answers: A dictionary where keys are question IDs and values are selected options.
    :return: Total score as an integer.
    """
    score = 0

    # Example: Assume `answers` is a dictionary like {1: 'A', 2: 'B'}
    for question_id, selected_option in answers.items():
        try:
            question = QuizQuestion.objects.get(id=question_id)  # Fetch the question from the database
            if question.correct_option == selected_option:
                score += question.points  # Add the points for the question
        except QuizQuestion.DoesNotExist:
            continue  # Ignore invalid question IDs

    return score
