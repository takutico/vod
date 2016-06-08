from django.db import models


class Type(models.Model):
    # Model basic information
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Type information
    name = models.CharField(max_length=100)


class Category(models.Model):
    # Model basic information
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Category information
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    id = models.CharField(primary_key=True, max_length=200)


class Movie(models.Model):
    # Model basic information
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Movie information
    publishedDate = models.DateTimeField(null=True)
    availableDate = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    id = models.CharField(primary_key=True, max_length=200)
    type = models.ForeignKey(Type, null=True)
    # This is to do it easy
    image = models.URLField()
    url = models.URLField()


def movie_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/movie/<id>/images/<filename>
    return 'movie/{0}/images/{1}'.format(instance.movie.id, filename)


class MovieImage(models.Model):
    # Model basic information
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Images information
    movie = models.ForeignKey(Movie)
    image = models.ImageField(upload_to=movie_image_directory_path)


class Content(models.Model):
    # Model basic information
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Content information
    id = models.CharField(primary_key=True, max_length=100)
    movie = models.ForeignKey(Movie)
    width = models.IntegerField()
    height = models.IntegerField()
    geoLock = models.BooleanField(default=False)
    language = models.CharField(max_length=20)
    duration = models.IntegerField(default=0)
    url = models.URLField()
    format = models.CharField(max_length=10)


class ParentalRating(models.Model):
    # Model basic information
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Parental information
    scheme = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
