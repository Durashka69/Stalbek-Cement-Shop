from rest_framework import serializers

from mainapp.models import Category, Product, Raiting


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class RaitingSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Raiting
        fields = ('id', 'user', 'username', 'product', 'score', 'comment')
        read_only_fields = ('user',)

    def create(self, validated_data):
        raiting = Raiting.objects.filter(
            user=validated_data.get('user'), product=validated_data.get('product')
        ).first()
        if raiting:
            raiting.score = validated_data.get('score')
            if not raiting.comment:
                raiting.comment = validated_data.get('comment')
            raiting.save()
            return raiting
        raiting = Raiting.objects.create(
            user=validated_data.get('user'),
            product=validated_data.get('product'),
            score=validated_data.get('score'),
            comment=validated_data.get('comment'),
        )
        return raiting


class ProductSerializer(serializers.ModelSerializer):
    raiting = RaitingSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'image', 'raiting',)
