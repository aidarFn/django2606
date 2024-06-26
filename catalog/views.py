from . import models, forms
from django.http import HttpResponse
from datetime import datetime
import random
from main_menu import models
from django.shortcuts import render, get_object_or_404
from django.views import generic


class CatalogListView(generic.ListView):
    template_name = "catalog/product_list.html"
    context_object_name = "catalog"
    model = models.PopularProduct



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_url'] = models.Video.objects.order_by('-id')
        context['popular_product'] = models.PopularProduct.objects.order_by('-id')
        return context



    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


class CatalogDetailView(generic.DetailView):
    template_name = "catalog/product_detail.html"
    context_object_name = "catalog_id"

    def get_object(self, **kwargs):
        catalog_id = self.kwargs.get("id")
        return get_object_or_404(models.PopularProduct, id=catalog_id)


class CreateProductView(generic.CreateView):
    template_name = "catalog/product_create.html"
    form_class = forms.CatalogForm
    success_url = "/main_menu/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateProductView, self).form_valid(form=form)


class DeleteProductView(generic.DeleteView):
    template_name = "catalog/product_delete.html"
    success_url = "/main_menu/"

    def get_object(self, **kwargs):
        catalog_id = self.kwargs.get("id")
        return get_object_or_404(models.PopularProduct, id=catalog_id)


class EditProductView(generic.UpdateView):
    template_name = "catalog/product_edit.html"
    form_class = forms.CatalogForm
    success_url = "/main_menu/"

    def get_object(self, **kwargs):
        catalog_id = self.kwargs.get("id")
        return get_object_or_404(models.PopularProduct, id=catalog_id)
