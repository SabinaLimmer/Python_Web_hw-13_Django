from django import forms
from django.forms import ModelForm
from .models import Author, Quote, Tag

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    tags = forms.CharField(label='Tags', max_length=20, required=False) 

    class Meta:
        model = Quote
        fields = ['author', 'tags', 'quote']

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tags'].initial = ', '.join(tag.name for tag in self.instance.tags.all())

    def save(self, commit=True):
        instance = super(QuoteForm, self).save(commit=False)
        tags_data = self.cleaned_data['tags']
        tags_list = [tag.strip() for tag in tags_data.split(',')]
        instance.save()
        instance.tags.clear()
        for tag_name in tags_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        if commit:
            instance.save()
        return instance