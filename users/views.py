from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to role-based dashboard
            if user.role == 'HOD':
                return redirect('hod_dashboard')
            elif user.role == 'Teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'Student':
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'users/login.html')  # Update with the correct login template path

def create_login(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Create a user
        if username and password and role:
            try:
                # Check if user already exists
                if CustomUser.objects.filter(username=username).exists():
                    return render(request, "users/create_login.html", {
                        "error": "Username already exists."
                    })
                # Create user with role
                user = CustomUser.objects.create_user(
                    username=username, password=password, role=role
                )
                user.save()
                return redirect('/users/login')
            except Exception as e:
                return render(request, "users/create_login.html", {
                    "error": f"An error occurred: {str(e)}"
                })
        else:
            return render(request, "users/create_login.html", {
                "error": "All fields are required."
            })

    return render(request, "users/create_login.html")

def logout_view(request):
    logout(request)
    return redirect('login/')
