from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    """Model for teachers in the education platform"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, help_text="e.g., Lead Teacher, Math Teacher")
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    is_lead_teacher = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_lead_teacher', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.title}"


class Course(models.Model):
    """Model for courses offered"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    duration_weeks = models.PositiveIntegerField(default=12)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title


class Student(models.Model):
    """Model for current students"""
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    grade_level = models.CharField(max_length=50, help_text="e.g., 11th Grade, 12th Grade")
    courses = models.ManyToManyField(Course, related_name='students', blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class GraduatedStudent(models.Model):
    """Model for students who have graduated and entered university"""
    name = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()
    university_name = models.CharField(max_length=200)
    major = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='graduated_students/', blank=True, null=True)
    testimonial = models.TextField(blank=True, help_text="Student's testimonial about their experience")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-graduation_year', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.university_name} ({self.graduation_year})"


class Achievement(models.Model):
    """Model for achievements and milestones"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_achieved = models.DateField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_achieved']
    
    def __str__(self):
        return self.title