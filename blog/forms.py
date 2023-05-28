from django import forms
from .models import Post, UserReport

from django.conf import settings
from django.core.mail import send_mail

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class ContactForm(forms.Form):

    username = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Emri'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Përshkrimi'}))

    def get_info(self):

        cl_data = super().clean()

        username = cl_data.get('username').strip()
        from_email = cl_data.get('email')

        msg = f'{username} with email {from_email} said:'
        msg += cl_data.get('text')

        return msg

    def send(self):

        msg = self.get_info()

        send_mail(
            subject="New mail",
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )