from django import forms
from .models import Jasosoel

class JssForm(forms.ModelForm):

    class Meta:
        model=Jasosoel
        fields=('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label="자기소개서"
        self.fields['title'].widget.attrs.update({
            'class':'jss_title',
            'placeholder':'제목',
        }
        )
