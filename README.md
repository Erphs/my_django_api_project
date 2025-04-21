
# Django Todo API Project

This is a simple API to manage tasks (CRUD) built with Django and Django REST Framework. This project is designed for learning purposes and to demonstrate how to create a RESTful API with Django.

## Features
- Full **CRUD** operations for tasks
- Built with Django and Django REST Framework
- Endpoints for listing tasks, creating new tasks, updating tasks, and deleting tasks

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Erphs/my-django-api-project.git
```

### 2. Install dependencies:
First, create a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

Then install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set up the database:
Run migrations to set up the database schema:
```bash
python manage.py migrate
```

### 4. Run the development server:
To run the project locally, use the following command:
```bash
python manage.py runserver
```

Now you can access the API at:
```
http://127.0.0.1:8000/api/
```

## API Endpoints
- **GET** `/api/tasks/` - Get a list of all tasks
- **POST** `/api/tasks/` - Create a new task
- **GET** `/api/tasks/{id}/` - Get a task by ID
- **PUT** `/api/tasks/{id}/` - Update a task by ID
- **PATCH** `/api/tasks/{id}/` - Partially update a task by ID
- **DELETE** `/api/tasks/{id}/` - Delete a task by ID

## Developers
- **Your Name** - [My GitHub Profile](https://github.com/Erphs)
- **Roxana** - Assisting with API development and README writing

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
