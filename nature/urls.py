from django.urls import path, include
from nature.views import home, gallery, single, contact, monuments, reserves, natural_res, PostSearch, langChanger

# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', home),
    path('home', home, name="home"),
    path('gallery', gallery, name="gallery"),
    path('single/<int:id>', single, name="single"),
    path('contact', contact, name="contact"),
    path('monuments/<str:destrict>', monuments, name="monuments"),
    path('reserves', reserves, name="reserves"),
    path('natural_res', natural_res, name="natural_res"),
    path('search', PostSearch, name="post-search"),
    path('language/<str:lang>', langChanger, name="lang"),
]
# urlpatterns = [
#     *i18n_patterns(*urlpatterns, prefix_default_language=False),
# ]
