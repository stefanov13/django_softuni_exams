from django import template

from apps.car_profile.models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile():
        return Profile.objects.first()
