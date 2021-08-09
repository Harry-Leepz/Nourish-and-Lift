from django.db.models.singals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem