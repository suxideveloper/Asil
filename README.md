# 🎓 Asliddin Kurbanov Education Center

A Django-based website for Asliddin Kurbanov's education center that prepares children for university entrance.

## 🚀 Live Demo
- **Website**: [Deploy to Render](https://render.com)
- **Admin Panel**: Available after deployment
- **Credentials**: admin / admin123

## 🛠️ Quick Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Click the "Deploy to Render" button above
2. Connect your GitHub account
3. Select this repository
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput --settings=asliddin_education.settings_production && python manage.py migrate --settings=asliddin_education.settings_production`
   - **Start Command**: `gunicorn asliddin_education.wsgi:application --bind 0.0.0.0:$PORT`
   - **Environment Variable**: `DJANGO_SETTINGS_MODULE=asliddin_education.settings_production`

## Features

- **Modern, Casual Design**: Beautiful and responsive UI with a casual, friendly appearance
- **Lead Teacher Profile**: Features Asliddin Kurbanov as the lead teacher and founder
- **Teacher Management**: Display all teachers with their profiles and specializations
- **Course Catalog**: Show available courses with detailed information
- **Student Profiles**: Showcase current students and their enrolled courses
- **Success Stories**: Display graduated students with their university achievements
- **Contact Information**: Easy-to-use contact form and contact details
- **Admin Panel**: Full Django admin interface for content management

## Technology Stack

- **Backend**: Django 5.2.7
- **Frontend**: Bootstrap 5.3, HTML5, CSS3, JavaScript
- **Database**: SQLite (development)
- **Image Handling**: Pillow
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## Installation & Setup

1. **Clone or navigate to the project directory**:
   ```bash
   cd /home/suhrob/Pictures/Asil
   ```

2. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies** (if not already installed):
   ```bash
   pip install django Pillow
   ```

4. **Run migrations** (if not already done):
   ```bash
   python manage.py migrate
   ```

5. **Create sample data** (if not already done):
   ```bash
   python manage.py populate_data
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the website**:
   - Main website: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
     - Username: `admin`
     - Password: `admin123`

## Website Structure

### Pages

1. **Home** (`/`): Welcome page with lead teacher profile, achievements, and recent graduates
2. **About** (`/about/`): Information about the education center, mission, and team
3. **Teachers** (`/teachers/`): Profiles of all teachers, featuring Asliddin Kurbanov as lead teacher
4. **Courses** (`/courses/`): Available courses with descriptions, teachers, and pricing
5. **Students** (`/students/`): Current students and their enrolled courses
6. **Graduates** (`/graduates/`): Success stories of graduated students with university information
7. **Contact** (`/contact/`): Contact form and contact information

### Models

- **Teacher**: Teacher profiles with photos, bios, and contact information
- **Course**: Course information including title, description, teacher, duration, and price
- **Student**: Current student information with enrolled courses
- **GraduatedStudent**: Alumni information with university details and testimonials
- **Achievement**: Center achievements and milestones

## Sample Data

The website comes with sample data including:

- **Lead Teacher**: Asliddin Kurbanov (Lead Teacher & Founder)
- **Additional Teachers**: Malika Karimova (Mathematics), Javlon Toshmatov (Physics)
- **Courses**: University Entrance Mathematics, Advanced Physics, Chemistry, English
- **Students**: 8 sample students with various course enrollments
- **Graduates**: 6 graduated students with university success stories
- **Achievements**: 6 achievements showcasing the center's success

## Customization

### Adding New Content

1. **Access Admin Panel**: Go to http://127.0.0.1:8000/admin/
2. **Login**: Use admin/admin123 credentials
3. **Manage Content**: Add/edit teachers, courses, students, graduates, and achievements

### Styling

- Main styles are in `templates/education/base.html`
- Custom CSS is embedded in the base template
- Colors and design can be modified in the CSS variables section

### Branding

- The brand name "Asliddin Kurbanov" is used throughout the site
- Lead teacher is prominently featured on the homepage and teachers page
- All content reflects the educational focus on university preparation

## Development

### Project Structure

```
asliddin_education/
├── asliddin_education/          # Main project settings
├── education/                   # Main app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # URL routing
│   ├── admin.py                # Admin configuration
│   └── management/commands/    # Custom management commands
├── templates/education/         # HTML templates
├── static/                     # Static files (CSS, JS, images)
├── media/                      # User uploaded files
└── manage.py                   # Django management script
```

### Key Features Implemented

✅ Django project setup with proper configuration  
✅ Models for teachers, students, courses, and graduates  
✅ Modern, casual UI design with Bootstrap  
✅ Responsive design for all devices  
✅ Lead teacher (Asliddin Kurbanov) prominently featured  
✅ Graduated students with university information  
✅ Admin panel for content management  
✅ Sample data for demonstration  
✅ Contact form and information  
✅ Success stories and achievements  

## Production Deployment

For production deployment, consider:

1. **Database**: Switch to PostgreSQL or MySQL
2. **Static Files**: Configure proper static file serving
3. **Media Files**: Set up proper media file handling
4. **Security**: Update SECRET_KEY and disable DEBUG
5. **Hosting**: Deploy to platforms like Heroku, DigitalOcean, or AWS

## Support

For questions or support regarding this website, please contact the development team or refer to the Django documentation.

---

**Asliddin Kurbanov Education Center** - Preparing students for university success! 🎓
