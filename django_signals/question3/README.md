# User Signal Project
### This Django project demonstrates the use of Django signals, specifically the post_save signal, to execute a function after a User model instance is saved. It showcases how transactions work in Django, including handling rollback scenarios when an error occurs during a transaction.

## Project Structure

```bash
├── README.md
└── signals_transaction
    ├── db.sqlite3
    ├── manage.py
    ├── signals_transaction
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── users
        ├── admin.py
        ├── apps.py
        ├── __init__.py
        ├── management
        │   └── commands # Command to create a user and test signal functionality
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── signals.py
        ├── tests.py
        └── views.py
```

## Setup:

### Clone the repository:
```bash
git clone <repository-url>
cd signal_transaction
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
python manage.py migrate
```

## Signal Setup

The `signals.py` file contains a signal handler that listens for the `post_save` signal of the User model. When a User instance is created, the handler prints a message. If an error occurs (simulated by raising an `IntegrityError`), the transaction is rolled back.

**File: users/signals.py**

```python
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import IntegrityError

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print(f"Signal executed for user: {instance.username}")
```

## Creating a User and Testing Transactions

The `create_user.py` management command attempts to create a User and demonstrates the rollback feature if an error occurs.

**File: users/management/commands/create_user.py**

```python
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db import IntegrityError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a user and demonstrate signal and transaction rollback'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                user = User.objects.create(username="testuser")
                print(f"User created: {user.username}")
                
                # Simulating an error to trigger rollback
                raise IntegrityError("Simulating a rollback")
        except IntegrityError:
            print("Transaction rolled back")
        
        print("Total users:", User.objects.count())
```

## Running the Command

You can run the management command to create a user and test the signal functionality along with transaction handling.

### Run the command:
```bash
python manage.py create_user
```

### Expected Output:

When you run the command, you should see output similar to the following:

```bash
User created: testuser
Transaction rolled back
Total users: 0
```