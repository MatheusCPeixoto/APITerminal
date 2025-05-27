from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()
router.register(r'ordem', orderViewSet)
router.register(r'itemordem', orderItemViewSet)
router.register(r'estrutura', structureViewSet)
router.register(r'atividadeestrutura', structureActivityViewSet)
router.register(r'produto', productViewSet)
router.register(r'produtocodigo', productCodeViewSet)
router.register(r'atividade', activityViewSet)
router.register(r'razoesparada', reasonsStoppingViewSet)
router.register(r'naoconformidade', nonComplianceViewSet)
router.register(r'equipamento', equipmentViewSet)
router.register(r'operador', operatorViewSet)
router.register(r'apontamento', noteActivityViewSet)
router.register(r'apontamentoequipamento', noteEquipmentViewSet)
router.register(r'apontamentooperador', noteOperatorViewSet)
router.register(r'apontamentonaoconformidade', noteNonComplianceViewSet)
router.register(r'paradaequipamento', noteEquipmentStopViewSet)
router.register(r'paradaoperador', noteOperatorStopViewSet)

app_name = 'apontamento'

urlpatterns = [
    path('login/', views.pagina_login, name='pagina_login'),
    path('', include(router.urls)),
]