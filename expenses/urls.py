from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expenses.views import ExpenseViewSet

router = DefaultRouter()
router.register('expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),
]