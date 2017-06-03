from django import forms
from SistemaImobiliaria.Imobiliaria.models import Apartamento, Fisica,\
 Juridica, Casa, SalaComercial, EstabelecimentoComercial, TerrenoLote,\
 PropriedadeRural, Empreendimento, Atendimento, Capitacao, Visita


class ApartamentoForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = Apartamento
        fields = '__all__'


class CasaForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = Casa
        fields = '__all__'


class TerrenoLoteForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = TerrenoLote
        fields = '__all__'


class EmpreendimentoForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = Empreendimento
        fields = '__all__'


class PropriedadeRuralForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = PropriedadeRural
        fields = '__all__'


class SalaComercialForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = SalaComercial
        fields = '__all__'


class EstabelecimentoComercialForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = EstabelecimentoComercial
        fields = '__all__'


class PessoaFisicaForm(forms.ModelForm):
    # required_css_class = 'table'
    # error_css_class = 'error'
    class Meta:
        model = Fisica
        fields = '__all__'
        error_messages = {
            'email': {
                'invalid': ("Email inválido. Exemplo: exemplo@email.com"),
            },
        }


class PessoaJuridicaForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = Juridica
        fields = '__all__'
        help_texts = {
            'nome': ('Nome do responsável'),
            'telefone_celular': ('Telefone celular do responsável. (DDD)99-99999999'),
        }
        error_messages = {
            'email': {
                'invalid': ("Email inválido"),
                'empty': ("Esse campo é obrigatório"),
            },
        }
        

class AtendimentoForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = Atendimento
        fields = '__all__'

class CapitacaoForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = Capitacao
        fields = '__all__'

class VisitaForm(forms.ModelForm):
    # required_css_class = 'table'
    class Meta:
        model = Visita
        exclude = ['atendimento']
        # fields = '__all__'
        help_texts = {
            'data': ('dd/mm/aaaa'),
        }
        error_messages = {
            'observacoes': {
                'max_length': ("Por favor, digite 500 caracteres no máximo."),
            },
        }

