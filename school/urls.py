from django.contrib import admin
from django.urls import path,include
from .views import add_student, login_view, dashboard,logout_view
from .views import add_teacher, view_students,delete_student,update_student,view_teachers,delete_teacher,update_teacher

urlpatterns = [
    path("",login_view, name="login"),
    path("login/", login_view, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("add-student/", add_student, name="add_student"),
    path("add-teacher/", add_teacher, name="add_teacher"),
    path("students/", view_students, name="view_students"),
    path("teachers/",view_teachers, name="view_teachers"),
    path("logout/", logout_view, name="logout"),
    path('student/update/<int:id>/', update_student, name='update_student'),
    path('student/delete/<int:id>/', delete_student, name='delete_student'),
    path('teacher/update/<int:id>/', update_teacher, name='update_teacher'),
    path('teacher/delete/<int:id>/', delete_teacher, name='delete_teacher'),
]

