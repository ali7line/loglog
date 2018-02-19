from django import forms
from django.core.exceptions import ValidationError

from .models import Topic, Type, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be create')
        return new_slug


class TopicAddEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be create')
        return new_slug
