from django.test import SimpleTestCase
from catalogos.forms import Peticiones

class testFormulario(SimpleTestCase):

    def test_Peticiones_valid_data(self):
        form = Peticiones(data={
            'usuario': 'Duoc',
            'email': 'duoc.uc@gmail.com',
            'nomAnime': 'naruto'
        })

        self.assertTrue(form.is_valid())


    def test_Peticiones_no_data(self):
        form = Peticiones(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)