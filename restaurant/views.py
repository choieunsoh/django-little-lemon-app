from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    #queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'

    def get_object(self):
        id = self.kwargs["id"]
        return get_object_or_404(Menu, id=id)
