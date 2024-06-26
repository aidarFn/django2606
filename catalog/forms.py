from django import forms
from main_menu import models


class CatalogForm(forms.ModelForm):
    class Meta:
        model = models.PopularProduct
        fields = "__all__"
