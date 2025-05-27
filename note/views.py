from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from .filters import *
from rest_framework.generics import ListAPIView

class orderViewSet(viewsets.ModelViewSet):
    queryset = FOrdem.objects.all()
    serializer_class = orderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = orderFilter
    
class orderItemViewSet(viewsets.ModelViewSet):
    queryset = FItemordem.objects.all()
    serializer_class = orderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = orderItemFilter
    
class structureViewSet(viewsets.ModelViewSet):
    queryset = FEstrutura.objects.all()
    serializer_class = structureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = structureFilter
    
class structureActivityViewSet(viewsets.ModelViewSet):
    queryset = FAtvestrutura.objects.all()
    serializer_class = structureActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = structureActivityFilter

class productViewSet(viewsets.ModelViewSet):
    queryset = Gproduto.objects.all()
    serializer_class = productSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = productFilter
    
class productCodeViewSet(viewsets.ModelViewSet):
    queryset = GprodutoCodigos.objects.all()
    serializer_class = productCodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = productCodeFilter
    
class activityViewSet(viewsets.ModelViewSet):
    queryset = FAtividade.objects.all()
    serializer_class = activitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = activityFilter
    
class reasonsStoppingViewSet(viewsets.ModelViewSet):
    queryset = FRazoesparada.objects.all()
    serializer_class = reasonsStoppingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = reasonsStoppingFilter
    
class nonComplianceViewSet(viewsets.ModelViewSet):
    queryset = FNaoconformidades.objects.all()
    serializer_class = nonComplianceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = nonComplianceFilter
    
class equipmentViewSet(viewsets.ModelViewSet):
    queryset = FEquipamento.objects.all()
    serializer_class = equipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = equipmentFilter
    
class operatorViewSet(viewsets.ModelViewSet):
    queryset = FMaoobra.objects.all()
    serializer_class = operatorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = operatorFilter
    
class noteActivityViewSet(viewsets.ModelViewSet):
    queryset = AAtividade.objects.all()
    serializer_class = noteActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = noteActivityFilter
    
class noteEquipmentViewSet(viewsets.ModelViewSet):
    queryset = AEquipamento.objects.all()
    serializer_class = noteEquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = noteEquipmentFilter
    
class noteOperatorViewSet(viewsets.ModelViewSet):
    queryset = AMaoobra.objects.all()
    serializer_class = noteOperatorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = noteOperatorFilter
    
class noteNonComplianceViewSet(viewsets.ModelViewSet):
    queryset = ANaoconformidade.objects.all()
    serializer_class = noteNonComplianceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = noteNonComplianceFilter
    
class noteEquipmentStopViewSet(viewsets.ModelViewSet):
    queryset = AParadaEquipamento.objects.all()
    serializer_class = noteEquipmentStopSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = noteEquipmentStopFilter
    
class noteOperatorStopViewSet(viewsets.ModelViewSet):
    queryset = AParadaMaoobra.objects.all()
    serializer_class = noteOperatorStopSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = noteOperatorStopFilter
    
def pagina_login(request):
    return render(request, 'note/login.html')