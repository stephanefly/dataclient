from django.urls import path
from app import views

urlpatterns = [
    path('', views.formulaire_evenement, name='formulaire_evenement'),
    path('next_row/', views.next_row, name='next_row'),  # Nouvelle URL pour passer à la ligne suivante
    path('reformate/', views.preparation_text, name='preparation_text'),  # Nouvelle URL pour passer à la ligne suivante

]
