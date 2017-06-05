from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Pessoa(models.Model):
    UF_CHOICES = (
    ('AC','Acre'), ('AL','Alagoas'), ('AP','Amapá'),
    ('AM','Amazonas'), ('BA','Bahia'), ('CE','Ceará'),
    ('DF','Distrito Federal'), ('ES','Espírito Santo'),
    ('GO','Goiás'), ('MA','Maranhão'), ('MT','Mato Grosso'),
    ('MS','Mato Grosso do Sul'), ('MG','Minas Gerais'),
    ('PA','Pará'), ('PB','Paraíba'), ('PR','Paraná'),
    ('PE','Pernambuco'), ('PI','Piauí'),
    ('RJ','Rio de Janeiro'), ('RN','Rio Grande do Norte'),
    ('RS','Rio Grande do Sul'), ('RO','Rondônia'),
    ('RR','Roraima'), ('SC','Santa Catarina'),
    ('SP','São Paulo'), ('SE','Sergipe'),
    ('TO','Tacantins'), )
    email = models.EmailField(help_text='exemplo@email.com')
    telefone_comercial = models.CharField(max_length=50, null=True,
     blank=True, verbose_name="Telefone Comercial"
     , help_text="(DDD)9999-9999")
    telefone_celular = models.CharField(max_length=50, null=True,
     blank=True, verbose_name="Telefone Celular"
     , help_text="(DDD)9-99999-9999")
    logradouro = models.CharField(max_length=50, verbose_name='Logradouro'
        , null=True, blank=True, help_text="Rua/Av/Vila etc...")
    numero = models.PositiveIntegerField(null=True, blank=True)
    nome = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, verbose_name='Estado',
     choices=UF_CHOICES, null=True, blank=True)
    pais = models.CharField(default='Brasil', max_length=20, null=True,
     blank=True, verbose_name="País")
    observacoes = models.TextField(max_length=500, blank=True, null=True
        , verbose_name="Observações", help_text='500 caracteres no máximo')

    def __str__(self):
        return self.nome


class Fisica(Pessoa):
    ESTADO_CIVIL_CHOICES = (('sol','solteiro(a)'), ('cas','casado(a)'),
    ('div','divorciado(a)'), ('sep','separado(a)'), ('dis','disquitado(a)'),
    ('ou','Outros'))
    rg = models.BigIntegerField(verbose_name='RG', null=True,
     blank=True, help_text="Somente Números")
    cpf = models.BigIntegerField(verbose_name='CPF', null=True
        , help_text="Somente Números")
    estado_civil = models.CharField(max_length=50,
     choices=ESTADO_CIVIL_CHOICES, blank=True, null=True
     , verbose_name="Estado Civil")
    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Físicas"


class Juridica(Pessoa):
    ESTADO_CIVIL_CHOICES = (('sol','solteiro'), ('cas','casado'),
    ('div','divorciado'), ('sep','separado'), ('dis','disquitado'),
    ('ou','Outros'))
    razao_social = models.CharField(max_length=30,
    verbose_name='Razão Social', blank=True, null=True)
    cnpj = models.CharField(max_length=30, verbose_name='CNPJ')
    rg = models.CharField(max_length=50, verbose_name='RG'
    , blank=True, null=True
    , help_text="RG do responsável. Somente Números")
    cpf = models.CharField(max_length=50, verbose_name='CPF'
    , blank=True, null=True
    , help_text="CPF do responsável. Somente Números")
    estado_civil = models.CharField(max_length=50,
     choices=ESTADO_CIVIL_CHOICES, blank=True, null=True, 
     help_text='Estado Civil do Responsável')

    ie = models.CharField(max_length=30, verbose_name='Inscrição Estadual',
    null=True, blank=True)

    class Meta:
        verbose_name = "Pessoa Jurídica"
        verbose_name_plural = "Pessoas Jurídicas"

class Atendimento(models.Model):
    SITUACAO_CHOICES = (
    ('AB','Aberto'), ('AT','Em Atendimento'),
    ('NF','Negócio Fechado'), ('NR','Negócio não Realizado'))
    cliente = models.ForeignKey(Pessoa)
    situacao = models.CharField(max_length=50, choices=SITUACAO_CHOICES)
    data = models.DateField(auto_now=True, editable=False)
    observacoes = models.TextField(max_length=500, blank=True, null=True, 
        verbose_name='Observações', help_text='500 caracteres no máximo')

class Visita(models.Model):
    
    atendimento = models.ForeignKey(Atendimento, null=True
        , verbose_name='Atendimento')
    data = models.DateField(default=timezone.now, 
        help_text='dd/mm/aaa', verbose_name='Data')
    observacoes = models.TextField(max_length=500, verbose_name="Observações",
        blank=True, null=True, help_text='500 caracteres no máximo')

class Imovel(models.Model):
    UF_CHOICES = (
    ('AC','Acre'), ('AL','Alagoas'), ('AP','Amapá'),
    ('AM','Amazonas'), ('BA','Bahia'), ('CE','Ceará'),
    ('DF','Distrito Federal'), ('ES','Espírito Santo'),
    ('GO','Goiás'), ('MA','Maranhão'), ('MT','Mato Grosso'),
    ('MS','Mato Grosso do Sul'), ('MG','Minas Gerais'),
    ('PA','Pará'), ('PB','Paraíba'), ('PR','Paraná'),
    ('PE','Pernambuco'), ('PI','Piauí'),
    ('RJ','Rio de Janeiro'), ('RN','Rio Grande do Norte'),
    ('RS','Rio Grande do Sul'), ('RO','Rondônia'),
    ('RR','Roraima'), ('SC','Santa Catarina'),
    ('SP','São Paulo'), ('SE','Sergipe'),
    ('TO','Tacantins'), )

    disponivel = models.BooleanField(verbose_name="Disponível")
    exibir = models.BooleanField(verbose_name="Exibir no Site")
    destaque = models.BooleanField(verbose_name="Destaque")
    descricao_curta = models.CharField(max_length=300, verbose_name="Descrição Curta")
    proprietario = models.ForeignKey(Pessoa, verbose_name='Proprietário')
    logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    numero = models.CharField(max_length=10, null=True, blank=True, verbose_name='Número')
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=50, choices=UF_CHOICES,
     verbose_name='UF')
    pais = models.CharField(max_length=50, default='Brasil', verbose_name='País')
    cep = models.CharField(max_length=50, verbose_name='CEP',
    null=True, blank=True)
    ponto_referencia = models.TextField(max_length=300,
        verbose_name='Ponto de Referência', blank=True, null=True)
    posse_chave = models.TextField(max_length=300,
        verbose_name='Posse das Chaves', blank=True, null=True)
    descricao = models.TextField(max_length=300,
        verbose_name='Descrição', blank=True, null=True)

    img1 = models.ImageField(upload_to='imovel', verbose_name='Imagem 1',
    null=True, blank=True)
    img2 = models.ImageField(upload_to='imovel', verbose_name='Imagem 2',
    null=True, blank=True)
    img3 = models.ImageField(upload_to='imovel', verbose_name='Imagem 3',
    null=True, blank=True)
    img4 = models.ImageField(upload_to='imovel', verbose_name='Imagem 4',
    null=True, blank=True)
    img5 = models.ImageField(upload_to='imovel', verbose_name='Imagem 5',
    null=True, blank=True)
    img6 = models.ImageField(upload_to='imovel', verbose_name='Imagem 6',
    null=True, blank=True)

    def __str__(self):
        return self.descricao_curta

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"

class Casa(Imovel):

    TIPO_CHOICES = (('is','Isolada'), ('ge','Germinada'),
    ('so','Sobrado'), ('al','Alto Padrão'), ('cd','Condomínio'),
    ('po','Pousada'), ('ht','Hotel'), ('as','Assombradada'),
    ('ter','Terrea'), ('vi','Village'))
    ESTADO_CONSERVACAO_CHOICES = (('nv','Novo'),('sn','Semi-Novo'),
    ('us','Usado'), ('ob','Em Obras'))
    FREQUENCIA_CHOICES = (('ms','Mensal'), ('dr','Diária'), ('sm','Semanal'),
    ('tr','Trimestral'), ('an','Anual'))
    SITUACAO_CHOICES = (('QU','Quitado'),('AL','Alienado'))
    TITULO_AQUISITIVO_CHOICES = (('RE','Regularizado'),
    ('ES','Escritura Pública'), ('EP','Escritura de Posse'),
    ('CC','Contrato de Compra'), ('HP','Hipotecado'),
    ('PO','Posse'), ('PC','Promessa de Compra'),
    ('FN','Financiável'))
    AVALIACAO_CHOICES = (('BO','Bom'), ('RG','Regular'),
    ('RS','Reformas Simples'), ('RI','Reformas Importantes'),
    ('RU','Ruim'))
    morador_locatario = models.ForeignKey(Pessoa, null=True, blank=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    estado_conservacao = models.CharField(max_length=100,
     choices=ESTADO_CONSERVACAO_CHOICES, null=True, blank=True)
    area_privativa = models.FloatField(verbose_name='Área Privativa'
    , null=True, blank=True)
    area_total = models.FloatField(verbose_name='Área Total'
    , null=True, blank=True)
    idade = models.PositiveIntegerField(verbose_name='Idade em Anos'
    , null=True, blank=True)
    avaliacao = models.CharField(max_length=100,
    verbose_name='Avaliação', choices=AVALIACAO_CHOICES,
    null=True, blank=True)
    dormitorios = models.PositiveIntegerField(verbose_name='Dormitórios'
    , null=True, blank=True)
    sanitarios = models.PositiveIntegerField(verbose_name='Sanitários'
    , null=True, blank=True)
    suites = models.PositiveIntegerField(verbose_name='Suítes'
    , null=True, blank=True)
    salas = models.PositiveIntegerField(null=True, blank=True)
    cozinhas = models.PositiveIntegerField(null=True, blank=True)
    areas_servico = models.PositiveIntegerField(verbose_name='Áreas de Serviço', null=True, blank=True)
    dep_empregada = models.PositiveIntegerField(verbose_name='Dependência de Empregadas', null=True, blank=True)
    sacadas = models.PositiveIntegerField(null=True, blank=True)
    garagens = models.PositiveIntegerField(null=True, blank=True)
    andares = models.PositiveIntegerField(null=True, blank=True)
    ediculas = models.PositiveIntegerField(verbose_name='Edículas'
    , null=True, blank=True)
    interfone = models.BooleanField(blank=True)
    torneira_quente = models.BooleanField(verbose_name='Torneira Quente'
    , blank=True)
    closet = models.BooleanField(blank=True)
    mobiliado = models.BooleanField(blank=True)
    moveis_planejados = models.BooleanField(verbose_name='Móveis Planejados'
    , blank=True)
    piscina_privativa = models.BooleanField(verbose_name='Piscina Privativa'
    , blank=True)
    quadra_esportiva = models.BooleanField(verbose_name='Quadra Esportiva'
    , blank=True)
    churrasqueira = models.BooleanField(blank=True)
    valor_venda = models.FloatField(verbose_name='Valor para Venda'
    , null=True,blank=True)
    pagamento = models.TextField(max_length=500,
     verbose_name='Pagamento detalhes', null=True, blank=True)
    valor_aluguel = models.FloatField(verbose_name='Valor para Aluguel')
    frequencia_aluguel = models.CharField(verbose_name='Frequência Aluguel',
     choices=FREQUENCIA_CHOICES, max_length=100)
    valor_altaemporada = models.FloatField(verbose_name='Valor na Alta Temporada')
    valor_baixatemporada = models.FloatField(verbose_name='Valor na Baixa Temporada')
    frequencia_temporada = models.CharField(max_length=100,
    choices=FREQUENCIA_CHOICES, verbose_name='Freqência Temporada')
    acomodacoes = models.PositiveIntegerField(verbose_name='Acomodações')
    condominio = models.FloatField(verbose_name='Valor do Condomínio'
    , null=True, blank=True)
    iptu = models.FloatField(verbose_name='Valor do IPTU'
    , null=True, blank=True)
    taxas_extras = models.FloatField(verbose_name='Taxas Extras'
    , null=True, blank=True)
    numero_matricola = models.CharField(max_length=100,
    verbose_name='Número da Matrícola', null=True, blank=True)
    situacao = models.CharField(max_length=100, choices=SITUACAO_CHOICES
    , null=True, blank=True)
    titulo_aquisitivo = models.CharField(max_length=100,
    choices=TITULO_AQUISITIVO_CHOICES, null=True, blank=True)
    video = models.URLField(null=True, blank=True)

class Apartamento(Imovel):
    TIPO_CHOICES = (('AP','Apartamento'), ('CB','Cobertura'),
    ('SL','Sala Living'), ('KT','Kitinet'),
    ('AD','Apartamento Alto Padrão'),
    ('PS','Posada'), ('HT','Hotel'), ('LF','Loft'),
    ('FT','Flat'))
    ESTADO_CONSERVACAO_CHOICES = (('NV','Novo'),('SV','Semi-Novo'),
    ('US','Usado'), ('EO','Em Obras'))
    AVALIACAO_CHOICES = (('BO','Bom'), ('RG','Regular'),
    ('RS','Reformas Simples'), ('RI','Reformas Importantes'),
    ('RU','Ruim'))
    FREQUENCIA_ALUGUEL_CHOICES = (('DA','Diária'), ('SM','Semanal'),
    ('MS','Mensal'), ('TR','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    FREQUENCIA_TEMPORADA_CHOICES = (('DI','Diária'),('SE','Semanal'),
    ('MS','Mensal'), ('TM','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    SITUACAO_CHOICES = (('QU','Quitado'), ('AL','Alienado'))
    TITULO_AQUISITIVO_CHOICES = (('RE','Regularizado'),
    ('ES','Escritura Pública'), ('EP','Escritura de Posse'),
    ('CC','Contrato de Compra'), ('HP','Hipotecado'),
    ('PO','Posse'), ('PC','Promessa de Compra'),
    ('FN','Financiável'))

    morador_locatario = models.ForeignKey(Fisica
        , null=True, blank=True, verbose_name='Morador/Locatário')
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES
        , null=True, blank=True, verbose_name='Tipo')
    estado_conservacao = models.CharField(max_length=100,
    verbose_name='Estado de Conservação', choices=ESTADO_CONSERVACAO_CHOICES
    , null=True, blank=True)
    nome_edificio = models.CharField(max_length=100
        , null=True, blank=True, verbose_name='Nome do Edifício')
    area_privativa = models.FloatField(null=True, blank=True
        , verbose_name='Área Privativa')
    area_total = models.FloatField(null=True, blank=True)
    idade = models.PositiveIntegerField(null=True, blank=True
        , verbose_name='Idade')
    avaliacao = models.CharField(max_length=100, verbose_name='Avaliação'
        , choices=AVALIACAO_CHOICES, null=True, blank=True)
    dormitorios = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Dormitórios')
    sanitarios = models.PositiveIntegerField(null=True, blank=True
        , verbose_name='Sanitários')
    suites = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Suítes')
    salas = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Salas')
    cozinhas = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Cozinhas')
    areas_servico = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Áreas de Serviço')
    dep_empregada = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Dependência de Empregada')
    sacadas = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Sacadas')
    garagens = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Garagens')
    elevadores = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Elevadores')
    interfone = models.BooleanField(blank=True, default=None, 
        verbose_name='Interfone')
    torneira_quente = models.BooleanField(blank=True, default=None, 
        verbose_name='Torneira Quente')
    gas_canalizado = models.BooleanField(blank=True, default=None, 
        verbose_name='Gás Canalizado')
    mobiliado = models.BooleanField(blank=True, default=None, 
        verbose_name='Mobiliado')
    armarios = models.BooleanField(blank=True, default=None, 
        verbose_name='Armários')
    closet = models.BooleanField(blank=True, default=None, 
        verbose_name='Closet')
    piscina_privativa = models.BooleanField(blank=True, default=None, 
        verbose_name='Piscina Privativa')
    piscina_comum = models.BooleanField(blank=True, default=None, 
        verbose_name='Piscina Comum')
    portaria = models.BooleanField(blank=True, default=None, 
        verbose_name='Portaria')
    salao_festas = models.BooleanField(blank=True, default=None, 
        verbose_name='Salão de Festas')
    salao_ginastica = models.BooleanField(blank=True, default=None, 
        verbose_name='Salão de Ginástica')
    salao_jogos = models.BooleanField(blank=True, default=None, 
        verbose_name='Salãode Jogos')
    playground = models.BooleanField(blank=True, default=None, 
        verbose_name='Play Ground')
    quadra_esportiva = models.BooleanField(blank=True, default=None, 
        verbose_name='Quadra Esportiva')
    churrasqueira = models.BooleanField(blank=True, default=None, 
        verbose_name='Churrascaria')
    brinquedoteca = models.BooleanField(blank=True, default=None, 
        verbose_name='Brinquedoteca')
    sauna = models.BooleanField(blank=True, default=None, 
        verbose_name='Sauna')
    vista_mar = models.BooleanField(blank=True, default=None, 
        verbose_name='Vista Para O Mar')
    espaco_gourmet = models.BooleanField(blank=True, default=None, 
        verbose_name='Espaço Gourmet')
    lan_house = models.BooleanField(blank=True, default=None, 
        verbose_name='Lan House')
    valor_venda = models.FloatField(null=True, blank=True, 
        verbose_name='Valor Venda')
    pagamento = models.TextField(null=True, blank=True, 
        verbose_name='Pagamento')
    valor_aluguel = models.FloatField(null=True, blank=True, 
        verbose_name='Valor do Aluguel')
    frequencia_aluguel = models.CharField(max_length=100, 
        choices=FREQUENCIA_ALUGUEL_CHOICES, null=True, blank=True, 
        verbose_name='Frequencia Aluguel')
    valor_altaemporada = models.FloatField(null=True, blank=True, 
        verbose_name='Valor Alta Temporada')
    valor_baixaemporada = models.FloatField(null=True, blank=True, 
        verbose_name='Valor Baixa Temporada')
    frequencia_temporada = models.CharField(max_length=50, 
        choices=FREQUENCIA_TEMPORADA_CHOICES, null=True, blank=True, 
        verbose_name='Frequencia Alta Temporada')
    acomodacoes = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='Acomodações')
    condominio = models.FloatField(null=True, blank=True, 
        verbose_name='Condomínio')
    iptu = models.PositiveIntegerField(null=True, blank=True, 
        verbose_name='IPTU')
    taxas_extras = models.FloatField(null=True, blank=True, 
        verbose_name='Taxas Extras')
    numero_matricola = models.CharField(max_length=100, null=True, blank=True, 
        verbose_name='Número da Matrícola')
    situacao = models.CharField(max_length=100, choices=SITUACAO_CHOICES
        , null=True, blank=True, verbose_name='Situação')
    titulo_aquisitivo = models.CharField(max_length=100, 
        choices=TITULO_AQUISITIVO_CHOICES, null=True, blank=True, 
        verbose_name='Título Aquisitivo')
    video = models.URLField(null=True, blank=True, 
        verbose_name='Vídeo')

class SalaComercial(Imovel):
    TIPO_CHOICES = (('SL','Sala'), ('GS','Grupo de Salas'),
    ('AC','Andar Corrido'), ('PC','Prédio Comercial'))
    ESTADO_CONSERVACAO_CHOICES = (('NV','Novo'),('SV','Semi-Novo'),
    ('US','Usado'), ('EO','Em Obras'))
    AVALIACAO_CHOICES = (('BO','Bom'), ('RG','Regular'),
    ('RS','Reformas Simples'), ('RI','Reformas Importantes'),
    ('RU','Ruim'))
    FREQUENCIA_ALUGUEL_CHOICES = (('DA','Diária'), ('SM','Semanal'),
    ('MS','Mensal'), ('TR','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    SITUACAO_CHOICES = (('QU','Quitado'), ('AL','Alienado'))
    TITULO_AQUISITIVO_CHOICES = (('RE','Regularizado'),
    ('ES','Escritura Pública'), ('EP','Escritura de Posse'),
    ('CC','Contrato de Compra'), ('HP','Hipotecado'),
    ('PO','Posse'), ('PC','Promessa de Compra'),
    ('FN','Financiável'))
    locatario = models.ForeignKey(Pessoa, null=True, blank=True)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    estado_conservacao = models.CharField(max_length=100,
    verbose_name='Estado de Conservação',
     choices=ESTADO_CONSERVACAO_CHOICES, null=True, blank=True)
    area_privativa = models.FloatField(null=True, blank=True)
    area_total = models.FloatField(verbose_name='Área Total'
    , null=True, blank=True)
    idade = models.PositiveIntegerField(verbose_name='Idade em Anos'
    , null=True, blank=True)
    avaliacao = models.CharField(verbose_name='Avaliação',
    choices=AVALIACAO_CHOICES, max_length=100, null=True, blank=True)
    sanitarios = models.PositiveIntegerField(null=True, blank=True)
    salas = models.PositiveIntegerField(null=True, blank=True)
    copas = models.PositiveIntegerField(null=True, blank=True)
    sacadas = models.PositiveIntegerField(null=True, blank=True)
    garagens = models.PositiveIntegerField(null=True, blank=True)
    andares = models.PositiveIntegerField(null=True, blank=True)
    interfone = models.BooleanField(blank=True)
    portaria = models.BooleanField(blank=True)
    hall_espera = models.BooleanField(verbose_name='Hall de Espera', blank=True)
    sala_reunioes = models.BooleanField(verbose_name='Sala de Reuniões', blank=True)
    auditorios = models.BooleanField(verbose_name='Auditórios', blank=True)
    rede_logica = models.BooleanField(verbose_name='Rede Lógica', blank=True)
    rede_piso = models.BooleanField(verbose_name='Rede Piso', blank=True)
    mobiliado = models.BooleanField(blank=True)
    ar_condicionado_central = models.BooleanField(blank=True)
    escada_emergencia = models.BooleanField(verbose_name='Escada de Emergência'
    , blank=True)
    detector_fumaca = models.BooleanField(verbose_name='Detector de Fumaça'
    , blank=True)
    alarme_incendio = models.BooleanField(verbose_name='Alarme de Incêndio'
    , blank=True)
    sprinkler = models.BooleanField(blank=True)
    gerador = models.BooleanField(blank=True)
    valor_venda = models.FloatField(verbose_name='Valor de Venda',
     null=True, blank=True)
    pagamento = models.TextField(max_length=500,
    verbose_name='Pagamento detalhes', blank=True, null=True)
    valor_aluguel = models.FloatField(verbose_name='Valor do Aluguel',
    null=True, blank=True)
    frequencia_aluguel = models.CharField(verbose_name='Frequência Aluguel',
     choices=FREQUENCIA_ALUGUEL_CHOICES, max_length=100, blank=True, null=True)
    condominio = models.FloatField(verbose_name='Condomínio', blank=True,
    null=True)
    iptu = models.FloatField(verbose_name='Valor do IPTU', blank=True, null=True)
    taxas_extras = models.FloatField(verbose_name='Taxas Extras'
    , blank=True, null=True)
    numero_matricula = models.CharField(verbose_name='Número da Matrícula',
    max_length=100, blank=True, null=True)
    situacao = models.CharField(verbose_name='Situação',
     choices=SITUACAO_CHOICES, max_length=100, null=True, blank=True)
    titulo_aquisitivo = models.CharField(verbose_name='Título Aquisitivo',
    choices=TITULO_AQUISITIVO_CHOICES, max_length=100, blank=True, null=True)
    video = models.URLField(null=True, blank=True)

class Empreendimento(Imovel):
    SITUACAO_EMPREENDIMENTO_CHOICES = (('PL','Pré Lançamento'),
    ('LA','Lançamento'), ('EO','Em Obras'),('PM','Pronto Para Morar'))
    FREQUENCIA_ALUGUEL_CHOICES = (('DA','Diária'), ('SM','Semanal'),
    ('MS','Mensal'), ('TR','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    TIPO_EMPREENDIMENTO_CHOICES = (('RS','Residencial'),
    ('CM','Comercial'))

    nome = models.CharField(max_length=500, null=True, blank=True)
    situacao = models.CharField(verbose_name='Situação',
    choices=SITUACAO_EMPREENDIMENTO_CHOICES, max_length=100
    , null=True, blank=True)
    tipo = models.CharField(verbose_name='Tipo de Empreendimento',
    choices=TIPO_EMPREENDIMENTO_CHOICES, max_length=100
    , null=True, blank=True)
    vagas_garagem = models.PositiveIntegerField(verbose_name='Vagas na Garagem'
    , null=True, blank=True)
    areas_das_unidades = models.FloatField(verbose_name='Áreas das Unidades'
    , null=True, blank=True)
    previsao_entrega = models.DateField(null=True, blank=True)
    torneira_quente = models.BooleanField(verbose_name='Torneira Quente'
    , blank=True)
    gas_canalizado = models.BooleanField(verbose_name='Gás Canalizado'
    , blank=True)
    piscina = models.BooleanField(blank=True)
    salao_fastas = models.BooleanField(verbose_name='Salão de Festas'
    , blank=True)
    salao_ginastica = models.BooleanField(verbose_name='Salão de Ginástica'
    , blank=True)
    quadra_esportiva = models.BooleanField(verbose_name='Quadra Esportiva'
    , blank=True)
    sauna = models.BooleanField(blank=True)
    vista_mar = models.BooleanField(verbose_name='Vista ao Mar'
    , blank=True)
    portaria_recepcao = models.BooleanField(verbose_name='Portaria/Recepção'
    , blank=True)
    circuito_tv = models.BooleanField(verbose_name='Circuito TV'
    , blank=True)
    hall_espera = models.BooleanField(verbose_name='Hall de Espera'
    , blank=True)
    sala_reunioes = models.BooleanField(verbose_name='Sala de Reuniões'
    , blank=True)
    auditorio = models.BooleanField(verbose_name='Auditórios'
    , blank=True)
    rede_logica = models.BooleanField(verbose_name='Rede Lógica'
    , blank=True)
    rede_de_piso = models.BooleanField(verbose_name='Rede de Piso'
    , blank=True)
    ar_condicionado_central = models.BooleanField(verbose_name='Ar Condicionado Central'
    , blank=True)
    site_empreendimento = models.URLField(verbose_name='Site Empreendimento'
    , blank=True, null=True)
    observacoes = models.TextField(verbose_name='Observações'
    , blank=True, null=True)
    valor_exibicao = models.CharField(verbose_name='Valor para Exibição',
    max_length=100, blank=True, null=True)
    valores_formas_pagamento = models.TextField(verbose_name='Valores e Formas de Pagamento', max_length=100, blank=True, null=True)
    video = models.URLField(null=True, blank=True, 
        verbose_name='Vídeo no Youtube')

class EstabelecimentoComercial(Imovel):
    ESTADO_CONSERVACAO_CHOICES = (('NV','Novo'),('SV','Semi-Novo'),
    ('US','Usado'), ('EO','Em Obras'))
    TIPO_CHOICES = (('PC','Ponto Comercial'), ('AC','Academia'),
    ('AÇ','Açougue'), ('AF','Artigos de Feta'), ('AT','Atacado'),
    ('AV','Avícola'), ('AC','Avicultura'), ('BJ','Banca de Jornal'),
    ('BR','Bar'), ('BP','Bazar e Papelaria'), ('Bo','Boate'),
    ('BM','Bom Boniere'), ('BF','Buffet'), ('CB','Cabelereiro'),
    ('CE','Café Expresso'), ('CS','Cantina de Escola'), ('CC','Casa Comercial'),
    ('CS','Casa de Sucos'), ('CT','Centro Automotivo'), ('CP','Copiadora'),
    ('CZ','Cozinha Industrial'), ('DP','Depósito'), ('DG','Depósito de gás'),
    ('DK','Disk Água'), ('DP','Disk Pizza'), ('DC','Doceria'),
    ('EM','Embalagens'), ('ES','Escola'), ('EF','Esfilharia'),
    ('ET','Estacionamento'), ('FB','Aábrica'), ('FM','Farmácia'),
    ('GL','Gelaria'), ('GP','Galpão'), ('HT','Hotel'),
    ('ID','Indústria'), ('LH','Lan House'), ('LC','Lanchonet'),
    ('LR','Lava Rápido'), ('LR','Locação de Roupas'),
    ('LC','Loja de Calçados'), ('LF','Loja de Ferragens'),
    ('LF','Loja de Fraudas'), ('LL','Loja de Langerie'),
    ('LR','Loja de Roupas'), ('LU','Loja de Utilidades'),
    ('LT','Lotérica'), ('MC','Mercado'), ('MT','Motel'),
    ('PD','Padria'), ('PP','Papelaria'), ('PS','Pastelaria'),
    ('PF','Perfumaria'), ('PS','Pet Shop'), ('PZ','Pizzaria'),
    ('PG','Posto de Gasolina'), ('PU','Pousada'), ('PC','Prédio Comercial'),
    ('PL','Produtos de Limpeza'), ('QU','Quitanda'), ('RT','Restaurante'),
    ('RF','Retífica'), ('RV','Revistaria'), ('RS','Rotisserie'),
    ('SC','Salão Comercial'), ('SP','Shoping Center'), ('SM','Supermercado'),
    ('VL','Video Locadora'), ('CL','Clínica'))
    ACESSO_CHOICES = (('TR','Térreo'), ('1S','1° Sobreloja'),
    ('2S','2° Sobreloja'), ('3S','3° Sobreloja'))
    AVALIACAO_CHOICES = (('BO','Bom'), ('RG','Regular'),
    ('RS','Reformas Simples'), ('RI','Reformas Importantes'),
    ('RU','Ruim'))
    FREQUENCIA_ALUGUEL_CHOICES = (('DA','Diária'), ('SM','Semanal'),
    ('MS','Mensal'), ('TR','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    SITUACAO_CHOICES = (('QU','Quitado'), ('AL','Alienado'))
    TITULO_AQUISITIVO_CHOICES = (('RE','Regularizado'),
    ('ES','Escritura Pública'), ('EP','Escritura de Posse'),
    ('CC','Contrato de Compra'), ('HP','Hipotecado'),
    ('PO','Posse'), ('PC','Promessa de Compra'),
    ('FN','Financiável'))

    locatario = models.ForeignKey(Pessoa, null=True, blank=True, 
        verbose_name='Morador Locatário')
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES
    , null=True, blank=True, verbose_name='Tipo')
    acesso = models.CharField(max_length=100, choices=ACESSO_CHOICES
    , null=True, blank=True, verbose_name='Acesso')
    estado_conservacao = models.CharField(verbose_name='Estado de Conservação'
    , max_length=100, choices=ESTADO_CONSERVACAO_CHOICES
    , null=True, blank=True)
    area_privativa = models.FloatField(verbose_name='Área Privativa'
    , null=True, blank=True)
    area_total = models.FloatField(verbose_name='Área Total'
    , null=True, blank=True)
    idade = models.PositiveIntegerField(verbose_name='Idade em Anos'
    , null=True, blank=True)
    avaliacao = models.CharField(max_length=100, choices=AVALIACAO_CHOICES
    , null=True, blank=True)
    sanitarios = models.PositiveIntegerField(verbose_name='Sanitários'
    , null=True, blank=True)
    copas = models.PositiveIntegerField(null=True, blank=True)
    pavimentos = models.PositiveIntegerField(null=True, blank=True)
    garagens = models.PositiveIntegerField(null=True, blank=True)
    elevadores = models.PositiveIntegerField(null=True, blank=True)
    interfone = models.BooleanField(blank=True)
    sala_reunioes = models.BooleanField(blank=True)
    rede_logica = models.BooleanField(verbose_name='Rede Lógica', blank=True)
    rede_piso = models.BooleanField(verbose_name='Rede de Piso', blank=True)
    ar_condicionado_central = models.BooleanField(verbose_name='Ar Condicionado Central'
    , blank=True)
    escada_rolante = models.BooleanField(verbose_name='Escada Rolante'
    , blank=True)
    escada_emergencia = models.BooleanField(verbose_name='Escada De Emergência'
    , blank=True)
    detector_fumaca = models.BooleanField(verbose_name='Detector de Fumaça'
    , blank=True)
    alarme_incendio = models.BooleanField(verbose_name='Alarme de Incêndio'
    , blank=True)
    sprinkler = models.BooleanField(blank=True)
    gerador = models.BooleanField(blank=True)
    valor_venda = models.FloatField(verbose_name='Valor de Venda'
    , blank=True)
    pagamento = models.TextField(max_length=300
    , verbose_name='Detalhes Pagamento', null=True)
    valor_aluguel = models.FloatField(verbose_name='Valor do Aluguel'
    , null=True, blank=True)
    frequencia_aluguel = models.CharField(max_length=100,
    choices=FREQUENCIA_ALUGUEL_CHOICES, verbose_name='Freqencia Aluguel'
    , null=True, blank=True)
    condominio = models.FloatField(verbose_name='Valor do Condomínio'
    , null=True, blank=True)
    iptu = models.FloatField(verbose_name='Valor do IPTU'
    , null=True, blank=True)
    taxas_extras = models.FloatField(verbose_name='Taxas Extras'
    , null=True, blank=True)
    numero_matricula = models.CharField(max_length=100,
    verbose_name='Número de Matrícula', null=True, blank=True)
    situacao = models.CharField(verbose_name='Situação',
    choices=SITUACAO_CHOICES, max_length=100, null=True, blank=True)
    titulo_aquisitivo = models.CharField(verbose_name='Título Aquisitivo',
    choices=TITULO_AQUISITIVO_CHOICES, max_length=100
    , null=True, blank=True)
    video = models.URLField(null=True, blank=True)


class TerrenoLote(Imovel):
    SUPERFICIE_CHOICES = (('CM','Cimentada'), ('SC','Seca'),
    ('MT','Matagal'), ('GR','Grama'), ('RC','Rochosa'), ('Al','Alagadiça'),
    ('AD','Alagada'))
    FREQUENCIA_ALUGUEL_CHOICES = (('DA','Diária'), ('SM','Semanal'),
    ('MS','Mensal'), ('TR','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    SITUACAO_CHOICES = (('QU','Quitado'), ('AL','Alienado'))
    TITULO_AQUISITIVO_CHOICES = (('RE','Regularizado'),
    ('ES','Escritura Pública'), ('EP','Escritura de Posse'),
    ('CC','Contrato de Compra'), ('HP','Hipotecado'),
    ('PO','Posse'), ('PC','Promessa de Compra'),
    ('FN','Financiável'))

    superficie = models.CharField(max_length=100, verbose_name='Superfície',
    choices=SUPERFICIE_CHOICES, null=True, blank=True)
    area = models.FloatField(verbose_name='Área em m²', null=True, blank=True)
    frente = models.FloatField(verbose_name='Frente em m', null=True, blank=True)
    area_edificada = models.FloatField(verbose_name='Área em m²', null=True
    , blank=True)
    observacoes = models.TextField(verbose_name='Observações', max_length=300
    , null=True, blank=True)
    valor_venda = models.FloatField(verbose_name='Valor de Venda', null=True
    , blank=True)
    valor_aluguel = models.FloatField(verbose_name='Valor do Aluguel', null=True
    , blank=True)
    frequencia_aluguel = models.CharField(verbose_name='Freqencia Aluguel',
    choices=FREQUENCIA_ALUGUEL_CHOICES, max_length=100, null=True, blank=True)
    pagamento = models.TextField(max_length=300,
    verbose_name='Detalhes Pagamento', null=True, blank=True)
    condominio = models.FloatField(verbose_name='Valor do Condomínio'
    , null=True, blank=True)
    iptu = models.FloatField(verbose_name='Valor do IPTU', null=True
    , blank=True)
    taxas_extras = models.FloatField(verbose_name='Taxas Extras', null=True
    , blank=True)
    numero_matricula = models.CharField(max_length=100,
    verbose_name='Número da Matrícula', null=True, blank=True)
    situacao = models.CharField(verbose_name='Situação'
    , choices=SITUACAO_CHOICES, max_length=100, null=True, blank=True)
    titulo_aquisitivo = models.CharField(max_length=100,
    choices=TITULO_AQUISITIVO_CHOICES, verbose_name='Título Aquisitivo'
    , null=True, blank=True)
    video = models.URLField(null=True, blank=True)

class PropriedadeRural(Imovel):
    PR_TIPO_CHOICES = (('ST','Sítio'), ('CH','Chácara'), ('TR','Terras'),
    ('FZ','Fazenda'))
    AVALIACAO_CHOICES = (('BO','Bom'), ('RG','Regular'),
    ('RS','Reformas Simples'), ('RI','Reformas Importantes'),
    ('RU','Ruim'))
    PAGAMENTO_CHOICE = (('AV','À Vista'),('FN','Financiado'),
    ('AG','Ágio'), ('AC','A Conbinar'))
    FREQUENCIA_ALUGUEL_CHOICES = (('DA','Diária'), ('SM','Semanal'),
    ('MS','Mensal'), ('TR','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    FREQUENCIA_TEMPORADA_CHOICES = (('DI','Diária'),('SE','Semanal'),
    ('MS','Mensal'), ('TM','Trimestral'), ('SM','Semestral'),
    ('AN','Anual'))
    SITUACAO_CHOICES = (('QU','Quitado'), ('AL','Alienado'))
    TITULO_AQUISITIVO_CHOICES = (('RE','Regularizado'),
    ('ES','Escritura Pública'), ('EP','Escritura de Posse'),
    ('CC','Contrato de Compra'), ('HP','Hipotecado'),
    ('PO','Posse'), ('PC','Promessa de Compra'),
    ('FN','Financiável'))

    morador_locatario = models.ForeignKey(Pessoa, verbose_name='Morador/Locatário'
    , null=True, blank=True)
    tipo = models.CharField(max_length=100, choices=PR_TIPO_CHOICES
    , null=True, blank=True)
    distancia_centro = models.FloatField(verbose_name='Distãncia do Centro Em Km'
    , null=True, blank=True)
    area_construida = models.FloatField(verbose_name='Área Contruída em m²'
    , null=True, blank=True)
    idade = models.PositiveIntegerField(verbose_name='Idade em anos'
    , null=True, blank=True)
    avaliacao = models.CharField(verbose_name='Avaliação', max_length=100,
    choices=AVALIACAO_CHOICES, null=True, blank=True)
    dormitorios = models.PositiveIntegerField(verbose_name='Dormitórios'
    , null=True, blank=True)
    suites = models.PositiveIntegerField(verbose_name='Suítes'
    , null=True, blank=True)
    sanitarios = models.PositiveIntegerField(verbose_name='Sanitários'
    , null=True, blank=True)
    cercado = models.BooleanField(blank=True)
    casa_caseiro = models.BooleanField(verbose_name='Casa de Caseiro'
    , blank=True)
    deposito = models.BooleanField(verbose_name='Depósito', blank=True)
    salao_festas = models.BooleanField(verbose_name='Salão de Festas'
    , blank=True)
    salao_jogos = models.BooleanField(verbose_name='Salão de Jogos'
    , blank=True)
    piscina = models.BooleanField(verbose_name='Piscina', blank=True)
    quadra_esportiva = models.BooleanField(verbose_name='Quadra Esportiva'
    , blank=True)
    campo_futbol = models.BooleanField(verbose_name='Campo de Futbol'
    , blank=True)
    churrasqueira = models.BooleanField(verbose_name='Churrasqueira'
    , blank=True)
    viveiro_passaros = models.BooleanField(verbose_name='Viveiro de Pássaros'
    , blank=True)
    curral = models.BooleanField(verbose_name='Curral', blank=True)
    galinheiro = models.BooleanField(verbose_name='Galinheiro', blank=True)
    chiqueiro = models.BooleanField(verbose_name='Chiqueiro', blank=True)
    horta = models.BooleanField(blank=True)
    lago = models.BooleanField(blank=True)
    cascata = models.BooleanField(blank=True)
    energia_eletrica = models.BooleanField(verbose_name='Energia Elétrica'
    , blank=True)
    energia_solar = models.BooleanField(verbose_name='Energia Solar', blank=True)
    saneamento_basico = models.BooleanField(verbose_name='Saneamento Básico', blank=True)
    observacoes = models.TextField(verbose_name='Observações', max_length=300
    , null=True, blank=True)
    valor_venda = models.FloatField(verbose_name='Valor de Venda'
    , null=True, blank=True)
    pagamento = models.CharField(max_length=100, null=True, blank=True
    , verbose_name='Detalhes Pagamento', choices=PAGAMENTO_CHOICE)
    valor_aluguel = models.FloatField(verbose_name='Valor Aluguel'
    , null=True, blank=True)
    frequencia_aluguel = models.CharField(verbose_name='Frequência Aluguel'
    , max_length=100, choices=FREQUENCIA_ALUGUEL_CHOICES
    , null=True, blank=True)
    valor_altaemporada = models.FloatField(verbose_name='Valor Alta Temporada'
    , null=True, blank=True)
    valor_baixaemporada = models.FloatField(verbose_name='Valor Baixa Temporada'
    , null=True, blank=True)
    frequencia_temporada = models.CharField(verbose_name='Frequência Temporada',
    max_length=100, choices=FREQUENCIA_TEMPORADA_CHOICES
    , null=True, blank=True)
    acomodacoes = models.PositiveIntegerField(verbose_name='Acomodações'
    , null=True, blank=True)
    condominio = models.FloatField(verbose_name='Valor do Condomínio'
    , null=True, blank=True)
    iptu = models.FloatField(verbose_name='Valor do IPTU'
    , null=True, blank=True)
    taxas_extras = models.FloatField(verbose_name='Taxas Extras'
    , null=True, blank=True)
    numero_matricula = models.CharField(max_length=100,
    verbose_name='Número da Matrícula', null=True, blank=True)
    situacao = models.CharField(max_length=100, verbose_name='Situação',
    choices=SITUACAO_CHOICES, null=True, blank=True)
    titulo_aquisitivo = models.CharField(max_length=100,
    verbose_name='Título Aquisitivo', null=True, blank=True
    , choices=TITULO_AQUISITIVO_CHOICES)
    video = models.URLField(null=True, blank=True)

class Capitacao(models.Model):
    TIPO_CHOICES = (('AP', 'Apartamento'), ('CS', 'Casa'),
        ('SC', 'Sala Comercial'), ('EC', 'Estabelecimento Comercial'),
        ('TR', 'Terreno ou Lote'), ('PR', 'Propriedade Rural'))
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES, null=True,
        blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    proprietario = models.CharField(max_length=100, null=True, blank=True, 
        verbose_name='Proprietário')
    telefone = models.CharField(max_length=100, null=True,
        blank=True, help_text='(DDD)99999-9999')
    email = models.EmailField(null=True, blank=True, 
        help_text='exemplo@email.com')
