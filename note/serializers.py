from rest_framework import serializers
from .models import *

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FOrdem
        fields = ('codigo', 'status', 'descordem', 'tipoordem', 'obsordem', 'obsordem', 'qtdeapontada', 'qtdeprevista', 'proporcionalidade')
        
class orderItemSerializer(serializers.ModelSerializer):
    codordem = serializers.PrimaryKeyRelatedField(queryset=FOrdem.objects.all())
    
    class Meta:
        model = FItemordem
        fields = ('codigo', 'codestrutura', 'codordem')
        
class structureSerializer(serializers.ModelSerializer):
    codproduto = serializers.PrimaryKeyRelatedField(queryset=Gproduto.objects.all())
    
    class Meta:
        model = FEstrutura
        fields = ('codigo', 'codproduto', 'idestrutura', 'revisao', 'principal')
        
class structureActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FAtvestrutura
        fields = ('codigo', 'codestrutura', 'sequencia', 'tempoprocesso', 'tempociclo', 'preparacao', 'execucao', 'conferencia')
        
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gproduto
        fields = ('codigo', 'idprd', 'nome', 'desctecnica')
        
class productCodeSerializer(serializers.ModelSerializer):
    codproduto = serializers.PrimaryKeyRelatedField(queryset=Gproduto.objects.all())
    
    class Meta:
        model = GprodutoCodigos
        fields = ('codproduto', 'codsimilar')
        
class activitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FAtividade
        fields = ('codigo', 'idatividade', 'descatividade', 'preparacao', 'execucao', 'conferencia')
        
class reasonsStoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FRazoesparada
        fields = ('codigo', 'idparada', 'descricaoparada', 'ativo')
        
class nonComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FNaoconformidades
        fields = ('codigo', 'codatividade', 'idnaoconformidade', 'descricaoconf')
        
class equipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FEquipamento
        fields = ('codigo', 'idequipamento', 'descequipamento', 'endereco')

class operatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FMaoobra
        fields = ('codigo', 'idoperador', 'nome', 'ativa', 'cracha')

class noteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AAtividade
        fields = '__all__'
        
class noteEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AEquipamento
        fields = '__all__'
        
class noteOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMaoobra
        fields = '__all__'
    
class noteNonComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ANaoconformidade
        fields = '__all__'
        
class noteEquipmentStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AParadaEquipamento
        fields = '__all__'
        
class noteOperatorStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AParadaMaoobra
        fields = '__all__'
        