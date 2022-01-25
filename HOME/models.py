from django.db import models


class SliderImages(models.Model):
    """ Slider Image Model """

    image = models.ImageField(upload_to='slider_images')
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_slider_image'
        verbose_name_plural = 'Slider Images'

    def __str__(self):
        return self.image.name
