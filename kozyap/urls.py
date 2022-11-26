from django.urls import path

from kozyap.views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index')
]
