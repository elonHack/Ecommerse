from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ("name",)

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_images/')
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self) -> str:
        return self.name+ " @" + str(self.date_created.time())