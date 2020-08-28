from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect


class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    def get_queryset(self): #ListView에서 사용-표시 하려는 개체 목록을 결정한다. 
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post #queryset = Post.objects.all()이랑 같은 기능
    template_name = 'detail.html'
    context_object_name='ppost'

    def get_context_data(self, **kwargs):
        context_data =  super(DetailView, self).get_context_data(**kwargs)
        context_data['form'] = CommentForm()
        context_data['comments'] = self.object.comment_set.all() #DetailView에서 가져오는 애를 열람할수 있음(_set)
        context_data['author'] = self.object.author
        return context_data

def comment_create(request, post_id):
    if not request.user.is_anonymous:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
        else:
            messages.info(request, "올바르지 않은 댓글 형식입니다.")
    else:
        messages.info(request, "로그인이 필요합니다.")
    return HttpResponseRedirect(reverse('detail', args = (post_id,)))

def comment_edit(request, comment_id, post_id):
    comments = Comment.objects.get(pk=comment_id)
    if comments.author != request.user:
        messages.warning(request, '권한이 없습니다')
        return HttpResponseRedirect(reverse('detail',args=(post_id,)))
    if request.method=="POST":
        edited = CommentForm(request.POST, instance = comments)
        if edited.is_valid():
            edited.save()
            return HttpResponseRedirect(reverse('detail', args = (post_id,)))
    else:
        edited = CommentForm(instance=comments)
    return render(request,'edit.html',{'post_id':post_id , 'comment_id' : comment_id, 'edited':edited})       
                


def comment_delete(request, comment_id, post_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if my_comment.author == request.user:
        my_comment.delete()
    else:
        messages.info(request, "권한이 없습니다.")
    return HttpResponseRedirect(reverse('detail', args = (post_id,)))