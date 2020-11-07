from .models import Ask
from django import forms

class AskForm(forms.ModelForm):
    class Meta:
        model = Ask
        fields = ('title', 'body', 'useremail', 'username')
        widgets = {
            'title':forms.TextInput(attrs={
                'class': 'form-title',
            }),
            'body':forms.TextInput(attrs={
                'class': 'form-body',
            }),
            'useremail':forms.TextInput(attrs={
                'class': 'form-useremail',
            }),
            'username':forms.TextInput(attrs={
                'class': 'form-username',
            })
        }
        def __init(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs['maxlength']=100