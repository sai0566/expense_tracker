from rest_framework import serializers
from .models import Expense


from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Expense
        fields = ['id','title','amount','category','date','note']
        read_only_fields = ['id', 'date']