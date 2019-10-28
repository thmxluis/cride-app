""" Circle memberships views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Permissions
from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.memberships import IsActiveCircleMember


# Models
from cride.circles.models import Circle, Membership

# Serializer
from cride.circles.serializers import MembershipModelSerializer


class MembershipViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """ Circle membership view set. """
    serializer_class = MembershipModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """ Verify that the circle existes. """
        slug_name = kwargs['slug_name']
        self.circle = get_object_or_404(Circle, slug_name=slug_name)
        return super(MembershipViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """ Sobrescribimos el metodo para asignar permisos."""
        permissions = [IsAuthenticated, IsActiveCircleMember]
        return [p() for p in permissions]

    def get_queryset(self):
        """ Return cicles members. """
        return Membership.objects.filter(
            circle=self.circle,
            is_active=True
        )

    def get_object(self):
        """ Return the circle member by using the users username."""
        return get_object_or_404(
            Membership,
            user__username=self.kwargs['pk'],
            circle=self.circle,
            is_active=True
        )

    def perform_destroy(self, instance):
        """ Desabilitar Miembro """
        instance.is_active = False
        instance.save()
