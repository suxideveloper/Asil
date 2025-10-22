from django.contrib import admin
from .models import Teacher, Course, Student, GraduatedStudent, Achievement


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'is_lead_teacher', 'email', 'created_at']
    list_filter = ['is_lead_teacher', 'created_at']
    search_fields = ['name', 'title', 'email']
    list_editable = ['is_lead_teacher']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'duration_weeks', 'price', 'is_active']
    list_filter = ['is_active', 'teacher', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'price']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade_level', 'enrollment_date', 'is_active']
    list_filter = ['grade_level', 'is_active', 'enrollment_date']
    search_fields = ['name', 'email']
    list_editable = ['is_active']
    filter_horizontal = ['courses']


@admin.register(GraduatedStudent)
class GraduatedStudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'university_name', 'major', 'graduation_year']
    list_filter = ['graduation_year', 'university_name']
    search_fields = ['name', 'university_name', 'major']
    ordering = ['-graduation_year', 'name']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_achieved', 'is_featured']
    list_filter = ['is_featured', 'date_achieved']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']