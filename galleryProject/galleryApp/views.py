from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import picEdit,UploadFileForm
from .forms import createForm
from django.contrib import messages

# Create your views here.
def home(request):
    picEdit_obj = picEdit.objects
    return render(request, 'home.html', {"home_key": picEdit_obj})

def detail(request, detail_id):
    detail_obj = get_object_or_404(picEdit, pk = detail_id)
    return render(request, 'detail.html', {"detail_key":detail_obj})

def new(request):
    form = createForm()
    if request.method =='POST':
        pass
    elif request.method =='GET':
        form = createForm()
        return render(request, 'create.html', {'form':form})
    else:
        pass

def create(request):
    picedit = picEdit()
    picedit.title = request.POST.get('title', False)
    picedit.explain = request.POST.get('explain', False)
    picedit.pic = request.FILES.get('pic', False)
    picedit.day = request.POST.get('day', False)
    picedit.save()
    messages.info(request, '추가')
    return redirect('home')

def update(request, update_id):
    update_obj = get_object_or_404(picEdit, pk = update_id)
    if request.method == "POST":
        update_obj.title = request.POST.get('title', False)
        update_obj.explain = request.POST.get('explain', False)
        update_obj.pic = request.FILES.get('pic',False)
        update_obj.save()
        return redirect(reverse('detail', args = [update_id]))
    else:
        pass
    return render(request, 'update.html', {"update_key":update_obj})


def delete(request, delete_id):
    delete_obj = get_object_or_404(picEdit, pk = delete_id)
    delete_obj.delete()
    return redirect('home')