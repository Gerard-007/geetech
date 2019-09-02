from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.#
def upload_dir(instance, filename):
    return "{}/{}".format(instance.author, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MusicScore(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255)
    document = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf'], 'pdf format only')])
    cover_picture = models.ImageField(upload_to=upload_dir, height_field=50, width_field=30, blank=True, null=True)
    composer = models.CharField(max_length=100)
    price = models.CharField(default='500.00', blank=True, max_length=100)
    free = models.BooleanField(default=True)
    uploader = models.ForeignKey(User)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("composer")
        unique_together = ["composer", "title"]
        verbose_name = 'MusicScore'
        verbose_name_plural = 'MusicScores'

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.cover_picture:
            return self.image_url
        else:
            return "default cloudinary image url here"

    def get_absolute_url(self):
        return reverse("musicscores:detail", kwargs={"slug": self.slug})
    

