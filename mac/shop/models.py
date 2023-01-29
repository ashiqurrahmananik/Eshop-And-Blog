from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date=models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class contact(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50,default="")
    text = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.email

