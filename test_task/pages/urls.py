from django.urls import path
from pages.views import index, page


urlpatterns = [
    path('index/', index, name='index'),
    path('<slug:page_slug>/', page, name='pages')
]
