from rest_framework import serializers

from thirty.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "tittle",
            "description",
            "hashtag",
            "image", 
        ]

    # def create(self, validated_data):
    #     designers_data = validated_data.pop("designer", [])
    #     new_game = super().create(validated_data)
    #     for v in designers_data:
    #         new_game.designer.add(Designers.objects.get(id=v["id"]))
    #     new_game.save()
    #     return new_game


class PostSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "tittle",
        ]




