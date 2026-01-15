from django.db import models
from django.contrib.auth.models import User

# =========================
# Teacher Model
# =========================
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# =========================
# Student Model
# =========================
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.roll_number}"
