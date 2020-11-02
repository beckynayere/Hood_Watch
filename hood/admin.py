from django.contrib import admin
from .models import Profile, NeighbourHood, Business, Post,Comment,Location,Category

# Register your models here.


admin.site.register(Profile)
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(Category)