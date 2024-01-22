from django import forms
from django.forms import ModelForm

from bookshop.models import Publisher, Store, Author


class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "is_active"]


class StoreCreateForm(ModelForm):
    class Meta:
        model = Store
        fields = ["name", "books"]


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = ["age", "address", "gender"]
