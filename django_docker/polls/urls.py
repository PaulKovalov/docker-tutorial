from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail_poll, name='poll_detail'),
    path('<int:poll_id>/question/<int:q_id>/answer/<int:a_id>/vote', views.vote_poll, name='poll_vote')
]