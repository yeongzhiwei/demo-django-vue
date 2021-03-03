from rest_framework import serializers
from expense.models import Expense, Tag


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Expense
        fields = (
            'id', 'timestamp', 'amount', 'payee', 
            'description', 'tags', 'status'
        )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Tag
        fields = [
            'id', 'name'
        ]