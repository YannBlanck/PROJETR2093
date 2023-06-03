from django.urls import path
from . import views, acheterviews

urlpatterns = [
    path('', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
    #
    path('acheterindex/', acheterviews.acheterindex),
    path('acheterajout/', acheterviews.acheterajout),
    path('achetertraitement/', acheterviews.achetertraitement),
    path('acheteraffiche/<int:id>/', acheterviews.acheteraffiche),
    path('acheterupdate/<int:id>/', acheterviews.acheterupdate),
    path('acheterupdatetraitement/<int:id>/', acheterviews.acheterupdatetraitement),
    path('acheterdelete/<int:id>/', acheterviews.acheterdelete),

]
