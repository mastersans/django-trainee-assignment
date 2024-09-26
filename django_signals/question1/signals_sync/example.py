import os
import django
from time import time
from django.core.management import call_command

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signals_test.settings')
django.setup()

# Create and apply migrations
call_command('makemigrations', 'myapp')
call_command('migrate')

# Import the model after setup
from myapp.models import MyModel

# Measure time to save an object
start = time()
obj = MyModel(name="Test Object")
obj.save()
end = time()

print(f"Time taken for save operation: {end - start} seconds")
