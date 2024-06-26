from django.shortcuts import render
from . import models
from django.views import generic


class MainMenuView(generic.ListView):
    template_name = 'menu/main_menu.html'
    context_object_name = 'slogan'
    model = models.Slogan
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_url'] = models.Video.objects.order_by('-id')
        context['popular_product'] = models.PopularProduct.objects.order_by('-id')
        return context

