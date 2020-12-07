from django.shortcuts import render, redirect

from hw_21.forms import PersonForm
from hw_21.models import Person


def home_page(request):
    context = {'person': Person.objects.all()}
    return render(request, 'home.html', context=context)


def add_person(request):
    if request.method == 'GET':
        context = {'person_form': PersonForm}
        return render(request, 'add_students.html', context=context)
    elif request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
