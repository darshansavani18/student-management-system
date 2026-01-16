from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher
from django.contrib.auth import logout
from .forms import StudentForm, TeacherForm
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # later dashboard
        else:
            return render(request, 'school/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'school/login.html')

@login_required(login_url="login")
def dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()

    context = {
        "total_students": total_students,
        "total_teachers": total_teachers,
    }
    return render(request, "school/dashboard.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username,password=password)

            student = form.save(commit=False)
            student.user = user 
            student.save()

            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, 'school/add_student.html', {'form': form})

def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username,password=password)

            teacher = form.save(commit=False)
            teacher.user = user 
            teacher.save()

            return redirect('dashboard')
    else:
        form = TeacherForm()
    return render(request, 'school/add_teacher.html', {'form': form})

def view_students(request): 
    query = request.GET.get('q','').strip()

    students = Student.objects.select_related('user').all()

    if query:
        students = students.filter(
            Q(user__username__icontains=query) |
            Q(roll_number__icontains=query) |
            Q(class_name__icontains=query)
        )

    return render(request, 'school/view_students.html', {
       'students': students,
       'query': query
    })

def delete_student(request, id):
    student = Student.objects.get(id=id)

    # delete related user also
    student.user.delete()

    return redirect('view_students')

def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.roll_number = request.POST.get('roll_number')
        student.class_name = request.POST.get('class_name')
        student.section = request.POST.get('section')
        student.gender = request.POST.get('gender')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.address = request.POST.get('address')
        student.save()

        return redirect('view_students')

    return render(request, 'school/update_student.html', {
        'student': student
    })

def view_teachers(request): 
    query = request.GET.get('q','').strip()

    teachers = Teacher.objects.select_related('user').all()

    if query:
        teachers = Teacher.filter(
            Q(user__username__icontains=query) |
            Q(full_name__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, 'school/view_teachers.html', {
       'teachers': teachers,
       'query': query
    })