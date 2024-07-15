from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentManager(BaseUserManager):
    def create_user(self, student_number, password=None, **extra_fields):
        if not student_number:
            raise ValueError("The Student Number field is required")
        user = self.model(student_number=student_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(student_number, password, **extra_fields)

class Student(AbstractBaseUser):
    student_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'student_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = StudentManager()

    def __str__(self):
        return self.student_number
from django.db import models






    # Add more fields as needed

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('natural_science', 'Natural Science'),
        ('social_science', 'Social Science'),
        ('maths', 'Mathematics'),
        ('english', 'English'),
        # Add more categories as needed
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
