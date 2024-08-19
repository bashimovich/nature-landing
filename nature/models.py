from django.db import models
from PIL import Image
# Create your models here.
from ckeditor.fields import RichTextField
from django.urls import reverse


class Carusel(models.Model):
    STATUS_CHOICES = (
        ('1', 'carusel 1'),
        ('2', 'carusel 2'),
        ('3', 'carusel 3'),
        ('4', 'carusel 4'),
        ('5', 'carusel 5'),
    )
    #----------------------
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    title_in_turkmen = models.CharField(max_length=300, null=True)
    description_in_turkmen = models.CharField(max_length=300, null=True)

    title_in_russian = models.CharField(max_length=300, null=True)
    description_in_russian = models.CharField(max_length=300, null=True)

    #----------------------
    image = models.ImageField(null=True, blank=True,
                              upload_to="carules/")
    item = models.CharField(max_length=10, choices=STATUS_CHOICES, default='1')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height != 2889 or img.width != 4816:
                output_size = (4816, 2889)
                img.resize(output_size)
                img.save(self.image.path)


class latest_news(models.Model):
    #----------------------
    category = models.CharField(max_length=100)
    news = models.CharField(max_length=300)

    category_in_turkmen = models.CharField(max_length=100, null=True)
    news_in_turkmen = models.CharField(max_length=300, null=True)

    category_in_russian = models.CharField(max_length=100, null=True)
    news_in_russian = models.CharField(max_length=300, null=True)
    #----------------------

    def __str__(self):
        return self.news[:10]


class HomePageMon(models.Model):
    STATUS_CHOICES = (
        ('1', 'Monument 1'),
        ('2', 'Monument 2'),
        ('3', 'Monument 3'),
        ('4', 'Monument 4'),
        ('5', 'Monument 5'),
        ('6', 'Monument 6'),
    )
    #----------------------
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    title_in_turkmen = models.CharField(max_length=300, null=True)
    description_in_turkmen = models.CharField(max_length=300, null=True)

    title_in_russian = models.CharField(max_length=300, null=True)
    description_in_russian = models.CharField(max_length=300, null=True)
    #----------------------
    image = models.ImageField(null=True, blank=True,
                              upload_to="monuments/")
    created_at = models.DateTimeField(auto_now=True)
    item = models.CharField(max_length=10, choices=STATUS_CHOICES, default='1')
    views = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height != 2889 or img.width != 4816:
                output_size = (4816, 2889)
                img.resize(output_size)
                img.save(self.image.path)


class HomePageGallery(models.Model):
    STATUS_CHOICES = (
        ('1', 'gallery 1'),
        ('2', 'gallery 2'),
        ('3', 'gallery 3'),
        ('4', 'gallery 4'),
        ('5', 'gallery 5'),
        ('6', 'gallery 6'),
        ('7', 'gallery 7'),
        ('8', 'gallery 8'),
    )
    #----------------------
    name = models.CharField(max_length=300)
    name_in_turkmen = models.CharField(max_length=300, null=True)
    name_in_russian = models.CharField(max_length=300, null=True)
    #----------------------
    image = models.ImageField(null=True, blank=True,
                              upload_to="monuments/")
    created_at = models.DateTimeField(auto_now=True)
    item = models.CharField(max_length=10, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height != 2889 or img.width != 4816:
                output_size = (4816, 2889)
                img.resize(output_size)
                img.save(self.image.path)


class HomePageTop(models.Model):
    #----------------------
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    title_in_turkmen = models.CharField(max_length=300, null=True)
    description_in_turkmen = models.CharField(max_length=300, null=True)

    title_in_russian = models.CharField(max_length=300, null=True)
    description_in_russian = models.CharField(max_length=300, null=True)
    #----------------------
    image = models.ImageField(null=True, blank=True,
                              upload_to="monuments/")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height != 2889 or img.width != 4816:
                output_size = (4816, 2889)
                img.resize(output_size)
                img.save(self.image.path)


class HomePageVideo(models.Model):
    STATUS_CHOICES = (
        ('1', 'video 1'),
        ('2', 'video 2'),
        ('3', 'video 3'),
        ('4', 'video 4'),
    )
    #----------------------
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=100)

    title_in_turkmen = models.CharField(max_length=150, null=True)
    description_in_turkmen = models.CharField(max_length=100, null=True)

    title_in_russian = models.CharField(max_length=150, null=True)
    description_in_russian = models.CharField(max_length=100, null=True)
    #----------------------
    image = models.ImageField(null=True, blank=True,
                              upload_to="monuments/")
    url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    item = models.CharField(max_length=10, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height != 2889 or img.width != 4816:
                output_size = (4816, 2889)
                img.resize(output_size)
                img.save(self.image.path)


class GalleryPageGallery(models.Model):
    #----------------------
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    name_in_turkmen = models.CharField(max_length=100, null=True)
    description_in_turkmen = models.CharField(max_length=100, null=True)

    name_in_russian = models.CharField(max_length=100, null=True)
    description_in_russian = models.CharField(max_length=100, null=True)
    #----------------------
    image = models.ImageField(null=True, blank=True,
                              upload_to="gallery/")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height != 2889 or img.width != 4816:
                output_size = (4816, 2889)
                img.resize(output_size)
                img.save(self.image.path)


class AllPost(models.Model):
    DES_CHOICES = (
        ('mary', 'Mary'),
        ('lebap', 'Lebap'),
        ('ahal', 'Ahal'),
        ('balkan', 'Balkan'),
        ('dasoguz', 'Dashoguz'),
    )
    CAT_CHOICES = (
        ('monument', 'Monument'),
        ('reserve', 'Reserve'),
        ('resources', 'Natural Resources'),
    )
    #----------------------
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    content = RichTextField(null=True)
    title_in_turkmen = models.CharField(max_length=255, null=True)
    description_in_turkmen = models.CharField(max_length=300, null=True)
    content_in_turkmen = RichTextField(null=True)
    title_in_russian = models.CharField(max_length=255, null=True)
    description_in_russian= models.CharField(max_length=300, null=True)
    content_in_russian = RichTextField(null=True)
    #----------------------
    destrict = models.CharField(
        max_length=100, choices=DES_CHOICES, default='mary')
    category = models.CharField(
        max_length=100, choices=CAT_CHOICES, default='monument')
    created_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True,
                              upload_to="posts/")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height != 2889 or img.width != 4816:
                output_size = (4816, 2889)
                img.resize(output_size)
                img.save(self.image.path)
