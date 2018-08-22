from django.db import models
import random
import os
from django.contrib.auth.models import User
# Create your models here.


def get_filename_ext(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    #print(instance)
    #print(filename)
    new_filename = random.randint(1, 384848399)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.title, filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    desciption = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=4, default=0.00000)
    cant = models.IntegerField()
    image = models.FileField(blank=True, null=True, upload_to=upload_image_path)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
