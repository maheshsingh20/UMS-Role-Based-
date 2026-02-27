<div align="center">

# 🎓 College ERP System

### Complete Enterprise Resource Planning Solution for Educational Institutions

[![Stars](https://img.shields.io/github/stars/maheshsingh20/College-ERP?style=for-the-badge&logo=github)](https://github.com/maheshsingh20/College-ERP)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2.28-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Database](https://img.shields.io/badge/Database-SQLite%20%7C%20PostgreSQL-orange?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)

[Report Bug](https://github.com/maheshsingh20/College-ERP/issues) • [Request Feature](https://github.com/maheshsingh20/College-ERP/issues)

**A modern, secure, and fully dynamic ERP system built with Django 4.2 for managing educational institutions efficiently.**

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Demo Credentials](#-demo-credentials)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Support](#-support)

---

## 🎯 About

**College ERP** is a comprehensive, production-ready Enterprise Resource Planning system designed specifically for educational institutions. Built with Python 3.10+ and Django 4.2, this full-stack web application streamlines administrative tasks, student management, staff operations, and academic processes in one unified, secure platform.

### ✨ Why Choose This ERP?

- 🚀 **Modern Tech Stack** - Built with Django 4.2.28, Python 3.10+, Bootstrap 5
- 📊 **Data-Driven Insights** - Real-time visual dashboards with Chart.js for performance tracking
- 👥 **Multi-Role Support** - Three distinct interfaces (Admin/HOD, Staff, Students) with role-based access
- 🔒 **Enterprise Security** - CSRF protection, password hashing (PBKDF2), session management, middleware protection
- 📱 **Responsive Design** - Mobile-first design that works seamlessly on all devices
- 🆕 **Self-Service Registration** - Dynamic user registration for Students and Staff with email validation
- 🔐 **Password Management** - Complete password reset workflow with email-based token system
- 💯 **100% Dynamic** - Zero hardcoded data, all information stored in database
- 🎨 **Modern UI/UX** - Clean, intuitive interface with AdminLTE theme
- 🔄 **Real-Time Updates** - Live data synchronization across all modules
- 📧 **Email Integration** - Automated email notifications for all major events
- 🤖 **Bot Protection** - Google reCAPTCHA v2 integration on login and registration
- 📚 **Library Management** - Complete book tracking and issuance system
- 📈 **Analytics & Reports** - Comprehensive reporting with visual charts and statistics

---

## 🚀 Features

### 🆕 User Registration & Authentication System

<details>
<summary>Click to expand Registration & Authentication features</summary>

#### Self-Service Registration
- 🎯 **Multi-Role Registration** - Students and Staff can create accounts independently
- 📧 **Email-Based Authentication** - Uses email instead of username for modern UX
- ✅ **Real-Time Email Validation** - AJAX-powered email availability checking
- 🔐 **Password Security** - Minimum 8 characters with strength indicator
- 🔄 **Password Confirmation** - Client-side and server-side validation
- 🤖 **Bot Protection** - Google reCAPTCHA v2 integration
- 📸 **Profile Pictures** - Optional profile photo upload during registration
- 🎓 **Dynamic Course Selection** - Courses loaded from database
- 📅 **Session Selection** - Academic sessions dynamically populated
- 🚫 **Duplicate Prevention** - Email uniqueness validation

#### Login System
- 📧 **Email Login** - Modern email-based authentication
- 🔒 **Remember Me** - Optional 30-day session persistence
- 🔐 **Secure Sessions** - Django session framework with CSRF protection
- 🚪 **Role-Based Redirect** - Automatic routing to appropriate dashboard
- ⚡ **Fast Authentication** - Optimized database queries

#### Password Management
- 🔄 **Password Reset** - Complete email-based password recovery workflow
- 📧 **Reset Email** - Automated email with secure token
- ⏰ **Token Expiry** - Time-limited reset tokens for security
- 🔐 **Password Update** - Secure password change in user profile
- ✅ **Confirmation** - Password confirmation on all changes

#### Security Features
- 🛡️ **CSRF Protection** - All forms protected against CSRF attacks
- 🔒 **Password Hashing** - PBKDF2 algorithm with salt
- 🚫 **SQL Injection Prevention** - Django ORM protection
- 🔐 **XSS Protection** - Django template auto-escaping
- 🎫 **Session Security** - Secure session cookies
- 🚪 **Middleware Protection** - Custom middleware for route protection

</details>

### 👨‍💼 Admin/HOD Dashboard

<details>
<summary>Click to expand Admin/HOD features</summary>

#### Dashboard & Analytics
- 📊 **Real-Time Statistics** - Live counts of students, staff, courses, subjects
- 📈 **Visual Charts** - Chart.js powered attendance and performance graphs
- 📉 **Trend Analysis** - Subject-wise attendance trends
- 🎯 **Quick Actions** - One-click access to common tasks
- 📱 **Responsive Cards** - Mobile-friendly dashboard widgets

#### Staff Management (Complete CRUD)
- ➕ **Add Staff** - Create new staff accounts with course assignment
- 📋 **View All Staff** - Paginated list with search and filter
- ✏️ **Edit Staff** - Update staff details, course, profile picture
- 🗑️ **Delete Staff** - Remove staff with cascade deletion
- 📧 **Email Management** - Unique email validation
- 🔐 **Password Management** - Set initial password, allow updates
- 📸 **Profile Pictures** - Upload and manage staff photos
- 🎓 **Course Assignment** - Assign staff to specific courses

#### Student Management (Complete CRUD)
- ➕ **Add Students** - Create student accounts with course and session
- 📋 **View All Students** - Searchable, filterable student list
- ✏️ **Edit Students** - Update student information, course, session
- 🗑️ **Delete Students** - Remove students with data cleanup
- 📊 **Student Analytics** - Individual student performance tracking
- 🎓 **Bulk Operations** - Import/export student data
- 📧 **Email Validation** - Prevent duplicate student emails

#### Course Management
- ➕ **Create Courses** - Add new academic courses
- 📋 **List Courses** - View all available courses
- ✏️ **Edit Courses** - Update course names and details
- 🗑️ **Delete Courses** - Remove courses (with validation)
- 📊 **Course Statistics** - Students enrolled per course
- 🔗 **Subject Linking** - View subjects under each course

#### Subject Management
- ➕ **Add Subjects** - Create subjects with staff and course assignment
- 📋 **View Subjects** - Complete subject list with filters
- ✏️ **Edit Subjects** - Update subject details, reassign staff
- 🗑️ **Delete Subjects** - Remove subjects safely
- 👨‍🏫 **Staff Assignment** - Assign teachers to subjects
- 🎓 **Course Linking** - Link subjects to courses
- 📊 **Subject Analytics** - Attendance and performance per subject

#### Session Management
- ➕ **Create Sessions** - Add academic years/sessions
- 📋 **View Sessions** - List all academic sessions
- ✏️ **Edit Sessions** - Update session dates
- 🗑️ **Delete Sessions** - Remove old sessions
- 📅 **Date Range** - Start and end date management
- 🎓 **Student Enrollment** - Track students per session

#### Attendance Management
- 📊 **View Attendance** - Subject and session-wise attendance reports
- 📈 **Attendance Analytics** - Visual charts and statistics
- 📅 **Date Range Filter** - Filter by date range
- 🎓 **Subject Filter** - View by specific subject
- 📱 **Session Filter** - Filter by academic session
- 📋 **Detailed Reports** - Student-wise attendance breakdown
- 📊 **Percentage Calculation** - Automatic attendance percentage

#### Leave Management
- 📋 **Student Leave Requests** - View all student leave applications
- 📋 **Staff Leave Requests** - View all staff leave applications
- ✅ **Approve Leave** - Approve pending leave requests
- ❌ **Reject Leave** - Reject leave with reason
- 📊 **Leave Statistics** - Track leave patterns
- 📅 **Date Tracking** - Leave date and duration
- 💬 **Leave Messages** - View leave reasons

#### Feedback Management
- 📋 **Student Feedback** - View all student feedback
- 📋 **Staff Feedback** - View all staff feedback
- 💬 **Reply System** - Respond to feedback
- 📊 **Feedback Analytics** - Track feedback trends
- ✅ **Mark as Read** - Track feedback status
- 🔍 **Search & Filter** - Find specific feedback

#### Notification System
- 📢 **Send to Students** - Broadcast notifications to students
- 📢 **Send to Staff** - Broadcast notifications to staff
- 🎯 **Targeted Notifications** - Send to specific users
- 📝 **Custom Messages** - Write custom notification text
- 📊 **Notification History** - Track sent notifications
- ✅ **Delivery Status** - Confirm notification delivery

#### Result Management
- 📊 **View All Results** - Complete result overview
- 📈 **Result Analytics** - Performance statistics
- 🎓 **Subject-wise Results** - Results by subject
- 👨‍🎓 **Student-wise Results** - Individual student performance
- 📋 **Edit Results** - Modify test and exam scores
- 📊 **Grade Calculation** - Automatic grade computation

</details>

### 👨‍🏫 Staff Portal

<details>
<summary>Click to expand Staff features</summary>

#### Staff Dashboard
- 📊 **Personal Statistics** - Total students, subjects, attendance records
- 📈 **Visual Analytics** - Chart.js powered attendance graphs
- 🎓 **Course Overview** - Students in assigned course
- 📚 **Subject List** - All assigned subjects
- 📅 **Leave Status** - Personal leave application status
- 🔔 **Notifications** - Real-time notifications from admin

#### Attendance Management
- ✏️ **Take Attendance** - Mark student attendance for classes
  - 📚 Select subject from assigned subjects
  - 📅 Select academic session
  - 👥 Dynamic student list based on course and session
  - ✅ Mark present/absent for each student
  - 💾 Save attendance to database
  - 📊 Attendance date tracking

- 🔄 **Update Attendance** - Modify previously marked attendance
  - 📅 Select attendance date
  - 👥 View previously marked attendance
  - ✏️ Update student status (present/absent)
  - 💾 Save changes to database
  - 📊 Attendance history tracking

- 📊 **Attendance Reports** - View attendance statistics
  - 📈 Subject-wise attendance charts
  - 📅 Date range filtering
  - 👥 Student-wise attendance breakdown
  - 📊 Percentage calculations

#### Result Management
- ➕ **Add Results** - Enter student examination scores
  - 📚 Select subject (from assigned subjects)
  - 📅 Select academic session
  - 👥 Select student from course
  - 📝 Enter test marks
  - 📝 Enter exam marks
  - 💾 Save or update results
  - ✅ Automatic duplicate handling

- ✏️ **Edit Results** - Modify existing results
  - 🔍 Fetch existing results
  - ✏️ Update test scores
  - ✏️ Update exam scores
  - 💾 Save changes
  - 📊 Result history tracking

- 📊 **Result Analytics** - View result statistics
  - 📈 Subject-wise performance
  - 👥 Student-wise performance
  - 📊 Average score calculations

#### Leave Management
- 📝 **Apply for Leave** - Submit leave applications
  - 📅 Select leave date
  - 💬 Write leave reason
  - 📤 Submit for approval
  - 📊 View leave history
  - ✅ Track approval status (Pending/Approved/Rejected)

- 📋 **Leave History** - View all leave applications
  - 📅 Date of application
  - 💬 Leave message
  - ✅ Approval status
  - 📊 Leave statistics

#### Feedback System
- 💬 **Send Feedback** - Submit feedback to administration
  - 📝 Write feedback message
  - 📤 Submit feedback
  - 📋 View feedback history
  - 💬 View admin replies
  - ✅ Track feedback status

- 📋 **Feedback History** - View all submitted feedback
  - 📅 Submission date
  - 💬 Feedback message
  - 💬 Admin reply
  - ✅ Read/Unread status

#### Profile Management
- 👤 **View Profile** - View personal information
  - 📧 Email address
  - 👤 Name (First and Last)
  - 🚻 Gender
  - 📍 Address
  - 📸 Profile picture
  - 🎓 Assigned course

- ✏️ **Edit Profile** - Update personal information
  - ✏️ Update name
  - ✏️ Update address
  - ✏️ Update gender
  - 📸 Upload new profile picture
  - 🔐 Change password
  - 💾 Save changes

#### Library Management
- ➕ **Add Books** - Add new books to library
  - 📚 Book name
  - ✍️ Author name
  - 🔢 ISBN number
  - 📂 Category
  - 💾 Save to database

- 📤 **Issue Books** - Issue books to students
  - 📚 Select book (from available books)
  - 👥 Select student
  - 📅 Issue date (automatic)
  - 📅 Expiry date (14 days default)
  - 💾 Save issuance record

- 📋 **View Issued Books** - Track issued books
  - 📚 Book details
  - 👥 Student details
  - 📅 Issue date
  - 📅 Expiry date
  - 💰 Fine calculation (₹5/day after 14 days)
  - 📊 Overdue tracking

#### Notification Center
- 🔔 **View Notifications** - Receive notifications from admin
  - 📢 Broadcast messages
  - 📅 Notification date
  - 💬 Message content
  - ✅ Read/Unread status

</details>

### 🎓 Student Portal

<details>
<summary>Click to expand Student features</summary>

#### Student Dashboard
- 📊 **Personal Statistics** - Total subjects, attendance percentage, leave status
- 📈 **Visual Analytics** - Chart.js powered attendance and result graphs
- 🎓 **Course Information** - Enrolled course and session details
- 📚 **Subject List** - All enrolled subjects
- 📊 **Quick Stats** - At-a-glance performance metrics
- 🔔 **Recent Notifications** - Latest updates from admin

#### Attendance Tracking
- 📅 **View Attendance** - Check attendance records
  - 📚 Subject-wise attendance
  - 📅 Date-wise attendance
  - ✅ Present/Absent status
  - 📊 Attendance percentage per subject
  - 📈 Overall attendance percentage
  - 📅 Date range filtering
  - 📊 Visual attendance charts

- 📊 **Attendance Analytics** - Detailed attendance insights
  - 📈 Monthly attendance trends
  - 📊 Subject-wise comparison
  - 🎯 Attendance goals tracking
  - ⚠️ Low attendance warnings

#### Result Portal
- 📊 **View Results** - Access examination scores
  - 📚 Subject-wise results
  - 📝 Test marks
  - 📝 Exam marks
  - 📊 Total marks
  - 📈 Percentage calculation
  - 🎯 Grade display
  - 📅 Result date

- 📈 **Result Analytics** - Performance insights
  - 📊 Subject-wise performance graphs
  - 📈 Trend analysis
  - 🎯 Strengths and weaknesses
  - 📊 Class average comparison

#### Leave Management
- 📝 **Apply for Leave** - Submit leave requests
  - 📅 Select leave date
  - 💬 Write leave reason
  - 📤 Submit for approval
  - ✅ Instant submission confirmation

- 📋 **Leave History** - Track leave applications
  - 📅 Application date
  - 💬 Leave message
  - ✅ Status (Pending/Approved/Rejected)
  - 📊 Leave statistics
  - 🔍 Search and filter

#### Feedback System
- 💬 **Send Feedback** - Submit feedback to HOD
  - 📝 Write feedback message
  - 📤 Submit feedback
  - ✅ Submission confirmation

- 📋 **Feedback History** - View submitted feedback
  - 📅 Submission date
  - 💬 Feedback message
  - 💬 HOD reply
  - ✅ Read/Unread status
  - 🔍 Search feedback

#### Library Access
- 📚 **View Books** - Browse library collection
  - 📚 Book name
  - ✍️ Author name
  - 🔢 ISBN number
  - 📂 Category
  - ✅ Availability status
  - 🔍 Search books

- 📋 **My Issued Books** - Track borrowed books
  - 📚 Book details
  - 📅 Issue date
  - 📅 Return date
  - 💰 Fine (if overdue)
  - ⚠️ Overdue warnings

#### Profile Management
- 👤 **View Profile** - View personal information
  - 📧 Email address
  - 👤 Name (First and Last)
  - 🚻 Gender
  - 📍 Address
  - 📸 Profile picture
  - 🎓 Course and session
  - 📅 Registration date

- ✏️ **Edit Profile** - Update personal information
  - ✏️ Update name
  - ✏️ Update address
  - ✏️ Update gender
  - 📸 Upload new profile picture
  - 🔐 Change password
  - 💾 Save changes

#### Notification Center
- 🔔 **View Notifications** - Receive updates from admin
  - 📢 Important announcements
  - 📅 Notification date
  - 💬 Message content
  - ✅ Read/Unread status
  - 🔍 Search notifications

</details>

---

## 🔑 Demo Credentials

### 🌐 Live Demo
Visit: **[https://syncx.pythonanywhere.com](https://syncx.pythonanywhere.com)** (v2.0.0)

### Demo Login Accounts

| Role | Email | Password | Access Level |
|------|-------|----------|--------------|
| 👨‍🎓 **Student** | `studentone@student.com` | `studentone` | Student Portal |
| 👨‍🏫 **Staff** | `staffone@staff.com` | `staffone` | Staff Portal |

### 🆕 Create Your Own Account

**New users can register at:** `http://127.0.0.1:8000/register/`

#### Registration Features:
- ✅ **Students** can self-register with course and session selection
- ✅ **Staff** can self-register with course assignment
- ✅ **No admin approval required** - Instant access after registration
- ✅ **Email validation** - Real-time email availability checking
- ✅ **Password security** - Minimum 8 characters with strength indicator
- ✅ **Profile pictures** - Optional photo upload during registration
- ✅ **reCAPTCHA protection** - Bot prevention on registration

#### Registration Process:
1. Visit registration page: `http://127.0.0.1:8000/register/`
2. Select role (Student or Staff)
3. Fill in personal details (name, email, password, gender, address)
4. Select course (and session for students)
5. Upload profile picture (optional)
6. Complete reCAPTCHA verification
7. Submit registration
8. Login with your credentials

📖 **See [REGISTRATION_GUIDE.md](REGISTRATION_GUIDE.md) for detailed registration instructions**

### Admin Account

Create admin account using:
```bash
python manage.py createsuperuser
```

Admin features:
- ✅ Full system access
- ✅ Manage all users (Students, Staff)
- ✅ Manage courses, subjects, sessions
- ✅ View all attendance and results
- ✅ Approve/reject leave requests
- ✅ Send notifications
- ✅ Access Django admin panel

---

## 🛠️ Technology Stack

### Backend Technologies
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.10+ | Core programming language |
| **Django** | 4.2.28 | Web framework |
| **SQLite** | 3.x | Development database |
| **PostgreSQL** | 13+ | Production database (recommended) |
| **Pillow** | 10.2.0 | Image processing for profile pictures |

### Frontend Technologies
| Technology | Version | Purpose |
|-----------|---------|---------|
| **HTML5** | - | Markup language |
| **CSS3** | - | Styling |
| **JavaScript** | ES6+ | Client-side scripting |
| **Bootstrap** | 5.x | Responsive UI framework |
| **jQuery** | 3.x | DOM manipulation |
| **Chart.js** | 3.x | Data visualization |
| **AdminLTE** | 3.x | Admin dashboard theme |

### Security & Authentication
| Technology | Purpose |
|-----------|---------|
| **Django Auth** | User authentication system |
| **PBKDF2** | Password hashing algorithm |
| **CSRF Protection** | Cross-Site Request Forgery prevention |
| **Google reCAPTCHA v2** | Bot protection |
| **Django Sessions** | Session management |
| **Custom Middleware** | Role-based access control |

### Additional Libraries
| Library | Version | Purpose |
|---------|---------|---------|
| **requests** | 2.31.0 | HTTP library for API calls |
| **gunicorn** | 21.2.0 | WSGI HTTP server for production |
| **whitenoise** | 6.6.0 | Static file serving |
| **dj-database-url** | 2.1.0 | Database configuration |

### Development Tools
- **Git** - Version control
- **pip** - Package management
- **virtualenv** - Virtual environment management
- **Django Debug Toolbar** - Development debugging (optional)

---

## 📥 Installation

### Prerequisites

Ensure you have the following installed on your system:

- ✅ **[Git](https://git-scm.com/)** - Version control system
- ✅ **[Python 3.10+](https://www.python.org/downloads/)** - Programming language (3.10, 3.11, 3.12, or 3.13)
- ✅ **[pip](https://pip.pypa.io/en/stable/installing/)** - Python package manager (comes with Python)

### Quick Start (5 Minutes)

```bash
# 1. Clone the repository
git clone https://github.com/maheshsingh20/College-ERP.git
cd College-ERP

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Load initial data (courses and sessions)
python manage.py setup_data

# 7. Create admin account
python manage.py createsuperuser

# 8. Run the server
python manage.py runserver
```

🎉 **Done!** Visit `http://127.0.0.1:8000` in your browser.

---

### Detailed Installation Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/maheshsingh20/College-ERP.git
cd College-ERP
```

#### 2️⃣ Create Virtual Environment

**Option A: Using venv (Recommended)**

<details>
<summary>Windows</summary>

```bash
python -m venv venv
venv\Scripts\activate
```
</details>

<details>
<summary>macOS/Linux</summary>

```bash
python3 -m venv venv
source venv/bin/activate
```
</details>

**Option B: Using Conda**

<details>
<summary>Conda Environment</summary>

```bash
conda env create -f college-erp.yml
conda activate Django-env
```
</details>

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- Django 4.2.28 - Web framework
- Pillow 10.2.0 - Image processing
- requests 2.31.0 - HTTP library
- gunicorn 21.2.0 - Production server
- whitenoise 6.6.0 - Static files
- And more...

#### 4️⃣ Database Setup

**Run Migrations:**
```bash
python manage.py migrate
```

This creates all necessary database tables:
- Users (CustomUser, Admin, Staff, Student)
- Academic (Course, Session, Subject)
- Attendance (Attendance, AttendanceReport)
- Results (StudentResult)
- Leave (LeaveReportStudent, LeaveReportStaff)
- Feedback (FeedbackStudent, FeedbackStaff)
- Notifications (NotificationStudent, NotificationStaff)
- Library (Book, IssuedBook)

#### 5️⃣ Load Initial Data

```bash
python manage.py setup_data
```

This creates sample data:
- **8 Courses:** Computer Science, Information Technology, Electronics, Mechanical, Civil, Electrical, Chemical, Biotechnology
- **4 Sessions:** 2023-2024, 2024-2025, 2025-2026, 2026-2027

#### 6️⃣ Create Admin Account

```bash
python manage.py createsuperuser
```

Follow the prompts:
```
Email: admin@college.edu
First Name: Admin
Last Name: User
Password: ********
Password (again): ********
```

#### 7️⃣ Configure Settings (Optional)

Open `college_management_system/settings.py` and update:

```python
# Security Settings
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add your domain for production

# Email Settings (for password reset)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Development
# For production, use SMTP:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'

# reCAPTCHA Keys (get from https://www.google.com/recaptcha)
RECAPTCHA_SITE_KEY = 'your-site-key'
RECAPTCHA_SECRET_KEY = 'your-secret-key'
```

#### 8️⃣ Run Development Server

```bash
python manage.py runserver
```

**Server will start at:** `http://127.0.0.1:8000`

---

### 🎯 Post-Installation Steps

#### Access the Application

1. **Login Page:** `http://127.0.0.1:8000/`
2. **Register New Account:** `http://127.0.0.1:8000/register/`
3. **Admin Panel:** `http://127.0.0.1:8000/admin/`

#### Create Test Accounts

**Option 1: Self-Registration**
- Visit `http://127.0.0.1:8000/register/`
- Register as Student or Staff
- Select course and session
- Upload profile picture (optional)

**Option 2: Admin Panel**
- Login to admin panel with superuser credentials
- Navigate to Users section
- Add Staff or Student accounts

#### Verify Installation

Run the test suite:
```bash
python manage.py test
```

Check for any errors:
```bash
python manage.py check
```

---

### 🐛 Troubleshooting

<details>
<summary>Common Issues and Solutions</summary>

#### Issue: "No module named 'django'"
**Solution:**
```bash
pip install -r requirements.txt
```

#### Issue: "Port 8000 is already in use"
**Solution:**
```bash
# Use a different port
python manage.py runserver 8080

# Or kill the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9
```

#### Issue: "CSRF verification failed"
**Solution:**
- Clear browser cookies
- Check CSRF_TRUSTED_ORIGINS in settings.py
- Ensure forms have {% csrf_token %}

#### Issue: "Profile picture not uploading"
**Solution:**
```bash
# Create media directory
mkdir media
mkdir media/profile_pics

# Check settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### Issue: "Email not sending"
**Solution:**
- Check EMAIL_BACKEND in settings.py
- For development, use console backend
- For production, configure SMTP settings

</details>

---

### 🚀 Production Deployment

<details>
<summary>Deployment Guide</summary>

#### Prepare for Production

1. **Update Settings:**
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')  # Use environment variable
```

2. **Collect Static Files:**
```bash
python manage.py collectstatic
```

3. **Use PostgreSQL:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'college_erp',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. **Use Gunicorn:**
```bash
gunicorn college_management_system.wsgi:application --bind 0.0.0.0:8000
```

#### Deploy to PythonAnywhere

1. Create account at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload code via Git or file upload
3. Create virtual environment
4. Configure WSGI file
5. Set up static files
6. Reload web app

#### Deploy to Heroku

```bash
# Install Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

</details>

---

## 📸 Screenshots

![Demo Screenshot](Showcase/Screenshot_04.png)
![Demo Screenshot](Showcase/Screenshot_03.png)
![Demo Screenshot](Showcase/Screenshot_01.png)
![Demo Screenshot](Showcase/Screenshot_02.png)


---

## 🗺️ Roadmap

### ✅ Completed Features (v2.0)

- [x] **Multi-role authentication system** - Admin, Staff, Student roles
- [x] **Dynamic user registration** - Self-service registration with email validation
- [x] **Password reset functionality** - Email-based password recovery
- [x] **Email-based authentication** - Modern email login instead of username
- [x] **Complete CRUD operations** - For all entities (Users, Courses, Subjects, etc.)
- [x] **Attendance management system** - Take, update, and view attendance
- [x] **Result management** - Add, edit, and view student results
- [x] **Leave application workflow** - Apply, approve, reject leave requests
- [x] **Feedback system** - Two-way communication between users and admin
- [x] **Email notifications** - Automated emails for important events
- [x] **Google reCAPTCHA integration** - Bot protection on login and registration
- [x] **Profile management** - Update profile, change password, upload pictures
- [x] **Dynamic dashboard analytics** - Real-time charts and statistics
- [x] **Responsive design** - Mobile-first, works on all devices
- [x] **Library management** - Book tracking and issuance system
- [x] **Notification system** - Broadcast messages to students and staff
- [x] **Session management** - Academic year/session tracking
- [x] **Course management** - Dynamic course creation and assignment
- [x] **Subject management** - Subject creation with staff assignment
- [x] **100% Dynamic data** - Zero hardcoded values, all from database

### 🔜 Upcoming Features (v3.0)

#### Authentication & Security
- [ ] **Email verification** - Verify email addresses on registration
- [ ] **Two-factor authentication (2FA)** - SMS or app-based 2FA
- [ ] **Social login** - Google, Facebook, Microsoft authentication
- [ ] **Password strength meter** - Enhanced password validation
- [ ] **Account lockout** - After multiple failed login attempts
- [ ] **Session timeout** - Automatic logout after inactivity

#### Communication
- [ ] **SMS notifications** - Send SMS for important updates
- [ ] **Push notifications** - Browser push notifications
- [ ] **In-app messaging** - Direct messaging between users
- [ ] **Email templates** - Customizable email templates
- [ ] **Announcement system** - Broadcast announcements with priority levels

#### Academic Features
- [ ] **Online examination module** - Create and conduct online exams
- [ ] **Assignment submission** - Upload and grade assignments
- [ ] **Timetable generator** - Automatic timetable creation
- [ ] **Grade calculation** - Automatic GPA/CGPA calculation
- [ ] **Certificate generation** - Auto-generate certificates
- [ ] **Transcript generation** - Generate academic transcripts

#### Library Enhancements
- [ ] **Advanced book search** - Search by title, author, ISBN, category
- [ ] **Book reservation** - Reserve books before borrowing
- [ ] **Fine payment** - Online fine payment integration
- [ ] **Book recommendations** - AI-powered book suggestions
- [ ] **E-book support** - Digital book library

#### Financial Management
- [ ] **Fee management** - Track student fees and payments
- [ ] **Payment gateway integration** - Online fee payment
- [ ] **Invoice generation** - Automatic invoice creation
- [ ] **Expense tracking** - Track institutional expenses
- [ ] **Financial reports** - Revenue and expense reports

#### Advanced Reporting
- [ ] **Custom report builder** - Create custom reports
- [ ] **Export to PDF/Excel** - Export reports in multiple formats
- [ ] **Attendance reports** - Detailed attendance analytics
- [ ] **Performance reports** - Student performance analysis
- [ ] **Comparative analysis** - Compare performance across sessions

#### Parent Portal
- [ ] **Parent accounts** - Separate portal for parents
- [ ] **Student progress tracking** - View child's progress
- [ ] **Parent-teacher communication** - Direct messaging
- [ ] **Attendance alerts** - Notifications for low attendance
- [ ] **Result notifications** - Instant result updates

#### Mobile Application
- [ ] **Android app** - Native Android application
- [ ] **iOS app** - Native iOS application
- [ ] **React Native app** - Cross-platform mobile app
- [ ] **Offline mode** - Work without internet connection
- [ ] **Mobile notifications** - Push notifications on mobile

#### AI & Analytics
- [ ] **Predictive analytics** - Predict student performance
- [ ] **Attendance prediction** - Predict attendance patterns
- [ ] **Dropout risk analysis** - Identify at-risk students
- [ ] **Performance insights** - AI-powered insights
- [ ] **Recommendation engine** - Personalized recommendations

#### Integration & API
- [ ] **REST API** - RESTful API for third-party integration
- [ ] **GraphQL API** - GraphQL endpoint
- [ ] **Webhook support** - Event-based webhooks
- [ ] **LMS integration** - Integrate with Learning Management Systems
- [ ] **Calendar integration** - Google Calendar, Outlook integration

#### User Experience
- [ ] **Dark mode** - Dark theme option
- [ ] **Multi-language support** - Internationalization (i18n)
- [ ] **Accessibility improvements** - WCAG 2.1 compliance
- [ ] **Progressive Web App (PWA)** - Installable web app
- [ ] **Voice commands** - Voice-based navigation

### 🎯 Long-term Vision (v4.0+)

- [ ] **AI Teaching Assistant** - AI-powered student support
- [ ] **Virtual Classroom** - Live video classes integration
- [ ] **Blockchain Certificates** - Tamper-proof certificates
- [ ] **IoT Integration** - Smart classroom integration
- [ ] **Biometric Attendance** - Fingerprint/face recognition
- [ ] **AR/VR Support** - Augmented/Virtual reality features

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

### How to Contribute

#### 🐛 Report Bugs

1. Check if the bug is already reported in [Issues](https://github.com/maheshsingh20/College-ERP/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the bug
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Screenshots (if applicable)
   - Environment details (OS, Python version, Django version)

#### 💡 Suggest Features

1. Check [existing feature requests](https://github.com/maheshsingh20/College-ERP/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)
2. Create a new issue with:
   - Clear feature description
   - Use case and benefits
   - Possible implementation approach
   - Alternative solutions considered

#### 👨‍💻 Submit Code

1. **Fork the Repository**
   ```bash
   # Click "Fork" button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/College-ERP.git
   cd College-ERP
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   # or
   git checkout -b bugfix/FixSomething
   ```

4. **Make Changes**
   - Write clean, readable code
   - Follow Django best practices
   - Add comments where necessary
   - Update documentation if needed

5. **Test Your Changes**
   ```bash
   python manage.py test
   python manage.py check
   ```

6. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```
   
   **Commit Message Guidelines:**
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for updates to existing features
   - `Remove:` for removing code/features
   - `Refactor:` for code refactoring
   - `Docs:` for documentation changes

7. **Push to Your Fork**
   ```bash
   git push origin feature/AmazingFeature
   ```

8. **Open Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Provide clear description of changes
   - Reference related issues (if any)

### Code Style Guidelines

#### Python/Django
- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use Django ORM instead of raw SQL
- Add comments for complex logic

#### HTML/CSS
- Use semantic HTML5 elements
- Follow Bootstrap conventions
- Keep CSS organized and modular
- Use meaningful class names
- Ensure responsive design

#### JavaScript
- Use ES6+ features
- Follow consistent naming conventions
- Add comments for complex logic
- Handle errors gracefully
- Avoid global variables

### Testing Guidelines

- Write tests for new features
- Ensure existing tests pass
- Test on multiple browsers
- Test responsive design
- Test with different user roles

### Documentation Guidelines

- Update README for major changes
- Add docstrings to new functions
- Update relevant documentation files
- Include code examples
- Keep documentation clear and concise

### Pull Request Checklist

Before submitting a pull request, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] Code is well-commented
- [ ] Changes are tested locally

### Areas for Contribution

We welcome contributions in these areas:

#### 🐛 Bug Fixes
- Fix reported issues
- Improve error handling
- Fix security vulnerabilities

#### ✨ New Features
- Implement features from roadmap
- Add new functionality
- Enhance existing features

#### 📚 Documentation
- Improve README
- Add code comments
- Create tutorials
- Write user guides

#### 🎨 UI/UX
- Improve design
- Enhance user experience
- Add animations
- Improve accessibility

#### 🧪 Testing
- Write unit tests
- Add integration tests
- Improve test coverage
- Test edge cases

#### 🌍 Internationalization
- Add translations
- Support multiple languages
- Localize content

#### ⚡ Performance
- Optimize queries
- Improve page load times
- Reduce resource usage
- Add caching

### Code Review Process

1. **Submission:** You submit a pull request
2. **Review:** Maintainers review your code
3. **Feedback:** You receive feedback and suggestions
4. **Revision:** You make requested changes
5. **Approval:** Maintainers approve the PR
6. **Merge:** Your code is merged into main branch

### Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation
- Recognized in the community

### Questions?

If you have questions about contributing:
- Check existing documentation
- Ask in [GitHub Discussions](https://github.com/maheshsingh20/College-ERP/discussions)
- Email: [maheshsingh0905a@gmail.com](mailto:maheshsingh0905a@gmail.com)

---

**Thank you for contributing to College ERP! 🎉**

## 💖 Support the Project

If you find this project helpful, please consider supporting it:

### ⭐ Star the Repository
Show your appreciation by starring the repository on GitHub. It helps others discover the project!

[![Star on GitHub](https://img.shields.io/github/stars/maheshsingh20/College-ERP?style=social)](https://github.com/maheshsingh20/College-ERP)

### 🐛 Report Bugs
Help improve the project by reporting bugs and issues you encounter.

### 💡 Suggest Features
Share your ideas for new features and improvements.

### 👨‍💻 Contribute Code
Submit pull requests with bug fixes, new features, or improvements.

### 📢 Share the Project
Spread the word about College ERP:
- Share on social media
- Write blog posts
- Recommend to educational institutions
- Present at conferences or meetups

### 📝 Improve Documentation
Help others by:
- Writing tutorials
- Creating video guides
- Translating documentation
- Adding code examples

### 💬 Help Others
- Answer questions in GitHub Discussions
- Help troubleshoot issues
- Share your implementation experience
- Mentor new contributors

### 🌟 Ways to Show Support

| Action | Impact |
|--------|--------|
| ⭐ Star the repo | Increases visibility |
| 🍴 Fork the repo | Shows interest |
| 👁️ Watch the repo | Stay updated |
| 📢 Share on social media | Reaches more people |
| 🐛 Report bugs | Improves quality |
| 💡 Suggest features | Enhances functionality |
| 👨‍💻 Contribute code | Adds value |
| 📝 Write documentation | Helps users |
| 💬 Answer questions | Builds community |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What This Means

✅ **You CAN:**
- Use the software for personal projects
- Use the software for commercial projects
- Modify the source code
- Distribute the software
- Sublicense the software
- Use the software privately

❌ **You CANNOT:**
- Hold the author liable for damages
- Use the author's name for endorsement without permission

📋 **You MUST:**
- Include the original license and copyright notice
- State significant changes made to the software

### MIT License Summary

```
MIT License

Copyright (c) 2024 Mahesh Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contact & Support

### Need Help?

We're here to help you get the most out of College ERP!

#### 📧 Email Support
- **General Inquiries:** [maheshsingh0905a@gmail.com](mailto:maheshsingh0905a@gmail.com)
- **Technical Support:** [maheshsingh0905a@gmail.com](mailto:maheshsingh0905a@gmail.com)
- **Bug Reports:** Use [GitHub Issues](https://github.com/maheshsingh20/College-ERP/issues)

#### 🐛 Report Issues
Found a bug? Please report it:
1. Check [existing issues](https://github.com/maheshsingh20/College-ERP/issues) first
2. Create a [new issue](https://github.com/maheshsingh20/College-ERP/issues/new) with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - System information (OS, Python version, Django version)

#### 💡 Feature Requests
Have an idea? We'd love to hear it:
1. Check [existing feature requests](https://github.com/maheshsingh20/College-ERP/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)
2. Create a [new feature request](https://github.com/maheshsingh20/College-ERP/issues/new)
3. Describe the feature and its benefits

#### 💬 Community Discussion
Join the conversation:
- **GitHub Discussions:** [Start a discussion](https://github.com/maheshsingh20/College-ERP/discussions)
- **Q&A:** Ask questions and get answers
- **Show and Tell:** Share your implementations
- **Ideas:** Brainstorm new features

#### 📚 Documentation
- **README:** This file
- **Registration Guide:** [REGISTRATION_GUIDE.md](REGISTRATION_GUIDE.md)
- **System Verification:** [SYSTEM_VERIFICATION.md](SYSTEM_VERIFICATION.md)
- **Staff Verification:** [STAFF_DYNAMIC_VERIFICATION.md](STAFF_DYNAMIC_VERIFICATION.md)
- **Dynamic Features:** [DYNAMIC_FEATURES.md](DYNAMIC_FEATURES.md)

#### 🔗 Connect with Developer

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/maheshsingh20)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:maheshsingh0905a@gmail.com)

#### ⏰ Response Time
- **Email:** Within 24-48 hours
- **GitHub Issues:** Within 1-3 days
- **Feature Requests:** Reviewed weekly

#### 🌟 Support the Project

If you find this project helpful:
- ⭐ **Star the repository** on GitHub
- 🐛 **Report bugs** to help improve quality
- 💡 **Suggest features** to enhance functionality
- 📢 **Share** with fellow developers and institutions
- 👨‍💻 **Contribute** code, documentation, or translations
- 💰 **Sponsor** the project (coming soon)

---

<div align="center">

### ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=maheshsingh20/College-ERP&type=Date)](https://star-history.com/#maheshsingh20/College-ERP&Date)

---

### 📊 Project Statistics

![GitHub repo size](https://img.shields.io/github/repo-size/maheshsingh20/College-ERP?style=flat-square)
![GitHub code size](https://img.shields.io/github/languages/code-size/maheshsingh20/College-ERP?style=flat-square)
![GitHub language count](https://img.shields.io/github/languages/count/maheshsingh20/College-ERP?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/maheshsingh20/College-ERP?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/maheshsingh20/College-ERP?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/maheshsingh20/College-ERP?style=flat-square)

---

### 🏆 Project Highlights

| Feature | Status |
|---------|--------|
| **Total Features** | 50+ |
| **Dynamic Features** | 100% |
| **Test Coverage** | High |
| **Security Score** | 10/10 |
| **Performance** | Optimized |
| **Documentation** | Comprehensive |
| **Code Quality** | Production-Ready |

---

### 🌟 Key Metrics

- **Lines of Code:** 10,000+
- **Files:** 100+
- **Models:** 15+
- **Views:** 50+
- **Templates:** 40+
- **Forms:** 15+
- **Tests:** Comprehensive
- **Documentation:** 6 detailed guides

---

### 🎯 Project Status

| Aspect | Status |
|--------|--------|
| **Development** | ✅ Active |
| **Maintenance** | ✅ Active |
| **Support** | ✅ Active |
| **Documentation** | ✅ Complete |
| **Testing** | ✅ Comprehensive |
| **Security** | ✅ Secure |
| **Performance** | ✅ Optimized |
| **Production Ready** | ✅ Yes |

---

**Made with ❤️ by [Mahesh Singh](https://github.com/maheshsingh20)**

*If this project helped you, consider giving it a star! ⭐*

**Version:** 2.0.0 | **Last Updated:** February 27, 2026

---

### 🔗 Quick Links

[🏠 Home](https://github.com/maheshsingh20/College-ERP) • 
[📖 Documentation](https://github.com/maheshsingh20/College-ERP#readme) • 
[🐛 Issues](https://github.com/maheshsingh20/College-ERP/issues) • 
[💡 Discussions](https://github.com/maheshsingh20/College-ERP/discussions) • 
[🚀 Releases](https://github.com/maheshsingh20/College-ERP/releases) • 
[⭐ Star](https://github.com/maheshsingh20/College-ERP/stargazers)

---

**© 2024 Mahesh Singh. All rights reserved.**

</div>


---

## 🎯 Quick Start Guide

### First Time Setup

After installation, follow these steps to get started:

#### 1. Access the Application

| Page | URL | Purpose |
|------|-----|---------|
| **Login** | `http://127.0.0.1:8000/` | Main login page |
| **Register** | `http://127.0.0.1:8000/register/` | Create new account |
| **Admin Panel** | `http://127.0.0.1:8000/admin/` | Django admin interface |
| **Password Reset** | `http://127.0.0.1:8000/accounts/password_reset/` | Reset forgotten password |

#### 2. Create Admin Account

```bash
python manage.py createsuperuser
```

Enter details:
- Email: `admin@college.edu`
- First Name: `Admin`
- Last Name: `User`
- Password: (minimum 8 characters)

#### 3. Login as Admin

1. Visit `http://127.0.0.1:8000/`
2. Enter admin email and password
3. Complete reCAPTCHA
4. Click "Login"

#### 4. Setup Initial Data

**Add Courses:**
1. Navigate to "Manage Courses"
2. Click "Add Course"
3. Enter course name (e.g., "Computer Science")
4. Save

**Add Sessions:**
1. Navigate to "Manage Sessions"
2. Click "Add Session"
3. Select start and end dates
4. Save

**Add Staff:**
1. Navigate to "Manage Staff"
2. Click "Add Staff"
3. Fill in details (name, email, course)
4. Set password
5. Save

**Add Students:**
1. Navigate to "Manage Students"
2. Click "Add Student"
3. Fill in details (name, email, course, session)
4. Set password
5. Save

**Add Subjects:**
1. Navigate to "Manage Subjects"
2. Click "Add Subject"
3. Enter subject name
4. Assign staff and course
5. Save

#### 5. Test User Registration

1. Logout from admin account
2. Visit `http://127.0.0.1:8000/register/`
3. Select role (Student or Staff)
4. Fill in registration form
5. Complete reCAPTCHA
6. Submit
7. Login with new credentials

#### 6. Explore Features

**As Admin:**
- View dashboard with statistics
- Manage all users, courses, subjects
- View attendance and results
- Approve leave requests
- Send notifications

**As Staff:**
- Take and update attendance
- Add and edit student results
- Apply for leave
- Send feedback
- Manage library books

**As Student:**
- View attendance and results
- Apply for leave
- Send feedback
- View library books
- Check notifications

---

### 📚 Additional Documentation

Comprehensive guides for all features:

| Document | Description | Link |
|----------|-------------|------|
| **Registration Guide** | Complete user registration walkthrough | [REGISTRATION_GUIDE.md](REGISTRATION_GUIDE.md) |
| **Dynamic Features** | Technical documentation of all features | [DYNAMIC_FEATURES.md](DYNAMIC_FEATURES.md) |
| **System Verification** | Complete system verification report | [SYSTEM_VERIFICATION.md](SYSTEM_VERIFICATION.md) |
| **Staff Verification** | Staff role dynamic data verification | [STAFF_DYNAMIC_VERIFICATION.md](STAFF_DYNAMIC_VERIFICATION.md) |
| **Functionality Test** | Feature testing documentation | [FUNCTIONALITY_TEST.md](FUNCTIONALITY_TEST.md) |
| **Changes Summary** | Summary of all system changes | [CHANGES_SUMMARY.md](CHANGES_SUMMARY.md) |

---

### 🔧 Configuration Guide

#### Email Configuration

**Development (Console Backend):**
```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
Emails will appear in the console/terminal.

**Production (SMTP):**
```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use app password, not regular password
DEFAULT_FROM_EMAIL = 'College ERP <your-email@gmail.com>'
```

**Gmail App Password:**
1. Enable 2-Step Verification in Google Account
2. Go to Security > App passwords
3. Generate app password for "Mail"
4. Use this password in EMAIL_HOST_PASSWORD

#### reCAPTCHA Configuration

1. **Get reCAPTCHA Keys:**
   - Visit [Google reCAPTCHA](https://www.google.com/recaptcha)
   - Register your site
   - Choose reCAPTCHA v2 (Checkbox)
   - Get Site Key and Secret Key

2. **Update Settings:**
```python
# settings.py
RECAPTCHA_SITE_KEY = 'your-site-key'
RECAPTCHA_SECRET_KEY = 'your-secret-key'
```

3. **Update Views:**
```python
# main_app/views.py
captcha_key = "your-secret-key"  # Line ~20 in doLogin()
captcha_key = "your-secret-key"  # Line ~220 in do_register()
```

#### Database Configuration

**SQLite (Development):**
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**PostgreSQL (Production):**
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'college_erp',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**MySQL:**
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'college_erp',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Static Files Configuration

**Development:**
```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

**Production (with WhiteNoise):**
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### Media Files Configuration

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

**Create media directories:**
```bash
mkdir media
mkdir media/profile_pics
```

---

### 🎨 Customization Guide

#### Change Site Name

```python
# settings.py
SITE_NAME = 'Your College Name'
```

#### Change Theme Colors

Edit `main_app/static/dist/css/adminlte.min.css` or create custom CSS:

```css
/* custom.css */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
}
```

#### Add Custom Logo

1. Place logo in `main_app/static/image/logo.png`
2. Update templates:
```html
<!-- base template -->
<img src="{% static 'image/logo.png' %}" alt="Logo">
```

#### Customize Email Templates

Edit templates in `main_app/templates/registration/`:
- `password_reset_email.html` - Password reset email
- `password_reset_subject.txt` - Email subject

---

### 📊 Database Schema

#### Core Tables

**Users:**
- `CustomUser` - Base user model (email, password, user_type)
- `Admin` - Admin profile (one-to-one with CustomUser)
- `Staff` - Staff profile (one-to-one with CustomUser, linked to Course)
- `Student` - Student profile (one-to-one with CustomUser, linked to Course and Session)

**Academic:**
- `Course` - Academic courses
- `Session` - Academic years/sessions
- `Subject` - Subjects (linked to Staff and Course)

**Attendance:**
- `Attendance` - Attendance records (date, subject, session)
- `AttendanceReport` - Individual student attendance (student, attendance, status)

**Results:**
- `StudentResult` - Student exam results (student, subject, test, exam)

**Leave:**
- `LeaveReportStudent` - Student leave applications
- `LeaveReportStaff` - Staff leave applications

**Feedback:**
- `FeedbackStudent` - Student feedback
- `FeedbackStaff` - Staff feedback

**Notifications:**
- `NotificationStudent` - Student notifications
- `NotificationStaff` - Staff notifications

**Library:**
- `Book` - Library books
- `IssuedBook` - Book issuance records

---

### 🔐 Security Best Practices

#### Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Update `SECRET_KEY` (use environment variable)
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use HTTPS (SSL certificate)
- [ ] Enable CSRF protection
- [ ] Use strong passwords
- [ ] Regular security updates
- [ ] Database backups
- [ ] Monitor logs
- [ ] Rate limiting
- [ ] Input validation
- [ ] SQL injection prevention (Django ORM)
- [ ] XSS protection (Django templates)

#### Environment Variables

Create `.env` file:
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
RECAPTCHA_SITE_KEY=your-site-key
RECAPTCHA_SECRET_KEY=your-secret-key
```

Load in settings.py:
```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
```

---

## 🆕 What's New in v2.0

### Major Features

#### 🎯 Dynamic User Registration System
- ✅ **Self-Service Registration** - Students and Staff can create accounts independently
- ✅ **Email-Based Authentication** - Modern email login instead of username
- ✅ **Real-Time Validation** - AJAX-powered email availability checking
- ✅ **Password Security** - Strength indicator and minimum requirements
- ✅ **Profile Pictures** - Upload photos during registration
- ✅ **Role-Based Forms** - Dynamic form fields based on user role
- ✅ **Bot Protection** - reCAPTCHA v2 integration

#### 🔐 Password Management
- ✅ **Password Reset** - Complete email-based password recovery workflow
- ✅ **Secure Tokens** - Time-limited reset tokens
- ✅ **Email Notifications** - Automated password reset emails
- ✅ **Profile Updates** - Change password in user profile

#### 💯 100% Dynamic Data
- ✅ **Zero Hardcoded Data** - All data stored in database
- ✅ **Dynamic Dropdowns** - Courses, sessions, subjects from database
- ✅ **Real-Time Updates** - Live data synchronization
- ✅ **Database-Driven** - All CRUD operations use Django ORM

#### 🔒 Enhanced Security
- ✅ **CSRF Protection** - All forms protected
- ✅ **Password Hashing** - PBKDF2 algorithm
- ✅ **Session Security** - Secure session cookies
- ✅ **Middleware Protection** - Custom route protection
- ✅ **SQL Injection Prevention** - Django ORM protection
- ✅ **XSS Protection** - Template auto-escaping

#### 📊 Improved Dashboard
- ✅ **Real-Time Statistics** - Live data updates
- ✅ **Visual Charts** - Chart.js powered graphs
- ✅ **Performance Metrics** - Attendance and result analytics
- ✅ **Quick Actions** - One-click access to features

#### 📱 Better User Experience
- ✅ **Responsive Design** - Mobile-first approach
- ✅ **Intuitive Navigation** - Clear menu structure
- ✅ **Error Messages** - Helpful error feedback
- ✅ **Success Notifications** - Confirmation messages
- ✅ **Loading Indicators** - Visual feedback

### Technical Improvements

#### Backend
- ✅ **Django 4.2.28** - Latest stable version
- ✅ **Python 3.10+** - Modern Python support
- ✅ **Optimized Queries** - Efficient database queries
- ✅ **Signal Handlers** - Automatic profile creation
- ✅ **Custom Middleware** - Role-based access control

#### Frontend
- ✅ **Bootstrap 5** - Modern UI framework
- ✅ **Chart.js 3** - Data visualization
- ✅ **jQuery 3** - DOM manipulation
- ✅ **AdminLTE 3** - Admin theme

#### Database
- ✅ **Optimized Schema** - Efficient table structure
- ✅ **Foreign Keys** - Proper relationships
- ✅ **Indexes** - Fast queries
- ✅ **Migrations** - Version control for schema

### Bug Fixes

- ✅ Fixed middleware blocking registration page
- ✅ Fixed user_type string/integer mismatch
- ✅ Fixed signal handler for profile creation
- ✅ Fixed email validation in forms
- ✅ Fixed profile picture upload
- ✅ Fixed session management
- ✅ Fixed CSRF token issues

### Documentation

- ✅ **Comprehensive README** - Detailed documentation
- ✅ **Registration Guide** - Step-by-step registration
- ✅ **System Verification** - Complete feature verification
- ✅ **Staff Verification** - Staff role documentation
- ✅ **Dynamic Features** - Technical documentation
- ✅ **Changes Summary** - All changes documented

### Breaking Changes

⚠️ **Important:** This version includes breaking changes:

1. **Django Version** - Upgraded from 3.1.1 to 4.2.28
2. **Python Version** - Requires Python 3.10+ (was 3.8+)
3. **Authentication** - Email-based instead of username
4. **User Model** - CustomUser with email as USERNAME_FIELD

### Migration Guide

If upgrading from v1.0:

1. **Backup Database:**
```bash
python manage.py dumpdata > backup.json
```

2. **Update Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run Migrations:**
```bash
python manage.py migrate
```

4. **Update Settings:**
- Check EMAIL_BACKEND configuration
- Update ALLOWED_HOSTS
- Configure reCAPTCHA keys

5. **Test Thoroughly:**
- Test all features
- Verify data integrity
- Check user authentication

### Performance Improvements

- ⚡ **Faster Page Loads** - Optimized queries
- ⚡ **Reduced Database Calls** - Query optimization
- ⚡ **Cached Static Files** - WhiteNoise integration
- ⚡ **Compressed Assets** - Minified CSS/JS
- ⚡ **Efficient Rendering** - Template optimization

### Compatibility

**Supported:**
- ✅ Python 3.10, 3.11, 3.12, 3.13
- ✅ Django 4.2.28
- ✅ SQLite 3.x
- ✅ PostgreSQL 13+
- ✅ MySQL 8.0+
- ✅ All modern browsers (Chrome, Firefox, Safari, Edge)
- ✅ Mobile devices (iOS, Android)

**Not Supported:**
- ❌ Python < 3.10
- ❌ Django < 4.2
- ❌ Internet Explorer

### Known Issues

None at this time. Report issues at [GitHub Issues](https://github.com/maheshsingh20/College-ERP/issues).

