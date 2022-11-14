from django.contrib import admin
from .models import RandomModel
from .models import Author

# Register your models here.

admin.site.register(RandomModel)
admin.site.register(Author)
