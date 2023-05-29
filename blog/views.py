from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy


from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView
from .forms import ContactForm

from .models import Post, UserReport
from django.views import generic
from django.views.generic import CreateView
from .forms import PostForm
from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#This class if for styling 
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control-title'}),
			'content': forms.Textarea(attrs={'class': 'form-control-content'}),
		}

#here it ends

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'index.html'

class DetailView(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'

class AddPostView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	success_url = reverse_lazy('blog:home')
    
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class reportForm(forms.ModelForm):
	class Meta:
		model = UserReport
		fields = '__all__'

# class reportUser(CreateView):
# 	model = UserReport
# 	form_class = reportForm
# 	template_name = "report.html"
# 	success_url = reverse_lazy('blog:success')

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['form'] = self.form_class()
# 		return context

#The code here is to delete the post

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('blog:post_detail', slug=post.slug)
    if timezone.now() - post.created_on > timezone.timedelta(minutes=30):
        return redirect('blog:post_detail', slug=post.slug)
    post.delete()
    return redirect('blog:home')


class reportUser(FormView):
    template_name = 'report.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:success')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = self.form_class()
		return context

	def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

       
class ContactSuccessView(TemplateView):
    template_name = 'success.html'