import datetime

from django.db import models

from django.utils import timezone

class Categoria(models.Model):
    categoria_nome = models.CharField(max_length=80)
    categoria_desc = models.CharField(max_length=300)

    def __str__(self):
        return self.categoria_nome

class Artigo(models.Model):
    artigo_titulo = models.CharField(max_length=200)
    artigo_subtitulo = models.CharField(max_length=800, blank=True)
    artigo_texto = models.TextField()
    artigo_img = models.ImageField(upload_to='img_artigos', blank=True)
    pub_date = models.DateTimeField('date published')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    @property
    def artigo_img_url(self):
        if self.artigo_img and hasattr(self.artigo_img, 'url'):
            return self.artigo_img.url

    def __str__(self):
        return self.artigo_titulo

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=5)

class Contato(models.Model):
    nome                = models.CharField(max_length=200, default='')
    email                = models.CharField(max_length=80, default='')
    endereço          = models.CharField(max_length=800, default='', blank=True)
    cidade              = models.CharField(max_length=80, default='')
    estado              = models.CharField(max_length=80, default='')
    cep                   = models.CharField(max_length=10, default='')
    tel_residencial  = models.CharField(max_length=11, default='', blank=True)
    tel_comercial    = models.CharField(max_length=11, default='', blank=True)
    celular              = models.CharField(max_length=11, default='', blank=True)
    mensagem       = models.TextField(default='', blank=True)
    dt_hr_envio      = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.nome

class Poema(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=800, blank=True)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='img_literatura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Conto(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=800, blank=True)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='img_literatura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Microconto(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=180, blank=True)
    texto = models.CharField(max_length=560)
    imagem = models.ImageField(upload_to='img_literatura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Video(models.Model):
    titulo = models.CharField(max_length=80)
    icon_video = models.ImageField(upload_to='img_video')
    link = models.URLField()
    codigo = models.CharField(max_length=20, blank=True)
    desc_video = models.TextField()
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo
        return self.link
        return self.codigo

    @property
    def icon_video_url(self):
        if self.icon_video and hasattr(self.icon_video, 'url'):
            return self.icon_video.url

class Juri(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    img = models.ImageField(upload_to='img_artigos', blank=True)
    comentario = models.TextField()
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url


class Plast(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    imagem = models.ImageField(upload_to='img_pintura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Rasc(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    imagem = models.ImageField(upload_to='img_pintura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Quadrinho(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    imagem = models.ImageField(upload_to='img_pintura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Tira(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    imagem = models.ImageField(upload_to='img_pintura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class Ilustracao(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    imagem = models.ImageField(upload_to='img_pintura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class VideoME(models.Model):
    titulo = models.CharField(max_length=80)
    icon_video = models.ImageField(upload_to='img_video')
    link = models.URLField()
    codigo = models.CharField(max_length=20, blank=True)
    desc_video = models.TextField()
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo
        return self.link
        return self.codigo

    @property
    def icon_video_url(self):
        if self.icon_video and hasattr(self.icon_video, 'url'):
            return self.icon_video.url

class VideoEK(models.Model):
    titulo = models.CharField(max_length=80)
    icon_video = models.ImageField(upload_to='img_video')
    link = models.URLField()
    codigo = models.CharField(max_length=20, blank=True)
    desc_video = models.TextField()
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo
        return self.link
        return self.codigo

    @property
    def icon_video_url(self):
        if self.icon_video and hasattr(self.icon_video, 'url'):
            return self.icon_video.url

class DesenhoEK(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    imagem = models.ImageField(upload_to='img_pintura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url

class EstoriaEK(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=256)
    imagem = models.ImageField(upload_to='img_pintura', blank=True)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.titulo

    @property
    def imagem_url(self):
        if self.imagem and hasattr(self.imagem, 'url'):
            return self.imagem.url