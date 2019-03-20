from django import forms
from .models import Project,Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','usability','design','content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile']
class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['link','description','profile','image','title']
