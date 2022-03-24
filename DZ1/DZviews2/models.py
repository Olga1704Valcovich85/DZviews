from django.db import models

# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    mail_director = models.EmailField()
    tel_nomber = models.CharField(max_length = 100)
    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

class Movie(models.Model):
    name = models.CharField(max_length = 30)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-defail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'


