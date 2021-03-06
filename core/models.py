from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

class PontoTuristico(models.Model):
	nome = models.CharField(max_length=150)
	descricao = models.TextField()
	aprovado = models.BooleanField(default=False)
	atracoes = models.ManyToManyField(Atracao)
	comentario = models.ManyToManyField(Comentario,null=True, blank=True)
	avaliacoe = models.ManyToManyField(Avaliacao,null=True, blank=True)
	endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE,null=True, blank=True)
	foto = models.ImageField(upload_to='PontoTuristico',null=True, blank=True)

	def __str__(self):
		return self.nome
