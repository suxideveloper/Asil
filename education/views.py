from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Course, Student, GraduatedStudent, Achievement


def home(request):
    """Home page view"""
    lead_teacher = Teacher.objects.filter(is_lead_teacher=True).first()
    featured_achievements = Achievement.objects.filter(is_featured=True)[:3]
    recent_graduates = GraduatedStudent.objects.all()[:6]
    
    context = {
        'lead_teacher': lead_teacher,
        'featured_achievements': featured_achievements,
        'recent_graduates': recent_graduates,
    }
    return render(request, 'education/home.html', context)


def about(request):
    """About page view"""
    teachers = Teacher.objects.all()
    achievements = Achievement.objects.all()[:10]
    
    context = {
        'teachers': teachers,
        'achievements': achievements,
    }
    return render(request, 'education/about.html', context)


def teachers(request):
    """Teachers page view"""
    lead_teacher = Teacher.objects.filter(is_lead_teacher=True).first()
    other_teachers = Teacher.objects.filter(is_lead_teacher=False)
    
    context = {
        'lead_teacher': lead_teacher,
        'other_teachers': other_teachers,
    }
    return render(request, 'education/teachers.html', context)


def courses(request):
    """Courses page view"""
    active_courses = Course.objects.filter(is_active=True)
    
    context = {
        'courses': active_courses,
    }
    return render(request, 'education/courses.html', context)


def students(request):
    """Current students page view"""
    active_students = Student.objects.filter(is_active=True)
    
    context = {
        'students': active_students,
    }
    return render(request, 'education/students.html', context)


def graduates(request):
    """Graduated students page view"""
    graduates = GraduatedStudent.objects.all()
    
    context = {
        'graduates': graduates,
    }
    return render(request, 'education/graduates.html', context)


def contact(request):
    """Contact page view"""
    lead_teacher = Teacher.objects.filter(is_lead_teacher=True).first()
    
    context = {
        'lead_teacher': lead_teacher,
    }
    return render(request, 'education/contact.html', context)