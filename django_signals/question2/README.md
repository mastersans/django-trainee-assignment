# Signals Threading Project

This Django project illustrates how Django signals operate within the same thread as the caller. It specifically utilizes the `post_save` signal to execute a function immediately after a model instance is saved, showcasing the synchronous nature of signal handling in Django.

## Project Structure

```bash
signals_thread/
├── README.md
└── signals_thread
    ├── db.sqlite3
    ├── manage.py
    ├── myapp
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py # Model definitions
    │   ├── signals.py  # Signal handlers for the models
    │   ├── tests.py
    │   └── views.py # View to create a user
    └── signals_thread
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd signals_thread
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:

```bash
pip install django
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

## Signal Setup

The `signals.py` file contains a signal handler that listens for the `post_save` signal of the `MyModel` model. When a `MyModel` instance is saved, the handler prints the thread ID of the signal handler to demonstrate that it runs in the same thread as the caller.

**File: myapp/signals.py**

```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().native_id}")
```

## Running the User Creation View

The `views.py` file includes a view that creates an instance of `MyModel` and prints the thread ID of the main request handler.

**File: myapp/views.py**

```python
from django.http import JsonResponse
from .models import MyModel
import threading

def create_user(request):
    print(f"Main thread: {threading.current_thread().native_id}")
    MyModel.objects.create(name="test_user")
    return JsonResponse({"username": "test_user", "message": "User created!"})
```

## Access the User Creation Endpoint

To trigger the signal and see the thread IDs, navigate to the following URL in your web browser or use a tool like curl or Postman:

```arduino
http://127.0.0.1:8000/create/
```

## Expected Output

Upon accessing the user creation endpoint, you should see output similar to the following in your terminal:

```bash
Main thread: 12345
Signal handler thread: 12345
```

This output confirms that both the main thread and the signal handler thread have the same thread ID, demonstrating that Django signals run in the same thread as the caller.