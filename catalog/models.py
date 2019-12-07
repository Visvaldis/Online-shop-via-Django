from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Create your models here.


class Category(models.Model):
    """
    Model representing a tea category (e.g. Black tea, Green tea etc.)
    """

    category_id = models.AutoField(max_length=11, primary_key=True, )
    name = models.CharField(max_length=100, help_text="Enter a tea category (e.g. Black tea, Green tea etc.)")
    description = models.CharField(max_length=1000, help_text="Enter description for current category")

    class Meta:
        managed = False
        db_table = 'tCategory'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    price = models.FloatField(help_text="Price for 100 grams")
    image_url = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'tProduct'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('tea-detail', args=[str(self.product_id)])