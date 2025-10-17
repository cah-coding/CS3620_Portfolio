from django.db import models

class BookData(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return self.name