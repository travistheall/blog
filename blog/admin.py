from django.contrib import admin
from .models import Post, Mostcommon, Mostpopular

admin.site.register(Post)
admin.site.register(Mostcommon)
admin.site.register(Mostpopular)
