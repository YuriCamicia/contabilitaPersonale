from django.conf.urls import url, include
from . import views
from .appDRF import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contos', views.ContoViewSet)
router.register(r'transaziones', views.TransazioneViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
    #url(r'^$',views.start, name='start'),
    #url(r'^conto/(?P<pk>[0-9]+)/$',views.gestione_conto, name='gestione_conto'),
]