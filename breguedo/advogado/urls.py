from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('advogado/', views.advogado, name='advogado'),
    path('artigo/', views.artigo, name='artigo'),
    path('artigo/<int:artigo_id>/', views.detartigo, name='artigo_detalhe'),
    path('direitocrianca/', views.direitocrianca, name='direitocrianca'),
    path('direitocrianca/<int:artigo_id>/', views.detdireitocrianca, name='direitocrianca_detalhe'),
    path('contato/', views.contato, name='contato'),
    path('videos/', views.videos, name='videos'),
    path('videos/<int:video_id>/', views.videoview, name='videoview'),
    path('juris/', views.juri, name='jurisprudencia'),
    path('juris/<int:juris_id>/', views.detJuris, name='juris_detalhe'),
    path('plast/', views.plast, name='artes_plasticas'),
    path('plast/<int:plast_id>/', views.detPlast, name='plast_detalhe'),
    path('rasc/', views.rasc, name='rascunho'),
    path('rasc/<int:rasc_id>/', views.detRasc, name='rasc_detalhe'),
    path('quadrinhos/', views.quadrinho, name='quadrinho'),
    path('quadrinhos/<int:quadrinho_id>/', views.detQuadrinho, name='quadrinhoDetalhe'),
    path('tiras/', views.tira, name='tira'),
    path('tiras/<int:tira_id>/', views.deTira, name='tiraDetalhe'),
    path('ilustracao/', views.ilustracao, name='ilustracao'),
    path('ilustracao/<int:ilustracao_id>/', views.detIlustracao, name='ilustracaoDetalhe'),
    path('poema/', views.poema, name='poema'),
    path('poema/<int:poema_id>/', views.detPoema, name='poemaDetalhe'),
    path('conto/', views.conto, name='conto'),
    path('conto/<int:conto_id>/', views.detconto, name='contoDetalhe'),
    path('microconto/', views.microconto, name='microconto'),
    path('microconto/<int:microconto_id>/', views.detmicroconto, name='videoDetalhe'),
    path('video_me/', views.video_me, name='video_me'),
    path('video_me/<int:video_me_id>/', views.videoview_me, name='videoview_meDetalhe'),
    path('video_ek/', views.video_ek, name='video_ek'),
    path('video_ek/<int:video_ek_id>/', views.videoview_ek, name='videoview_ekDetalhe'),
    path('desenho_ek/', views.desenho_ek, name='desenho_ek'),
    path('desenho_ek/<int:desenho_ek_id>/', views.detDesenho_ek, name='desenho_ekDetalhe'),
    path('estoria_ek/', views.estoria_ek, name='estoria_ek'),
    path('sucesso/', views.successView, name='sucesso'),
    path('estoria_ek/<int:estoria_ek_id>/', views.detestoria_ek, name='estoria_ekDetalhe'),
]