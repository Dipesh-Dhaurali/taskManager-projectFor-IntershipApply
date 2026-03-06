# Task Management System - API Postman Collection (V2.0)

This guide describes the updated API endpoints, including the new professional statistics features.

---

## 1. Authentication

### Register User
- **URL**: `/api/register/`
- **Method**: `POST`
- **Body** (JSON):
  ```json
  {
    "username": "newuser",
    "email": "user@example.com",
    "password": "password123"
  }
  ```

### Login (Obtain JWT Tokens)
- **URL**: `/api/login/`
- **Method**: `POST`
- **Body** (JSON):
  ```json
  {
    "username": "newuser",
    "password": "password123"
  }
  ```
- **Response**: `200 OK` with `access` and `refresh` tokens.

---

## 2. Task Management (Auth Required)
*Header: `Authorization: Bearer <access_token>`*

### 📊 Dashboard Statistics (New)
- **URL**: `/task/api/tasks/statistics/`
- **Method**: `GET`
- **Description**: Returns a professional summary of the user's productivity.
- **Sample Response**:
  ```json
  {
    "total_tasks": 10,
    "completed_tasks": 6,
    "pending_tasks": 4,
    "completion_rate": 60.0
  }
  ```

### List My Task History
- **URL**: `/task/api/tasks/`
- **Method**: `GET`
- **Description**: Returns all tasks belonging to the current user, ordered by most recent.

### Create Task
- **URL**: `/task/api/tasks/`
- **Method**: `POST`
- **Body** (JSON):
  ```json
  {
    "title": "My New Task",
    "description": "Details about the task",
    "status": "Pending"
  }
  ```

### Update/Edit Task
- **URL**: `/task/api/tasks/<task_id>/`
- **Method**: `PUT` or `PATCH`
- **Body** (JSON):
  ```json
  {
    "title": "Updated Title",
    "status": "Completed"
  }
  ```

### Delete Task
- **URL**: `/task/api/tasks/<task_id>/`
- **Method**: `DELETE`

---

## 💡 Postman Pro Tips:
1. **Environment**: Create a `base_url` variable set to `http://127.0.0.1:8000`.
2. **Auto-Auth**: In the Collection settings, go to the **Auth** tab, select **Bearer Token**, and use `{{access_token}}`.
3. **Tests**: Add a test script to your login request to automatically update your `access_token` variable.
   ```javascript
   var jsonData = JSON.parse(responseBody);
   postman.setEnvironmentVariable("access_token", jsonData.access);
   ```
