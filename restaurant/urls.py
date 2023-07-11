# define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:id>', views.SingleMenuItemView.as_view()),
]
