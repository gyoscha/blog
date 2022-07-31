from django.urls import path, include

from . import views

urlpatterns = [
    path('notes/', views.NoteAPIView.as_view()),
    path('notes/<int:pk>/', views.NoteDetailAPIView.as_view()),
    path('accounts/', views.UsersAPIView.as_view(), name='users'),
    path('accounts/<int:pk>/', views.UsersDetailAPIView.as_view()),
]
