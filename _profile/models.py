from colorful.fields import RGBColorField
# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django_countries.fields import CountryField

from Portfolio.settings import DEFAULT_REDIRECT_URL
from users.models import User

TagChoice = (
    ('Graphics', 'Graphics'),
    ('Web development', 'Web development'),
    ('UI/Ux', 'UI/Ux'),
)


class PortfolioTemplate(models.Model):
    name = models.CharField(max_length=20)
    portfolio_version = models.CharField(max_length=30)
    tag = models.CharField(max_length=20, choices=TagChoice)
    image = models.ImageField(upload_to='home_page/portfolio_tag')
    price = models.IntegerField(default=0)
    paid = models.BooleanField(default=True)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = None
        return image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    motto = models.CharField(blank=True, null=True, max_length=100)
    main_skill = models.CharField(blank=True, null=True, max_length=100)

    country = CountryField(multiple=False)
    address = models.CharField(max_length=200, blank=True, null=True)

    phone_number = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    about = models.TextField(blank=True, null=True, max_length=1000)

    def get_portfolio_absolute_url(self):
        return reverse('portfolio:portfolio', kwargs={'username': self.user.username})

    def __str__(self):
        return f'{self.user.username} '


background_colors = (
    ('dark', 'dark'),
    ('light', 'light')
)


class Layout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to='profile_pics', default='profile_pics/profile_pics.jpg')
    logo = models.ImageField(blank=True, null=True)
    background_image = models.ImageField(upload_to='background_image',
                                         default='profile/backgroundImage.jpg')
    background_color = models.CharField(choices=background_colors, max_length=10, default='light')
    primary_color = RGBColorField(default='#100F0F')
    secondary_color = RGBColorField(default='#838FF')
    portfolio_version = models.OneToOneField(PortfolioTemplate, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def backgroundImageURL(self):
        try:
            image_ = self.background_image.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image

    @property
    def profilePicsImageURL(self):
        try:
            image_ = self.profile_pics.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image

    @property
    def logoImageURL(self):
        try:
            image_ = self.logo.url
            image = DEFAULT_REDIRECT_URL + image_
        except:
            image = ''
        return image


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    description = models.TextField()


def post_save_user_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        Layout.objects.get_or_create(user=instance)
    user_profile, created = Profile.objects.get_or_create(user=instance)
    user_layout, created = Layout.objects.get_or_create(user=instance)


post_save.connect(post_save_user_profile_create, sender=settings.AUTH_USER_MODEL)
