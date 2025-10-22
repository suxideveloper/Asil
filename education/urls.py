from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teachers, name='teachers'),
    path('courses/', views.courses, name='courses'),
    path('students/', views.students, name='students'),
    path('graduates/', views.graduates, name='graduates'),
    path('contact/', views.contact, name='contact'),
]
