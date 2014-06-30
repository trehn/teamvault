from guardian.shortcuts import assign_perm
from rest_framework import generics
from rest_framework import serializers

from .models import Password


class PasswordSerializer(serializers.ModelSerializer):
    id_token = serializers.CharField(
        read_only=True,
        required=False,
        source='id_token',
    )
    password = serializers.CharField(
        required=False,
        write_only=True,
    )
    secret_readable = serializers.BooleanField(
        read_only=True,
        required=False,
        source='id',
    )

    def transform_secret_readable(self, obj, value):
        return self.context['request'].user.has_perm('secrets.change_password', obj)

    class Meta:
        model = Password
        fields = (
            'access_policy',
            'created',
            'created_by',
            'description',
            'id_token',
            'last_read',
            'name',
            'needs_changing_on_leave',
            'password',
            'secret_readable',
            'status',
            'username',
        )
        read_only_fields = (
            'created',
            'created_by',
            'last_read',
        )

    def save_object(self, obj, **kwargs):
        if not obj.pk:
            obj.created_by = self.context['request'].user
        super(PasswordSerializer, self).save_object(obj, **kwargs)
        assign_perm('secrets.change_password', self.context['request'].user, obj)


class PasswordList(generics.ListCreateAPIView):
    model = Password
    paginate_by = 50
    serializer_class = PasswordSerializer

    def get_queryset(self):
        return Password.get_all_visible_to_user(self.request.user)