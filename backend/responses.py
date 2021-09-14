from rest_framework import serializers


class RoomInfoResponse(serializers.Serializer):
    _id = serializers.ReadOnlyField()
    org_id = serializers.CharField(read_only=True)
    room_user_ids = serializers.ListField(child=serializers.CharField(read_only=True))
    created_at = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(read_only=True)


class MessageResponse(serializers.Serializer):
    status = serializers.CharField(read_only=True)
    message_id = serializers.ReadOnlyField()
    data = serializers.DictField(child=serializers.CharField(), read_only=True)
    created_at = serializers.DateTimeField(read_only=True)


class CreateRoomResponse(serializers.Serializer):
    pass


class UserRoomsResponse(serializers.Serializer):
    pass