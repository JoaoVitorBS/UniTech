from django.db import models


# ---------- Colaborador
class Colaborador(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=True)
    telefone = models.CharField(max_length=18, null=False, blank=True)
    cargo = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name = "Colaborador"
        permissions = (
            ("view_colaborador", "Can view colaborador"),
        )

    def __unicode__(self):
        s = u'%s' % self.nome
        return s

    def __str__(self):
        s = u'%s' % self.nome
        return s


# ---------- Categoria
class Categoria(models.Model):
    categoria_desc = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Categoria"
        permissions = (
            ("view_categoria", "Can view categoria"),
        )

    def __unicode__(self):
        s = u'%s' % self.categoria_desc
        return s

    def __str__(self):
        s = u'%s' % self.categoria_desc
        return s


# ---------- Marca
class Marca(models.Model):
    marca_desc = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Marca"
        permissions = (
            ("view_marca", "Can view marca"),
        )

    def __unicode__(self):
        s = u'%s' % self.marca_desc
        return s

    def __str__(self):
        s = u'%s' % self.marca_desc
        return s


# ---------- Serviço
class Servico(models.Model):
    servico_desc = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Serviço"
        permissions = (
            ("view_servico", "Can view servico"),
        )

    def __unicode__(self):
        s = u'%s' % self.servico_desc
        return s

    def __str__(self):
        s = u'%s' % self.servico_desc
        return s


# ---------- Unidade de Medida
class Unidade(models.Model):
    sigla_unidade = models.CharField(max_length=3)
    unidade_desc = models.CharField(max_length=16)

    class Meta:
        verbose_name = "Unidade"
        permissions = (
            ("view_unidade", "Can view unidade"),
        )

    def __unicode__(self):
        s = u'(%s) %s' % (self.sigla_unidade, self.unidade_desc)
        return s

    def __str__(self):
        s = u'(%s) %s' % (self.sigla_unidade, self.unidade_desc)
        return s


# ---------- Departamento
class Departamento(models.Model):
    departamento_desc = models.CharField(max_length=30, null=False, blank=True, unique=True)
    nome_responsavel = models.CharField(max_length=100, null=False, blank=True)
    telefone_responsavel = models.CharField(max_length=18, null=False, blank=True)
    email_responsavel = models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        verbose_name = "Departamento"
        permissions = (
            ("view_departamento", "Can view departamento"),
        )

    def __unicode__(self):
        s = u'%s' % self.departamento_desc
        return s

    def __str__(self):
        s = u'%s' % self.departamento_desc
        return s


# ---------- Peças
class Peça(models.Model):
    ESTADO_CHOICES = (
        ("NOVO", "NOVO"),
        ("USADO", "USADO"),
        ("DESCARTE", "DESCARTE")
    )
    codigo = models.CharField(max_length=15, unique=True, null=False, blank=False)
    peça_desc = models.CharField(max_length=255, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, null=False, blank=False, on_delete=models.PROTECT)
    unidade = models.ForeignKey(Unidade, null=False, blank=False, on_delete=models.PROTECT)
    quantidade = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=8, null=False, choices=ESTADO_CHOICES)
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Peça"
        permissions = (
            ("view_peça", "Can view peça"),
        )

    def __unicode__(self):
        s = u'(%s) %s' % (self.codigo, self.peça_desc)
        return s

    def __str__(self):
        s = u'(%s) %s' % (self.codigo, self.peça_desc)
        return s


# ---------- Dispositivo
class Dispositivo(models.Model):
    STATUS_CHOICES = (
        ("ATIVO", "ATIVO"),
        ("INATIVO", "INATIVO"),
        ("DESCARTE", "DESCARTE")
    )
    codigo = models.CharField(max_length=15, unique=True, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, null=False, blank=False, on_delete=models.PROTECT)
    unidade = models.ForeignKey(Unidade, null=False, blank=False, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=8, default='ATIVO', null=False, choices=STATUS_CHOICES)
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Dispositivo"
        permissions = (
            ("view_dispositivo", "Can view dispositivo"),
        )

    def __unicode__(self):
        s = u'(%s) %s - %s' % (self.codigo, self.descricao, self.departamento)
        return s

    def __str__(self):
        s = u'(%s) %s - %s' % (self.codigo, self.descricao, self.departamento)
        return s


# ---------- Tarefa
class Tarefa(models.Model):
    STATUS_CHOICES = (
        ("Pendente", "Pendente"),
        ("Na bancada", "Na bancada"),
        ("Finalizada", "Finalizada")
    )
    data_abertura = models.DateTimeField(auto_now_add=True)
    status_servico = models.CharField(max_length=50, null=False, blank=True, choices=STATUS_CHOICES)
    dispositivo = models.ForeignKey(Dispositivo, null=True, blank=True, on_delete=models.PROTECT)
    defeito = models.CharField(max_length=50, null=False, blank=True)
    servico = models.ForeignKey(Servico, null=True, blank=False, on_delete=models.PROTECT)
    colaborador = models.ForeignKey(Colaborador, null=True, blank=True, on_delete=models.PROTECT)
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Tarefa"
        permissions = (
            ("view_tarefa", "Can view tarefa"),
        )

    def __unicode__(self):
        s = u'(%s) %s' % (self.dispositivo, self.defeito, self.servico)
        return s

    def __str__(self):
        s = u'(%s) %s' % (self.dispositivo, self.defeito, self.servico)
        return s


# ---------- Troca de Peças
class TrocaPecas(models.Model):
    STATUS_CHOICES = (
        ("Pendente", "Pendente"),
        ("Na bancada", "Na bancada"),
        ("Finalizada", "Finalizada")
    )
    data_troca = models.DateTimeField(auto_now_add=True)
    status_servico = models.CharField(max_length=50, null=False, blank=True, choices=STATUS_CHOICES)
    dispositivo = models.ForeignKey(Dispositivo, null=True, blank=True, on_delete=models.PROTECT)
    peca = models.ForeignKey(Peça, null=True, blank=False, on_delete=models.PROTECT)
    motivo_troca = models.CharField(max_length=100, null=False, blank=True)
    colaborador = models.ForeignKey(Colaborador, null=True, blank=True, on_delete=models.PROTECT)
    inf_adicionais = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "TrocaPecas"
        permissions = (
            ("view_trocaPeca", "Can view trocaPeca"),
        )

    def __unicode__(self):
        s = u'(%s) %s' % (self.dispositivo, self.motivo_troca, self.peca)
        return s

    def __str__(self):
        s = u'(%s) %s' % (self.dispositivo, self.defeito, self.peca)
        return s


@property
def format_unidade(self):
    if self.unidade:
        return self.unidade.sigla_unidade
    else:
        return ''


def get_sigla_unidade(self):
    if self.unidade:
        return self.unidade.sigla_unidade
    else:
        return ''


@property
def format_dispositivo(self):
    if self.dispositivo:
        return self.codigo.descricao.departamento
    else:
        return ''


def get_dispositivo(self):
    if self.dispositivo:
        return self.codigo.descricao.departamento
    else:
        return ''


@property
def format_peça(self):
    if self.peça:
        return self.codigo.peça_desc
    else:
        return ''


def get_peça(self):
    if self.peça:
        return self.codigo.peça_desc
    else:
        return ''
