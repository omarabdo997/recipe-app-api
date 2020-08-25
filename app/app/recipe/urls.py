from django.urls import path
from recipe import views


app_name = 'recipe'

urlpatterns = [
    path('tags/', views.ListTags.as_view(), name='tags'),
    path('tags/<int:pk>/', views.CreateTag.as_view(), name='tags'),
]
