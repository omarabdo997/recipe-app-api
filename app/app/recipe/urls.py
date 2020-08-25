from django.urls import path
from recipe import views


app_name = 'recipe'

urlpatterns = [
    path('tags/', views.ListTags.as_view(), name='tags'),
    path('tags/<int:pk>/', views.ManageTag.as_view(), name='tag'),
    path('ingredients/', views.ListIngredients.as_view(), name='ingredients'),
    path('ingredients/<int:pk>/', views.ManageIngredient.as_view(), name='ingredient')
]
