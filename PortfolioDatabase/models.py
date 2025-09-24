from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hobbies/', blank=True, null=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)

    def __str__(self):
        return self.name
