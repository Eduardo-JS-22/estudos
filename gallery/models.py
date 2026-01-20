from django.db import models

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

    def __str__(self):
        return self.name