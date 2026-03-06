# TaskMaster - Professional Task Management System

TaskMaster is a full-stack, professional-grade task management application built with a modern API-first architecture. It features a robust Django REST Framework (DRF) backend, secure JWT authentication, and a sleek, dynamic frontend.

---

## 🚀 Tech Stack

- **Backend**: Django 6.0.3 (Latest Python 3.14 compatible version)
- **API Framework**: Django REST Framework (DRF)
- **Authentication**: SimpleJWT (JSON Web Tokens)
- **Database**: MySQL (Professional-grade relational database)
- **Frontend**: HTML5, CSS3, Bootstrap 5 (Styling), Vanilla JavaScript (Dynamic UI)
- **Icons**: Bootstrap Icons

---

## 🛠️ How it Works

### 1. API-First Architecture (DRF)
The project is built around DRF. Every action (login, registration, task creation, statistics) happens via asynchronous API calls.
- **Serializers**: Handle complex data types, converting between Python objects and JSON.
- **ViewSets**: Provide standardized logic for CRUD (Create, Read, Update, Delete) operations.
- **Custom Actions**: I implemented a specialized `@action` in `TaskViewSet` to calculate real-time user statistics (Total, Completed, Pending, Completion Rate).

### 2. Security & JWT Handling
- **Stateless Auth**: Uses JSON Web Tokens. After login, the server returns an `access` and `refresh` token.
- **Secure Storage**: Tokens are stored in the browser's `localStorage` and sent in the `Authorization: Bearer <token>` header for every protected request.
- **Ownership Validation**: Every API request is filtered to ensure a user can *only* see and modify tasks they created.

### 3. Dynamic Frontend (Vanilla JS)
Instead of traditional page reloads, the application uses Vanilla JS to:
- **Fetch Data**: Retrieve task history and statistics without refreshing the page.
- **DOM Manipulation**: Dynamically build task tables and update statistics cards.
- **Authentication Guards**: Check for tokens on page load and redirect unauthorized users to the login page.
- **Real-time Notifications**: Custom notification system for immediate user feedback.

---

## ✨ Features

### 👤 User Features
- **Modern Landing Page**: Professional introduction to the platform.
- **Dashboard Command Center**: View productivity metrics at a glance.
- **Task History**: Complete history of all tasks with status indicators.
- **Easy Task Creation**: Dedicated page for adding new tasks with descriptions.
- **CRUD Operations**: Edit or delete tasks directly from the dashboard.

### 🔑 Admin Features
- **Admin Panel**: Dedicated portal to manage all users and tasks.
- **Audit Capability**: View which user created which task for system-wide monitoring.
- **Data Integrity**: Manage and filter tasks by status or owner.

---

## 💻 Local Setup Guide

### Prerequisites
- Python 3.10+ (Tested on 3.14)
- MySQL Server installed and running

### Installation Steps

1. **Download/Clone the Project**:
   ```bash
   git clone <repository_url>
   cd taskManager
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration**:
   - Create a MySQL database:
     ```sql
     CREATE DATABASE task_manager_db;
     ```
   - Open `taskManager/settings.py` and update the `DATABASES` section with your MySQL `USER` and `PASSWORD`.

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create Admin User**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Server**:
   ```bash
   python manage.py runserver
   ```
   Visit: `http://127.0.0.1:8000/`

---

## 📂 Project Structure
- `home/`: Authentication, landing pages, and base templates.
- `task/`: Task models, dashboard, and the core API logic.
- `taskManager/`: Project configuration and settings.
