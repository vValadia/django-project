from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class product(models.Model):
    name = models.CharField(max_length=100)
    category = models.






    
    # id_product = models.CharField(max_length=100000, primary_key=True)
    # id_category = models.
    # product_name = models.
    # price = models.
    # year = models.
    # photo = models.
    # producer = models.
    # type = models.

class category(models.Model):
    id_category = models.
    category = models.

class user(models.Model):
    id_user = models.
    id_category = models.
    user_name = models.
    login = models.
    email = models.
    password = models.

class order(models.Model):
    id_order = models.
    id_user = models.
    date = models.
    status = models.
    info = models.
    
class order(models.Model):
    id_order = models.
    id_product = models.
    cost = models.
    quantity = models.
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
