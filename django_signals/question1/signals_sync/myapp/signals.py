from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import time

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received. Executing synchronously...")
    time.sleep(5) 
    print("Signal finished after delay.")
