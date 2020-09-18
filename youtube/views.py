from django.shortcuts import render
from .models import Youtube
# Create your views here.
def youtuber(request):
    youtubes = Youtube.objects.all()
    return render(request, 'youtube.html', {'youtubes':youtubes})