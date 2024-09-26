# Signals Test Project
### This Django project demonstrates the use of Django signals, specifically the post_save signal, to execute a function after a model instance is saved. It includes a basic Django setup and a script to test the signal functionality.
## Project Structure

```bash
Question1/
├── README.md
└── signals_test
    ├── db.sqlite3
    ├── example.py  # Script to test signal execution and measure save time
    ├── manage.py  # Django management commands
    ├── myapp
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py  # Model definitions
    │   ├── signals.py  # Signal handlers for the models
    │   ├── tests.py
    │   └── views.py
    └── signals_test
        ├── asgi.py
        ├── __init__.py
        ├── settings.py  # Django settings file
        ├── urls.py
        └── wsgi.py
```

## Setup
### Clone the repository:

```bash
git clone <repository-url>
cd signals_test
```

### Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the required packages:

```bash
pip install django
```
### Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the development server:

```bash
python manage.py runserver
```

## Signal Setup
The signals.py file contains a signal handler that listens for the post_save signal of the MyModel model. When a MyModel instance is saved, the handler introduces a 5-second delay to simulate a long-running operation.

`File: myapp/signals.py`

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import time

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received. Executing synchronously...")
    time.sleep(5) 
    print("Signal finished after delay.")
```
## Running the Example Script
The example.py script measures the time taken to save an object and triggers the signal.

`Steps to run:`

### Run the script:

```bash
python example.py
```
`Expected Output:`

The script will create and save an instance of MyModel and print the time taken for the operation.

```bash
Signal received. Executing synchronously...
Signal finished after delay.
Time taken for save operation: 5.XXXX seconds
The delay introduced in the signal handler should be reflected in the time printed.
```