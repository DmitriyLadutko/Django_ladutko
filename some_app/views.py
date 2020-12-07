from django.http import HttpResponse
from django.shortcuts import render, loader

NAME_TEMPLATE = 'name.html'
PRINT_TEMPLATE_NAME = 'print_name.html'
INPUT_NAME = 'input_name.html'


def hello_user(request):
    template = loader.get_template('hello_user.html')
    context = {"name": None}
    return HttpResponse(template.render(context, request))
