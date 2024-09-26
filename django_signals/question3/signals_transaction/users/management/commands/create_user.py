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