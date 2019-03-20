from django import forms
from .models import Post,Profile,Project
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','post_date','likes','profilePhotos']


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Project

        exclude=['username','post_date']
