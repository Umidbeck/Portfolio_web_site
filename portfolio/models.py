from django.db import models


# Create your models here.

class CV_Model(models.Model):
    pro_img = models.ImageField(upload_to='cv_images/')
    age = models.IntegerField()

    def __str__(self):
        return f"CV Model #{self.pk}"


class Portfolio_Model(models.Model):
    category = models.CharField(max_length=100)
    parts = models.TextField(max_length=250, null=True, blank=True )
    project_url = models.URLField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return self.title
