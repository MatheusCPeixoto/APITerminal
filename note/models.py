# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Gproduto(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    idprd = models.CharField(db_column='IDPRD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desctecnica = models.CharField(db_column='DESCTECNICA', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    datacriacao = models.DateTimeField(db_column='DATACRIACAO', blank=True, null=True)  # Field name made lowercase.
    codusuario = models.IntegerField(db_column='CODUSUARIO', blank=True, null=True)  # Field name made lowercase.
    inativo = models.CharField(db_column='INATIVO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    codundcontrole = models.IntegerField(db_column='CODUNDCONTROLE', blank=True, null=True)  # Field name made lowercase.
    codundcompra = models.IntegerField(db_column='CODUNDCOMPRA', blank=True, null=True)  # Field name made lowercase.
    codgrupo = models.IntegerField(db_column='CODGRUPO', blank=True, null=True)  # Field name made lowercase.
    codsubgrupo = models.IntegerField(db_column='CODSUBGRUPO', blank=True, null=True)  # Field name made lowercase.
    campolivre1 = models.CharField(db_column='CAMPOLIVRE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    campolivre2 = models.CharField(db_column='CAMPOLIVRE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    campolivre3 = models.CharField(db_column='CAMPOLIVRE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datalivre1 = models.DateTimeField(db_column='DATALIVRE1', blank=True, null=True)  # Field name made lowercase.
    datalivre2 = models.DateTimeField(db_column='DATALIVRE2', blank=True, null=True)  # Field name made lowercase.
    datalivre3 = models.DateTimeField(db_column='DATALIVRE3', blank=True, null=True)  # Field name made lowercase.
    valorlivre1 = models.DecimalField(db_column='VALORLIVRE1', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorlivre2 = models.DecimalField(db_column='VALORLIVRE2', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorlivre3 = models.DecimalField(db_column='VALORLIVRE3', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pesoliquido = models.DecimalField(db_column='PESOLIQUIDO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pesobruto = models.DecimalField(db_column='PESOBRUTO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minimo = models.DecimalField(db_column='MINIMO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maximo = models.DecimalField(db_column='MAXIMO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pontopedido = models.DecimalField(db_column='PONTOPEDIDO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preco1 = models.DecimalField(db_column='PRECO1', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preco2 = models.DecimalField(db_column='PRECO2', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preco3 = models.DecimalField(db_column='PRECO3', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    customedio = models.DecimalField(db_column='CUSTOMEDIO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imagem = models.CharField(db_column='IMAGEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    comprimento = models.DecimalField(db_column='COMPRIMENTO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    largura = models.DecimalField(db_column='LARGURA', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    espessura = models.DecimalField(db_column='ESPESSURA', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    diametro = models.DecimalField(db_column='DIAMETRO', max_digits=14, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    validadeemdias = models.IntegerField(db_column='VALIDADEEMDIAS', blank=True, null=True)  # Field name made lowercase.
    descontomaximo = models.DecimalField(db_column='DESCONTOMAXIMO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comissao1 = models.DecimalField(db_column='COMISSAO1', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comissao2 = models.DecimalField(db_column='COMISSAO2', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comissao3 = models.DecimalField(db_column='COMISSAO3', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codcoloracao = models.IntegerField(db_column='CODCOLORACAO', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    compfab = models.CharField(db_column='COMPFAB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    detalhes = models.CharField(db_column='DETALHES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tamanho = models.CharField(db_column='tamanho', max_length=100, blank=True, null=True)
    precovenda = models.DecimalField(db_column='PRECOVENDA', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codprodutopai = models.IntegerField(db_column='CODPRODUTOPAI', blank=True, null=True)  # Field name made lowercase.
    codprodutopeso1 = models.IntegerField(db_column='CODPRODUTOPESO1', blank=True, null=True)  # Field name made lowercase.
    codprodutopeso2 = models.IntegerField(db_column='CODPRODUTOPESO2', blank=True, null=True)  # Field name made lowercase.
    alterarestoquepai = models.DecimalField(db_column='ALTERARESTOQUEPAI', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipoalteracaoestoquepai = models.CharField(db_column='TIPOALTERACAOESTOQUEPAI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    leadtime = models.IntegerField(db_column='LEADTIME', blank=True, null=True)  # Field name made lowercase.
    tempoanalise1 = models.IntegerField(db_column='TEMPOANALISE1', blank=True, null=True)  # Field name made lowercase.
    tempoanalise2 = models.IntegerField(db_column='TEMPOANALISE2', blank=True, null=True)  # Field name made lowercase.
    codusuario_rm = models.CharField(db_column='CODUSUARIO_RM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    simbolo_undcontrole = models.CharField(db_column='SIMBOLO_UNDCONTROLE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    simbolo_undcompra = models.CharField(db_column='SIMBOLO_UNDCOMPRA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    simbolo_undvenda = models.CharField(db_column='SIMBOLO_UNDVENDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codundvenda = models.IntegerField(db_column='CODUNDVENDA', blank=True, null=True)  # Field name made lowercase.
    codigoprd_rm = models.CharField(db_column='CODIGOPRD_RM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idprd_rm = models.IntegerField(db_column='IDPRD_RM', blank=True, null=True)  # Field name made lowercase.
    utilizalote = models.CharField(db_column='UTILIZALOTE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    altura = models.DecimalField(db_column='ALTURA', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    codfamilia1 = models.IntegerField(db_column='CODFAMILIA1', blank=True, null=True)  # Field name made lowercase.
    codfamilia2 = models.IntegerField(db_column='CODFAMILIA2', blank=True, null=True)  # Field name made lowercase.
    referencia_ncm = models.CharField(db_column='REFERENCIA_NCM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numero_ncm = models.IntegerField(db_column='NUMERO_NCM', blank=True, null=True)  # Field name made lowercase.
    codigo_ncm = models.IntegerField(db_column='CODIGO_NCM', blank=True, null=True)  # Field name made lowercase.
    procedencia = models.IntegerField(db_column='PROCEDENCIA', blank=True, null=True)  # Field name made lowercase.
    classificacaofiscal = models.IntegerField(db_column='CLASSIFICACAOFISCAL', blank=True, null=True)  # Field name made lowercase.
    itemcomercial = models.CharField(db_column='ITEMCOMERCIAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codsisantigo = models.CharField(db_column='CodSisAntigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigoauxiliar = models.CharField(db_column='CODIGOAUXILIAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lote_minimo_venda = models.DecimalField(db_column='LOTE_MINIMO_VENDA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    lote_multiplo_venda = models.DecimalField(db_column='LOTE_MULTIPLO_VENDA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    placa_em_terceiro_1 = models.TextField(db_column='PLACA_EM_TERCEIRO_1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    placa_em_terceiro_2 = models.TextField(db_column='PLACA_EM_TERCEIRO_2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    endereco_estoque1 = models.CharField(db_column='ENDERECO_ESTOQUE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    divisao_prateleira1 = models.CharField(db_column='DIVISAO_PRATELEIRA1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero_prateleira1 = models.CharField(db_column='NUMERO_PRATELEIRA1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endereco_estoque2 = models.CharField(db_column='ENDERECO_ESTOQUE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    divisao_prateleira2 = models.CharField(db_column='DIVISAO_PRATELEIRA2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero_prateleira2 = models.CharField(db_column='NUMERO_PRATELEIRA2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endereco_estoque3 = models.CharField(db_column='ENDERECO_ESTOQUE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    divisao_prateleira3 = models.CharField(db_column='DIVISAO_PRATELEIRA3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero_prateleira3 = models.CharField(db_column='NUMERO_PRATELEIRA3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_planos_comprimento = models.DecimalField(db_column='DTEC_MOV_PLANOS_COMPRIMENTO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_planos_largura = models.DecimalField(db_column='DTEC_MOV_PLANOS_LARGURA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_planos_espessura = models.DecimalField(db_column='DTEC_MOV_PLANOS_ESPESSURA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_nplanos_dmacico = models.DecimalField(db_column='DTEC_MOV_NPLANOS_DMACICO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_nplanos_dinterno = models.DecimalField(db_column='DTEC_MOV_NPLANOS_DINTERNO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_nplanos_dexterno = models.DecimalField(db_column='DTEC_MOV_NPLANOS_DEXTERNO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_nplanos_comprimento = models.DecimalField(db_column='DTEC_MOV_NPLANOS_COMPRIMENTO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    dtec_mov_pteorico = models.DecimalField(db_column='DTEC_MOV_PTEORICO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    origem_mercadoria = models.IntegerField(db_column='ORIGEM_MERCADORIA', blank=True, null=True)  # Field name made lowercase.
    codigo_classificacaofiscal = models.IntegerField(db_column='CODIGO_CLASSIFICACAOFISCAL', blank=True, null=True)  # Field name made lowercase.
    custo_arbitrado = models.DecimalField(db_column='CUSTO_ARBITRADO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    produtocomposto = models.IntegerField(db_column='PRODUTOCOMPOSTO', blank=True, null=True)  # Field name made lowercase.
    estoque_mrp = models.DecimalField(db_column='ESTOQUE_MRP', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    cf_margemll = models.CharField(db_column='CF_MARGEMLL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cf_observacao_prd = models.CharField(db_column='CF_OBSERVACAO_PRD', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    situacao_tributaria_ipi = models.CharField(db_column='SITUACAO_TRIBUTARIA_IPI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cf_precominimo = models.CharField(db_column='CF_PRECOMINIMO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    configuravel = models.IntegerField(db_column='CONFIGURAVEL', blank=True, null=True)  # Field name made lowercase.
    kanban = models.IntegerField(db_column='KANBAN', blank=True, null=True)  # Field name made lowercase.
    log_data_hora = models.DateTimeField(db_column='LOG_DATA_HORA', blank=True, null=True)  # Field name made lowercase.
    codigo_sped_tipo_item = models.IntegerField(db_column='CODIGO_SPED_TIPO_ITEM', blank=True, null=True)  # Field name made lowercase.
    id_sped_tipo_item = models.CharField(db_column='ID_SPED_TIPO_ITEM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codigo_sped_cod_gen = models.IntegerField(db_column='CODIGO_SPED_COD_GEN', blank=True, null=True)  # Field name made lowercase.
    id_sped_cod_gen = models.CharField(db_column='ID_SPED_COD_GEN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codigo_sped_cod_lst = models.IntegerField(db_column='CODIGO_SPED_COD_LST', blank=True, null=True)  # Field name made lowercase.
    id_sped_cod_lst = models.CharField(db_column='ID_SPED_COD_LST', max_length=4, blank=True, null=True)  # Field name made lowercase.
    codigo_cor = models.IntegerField(db_column='CODIGO_COR', blank=True, null=True)  # Field name made lowercase.
    codigo_filial = models.IntegerField(db_column='CODIGO_FILIAL', blank=True, null=True)  # Field name made lowercase.
    preco_venda_minimo = models.DecimalField(db_column='PRECO_VENDA_MINIMO', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codigo_enquadramento = models.IntegerField(db_column='CODIGO_ENQUADRAMENTO', blank=True, null=True)  # Field name made lowercase.
    fator_conversao_pauta = models.DecimalField(db_column='FATOR_CONVERSAO_PAUTA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    situacao_tributaria_ipi_entrada = models.CharField(db_column='SITUACAO_TRIBUTARIA_IPI_ENTRADA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigo_enquadramento_entrada = models.IntegerField(db_column='CODIGO_ENQUADRAMENTO_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    valorlivre4 = models.DecimalField(db_column='VALORLIVRE4', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorlivre5 = models.DecimalField(db_column='VALORLIVRE5', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datalivre4 = models.DateTimeField(db_column='DATALIVRE4', blank=True, null=True)  # Field name made lowercase.
    datalivre5 = models.DateTimeField(db_column='DATALIVRE5', blank=True, null=True)  # Field name made lowercase.
    campolivre4 = models.CharField(db_column='CAMPOLIVRE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    campolivre5 = models.CharField(db_column='CAMPOLIVRE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ean = models.CharField(db_column='EAN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ean_tributavel = models.CharField(db_column='EAN_TRIBUTAVEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nao_considerar_inventario = models.CharField(db_column='NAO_CONSIDERAR_INVENTARIO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    numero_fci = models.CharField(db_column='NUMERO_FCI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    indicador_escala_relevante = models.CharField(db_column='INDICADOR_ESCALA_RELEVANTE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cnpj_fabricante = models.CharField(db_column='CNPJ_FABRICANTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigo_beneficio_fiscal = models.CharField(db_column='CODIGO_BENEFICIO_FISCAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    utiliza_lote_nfe = models.CharField(db_column='UTILIZA_LOTE_NFE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codigo_anp = models.CharField(db_column='CODIGO_ANP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    descricao_anp = models.CharField(db_column='DESCRICAO_ANP', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nao_controla_estoque = models.IntegerField(db_column='NAO_CONTROLA_ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    percentual_gpl = models.DecimalField(db_column='PERCENTUAL_GPL', max_digits=22, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percentual_glgnn = models.DecimalField(db_column='PERCENTUAL_GLGNN', max_digits=22, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percentual_glgni = models.DecimalField(db_column='PERCENTUAL_GLGNI', max_digits=22, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valor_partida = models.DecimalField(db_column='VALOR_PARTIDA', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    codfamilia3 = models.IntegerField(db_column='CODFAMILIA3', blank=True, null=True)  # Field name made lowercase.
    codfamilia4 = models.IntegerField(db_column='CODFAMILIA4', blank=True, null=True)  # Field name made lowercase.
    codfamilia5 = models.IntegerField(db_column='CODFAMILIA5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPRODUTO'


class GprodutoCodigos(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codproduto = models.ForeignKey('Gproduto', models.DO_NOTHING, db_column='CODPRODUTO')  # Field name made lowercase.
    codsimilar = models.CharField(db_column='CODSIMILAR', max_length=50)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA')  # Field name made lowercase.
    datageracao = models.DateTimeField(db_column='DATAGERAÇAO')  # Field name made lowercase.
    precovenda = models.DecimalField(db_column='PRECOVENDA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    codigo_familia1 = models.IntegerField(db_column='CODIGO_FAMILIA1', blank=True, null=True)  # Field name made lowercase.
    descricao_familia1 = models.CharField(db_column='DESCRICAO_FAMILIA1', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPRODUTO_CODIGOS'


class FOrdem(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    idordem = models.CharField(db_column='IDORDEM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dataabertura = models.DateTimeField(db_column='DATAABERTURA', blank=True, null=True)  # Field name made lowercase.
    datatermino = models.DateTimeField(db_column='DATATERMINO', blank=True, null=True)  # Field name made lowercase.
    origemnecessidade = models.IntegerField(db_column='ORIGEMNECESSIDADE', blank=True, null=True)  # Field name made lowercase.
    tipoprogramacao = models.IntegerField(db_column='TIPOPROGRAMACAO', blank=True, null=True)  # Field name made lowercase.
    descordem = models.CharField(db_column='DESCORDEM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    responsavel = models.CharField(db_column='RESPONSAVEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipoordem = models.IntegerField(db_column='TIPOORDEM', blank=True, null=True)  # Field name made lowercase.
    obsordem = models.TextField(db_column='OBSORDEM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expmobile = models.CharField(db_column='EXPMOBILE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    custoordem = models.DecimalField(db_column='CUSTOORDEM', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qtdeapontada = models.DecimalField(db_column='QTDEAPONTADA', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qtdeprevista = models.DecimalField(db_column='QTDEPREVISTA', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    proporcionalidade = models.DecimalField(db_column='PROPORCIONALIDADE', max_digits=20, decimal_places=10)  # Field name made lowercase.
    codigo_planejamento = models.IntegerField(db_column='CODIGO_PLANEJAMENTO', blank=True, null=True)  # Field name made lowercase.
    codigo_necessidademrp = models.IntegerField(db_column='CODIGO_NECESSIDADEMRP', blank=True, null=True)  # Field name made lowercase.
    ordemimpressa = models.CharField(db_column='ORDEMIMPRESSA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    data_ultimo_recalculo = models.DateTimeField(db_column='DATA_ULTIMO_RECALCULO', blank=True, null=True)  # Field name made lowercase.
    coditemnovo = models.CharField(db_column='CODITEMNOVO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_ORDEM'


class FItemordem(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    codnecessidade = models.IntegerField(db_column='CODNECESSIDADE', blank=True, null=True)  # Field name made lowercase.
    idordem = models.CharField(db_column='IDORDEM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codestrutura = models.ForeignKey('FEstrutura', models.DO_NOTHING, db_column='CODESTRUTURA', blank=True, null=True)  # Field name made lowercase.
    dtnecessidade = models.DateTimeField(db_column='DTNECESSIDADE', blank=True, null=True)  # Field name made lowercase.
    quantidadeprevista = models.DecimalField(db_column='QUANTIDADEPREVISTA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    quantidaderealizada = models.DecimalField(db_column='QUANTIDADEREALIZADA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    codordem = models.ForeignKey('FOrdem', models.DO_NOTHING, db_column='CODORDEM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_ITEMORDEM'


class FEstrutura(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='TIPO', blank=True, null=True)  # Field name made lowercase.
    idestrutura = models.CharField(db_column='IDESTRUTURA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    custoindireto = models.DecimalField(db_column='CUSTOINDIRETO', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    custoprevistoestrutura = models.DecimalField(db_column='CUSTOPREVISTOESTRUTURA', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='SEQUENCIA', blank=True, null=True)  # Field name made lowercase.
    enderecoimagem = models.CharField(db_column='ENDERECOIMAGEM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    codproduto = models.ForeignKey('Gproduto', models.DO_NOTHING, db_column='CODPRODUTO', blank=True, null=True)  # Field name made lowercase.
    dados_tec_multiplo_qtde = models.DecimalField(db_column='DADOS_TEC_MULTIPLO_QTDE', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    dados_tec_multiplo_padrao_largura = models.DecimalField(db_column='DADOS_TEC_MULTIPLO_PADRAO_LARGURA', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    dados_tec_multiplo_padrao_comprimento = models.DecimalField(db_column='DADOS_TEC_MULTIPLO_PADRAO_COMPRIMENTO', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    validacao_engrenagem = models.IntegerField(db_column='VALIDACAO_ENGRENAGEM', blank=True, null=True)  # Field name made lowercase.
    asa = models.IntegerField(db_column='ASA', blank=True, null=True)  # Field name made lowercase.
    z = models.IntegerField(db_column='Z', blank=True, null=True)  # Field name made lowercase.
    revisao1 = models.CharField(db_column='REVISAO1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    codigo_estrutura_pai = models.ForeignKey('self', models.DO_NOTHING, db_column='CODIGO_ESTRUTURA_PAI', blank=True, null=True)  # Field name made lowercase.
    codigo_usuario = models.IntegerField(db_column='CODIGO_USUARIO', blank=True, null=True)  # Field name made lowercase.
    revisao = models.IntegerField(db_column='REVISAO', blank=True, null=True)  # Field name made lowercase.
    principal = models.IntegerField(db_column='PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    data_criacao = models.DateTimeField(db_column='DATA_CRIACAO', blank=True, null=True)  # Field name made lowercase.
    percentual_perda = models.DecimalField(db_column='PERCENTUAL_PERDA', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ativa = models.IntegerField(db_column='ATIVA', blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='OBSERVACAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saldo_ordens_mrp = models.DecimalField(db_column='SALDO_ORDENS_MRP', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_ESTRUTURA'


class FAtvestrutura(models.Model):
    codcoligada = models.IntegerField(db_column='CODCOLIGADA')  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    codatividade = models.ForeignKey('FAtividade', models.DO_NOTHING, db_column='CODATIVIDADE')  # Field name made lowercase.
    codestrutura = models.ForeignKey('FEstrutura', models.DO_NOTHING, db_column='CODESTRUTURA')  # Field name made lowercase.
    tempoprocesso = models.DecimalField(db_column='TEMPOPROCESSO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    tipoprocesso = models.IntegerField(db_column='TIPOPROCESSO', blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='SEQUENCIA', blank=True, null=True)  # Field name made lowercase.
    codposto = models.IntegerField(db_column='CODPOSTO', blank=True, null=True)  # Field name made lowercase.
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    tempociclo = models.DecimalField(db_column='TEMPOCICLO', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    programacnc = models.CharField(db_column='PROGRAMACNC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preparacao = models.TextField(db_column='PREPARACAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    execucao = models.TextField(db_column='EXECUCAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conferencia = models.TextField(db_column='CONFERENCIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'F_ATVESTRUTURA'


class FRazoesparada(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    idparada = models.CharField(db_column='IDPARADA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricaoparada = models.CharField(db_column='DESCRICAOPARADA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_RAZOESPARADA'
        

class FNaoconformidades(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    codatividade = models.ForeignKey('FAtividade', models.DO_NOTHING, db_column='CODATIVIDADE', blank=True, null=True)  # Field name made lowercase.
    idnaoconformidade = models.CharField(db_column='IDNAOCONFORMIDADE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricaonconf = models.CharField(db_column='DESCRICAONCONF', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_NAOCONFORMIDADES'
        
        
class FAtividade(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    descatividade = models.CharField(db_column='DESCATIVIDADE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    preparacao = models.TextField(db_column='PREPARACAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    execucao = models.TextField(db_column='EXECUCAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conferencia = models.TextField(db_column='CONFERENCIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idatividade = models.CharField(db_column='IDATIVIDADE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    setup = models.IntegerField(db_column='SETUP', blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_ATIVIDADE'


class FEquipamento(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    descequipamento = models.CharField(db_column='DESCEQUIPAMENTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    codposto = models.IntegerField(db_column='CODPOSTO', blank=True, null=True)  # Field name made lowercase.
    custohoraeqp = models.DecimalField(db_column='CUSTOHORAEQP', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    codccusto = models.CharField(db_column='CODCCUSTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customeseqp = models.DecimalField(db_column='CUSTOMESEQP', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    efetividade = models.DecimalField(db_column='EFETIVIDADE', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtdativa = models.IntegerField(db_column='QTDATIVA', blank=True, null=True)  # Field name made lowercase.
    prodhora = models.DecimalField(db_column='PRODHORA', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    idequipamento = models.CharField(db_column='IDEQUIPAMENTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=300, blank=True, null=True)  # Field name made lowercase.
    eficienciadia = models.DecimalField(db_column='EFICIENCIADIA', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    eficienciames = models.DecimalField(db_column='EFICIENCIAMES', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='TIPO', blank=True, null=True)  # Field name made lowercase.
    tt_turno_trab_minutos = models.IntegerField(db_column='TT_TURNO_TRAB_MINUTOS', blank=True, null=True)  # Field name made lowercase.
    sql_custo = models.TextField(db_column='SQL_CUSTO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cf_observacao_eqp = models.CharField(db_column='CF_OBSERVACAO_EQP', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    cf_utilidade = models.CharField(db_column='CF_UTILIDADE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cf_utilizacao = models.CharField(db_column='CF_UTILIZACAO', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_EQUIPAMENTO'


class FMaoobra(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.IntegerField(db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    rua = models.CharField(db_column='RUA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    datanascimento = models.DateTimeField(db_column='DATANASCIMENTO', blank=True, null=True)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='FONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nomepai = models.CharField(db_column='NOMEPAI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nomemae = models.CharField(db_column='NOMEMAE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ativa = models.IntegerField(db_column='ATIVA', blank=True, null=True)  # Field name made lowercase.
    custohoramo = models.DecimalField(db_column='CUSTOHORAMO', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    customesmo = models.DecimalField(db_column='CUSTOMESMO', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    efetividade = models.DecimalField(db_column='EFETIVIDADE', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    eficienciadia = models.DecimalField(db_column='EFICIENCIADIA', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    eficienciames = models.DecimalField(db_column='EFICIENCIAMES', max_digits=18, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    chapa = models.CharField(db_column='CHAPA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cracha = models.CharField(db_column='CRACHA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tt_turno_trab_minutos = models.IntegerField(db_column='TT_TURNO_TRAB_MINUTOS', blank=True, null=True)  # Field name made lowercase.
    idmaoobra = models.CharField(db_column='IDMAOOBRA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codcidade = models.IntegerField(db_column='codcidade', blank=True, null=True)
    sql_custo = models.TextField(db_column='SQL_CUSTO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cf_setor = models.CharField(db_column='CF_SETOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cf_situacao = models.CharField(db_column='CF_SITUACAO', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_MAOOBRA'


class AAtividade(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codigo_coligada = models.IntegerField(db_column='CODIGO_COLIGADA')  # Field name made lowercase.
    codigo_filial = models.IntegerField(db_column='CODIGO_FILIAL')  # Field name made lowercase.
    codigo_ordem = models.ForeignKey('FOrdem', models.DO_NOTHING, db_column='CODIGO_ORDEM')  # Field name made lowercase.
    codigo_atividade = models.ForeignKey('FAtividade', models.DO_NOTHING, db_column='CODIGO_ATIVIDADE')  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='SEQUENCIA')  # Field name made lowercase.
    data_inicio = models.DateTimeField(db_column='DATA_INICIO', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateTimeField(db_column='DATA_FIM', blank=True, null=True)  # Field name made lowercase.
    quantidade = models.DecimalField(db_column='QUANTIDADE', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_ATIVIDADE'


class AEquipamento(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codigo_apontamentoatividade = models.ForeignKey(AAtividade, models.DO_NOTHING, db_column='CODIGO_APONTAMENTOATIVIDADE')  # Field name made lowercase.
    codigo_equipamento = models.ForeignKey('FEquipamento', models.DO_NOTHING, db_column='CODIGO_EQUIPAMENTO')  # Field name made lowercase.
    data_inicio = models.DateTimeField(db_column='DATA_INICIO', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateTimeField(db_column='DATA_FIM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_EQUIPAMENTO'


class AMaoobra(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codigo_apontamentoatividade = models.ForeignKey(AAtividade, models.DO_NOTHING, db_column='CODIGO_APONTAMENTOATIVIDADE')  # Field name made lowercase.
    codigo_maoobra = models.ForeignKey('FMaoobra', models.DO_NOTHING, db_column='CODIGO_MAOOBRA')  # Field name made lowercase.
    data_inicio = models.DateTimeField(db_column='DATA_INICIO', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateTimeField(db_column='DATA_FIM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_MAOOBRA'


class ANaoconformidade(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codigo_apontamentoatividade = models.ForeignKey('AAtividade', models.DO_NOTHING, db_column='CODIGO_APONTAMENTOATIVIDADE', blank=True, null=True)  # Field name made lowercase.
    codigo_naoconformidades = models.ForeignKey('FNaoconformidades', models.DO_NOTHING, db_column='CODIGO_NAOCONFORMIDADES', blank=True, null=True)  # Field name made lowercase.
    quantidade = models.DecimalField(db_column='QUANTIDADE', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_NAOCONFORMIDADE'


class AParadaEquipamento(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codigo_apontamentoatividade = models.ForeignKey('AAtividade', models.DO_NOTHING, db_column='CODIGO_APONTAMENTOATIVIDADE')  # Field name made lowercase.
    codigo_equipamento = models.ForeignKey('FEquipamento', models.DO_NOTHING, db_column='CODIGO_EQUIPAMENTO')  # Field name made lowercase.
    codigo_razaoparada = models.ForeignKey('FRazoesparada', models.DO_NOTHING, db_column='CODIGO_RAZAOPARADA')  # Field name made lowercase.
    data_inicio = models.DateTimeField(db_column='DATA_INICIO', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateTimeField(db_column='DATA_FIM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_PARADA_EQUIPAMENTO'


class AParadaMaoobra(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codigo_apontamentoatividade = models.ForeignKey('AAtividade', models.DO_NOTHING, db_column='CODIGO_APONTAMENTOATIVIDADE')  # Field name made lowercase.
    codigo_maoobra = models.ForeignKey('FMaoobra', models.DO_NOTHING, db_column='CODIGO_MAOOBRA')  # Field name made lowercase.
    codigo_razaoparada = models.ForeignKey('FRazoesparada', models.DO_NOTHING, db_column='CODIGO_RAZAOPARADA')  # Field name made lowercase.
    data_inicio = models.DateTimeField(db_column='DATA_INICIO', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateTimeField(db_column='DATA_FIM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_PARADA_MAOOBRA'
