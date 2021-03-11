from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from expense.models import Expense, Tag
from expense.serializers import ExpenseSerializer, TagSerializer


@ensure_csrf_cookie
@api_view(['GET'])
def set_cookie(request):
    return Response()


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('timestamp')
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated,)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)