from rest_framework import serializers

from .models import Category, Director, Movie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
        read_only_fields = ("id",)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("id", "name")
        read_only_fields = ("id",)


class MovieSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True,
    )
    new_category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True,
        write_only=True,
    )

    director = DirectorSerializer(
        read_only=True,
    )
    new_director = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(),
        required=True,
        write_only=True,
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "name",
            "new_director",
            "director",
            "new_category",
            "category",
            "release_date",
            "created_at",
        )
        read_only_fields = ("id", "created_at")

    def validate(self, attrs):
        attrs["category"] = attrs.pop("new_category")
        attrs["director"] = attrs.pop("new_director")
        return attrs
