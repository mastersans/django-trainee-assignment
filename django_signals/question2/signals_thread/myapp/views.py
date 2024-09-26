from django.http import JsonResponse
from myapp.models import MyModel
import threading

def create_user(request):
    print(f"Main thread: {threading.current_thread().native_id}")
    print(f"Creating user...")# just to mimic the user creation
    MyModel.objects.create(name="test_user")
    return JsonResponse({"username": "test_user", "message": "User created!"})
