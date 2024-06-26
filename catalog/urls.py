from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('catalog/', views.CatalogListView.as_view()),
    path('catalog/<int:id>/', views.CatalogDetailView.as_view()),
    path('product_create/', views.CreateProductView.as_view()),
    path("catalog/<int:id>/delete/", views.DeleteProductView.as_view()),
    path("catalog/<int:id>/update/", views.EditProductView.as_view()),
]