from django.shortcuts import render
from celery.result import AsyncResult
from example.tasks import go_to_sleep, add

# Create your views here.
def index(request):
    go_to_sleep.delay(5)
    task_id = add.delay(1,3)
    result = AsyncResult(task_id)
    print(result.state)
    print(result.ready)
    return render(request, 'example/index.html')