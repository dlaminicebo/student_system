from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('api/', views.api_page, name='api_page'),
    path('update-details/', views.update_details, name='update_details'),
    path('tasks/', views.tasks, name='tasks'),
    path('convert-pdf-to-word/', views.convert_pdf_to_word, name='convert_pdf_to_word'),
]

