from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return  render(request, 'home/onepage-particles.html')