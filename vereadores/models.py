from django.db import models

from deputados.models import Deputado

class Vereador(models.Model):
    nomevereador = models.CharField(max_length=250)
    deputado = models.ForeignKey(Deputado, on_delete=models.PROTECT, related_name='vereadores',null=True, blank=True, default='1')
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=50)
    cpf_cnpj = models.CharField(null=True, blank=True, max_length=14)
    cep = models.CharField(null=True, blank=True, max_length=8)
    rua = models.CharField(null=True, blank=True, max_length=250)
    numero = models.CharField(null=True, blank=True, max_length=4)
    complemento = models.CharField(null=True, blank=True, max_length=50)
    bairro = models.CharField(null=True, blank=True, max_length=250)
    cidade = models.CharField(null=True, blank=True, max_length=250)
    uf = models.CharField(null=True, blank=True, max_length=2, default='RJ')
    whatsapp = models.CharField(null=True, blank=True, max_length=15)
    observacao = models.CharField(null=True, blank=True, max_length=250)
    ativo = models.BooleanField(null=True, blank=True,max_length=1, default=True)
    partido = models.CharField(max_length=100)
    nomeurna = models.CharField(max_length=250)
    numcandidatura = models.CharField(max_length=8)
    numurna = models.CharField(max_length=8)
    emailcaduf = models.EmailField(null=True, blank=True, max_length=50)
    emailinfodep = models.EmailField(null=True, blank=True, max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nomevereador
