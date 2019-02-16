from django.contrib import admin

from .models import Movie, Genre


admin.site.register(Movie)
admin.site.register(Genre)
