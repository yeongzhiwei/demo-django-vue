from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from expense.models import Expense, Tag
from expense.serializers import ExpenseSerializer, TagSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tags': reverse('tag-list', request=request, format=format),
        'expenses': reverse('expense-list', request=request, format=format)
    }) 


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('timestamp')
    serializer_class = ExpenseSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer