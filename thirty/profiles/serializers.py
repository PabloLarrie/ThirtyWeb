from rest_framework import serializers

from thirty.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "distinction",
            "user",
            "image",
            "bio",
            "friends",
            "posts",
        ]

    # def create(self, validated_data):
    #     designers_data = validated_data.pop("designer", [])
    #     new_game = super().create(validated_data)
    #     for v in designers_data:
    #         new_game.designer.add(Designers.objects.get(id=v["id"]))
    #     new_game.save()
    #     return new_game


class ProfileSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "image",
        ]




