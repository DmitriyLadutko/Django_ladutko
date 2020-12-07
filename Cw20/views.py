import os

from django.http import HttpResponse
from django.shortcuts import render

from Cw20.forms import WriteLinesForm

file = 'person_data.txt'


def write_file(request):
    context = {"form": WriteLinesForm()}
    if request.method == "GET":
        return render(request, "lines.html", context=context)

    elif request.method == "POST":
        form = WriteLinesForm(request.POST)

        if not form.is_valid():
            errors = form.errors
            return HttpResponse(f'errors {errors}')

        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        age = data.get('age')
        comment = data.get('comment')

        with open(file, 'a+') as person_data_file:
            person_data_file.write(f'{first_name}|{last_name}|{age}|{comment}\n')

        return render(request, "lines.html", context=context, )


def read_file(request):
    with open(file, 'r') as person_data_file:
        file_content = person_data_file.readlines()
        if not file_content:
            return HttpResponse('Файл пуст')
    return HttpResponse(file_content)


def clear_file(request):
    open(file, 'w').close()
    return HttpResponse(f'Файл {file} очищен')
