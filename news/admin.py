from django.contrib import admin

from .models import Author
from .models import Category
from .models import Comment
from .models import Post
from .models import PostCategory

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

