from django.shortcuts import render,get_object_or_404,redirect
from .models import prac
from .forms import createForm

# Create your views here.
def home(request):
    crud = prac.objects.all()
    return render(request, 'home.html', {'crud_key':crud})

def detail(request, detail_id):
    detail = get_object_or_404(prac, pk = detail_id)
    return render(request, 'detail.html', {'content':detail})

def new(request):
    form = createForm()
    if request.method =='POST':
        pass
    elif request.method =='GET':
        form = createForm
        return render(request, 'new.html',{'form':form})
    else:
        pass

def create(request):
    prac.photo = request.FILES['photo']
    prac.save()
    return redirect('')

