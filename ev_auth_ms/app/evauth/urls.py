from django.conf.urls import url
from app.evauth import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
]
