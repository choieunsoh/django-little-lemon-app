# define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:id>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
