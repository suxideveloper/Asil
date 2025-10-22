from django.core.management.base import BaseCommand
from education.models import Teacher, Course, Student, GraduatedStudent, Achievement
from django.contrib.auth.models import User
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create Lead Teacher - Asliddin Kurbanov
        lead_teacher = Teacher.objects.create(
            name="Asliddin Kurbanov",
            title="Lead Teacher & Founder",
            bio="Experienced educator with over 10 years of experience in preparing students for university entrance. Specialized in mathematics and physics with a proven track record of student success.",
            email="asliddin@asliddin.edu",
            phone="+998 XX XXX XX XX",
            is_lead_teacher=True
        )

        # Create other teachers
        teacher2 = Teacher.objects.create(
            name="Malika Karimova",
            title="Mathematics Teacher",
            bio="Mathematics specialist with expertise in algebra, geometry, and calculus. Passionate about making complex concepts accessible to all students.",
            email="malika@asliddin.edu",
            phone="+998 XX XXX XX XX"
        )

        teacher3 = Teacher.objects.create(
            name="Javlon Toshmatov",
            title="Physics Teacher",
            bio="Physics educator with a background in engineering. Focuses on practical applications and problem-solving techniques.",
            email="javlon@asliddin.edu",
            phone="+998 XX XXX XX XX"
        )

        # Create courses
        course1 = Course.objects.create(
            title="University Entrance Mathematics",
            description="Comprehensive mathematics course covering all topics required for university entrance exams. Includes algebra, geometry, trigonometry, and calculus fundamentals.",
            teacher=lead_teacher,
            duration_weeks=16,
            price=500.00
        )

        course2 = Course.objects.create(
            title="Advanced Physics Preparation",
            description="Intensive physics course designed for students aiming for top universities. Covers mechanics, thermodynamics, electricity, and modern physics.",
            teacher=teacher3,
            duration_weeks=14,
            price=450.00
        )

        course3 = Course.objects.create(
            title="Chemistry Fundamentals",
            description="Complete chemistry course covering organic, inorganic, and physical chemistry. Perfect for students preparing for science and engineering programs.",
            teacher=teacher2,
            duration_weeks=12,
            price=400.00
        )

        course4 = Course.objects.create(
            title="English for University",
            description="English language preparation course focusing on academic writing, reading comprehension, and communication skills needed for university success.",
            teacher=lead_teacher,
            duration_weeks=10,
            price=350.00
        )

        # Create students
        students_data = [
            ("Ahmad Karimov", "11th Grade", "ahmad@email.com", "+998 XX XXX XX XX"),
            ("Malika Toshmatova", "12th Grade", "malika@email.com", "+998 XX XXX XX XX"),
            ("Javlon Umarov", "11th Grade", "javlon@email.com", "+998 XX XXX XX XX"),
            ("Dilnoza Karimova", "12th Grade", "dilnoza@email.com", "+998 XX XXX XX XX"),
            ("Bobur Toshmatov", "11th Grade", "bobur@email.com", "+998 XX XXX XX XX"),
            ("Sevara Umarova", "12th Grade", "sevara@email.com", "+998 XX XXX XX XX"),
            ("Aziz Karimov", "11th Grade", "aziz@email.com", "+998 XX XXX XX XX"),
            ("Madina Toshmatova", "12th Grade", "madina@email.com", "+998 XX XXX XX XX"),
        ]

        for name, grade, email, phone in students_data:
            student = Student.objects.create(
                name=name,
                email=email,
                phone=phone,
                grade_level=grade,
                enrollment_date=date.today() - timedelta(days=random.randint(30, 180))
            )
            # Assign random courses
            courses = random.sample([course1, course2, course3, course4], random.randint(1, 3))
            student.courses.set(courses)

        # Create graduated students
        graduates_data = [
            ("Akmal Karimov", 2023, "Tashkent State Technical University", "Computer Science", "The education I received at Asliddin Kurbanov Education Center was instrumental in my success. The teachers were dedicated and the curriculum was perfectly aligned with university requirements."),
            ("Malika Umarova", 2023, "Tashkent State University", "Mathematics", "I couldn't have achieved my dream of studying mathematics at TSU without the excellent preparation I received here. The teachers made complex concepts easy to understand."),
            ("Javlon Toshmatov", 2022, "Inha University in Tashkent", "Information Technology", "The comprehensive preparation helped me excel in my university entrance exams. I'm now pursuing my passion for technology at one of the best universities."),
            ("Dilnoza Karimova", 2022, "Westminster International University", "Business Administration", "The English course was particularly helpful for my international university application. The teachers provided excellent guidance throughout the process."),
            ("Bobur Umarov", 2021, "Tashkent Medical Academy", "Medicine", "The rigorous preparation in science subjects prepared me well for medical school. I'm grateful for the foundation I received here."),
            ("Sevara Toshmatova", 2021, "Tashkent State University of Economics", "Economics", "The analytical thinking skills I developed here have been invaluable in my economics studies. The teachers were supportive and knowledgeable."),
        ]

        for name, year, university, major, testimonial in graduates_data:
            GraduatedStudent.objects.create(
                name=name,
                graduation_year=year,
                university_name=university,
                major=major,
                testimonial=testimonial
            )

        # Create achievements
        achievements_data = [
            ("95% University Acceptance Rate", "Our students achieved a 95% acceptance rate to their preferred universities in 2023.", date(2023, 12, 15), True),
            ("Top 10 National Ranking", "Our education center was ranked in the top 10 private education centers in Uzbekistan.", date(2023, 11, 20), True),
            ("1000+ Successful Graduates", "We have successfully prepared over 1000 students for university entrance since our founding.", date(2023, 10, 1), True),
            ("Excellence in Mathematics", "Our mathematics program was recognized for excellence by the Ministry of Education.", date(2023, 9, 15), False),
            ("Best Physics Teacher Award", "Our physics teacher received the Best Physics Teacher Award for 2023.", date(2023, 8, 30), False),
            ("Student Satisfaction Award", "We received the Student Satisfaction Award with a 98% satisfaction rate.", date(2023, 7, 20), False),
        ]

        for title, description, date_achieved, is_featured in achievements_data:
            Achievement.objects.create(
                title=title,
                description=description,
                date_achieved=date_achieved,
                is_featured=is_featured
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write(f'Created:')
        self.stdout.write(f'- {Teacher.objects.count()} teachers')
        self.stdout.write(f'- {Course.objects.count()} courses')
        self.stdout.write(f'- {Student.objects.count()} students')
        self.stdout.write(f'- {GraduatedStudent.objects.count()} graduated students')
        self.stdout.write(f'- {Achievement.objects.count()} achievements')
