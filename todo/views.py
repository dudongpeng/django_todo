from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from .models import Todo,User
from datetime import datetime


# Create your views here.
def index(request):
    x = Todo.objects.select_related().order_by('status', '-creat_time')
    content = {
        'x': x
    }
    return render(request, 'todo/index.html', content)


def detail(request, id):
    x = Todo.objects.get(pk=id)
    i = Todo.objects.all()
    context = {
        'x': x,
        'i': i
    }
    return render(request, 'todo/detail.html', context)


def finish(request, id):
    x = Todo.objects.get(pk=id)
    x.status = True
    x.finish_time = datetime.now()
    x.save()
    return HttpResponseRedirect(reverse('todo:index'))


def cancel(request, id):
    x = Todo.objects.get(pk=id)
    x.status = False
    x.save()
    return HttpResponseRedirect(reverse('todo:index'))


def create(request):
    content = request.POST["content"]
    x = Todo(content=content,
             creat_time=datetime.now(),
             qid_id=1
             )
    x.save()

    return HttpResponseRedirect(reverse('todo:index'))





