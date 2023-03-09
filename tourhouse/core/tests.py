from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User

from core.models import Funcionario, Sede, Departamento


class TestBase(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('greg', 'greg@gmail.com', '123')
        self.client.login(username='greg', password='123')
        self.data = {'username': 'greg', 'first_name': 'Greg', 'last_name': 'hono'}

    def authentication(self):
        print(f'Iniciando de {self} testes...')
        self.client = APIClient()
        self.client.force_authenticate(
            user=User.objects.get(email="greg@gmail.com")
        )    

class TestDepartamento(TestBase):
    def setUp(self):
        super().setUp()
        self.url_base = '/api/departamento/'
        
    def test_insert_departamento(self):
        self.authentication()
        departamento_fake = self.fake_departamento()
        response = self.client.post(self.url_base, data=departamento_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 3)
    
    def test_update_departamento(self):
        self.authentication()
        departamento_fake = self.fake_departamento()
        response = self.client.post(self.url_base, data=departamento_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 3)
        departamento_fake['centro_custo'] = 2
        departamento_fake['codigo_integracao'] = 2
        response = self.client.put(self.url_base+'1/', data=departamento_fake)
        self.assertEqual(response.json()['codigo_integracao'], 2)
        self.assertEqual(response.json()['centro_custo'], 2)

    def test_delete_departamento(self):
        self.authentication()
        departamento_fake = self.fake_departamento()
        response = self.client.post(self.url_base, data=departamento_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 3)
        response = self.client.delete(self.url_base+'1/')
        self.assertEqual(response.status_code, 204)
                            
    @staticmethod
    def fake_departamento():
        return    {
            "id": 2,
            "centro_custo": 1,
            "codigo_integracao": 3
            }                   
   
        
class TestFuncionario(TestBase):
    def setUp(self):
        super().setUp()
        self.url_base = '/api/funcionario/'
        
    def test_insert_funcionario(self):
        self.authentication()
        departamento_fake = TestDepartamento.fake_departamento()
        response = self.client.post('/api/departamento/', data=departamento_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 3)
        funcionario_fake = self.fake_funcionar()
        response = self.client.post(self.url_base, data=funcionario_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 10)

    def test_insert_funcionario_without_departamento(self):
        self.authentication()
        funcionario_fake = self.fake_funcionar()
        response = self.client.post(self.url_base, data=funcionario_fake)
        self.assertEqual(response.status_code, 400)
                    
    def test_update_funcionario(self):
        self.authentication()
        departamento_fake = TestDepartamento.fake_departamento()
        response = self.client.post('/api/departamento/', data=departamento_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 3)
        funcionario_fake = self.fake_funcionar()
        response = self.client.post(self.url_base, data=funcionario_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 10)
        funcionario_fake['nome_completo'] = 'Gregorio Honorato'
        funcionario_fake['telefone'] = '123'
        response = self.client.put(self.url_base+'1/', data=funcionario_fake)
        self.assertEqual(response.json()['nome_completo'], 'Gregorio Honorato')
        self.assertEqual(response.json()['telefone'], '123')        

    def test_delete_funcionario(self):
        self.authentication()
        departamento_fake = TestDepartamento.fake_departamento()
        response = self.client.post('/api/departamento/', data=departamento_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 3)
        funcionario_fake = self.fake_funcionar()
        response = self.client.post(self.url_base, data=funcionario_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 10)
        response = self.client.delete(self.url_base+'1/')
        self.assertEqual(response.status_code, 204)        
                                    
    @staticmethod
    def fake_funcionar():
        return {
            "data_ingresso": "2023-03-09",
            "nome_completo": "manoel henrique",
            "email": "123@gmail.com",
            "telefone": "19992509911",
            "data_nascimento": "1988-12-24",
            "cidade": "campinas",
            "departamento_sede": 1
        }

class Testsede(TestBase):
    def setUp(self):
        super().setUp()
        self.url_base = '/api/sede/'
        
    def test_insert_sede(self):
        self.authentication()
        sede_fake = self.fake_sede()
        response = self.client.post(self.url_base, data=sede_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 5)

    def test_update_sede(self):
        self.authentication()
        sede_fake = self.fake_sede()
        response = self.client.post(self.url_base, data=sede_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 5)
        sede_fake['cnpj'] = '123456789'
        sede_fake['pais'] = 'ocaida'
        response = self.client.put(self.url_base+'1/', data=sede_fake)
        self.assertEqual(response.json()['cnpj'], '123456789')
        self.assertEqual(response.json()['pais'], 'ocaida')        

    def test_delete_sede(self):
        self.authentication()
        sede_fake = self.fake_sede()
        response = self.client.post(self.url_base, data=sede_fake)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), 5)
        response = self.client.delete(self.url_base+'1/')
        self.assertEqual(response.status_code, 204)        
                                    
    @staticmethod
    def fake_sede():
        return {
        "cnpj": "1231231231231",
        "logradouro": "rua 123",
        "cidade": "Campinas",
        "pais": "brazil"
        }        