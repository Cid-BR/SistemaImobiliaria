from django.test import TestCase

class NovoEmpreendimentoGet(TestCase):
	def setUp(self):
		self.resp = self.client.get('/imobiliaria/novo_empreendimento')

	def test_get(self):
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.resp, 'imobiliaria/novo_empreendimento.html')
