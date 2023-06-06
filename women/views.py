from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})

# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
