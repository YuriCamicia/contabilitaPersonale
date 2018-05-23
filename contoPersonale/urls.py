from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.start, name='start'),
    url(r'^conto/(?P<pk>[0-9]+)/$',views.gestione_conto, name='gestione_conto'),
]