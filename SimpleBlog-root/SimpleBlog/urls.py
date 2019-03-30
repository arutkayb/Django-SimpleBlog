
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
	path('posts/',include("Posts.urls")),
	path('hello/',TemplateView.as_view(template_name='hello_world.html')),
    path('admin/', admin.site.urls),
]
