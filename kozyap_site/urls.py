from django.urls import path

from kozyap_site.views import IndexPageView, AboutPageView, ReferencePageView, FriendPageView, GalleryPageView, \
    CommunicatePageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('reference/', ReferencePageView.as_view(), name='reference'),
    path('partner/', FriendPageView.as_view(), name='partner'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('communicate/', CommunicatePageView.as_view(), name='communicate')
]
