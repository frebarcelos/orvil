from django.test import TestCase, Client
from django.urls import reverse
import datetime

from .forms import CadastroForms, NotaForm,LoginForms,ResenhaForms
from .models import Livro, Resenha, Avaliacao, User

class FormsTestCase(TestCase):
    def test_login_forms(self):
        form = LoginForms()
        
        self.assertTrue(form.fields['nome_login'].required)
        self.assertEqual(form.fields['nome_login'].max_length, 100)
        self.assertTrue(form.fields['senha'].required)
        self.assertEqual(form.fields['senha'].max_length, 70)
        
    def test_cadastro_forms(self):
        form = CadastroForms()
        
        self.assertTrue(form.fields['nome_cadastro'].required)
        self.assertEqual(form.fields['nome_cadastro'].max_length, 100)
        self.assertTrue(form.fields['email'].required)
        self.assertEqual(form.fields['email'].max_length, 100)
        self.assertTrue(form.fields['senha_1'].required)
        self.assertEqual(form.fields['senha_1'].max_length, 70)
    
    def test_nota_forms(self):
        form = NotaForm()
        
        self.assertTrue(form.fields['nota'].required)
        
        
    def test_resenha_forms(self):
        form = ResenhaForms()
        
        self.assertEqual(form.fields['titulo_resenha'].max_length, 100)
        self.assertTrue(form.fields['titulo_resenha'].required)
        self.assertEqual(form.fields['titulo_resenha'].label, 'Titulo')
        
        self.assertEqual(form.fields['texto_resenha'].max_length, 3000)
        self.assertTrue(form.fields['texto_resenha'].required)
        self.assertEqual(form.fields['texto_resenha'].label, 'Resenha')

class ModelsTestCase(TestCase):
    def test_livro(self):
        livro = Livro(
            Title="Teste",
            description="Descricao teste",
            authors="Autor teste",
            image="imagem teste",
            previewLink="link teste",
            publisher="Editora teste",
            publishedDate=datetime.datetime.now(),
            infoLink="link teste",
            categories="categoria teste",
            ratingsCount="1"
        )
        self.assertTrue(livro.Title == "Teste")
        self.assertTrue(livro.description == "Descricao teste")
        self.assertTrue(livro.authors == "Autor teste")
        self.assertTrue(livro.image == "imagem teste")
        self.assertTrue(livro.previewLink == "link teste")
        self.assertTrue(livro.publisher == "Editora teste")
        self.assertTrue(livro.infoLink == "link teste")
        self.assertTrue(livro.categories == "categoria teste")
        self.assertTrue(livro.ratingsCount == "1")
        
    def test_resenha(self):
        livro = Livro(
            Title="Livro teste",
            description="Descricao teste",
            authors="Autor teste",
            image="imagem teste",
            previewLink="link teste",
            publisher="Editora teste",
            publishedDate="2021-09-01T00:00:00Z",
            infoLink="link teste",
            categories="categoria teste",
            ratingsCount="1"
        )
        
        user = User(
            username="Usuario teste",
            email="teste@teste.com",
            password="123456",
            first_name="Teste",
            last_name="Teste"
        )
        
        resenha = Resenha(
            livro=livro,
            usuario=user,
            titulo="Titulo teste",
            texto="Texto teste",
            data_publicacao=datetime.datetime.now(),
            media_avaliacoes=0,
            num_avaliacoes_resenhas=0
        )
        
        self.assertEqual(resenha.livro.Title, "Livro teste")
        self.assertEqual(resenha.usuario.username, "Usuario teste")
        self.assertEqual(resenha.titulo, "Titulo teste")
        self.assertEqual(resenha.texto, "Texto teste")
        self.assertEqual(resenha.media_avaliacoes, 0)
        self.assertEqual(resenha.num_avaliacoes_resenhas, 0)
        
    def test_avaliacao(self):
        livro = Livro(
            Title="Livro teste",
            description="Descricao teste",
            authors="Autor teste",
            image="imagem teste",
            previewLink="link teste",
            publisher="Editora teste",
            publishedDate="2021-09-01T00:00:00Z",
            infoLink="link teste",
            categories="categoria teste",
            ratingsCount="1"
        )
        
        user = User(
            username="Usuario teste",
            email="teste@teste.com",
            password="123456",
            first_name="Teste",
            last_name="Teste"
        )
        
        resenha = Resenha(
            livro=livro,
            usuario=user,
            titulo="Titulo teste",
            texto="Texto teste",
            data_publicacao=datetime.datetime.now(),
            media_avaliacoes=0,
            num_avaliacoes_resenhas=0
        )
        
        avaliacao = Avaliacao(
            resenha=resenha,
            usuario=user,
            nota="5"
        )
        
        self.assertEqual(avaliacao.resenha.livro.Title, "Livro teste")
        self.assertEqual(avaliacao.usuario.username, "Usuario teste")
        self.assertEqual(avaliacao.nota, "5")
        
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='teste', password='teste123')
        self.client.login(username='teste', password='teste123')
        
        #urls
        self.index_url = reverse('index')
        self.livro_url = reverse('livro', args=[1])
        self.cadastro_url = reverse('cadastro')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')    
            
    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livros/index.html')
        
    def test_index_user_not_logged(self):
        self.client.logout()
        
        response = self.client.get(self.index_url)
        
        self.assertEqual(response.status_code, 302)
        
    def test_livro_not_found(self):
        response = self.client.get(self.livro_url)
        
        self.assertEqual(response.status_code, 404)
        
    def test_livro(self):
        livro = Livro.objects.create(
            Title="Teste",
            description="Descricao teste",
            authors="Autor teste",
            image="imagem teste",
            previewLink="link teste",
            publisher="Editora teste",
            publishedDate=datetime.datetime.now(),
            infoLink="link teste",
            categories="categoria teste",
            ratingsCount="1"
        )
        
        response = self.client.get(self.livro_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['livro'], livro)
        self.assertTemplateUsed(response, 'livros/livro.html')
        
    def test_cadastro(self):
        response = self.client.get(self.cadastro_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livros/cadastro.html')

        
    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livros/login.html')
    
    def test_logout(self):
        response = self.client.get(self.logout_url)
        
        self.assertEqual(response.status_code, 302)
                
   