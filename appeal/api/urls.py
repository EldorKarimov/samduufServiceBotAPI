from django.urls import path
from . import views

urlpatterns = [
    path('create/requested-user/', views.RequestedUserCreateView.as_view()),
    path('create/message/', views.RequestedUserMessageCreateAPIView.as_view())
]