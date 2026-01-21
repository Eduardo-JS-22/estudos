from django.db import models
from datetime import datetime

class Image(models.Model):
    CATEGORY_OPTIONS = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    name = models.CharField(max_length=255, null=False, blank=False)
    legend = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField()
    photo = models.CharField(max_length=255, null=False, blank=False)
    published = models.BooleanField(default=False)
    image_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name