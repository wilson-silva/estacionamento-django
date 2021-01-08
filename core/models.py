from math import ceil

from django.db import models


# Create your mo
# dels here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_clientes', blank=True, null=True)

    def __str__(self):
        return f' {self.nome} - {str(self.id)}'

    class Meta:
        verbose_name_plural = 'Clientes'


class Veiculo(models.Model):
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=4, blank=True, null=True)
    cor = models.CharField(max_length=20, blank=True, null=True)
    placa = models.CharField(max_length=10)
    Id_cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_veiculos', blank=True, null=True)

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name_plural = 'Veiculos'


class Parametro(models.Model):
    descricao = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao + '(' + str(self.valor) + ')'

    class Meta:
        verbose_name_plural = 'Parametros'


class Movimento(models.Model):
    data_entrada = models.DateTimeField(auto_now_add=None)
    data_saida = models.DateTimeField(auto_now_add=None, blank=True, null=True)
    id_veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
    valor_hora = models.ForeignKey('Parametro', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.id}- {self.data_entrada} - {self.id_veiculo.placa}'

    class Meta:
        verbose_name_plural = 'Movimentos'

    # regra de negócio para calculat total baseado no checkout
    def calcula_total(self):
        if self.data_saida:
            horas = ceil((self.data_saida - self.data_entrada).total_seconds() / 3600)
            self.total = horas * self.valor_hora.valor
            return self.total
        return 0.0


class Mensalista(models.Model):
    observacao = models.TextField(blank=True, null=True)
    mensalidade = models.ForeignKey('Parametro', on_delete=models.CASCADE)
    id_veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_veiculo.placa} {self.id_veiculo.modelo} {self.mensalidade.valor}'

    class Meta:
        verbose_name_plural = 'Mensalistas'
