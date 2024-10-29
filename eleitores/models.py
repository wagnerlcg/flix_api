from django.db import models

from vereadores.models import Vereador

class Eleitor(models.Model):
    nomeeleitor = models.CharField(max_length=250)
    vereador = models.ForeignKey(Vereador, on_delete=models.PROTECT, related_name='eleitores',null=True, blank=True, default='1')
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=50)
    cpf_cnpj = models.CharField(null=True, blank=True, max_length=14)
    phone_1 = models.CharField(null=True, blank=True, max_length=15)
    phone_2  = models.CharField(null=True, blank=True, max_length=15)
    cep = models.CharField(null=True, blank=True, max_length=8)
    rua = models.CharField(null=True, blank=True, max_length=250)
    numero = models.CharField(null=True, blank=True, max_length=4)
    complemento = models.CharField(null=True, blank=True, max_length=50)
    bairro = models.CharField(null=True, blank=True, max_length=250)
    cidade = models.CharField(null=True, blank=True, max_length=250)
    uf = models.CharField(null=True, blank=True, max_length=2, default='RJ')
    whatsapp = models.CharField(null=True, blank=True, max_length=15)
    genero  = models.CharField(null=True, blank=True, max_length=15)
    religiao  = models.CharField(null=True, blank=True, max_length=15)
    profissao  = models.CharField(null=True, blank=True, max_length=50)
    nascimento  = models.DateField(null=True, blank=True)
    observacao = models.CharField(null=True, blank=True, max_length=250)
    escolaridade = models.CharField(null=True, blank=True, max_length=250)
    ativo = models.BooleanField(null=True, blank=True,max_length=1, default=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nomeeleitor
