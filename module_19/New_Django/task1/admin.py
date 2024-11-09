from django.contrib import admin

# Register your models here.
# from .models import Post
# admin.site.register(Post)
from .models import Game
admin.site.register(Game)
from .models import Buyer
admin.site.register(Buyer)