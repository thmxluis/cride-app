''' Circles model. '''

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel


class Circle(CRideModel):
    ''' Circles Model '''

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/piectures', blank=True, null=True)

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circle are also know as oficial communities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public Circle are listed in the main page so everyone about their existence.'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number od members.'
    )
    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this will be the limit on the number of members.'
    )

    def __str__(self):
        ''' return circle name. '''
        return self.name

    class Meta(CRideModel.Meta):
        ''' Meta class. '''

        ordering = ['-rides_taken', '-rides_offered']
