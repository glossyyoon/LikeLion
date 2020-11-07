from django.shortcuts import render, redirect
from .forms import AskForm
from .models import Ask

# Create your views here.
def main(request):
    if request.method == 'POST':
        post_form = AskForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = AskForm()

    return render(request, 'main.html', {'post_form':post_form})