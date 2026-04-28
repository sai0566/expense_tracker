from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user).order_by('-id')

        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')

        if category:
            queryset = queryset.filter(category=category)

        if date:
            queryset = queryset.filter(date=date)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        expenses = Expense.objects.filter(user=request.user)
        today = timezone.now().date()

        daily_total = expenses.filter(
            date=today
        ).aggregate(total=Sum('amount'))['total'] or 0

        monthly_total = expenses.filter(
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum('amount'))['total'] or 0

        yearly_total = expenses.filter(
            date__year=today.year
        ).aggregate(total=Sum('amount'))['total'] or 0

        overall_total = expenses.aggregate(
            total=Sum('amount')
        )['total'] or 0

        # Category breakdown
        categories = ['food', 'travel', 'shopping', 'bills', 'health', 'other']
        category_totals = {}
        for cat in categories:
            total = expenses.filter(category=cat).aggregate(
                total=Sum('amount')
            )['total'] or 0
            category_totals[cat] = float(total)

        # Recent 5 transactions
        recent_expenses = expenses.order_by('-date', '-id')[:5]
        recent = ExpenseSerializer(recent_expenses, many=True).data

        return Response({
            "daily_total": daily_total,
            "monthly_total": monthly_total,
            "yearly_total": yearly_total,
            "overall_total": overall_total,
            "total_count": expenses.count(),
            "category_totals": category_totals,
            "recent_expenses": recent,
        })