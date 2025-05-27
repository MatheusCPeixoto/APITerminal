import django_filters
from .models import *

class orderFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    obsordem = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = FOrdem
        fields = ('codigo', 'obsordem')
        
class orderItemFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    codestrutura = django_filters.NumberFilter(lookup_expr='exact')
    codordem = django_filters.NumberFilter(lookup_expr='exact')
    
    class Meta:
        model = FItemordem
        fields = ('codigo', 'codordem', 'codestrutura')
        
class structureFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    codproduto = django_filters.NumberFilter(lookup_expr='exact')
    idestrutura = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = FEstrutura
        fields = ('codigo', 'codproduto', 'idestrutura')
        
class structureActivityFilter(django_filters.FilterSet):
    codestrutura = django_filters.NumberFilter(lookup_expr='exact')
    sequencia = django_filters.NumberFilter(lookup_expr='exact')
    
    class Meta:
        model = FAtvestrutura
        fields = ('codestrutura', 'sequencia')
        
class productFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    descricao = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Gproduto
        fields = ('codigo', 'idprd', 'nome', 'desctecnica')
        
class productCodeFilter(django_filters.FilterSet):
    codproduto = django_filters.NumberFilter(lookup_expr='exact')
    codsimilar = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = GprodutoCodigos
        fields = ('codproduto', 'codsimilar')

class activityFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    descatividade = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = FAtividade
        fields = ('codigo', 'idatividade', 'descatividade', 'preparacao', 'execucao', 'conferencia')
        
class reasonsStoppingFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    descricaoparada = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = FRazoesparada
        fields = ('codigo', 'idparada', 'descricaoparada', 'ativo')
        
class nonComplianceFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    idnaoconformidade = django_filters.CharFilter(lookup_expr='icontains')
    descricaoconf = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = FNaoconformidades
        fields = ('codigo', 'codatividade', 'idnaoconformidade', 'descricaoconf')
        
class equipmentFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    descequipamento = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = FEquipamento
        fields = ('codigo', 'idequipamento', 'descequipamento', 'endereco')
        
class operatorFilter(django_filters.FilterSet):
    codigo = django_filters.NumberFilter(lookup_expr='exact')
    nome = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = FMaoobra
        fields = ('codigo', 'idmaoobra', 'nome', 'ativa', 'cracha')
        
class noteActivityFilter(django_filters.FilterSet):
    class Meta:
        model = AAtividade
        fields = '__all__'
        
class noteEquipmentFilter(django_filters.FilterSet):
    class Meta:
        model = AEquipamento
        fields = '__all__'
        
class noteOperatorFilter(django_filters.FilterSet):
    class Meta:
        model = AMaoobra
        fields = '__all__'
        
class noteNonComplianceFilter(django_filters.FilterSet):
    class Meta:
        model = ANaoconformidade
        fields = '__all__'
        
class noteEquipmentStopFilter(django_filters.FilterSet):
    class Meta:
        model = AParadaEquipamento
        fields = '__all__'
        
class noteOperatorStopFilter(django_filters.FilterSet):
    class Meta:
        model = AParadaMaoobra
        fields = '__all__'
        

