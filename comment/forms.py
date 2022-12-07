from django import forms
from .models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'userNameField'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
