from django.contrib import admin
from .models import Profile, NeighbourHood, Business, Post

# Register your models here.


admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Post)
