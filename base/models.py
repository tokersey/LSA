from django.db import models
from django.db.models import Q
import operator


# Create your models here.
class ContactManager(models.Manager):
    def search(self, search_terms):
        terms = [term.strip() for term in search_terms.split()]
        q_objects = []

        for term in terms:
            q_objects.append(Q(first_name__icontains=term))
            q_objects.append(Q(last_name__icontains=term))
            q_objects.append(Q(address__icontains=term))
            q_objects.append(Q(email__icontains=term))
            q_objects.append(Q(phone__icontains=term))

        # Start with a bare QuerySet
        qs = self.get_queryset()

        # Use operator's or_ to string together all of your Q objects.
        return qs.filter(reduce(operator.or_, q_objects))


class Contact(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    address = models.CharField(max_length=255, verbose_name="Address")
    email = models.EmailField(max_length=50, verbose_name="Email")
    phone = models.CharField(max_length=16, verbose_name="Phone Number")
    objects = ContactManager()
