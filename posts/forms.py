from django import forms
from tinymce import TinyMCE
from .models import post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False



class PostForm(forms.ModelForm):
    content= forms.CharField(
        widget = TinyMCEWidget(
            attrs = {'request': False, 'cols': 30, 'rows' :100}
        )

    )

    class Meta:
        model : post
        Fields = '__all__'

