from django.core.management.base import BaseCommand
from main_app.models import Course, Session
from datetime import date


class Command(BaseCommand):
    help = 'Setup initial courses and sessions for College ERP'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Setting up initial data for College ERP...'))
        
        # Create Courses
        courses_data = [
            "Computer Science",
            "Information Technology",
            "Electronics Engineering",
            "Mechanical Engineering",
            "Civil Engineering",
            "Business Administration",
            "Commerce",
            "Arts",
        ]
        
        self.stdout.write('\nCreating Courses...')
        for course_name in courses_data:
            course, created = Course.objects.get_or_create(name=course_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created course: {course_name}'))
            else:
                self.stdout.write(f'- Course already exists: {course_name}')
        
        # Create Sessions
        sessions_data = [
            (date(2023, 7, 1), date(2024, 6, 30)),  # 2023-2024
            (date(2024, 7, 1), date(2025, 6, 30)),  # 2024-2025
            (date(2025, 7, 1), date(2026, 6, 30)),  # 2025-2026
            (date(2026, 7, 1), date(2027, 6, 30)),  # 2026-2027
        ]
        
        self.stdout.write('\nCreating Sessions...')
        for start_year, end_year in sessions_data:
            session, created = Session.objects.get_or_create(
                start_year=start_year,
                end_year=end_year
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created session: {session}'))
            else:
                self.stdout.write(f'- Session already exists: {session}')
        
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS('Initial data setup complete!'))
        self.stdout.write('='*50)
        self.stdout.write(f'\nTotal Courses: {Course.objects.count()}')
        self.stdout.write(f'Total Sessions: {Session.objects.count()}')
        self.stdout.write('\nYou can now:')
        self.stdout.write('1. Register new users at: http://127.0.0.1:8000/register/')
        self.stdout.write('2. Login at: http://127.0.0.1:8000/')
        self.stdout.write('3. Access admin panel at: http://127.0.0.1:8000/admin/')
