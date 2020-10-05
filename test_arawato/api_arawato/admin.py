from django.contrib import admin
from .models import developer, console, game

# Register your models here.

admin.site.register(developer)
admin.site.register(console)
admin.site.register(game)