from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
class index(ListView):
    template_name = 'index.html'
    context_object_name = 'blog_list'
    def get_queryset(self):
        return Blog.objects.all #Blog모델을 가져오고 이름을 부여하고 싶음 -> 'blog_list'

class detail(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'

class delete(DeleteView):
    model = Blog
    template_name = 'delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('index')

class update(UpdateView):
    model = Blog
    template_name = 'update.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('index')

class create(CreateView):
    model = Blog
    template_name = 'create.html'
    fields = ['title', 'text']

    def form_vaild(self,form):
        Blog = form.save(commit=False)
        Blog.author = self.request.user
        Blog.save()
        return HttpResponseRedirect(self.request.POST.get('index'))
    def get_absolute_url(self):
        return u'/some_url/%d' % self.id 

# def result(request):
#     BlogPosts = Blog.objects.all()
#     query = request.GET.get('query', '')

#     if query:
#         BlogPosts = BlogPosts.file