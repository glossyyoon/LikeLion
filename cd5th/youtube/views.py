from django.shortcuts import render,get_object_or_404
from .models import Youtube
# Create your views here.
def youtuber(request):
    youtubes = Youtube.objects.all()
    return render(request, 'youtube.html', {'youtubes':youtubes})

def detail(request, detail_id):
    detail = get_object_or_404(Youtube, pk = detail_id)
    return render(request, 'detail.html', {'content':detail})