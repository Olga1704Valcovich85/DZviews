from django.contrib import admin

# Register your models here.
from .models import Movie
admin.site.register(Movie)

from .models import Director
admin.site.register(Director)