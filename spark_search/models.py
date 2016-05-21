from django.db import models

class Image(models.Model):
    small = models.URLField()
    medium = models.URLField()
    large = models.URLField()

    def __str__(self):
        return self.small

class ProductGroup(models.Model):
    name = models.CharField(max_length=20);

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20);

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=20);

    def __str__(self):
        return self.name

class Item(models.Model):
    asin = models.CharField(max_length=15);
    title = models.CharField(max_length=150);
    binding = models.CharField(max_length=20);
    salesrank = models.IntegerField(default=0)
    author = models.CharField(max_length=30);
    is_adult_product = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=20);
    release_date = models.DateField()
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
