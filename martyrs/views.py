from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Martyr
from .forms import MartyrForm
import traceback


def index(request):
    martyrs = Martyr.objects.all()
    if request.method == 'GET':
        add_form = MartyrForm()
        return render(request, 'martyrs/index.html', {'add_form': add_form, 'martyrs': martyrs})
    elif request.method == 'POST':
        add_form = MartyrForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'Martyr record added successfully.')
            return redirect('index')
        else:
            messages.error(request, "Please check the following form errors.")
            return render(request, 'martyrs/index.html', {'add_form': add_form, 'martyrs': martyrs})
    else:
        return render(request, 'martyrs/404.html', {'error': {'code': 404, 'text': 'A bit excited so started to look around?'}})


def detail(request, martyr_id):
    try:
        martyr = Martyr.objects.get(id=martyr_id)
        return render(request, 'martyrs/detail.html', {'martyr': martyr})
    except (KeyError, Martyr.DoesNotExist):
        # Martyr with matching ID doesn't exist
        return render(request, 'martyrs/404.html', {'error': {'code': 404, 'text': 'A bit excited so started to look around?'}})


def delete(request, martyr_id):
    try:
        Martyr.objects.get(id=martyr_id).delete()
        martyrs = Martyr.objects.all()
        messages.success(request, 'Martyr record deleted successfully.')
        return redirect('index')
    except (KeyError, Martyr.DoesNotExist):
        # Martyr with matching ID doesn't exist
        return render(request, 'martyrs/404.html', {'error': {'code': 404, 'text': 'A bit excited so started to look around?'}})


def edit(request, martyr_id):
    try:
        martyr = Martyr.objects.get(id=martyr_id)
        if request.method == 'GET':
            edit_form = MartyrForm(instance=martyr)
            return render(request, 'martyrs/edit.html', {'add_form': edit_form})
        elif request.method == 'POST':
            edit_form = MartyrForm(request.POST, instance=martyr)
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, 'Martyr %s record updated successfully.' % martyr.name)
                return redirect('index')
            else:
                messages.error(request, "Please check the following form errors.")
                return render(request, 'martyrs/edit.html', {'add_form': edit_form})
    except (KeyError, Martyr.DoesNotExist):
        return render(request, 'martyrs/404.html', {'error': {'code': 404, 'text': 'A bit excited so started to look around?'}})
