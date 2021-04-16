import django.forms as forms
from django_tagify.fields import TagsField
from .models import Game


class TagsForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['code']
