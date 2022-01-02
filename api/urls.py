from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.ProjectListCreateAPIView.as_view(), name='create-list'),
    path('projects/<int:pk>', views.ProjectRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy'),
]
