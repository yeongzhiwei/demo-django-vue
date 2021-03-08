from rest_framework import serializers
from expense.models import Expense, Tag


class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Tag
        fields = [
            'id', 'name'
        ]


class ExpenseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tag_names = serializers.ListField(write_only=True)

    class Meta:
        model = Expense
        fields = (
            'id', 'timestamp', 'amount', 'payee', 
            'description', 'tags', 'tag_names', 'status'
        )

    def create(self, validated_data):
        tag_names = validated_data.pop('tag_names', [])
        tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_names]
        expense = Expense.objects.create(**validated_data)
        expense.tags.set(tags)
        return expense
