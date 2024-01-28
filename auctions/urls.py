from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-job/', views.create_job, name="create-job"),
    path('auctions/make-bid/', views.make_bid, name="make-bid")
]
