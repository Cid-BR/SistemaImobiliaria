#Imobiliaria
from django.shortcuts import render
from .forms import ApartamentoForm, PessoaFisicaForm, PessoaJuridicaForm, \
CasaForm, SalaComercialForm, EstabelecimentoComercialForm, TerrenoLoteForm, \
PropriedadeRuralForm, EmpreendimentoForm, AtendimentoForm, CapitacaoForm, \
VisitaForm
from django.http import HttpResponse
from SistemaImobiliaria.Imobiliaria.models import Fisica, Juridica, Apartamento, \
Casa, SalaComercial, EstabelecimentoComercial, TerrenoLote, \
PropriedadeRural, Empreendimento, Atendimento, Capitacao, Pessoa

def index(request):
    return render(request, 'imobiliaria/index.html')

def novo_apartamento(request):
    context = {}
    if request.method == 'POST':
        form = ApartamentoForm(request.POST, request.FILES)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context.update({'msg': 'O Apartamento foi registrado com sucesso'})
        else:
            context.update({'msg': form.errors})
    else:
        form = ApartamentoForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/novo_apartamento.html', context)

def nova_casa(request):
    context = {}
    if request.method == 'POST':
        form = CasaForm(request.POST, request.FILES)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context = {'msg':'Casa registrada com sucesso'}
        else:
            form.update({'msg': form.errors})
    else:
        form = CasaForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/nova_casa.html', context)


def novo_terreno_lote(request):
    context = {}
    if request.method == 'POST':
        form = TerrenoLoteForm(request.POST, request.FILES)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context = {'msg':'Terrono/Lote registrado com sucesso'}
        else:
            context.update({'msg': form.errors})
    else:
        form = TerrenoLoteForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/novo_terreno_lote.html', context)

def nova_propriedade_rural(request):
    context = {}
    if request.method == 'POST':
        form = PropriedadeRuralForm(request.POST, request.FILES)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context = {'msg':'Propriedade Rural registrada com sucesso'}
        else:
            context.update({'msg': form.errors})
    else:
        form = PropriedadeRuralForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/nova_propriedade_rural.html', context)


def nova_sala_comercial(request):
    context = {}
    if request.method == 'POST':
        form = SalaComercialForm(request.POST, request.FILES)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context = {'msg':'Sala Comercial registrada com sucesso'}
        else:
            context.update({'msg': form.errors})
    else:
        form = SalaComercialForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/nova_sala_comercial.html', context)


def novo_estabelecimento_comercial(request):
    context = {}
    if request.method == 'POST':
        context.update({'form': form})
        form = EstabelecimentoComercialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'msg':'Estabelecimento Comercial registrado com sucesso'}
        else:
            context.update({'msg':form.errors})
    else:
        form = EstabelecimentoComercialForm()
        context.update({'form': form})
    return render(request, 'imobiliaria/novo_estabelecimento_comercial.html'
        , context)

def novo_empreendimento(request):
    context = {}
    if request.method == 'POST':
        form = EmpreendimentoForm(request.POST, request.FILES)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context = {'msg':'Empreendimento registrado com sucesso'}
        else:
            context.update({'msg': form.errors})
    else:
        form = EmpreendimentoForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/novo_empreendimento.html',
     context)

def nova_pessoa_fisica(request):
    context = {}
    if request.method == 'POST':
        form = PessoaFisicaForm(data=request.POST)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context.update({'msg': 'Pessoa física registrada com sucesso'})
        else:
            context.update({'msg': form.errors})
    else:
        form = PessoaFisicaForm()
        context.update({'form': form})
    return render(request, 'imobiliaria/nova_pessoa_fisica.html', context)

def nova_pessoa_juridica(request):
    context = {}
    if request.method == 'POST':
        form = PessoaJuridicaForm(data=request.POST)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context.update({'msg': 'Pessoa jurídica registrada com sucesso'})
        else:
            context.update({'msg': form.errors})   
    else:
        form = PessoaJuridicaForm()
        context.update({'form': form})
    return render(request, 'imobiliaria/nova_pessoa_juridica.html', context)

# pf
def exibir_pf(request):
    pfs = Fisica.objects.all()
    context = {'pfs': pfs}
    return render(request, "imobiliaria/exibir_pf.html",
        context)


def pesquisa_pf(request, valor):
    pfs = None
    if valor == 'all':
        pfs = Fisica.objects.all()
    else:
        pfs = Fisica.objects.filter(nome__contains=valor)

    context = {'pfs': pfs}
    return render(request, "imobiliaria/pesquisa_pf.html",
        context)


def detalhes_pf(request, id):
    pf = Fisica.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = PessoaFisicaForm(request.POST, instance=pf)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed():
                pf = form.save()
                context.update({'msg': 'As informações foram atualizadas com sucesso'})
            else:
                context.update({'msg': 'Nenhuma alteração foi realizada'})
        else:
            context.update({'msg': form.errors})
    
    else:
        form = PessoaFisicaForm(instance=pf)
        context.update({'form': form})
    
    return render(request, 'imobiliaria/detalhes_pf.html', context)

# pj
def exibir_pj(request):
    pjs = Juridica.objects.all()
    context = {'pjs': pjs}
    return render(request, "imobiliaria/exibir_pj.html",
        context)


def pesquisa_pj(request, valor):

    pjs = None
    if valor == 'all':
        pjs = Juridica.objects.all()
    else:
        pjs = Juridica.objects.filter(nome__contains=valor)

    context = {'pjs': pjs}
    return render(request, "imobiliaria/pesquisa_pj.html",
        context)


def detalhes_pj(request, id):
    pj = Juridica.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = PessoaJuridicaForm(request.POST, instance=pj)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed():
                pj = form.save()
                context.update({'msg': 'Os dados da pessoa jurídica foram editados com sucesso'})
            else:
                context.update({'msg': 'Nenhuma mudança foi detectada'})
        else:
            context.update({'msg': form.errors})

    else:
        form = PessoaJuridicaForm(instance=pj)
        context = {'form': form}
    
    return render(request, 'imobiliaria/detalhes_pj.html', context)

#apartamento
def exibir_apartamento(request):
    apartamentos = Apartamento.objects.all()
    context = {'apartamentos': apartamentos}
    return render(request, "imobiliaria/exibir_apartamento.html",
        context)


def pesquisa_apartamento(request, valor):
    apartamentos = None
    if valor == 'all':
        apartamentos = Apartamento.objects.all()
    else:
        apartamentos = Apartamento.objects.filter(bairro__contains=valor)

    context = {'apartamentos': apartamentos}
    return render(request, "imobiliaria/pesquisa_apartamento.html",
        context)


def detalhes_apartamento(request, id):
    apartamento = Apartamento.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = ApartamentoForm(request.POST, instance=apartamento)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                apartamento = form.save()
                context = {'msg': 'Os dados do Apartamento foram atualizados com sucesso'}
            else:
                context.update({'msg': 'Os dados não foram alterados'})
        else:
            context.update({'msg': form.errors})
    else:
        form = ApartamentoForm(instance=apartamento)
        context = {'form': form}
    return render(request, 'imobiliaria/detalhes_apartamento.html', context)

# casa
def exibir_casa(request):
    casas = Casa.objects.all()
    context = {'casas': casas}
    return render(request, "imobiliaria/exibir_casa.html",
        context)

def pesquisa_casa(request, valor):
    casas = None
    if valor == 'all':
        casas = Casa.objects.all()
    else:
        casas = Casa.objects.filter(bairro__contains=valor)

    context = {'casas': casas}
    return render(request, "imobiliaria/pesquisa_casa.html",
        context)


def detalhes_casa(request, id):
    casa = Casa.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = CasaForm(request.POST, instance=casa)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                casa = form.save()
                context = {'mas':'Os Dados Foram Editados Com Sucesso'}
        else:
            context.update({'msg': form.errors})
    else:
        form = CasaForm(instance=casa)
        context = {'form': form}
    return render(request, 'imobiliaria/detalhes_casa.html', context)

# salacomercial
def exibir_salacomercial(request):
    salascomerciais = SalaComercial.objects.all()
    context = {'salascomerciais': salascomerciais}
    return render(request, "imobiliaria/exibir_salacomercial.html",
        context)

def pesquisa_salacomercial(request, valor):
    salascomerciais = None
    if valor == 'all':
        salascomerciais = SalaComercial.objects.all()
    else:
        salascomerciais = SalaComercial.objects.filter(bairro__contains=valor)

    context = {'salascomerciais': salascomercias}
    return render(request, "imobiliaria/pesquisa_salacomercial.html",
        context)


def detalhes_salacomercial(request, id):
    salacomercial = SalaComercial.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = SalaComercialForm(request.POST, instance=salacomercial)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                salacomercial = form.save()
                context = {'msg':'Os dados foram editados com sucesso'}
            else:
                context.update({'msg': 'Os dados não foram alterados'})
        else:
            context.update({'msg': form.errors})
    else:
        form = SalaComercialForm(instance=salacomercial)
        context.update({'form': form})
        context = {'form': form}
    return render(request, 'imobiliaria/detalhes_salacomercial.html', context)

# estabelecimentocomercial
def exibir_estabalecimentocomercial(request):
    estabalecimentoscomerciais = EstabelecimentoComercial.objects.all()
    context = {'estabalecimentoscomerciais': estabalecimentoscomerciais}
    return render(request, "imobiliaria/exibir_estabalecimentocomercial.html",
        context)

def pesquisa_estabalecimentocomercial(request, valor):
    estabalecimentoscomerciais = None
    if valor == 'all':
        estabalecimentoscomerciais = EstabelecimentoComercial.objects.all()
    else:
        esbelecimentoscomerciais = EstabelecimentoComercial.objects.filter(bairro__contains=valor)

    context = {'estabalecimentoscomerciais': estabalecimentoscomerciais}
    return render(request, "imobiliaria/pesquisa_estabalecimentocomercial.html",
        context)

def detalhes_estabelecimentocomercial(request, id):
    estabalecimentocomercial = EstabelecimentoComercial.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = EstabelecimentoComercialForm(request.POST, instance=estabalecimentocomercial)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                estabalecimentocomercial = form.save()
                context = {'msg': 'Os Dados Foram Editados Com Sucesso'}
            else:
                context.update({'msg': 'Os dados não foram alterados'})
        else:
            context.update({'msg': form.errors})
    else:
        form = EstabelecimentoComercialForm(instance=estabalecimentocomercial)
        context = {'form': form}
    return render(request, 'imobiliaria/detalhes_estabalecimentocomercial.html', context)

# TerrenoLote
def exibir_terrenolote(request):
    terrenos = TerrenoLote.objects.all()
    context = {'terrenos': terrenos}
    return render(request, "imobiliaria/exibir_terrenolote.html",
        context)

def pesquisa_terrenolote(request, valor):
    terrenos = None
    if valor == 'all':
        terrenos = TerrenoLote.objects.all()
    else:
        terrenos = TerrenoLote.objects.filter(bairro__contains=valor)

    context = {'terrenos': terrenos}
    return render(request, "imobiliaria/pesquisa_terrenolote.html",
        context)

def detalhes_terrenolote(request, id):
    terrenolote = TerrenoLote.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = TerrenoLoteForm(request.POST, instance=terrenolote)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                terrenolote = form.save()
                context = {'msg':'Os dados foram editados com sucesso'}
            else:
                context.update({'msg': 'Os dados não foram alterados'})
        else:
            context.update({'msg': form.errors})
    else:
        form = TerrenoLoteForm(instance=terrenolote)
        context = {'form': form}
        return render(request, 'imobiliaria/detalhes_terrenolote.html'
            , context)


# PropriedadeRural
def exibir_propriedaderural(request):
    propriedades = PropriedadeRural.objects.all()
    context = {'propriedades': propriedades}
    return render(request, "imobiliaria/exibir_propriedaderural.html",
        context)

def pesquisa_propriedaderural(request, valor):
    propriedades = None
    if valor == 'all':
        propriedades = PropriedadeRural.objects.all()
    else:
        propriedades = PropriedadeRural.objects.filter(bairro__contains=valor)

    context = {'propriedades': propriedades}
    return render(request, "imobiliaria/pesquisa_propriedaderural.html",
        context)

def detalhes_propriedaderural(request, id):
    propriedaderural = PropriedadeRural.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = PropriedadeRuralForm(request.POST, instance=propriedaderural)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                propriedaderural = form.save()
                context = {'mas':'Os dados foram editados com sucesso'}
            else:
                context = {'mas':'Os dados foram alterados'}
    else:
        form = PropriedadeRuralForm(instance=propriedaderural)
        context = {'form': form}
    return render(request, 'imobiliaria/detalhes_propriedaderural.html', context)

# Empreendimento
def exibir_empreendimento(request):
    empreendimentos = Empreendimento.objects.all()
    context = {'empreendimentos': empreendimentos}
    return render(request, "imobiliaria/exibir_empreendimento.html",
        context)

def pesquisa_empreendimento(request, valor):
    empreendimentos = None
    if valor == 'all':
        empreendimentos = Empreendimento.objects.all()
    else:
        empreendimentos = Empreendimento.objects.filter(bairro__contains=valor)

    context = {'empreendimentos': empreendimentos}
    return render(request, "imobiliaria/pesquisa_empreendimento.html",
        context)

def detalhes_empreendimento(request, id):
    empreendimento = Empreendimento.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = EmpreendimentoForm(request.POST, instance=empreendimento)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                empreendimento = form.save()
                context = {'msg': 'Os dados foram editados com sucesso'}
            else:
                context = {'msg': 'Os dados não foram alterados'}
    else:
        form = EmpreendimentoForm(instance=empreendimento)
        context = {'form': form}
        return render(request, 'imobiliaria/detalhes_empreendimento.html'
            , context)

# Atendimento
def novo_atendimento(request):
    context = {}
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context.update({'msg': 'Atendimento cadastrado com sucesso'})
        else:
            context.update({'msg': form.errors})
                
    else:
        form = AtendimentoForm()
        context.update({'form': form})
    return render(request, 'imobiliaria/novo_atendimento.html', context)


def exibir_atendimento(request):
    ats = Atendimento.objects.all()
    context = {'ats': ats}
    return render(request, "imobiliaria/exibir_atendimento.html",
        context)

def pesquisa_atendimento(request, valor=None):
    clientes = Pessoa.objects.all()
    context = {'clientes': clientes}
    return render(request, "imobiliaria/pesquisa_atendimento.html", 
        context)

def detalhes_atendimento(request, id):
    atendimento = Atendimento.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=atendimento)
        context.update({'form': form})
        if form.is_valid():
            if form.has_changed:
                atendimento = form.save()
                context = {'msg': 'Os dados foram editados com sucesso'}
            else:
                context = {'msg': 'Os dados não foram alterados'}
        else:
            context.update({'msg': errors})
    else:
        form = AtendimentoForm(instance=atendimento)
        context = {'form': form}
        return render(request, 'imobiliaria/detalhes_atendimento.html'
            , context)

def realizar_pesquisa(request):
    from datetime import date, timedelta
    q = ''
    if request.method == 'POST':
        client = request.POST.get('client')
        situation = request.POST.get('situation')
        period = request.POST.get('period')

        q = "select * from public.\"Imobiliaria_atendimento\" "\
        "where situacao = '{}'".format(situation)

        # defining the client
        if client != 'all':
            q += " and cliente_id = {}".format(client)

        sd = None # date for search
        sdf = None # date final for search

        # defining the period
        if period == 'today':
            sd = date.today()
            q += " and data = '{}'".format(sd)
        elif period == 'tomorrow':
            sd = date.today() + timedelta(days=1)
            q += " and data = '{}'".format(sd)
        elif period == 'next_seven_days':
            sd = date.today()
            sdf = date.today() + timedelta(days=7)
            q += " and data between '{}' and '{}'".format(sd, sdf)
        elif period == 'next_thirty_days':
            sd = date.today()
            sdf = date.today() + timedelta(days=30)
            q += " and data between '{}' and '{}'".format(sd, sdf)

    ats = Atendimento.objects.raw(q)
    context = {'ats': ats}
    return render(request, 'imobiliaria/exibir_atendimento.html'
        , context)

def agendar_visita(request, id_atendimento):
    # at = Atendimento.objects.get(id=id_atendimento)
    context = {}
    if request.method == 'POST':
        data = request.POST['data']
        observacoes = request.POST['observacoes']
        dados = {'atendimento': id_atendimento, 'data': data
        , 'observacoes': observacoes}
        form = VisitaForm(dados)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context.update({'msg':'Visita registrada com sucesso'})

        else:
            context.update({'msg':form.errors})

    else:
        form = VisitaForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/nova_visita.html', 
        context)


# Capitacao
def nova_capitacao(request):
    context = {}
    if request.method == 'POST':
        form = CapitacaoForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            form.save()
            context.update({'msg': 'Captação Registrada com Sucesso'})
        else:
            context.update({'msg': form.errors})
    else:
        form = CapitacaoForm()
        context.update({'form': form})

    return render(request, 'imobiliaria/nova_capitacao.html', context)


def exibir_captacao(request):
    cps = Capitacao.objects.all()
    context = {'cps': cps}
    return render(request, "imobiliaria/exibir_capitacao.html",
        context)

def detalhes_capitacao(request, id):
    capitacao = Capitacao.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = CapitacaoForm(request.POST, instance=capitacao)
        context.update({'form': form})
        if form.is_valid():
            capitacao = form.save()
            context.update({'msg':'Os dados foram editados com sucesso'})
        else:
            context.update({'msg':form.errors})
            
    else:
        form = CapitacaoForm(instance=capitacao)
        context.update({'form': form, 'id': id})
        return render(request, 'imobiliaria/detalhes_capitacao.html'
            , context)
