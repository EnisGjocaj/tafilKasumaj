from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .forms import EmailForm

from django.urls import reverse_lazy


from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView

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


# class reportUser(FormView):
# 	template_name = 'report.html'
# 	form_class = ContactForm
# 	success_url = reverse_lazy('blog:success')

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['form'] = self.form_class()
# 		return context

# 	def form_valid(self, form):
# 		# Calls the custom send method
# 		form.send()
# 		return super().form_valid(form)

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['username']
            sender_email = form.cleaned_data['email']
            text = form.cleaned_data['text']

            from_email = 'enisgjocaj1@hotmail.com'  # Use your desired sender email address
            recipient_email = 'enisgjocaj1@hotmail.com'  # Specify the recipient email address

            # Construct the email content
            email_content = f"From: {sender_name} <{sender_email}>\n\n{text}"

            # Send the email using Django's send_mail() function
            send_mail('Email i ri', email_content, from_email, [recipient_email])

			return redirect('blog:success')  # Redirect to a success page or appropriate URL

	else:
		form = EmailForm()

	return render(request, 'report.html', {'form': form})


       
class ContactSuccessView(TemplateView):
    template_name = 'success.html'