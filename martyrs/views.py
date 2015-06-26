from django.shortcuts import render
from django.http import HttpResponse
from .models import Martyr
from .forms import MartyrForm

def index(request):
    if request.method == 'GET':
        martyrs = Martyr.objects.all()
        return render(request, 'martyrs/index.html', {'martyrs': martyrs})
    elif request.method == 'POST':
        pass
    else:
        return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, martyr_id):
    try:
        martyr = Martyr.objects.get(id=martyr_id)
        return render(request, 'martyrs/detail.html', {'martyr': martyr})
    except (KeyError, Martyr.DoesNotExist):
        # Martyr with matching ID doesn't exist
        return HttpResponse("Doesn't exist")

def delete(request, martyr_id):
    try:
        Martyr.objects.get(id=martyr_id).delete()
    except (KeyError, Martyr.DoesNotExist):
        # Martyr with matching ID doesn't exist
        return HttpResponse("Doesn't exist")
    except:
        pass

def update(request, martyr_id):
    pass