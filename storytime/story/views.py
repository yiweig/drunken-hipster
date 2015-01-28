from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Line

# Create your views here.
def home(request):
	return render_to_response("story/home.html", {'lines': Line.objects.all() })
