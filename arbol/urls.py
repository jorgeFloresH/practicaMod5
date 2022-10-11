
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router= DefaultRouter()
router.register(r"predios", views.PredioViewSet)
router.register(r"direcciones", views.DireccionViewSet)
router.register(r"fotos", views.FotoViewSet)

urlpatterns = [
    # path('contacto/<str:nombre>', views.contacto, name='contacto'),
    #path('', views.index, name='index'),
    path('', include(router.urls)),
    #path('arbol/', views.viewArbol, name='arboles'),
    #path('productos/', views.productoFormView, name='productos'),
]
