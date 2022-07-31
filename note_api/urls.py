from django.urls import path, include

from . import views

urlpatterns = [
    path('notes/', views.NoteAPIView.as_view()),
    path('notes/<int:pk>/', views.NoteDetailAPIView.as_view()),
    path('users/', views.UsersAPIView.as_view()),
    path('users/<int:pk>/', views.UsersDetailAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
