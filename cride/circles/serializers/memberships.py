""" Membership Serializer. """

# Django REST Framework
from rest_framework import serializers

# Models
from cride.circles.models import Membership

# serializer
from cride.users.serializers import UserModelSerializer


class MembershipModelSerializer(serializers.ModelSerializer):
    """ Member model Sereializer. """

    user= UserModelSerializer(read_only=True)
    invited_by = serializers.StringRelatedField()
    joined_at = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """ Meta class. """

        model = Membership
        fields = (
            'user',
            'is_admin', 'is_active',
            'used_invitations', 'remaining_invitations',
            'invited_by',
            'rides_taken', 'rides_offered',
            'joined_at'
        )
        read_only_fields = (
            'user',
            'used_invitations',
            'invited_by',
            'rides_taken', 'rides_offered'
        )
        
        
