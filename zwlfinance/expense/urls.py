from django.urls import include, path
from rest_framework.routers import DefaultRouter

from expense import views

router = DefaultRouter()
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]