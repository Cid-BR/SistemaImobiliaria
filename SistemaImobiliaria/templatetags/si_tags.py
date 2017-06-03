import datetime
from django import template
from SistemaImobiliaria.Imobiliaria.models import Atendimento, Visita

register = template.Library()

@register.simple_tag
def current_time(format_string):
	return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def number_of_visits(id_atendimento):
	"""This function get the number of visits for one atendimento"""
	visitas = Visita.objects.filter(atendimento_id=id_atendimento)
	
	response = None
	if visitas.count() == 0:
		response = "Nenhuma visita agendada"
	elif visitas.count() == 1:
		response = "1 visita agendada"
	elif visitas.count() > 1:
		response = "{} visitas agendadas ".format(visitas.count())

	return response
	
	 

