from django.shortcuts import render, get_object_or_404

from .models import Categoria, Artigo, Poema, Conto, Microconto, Video, Juri, Plast, Rasc, Quadrinho, Tira, Ilustracao, VideoME, VideoEK, DesenhoEK, EstoriaEK
from .forms import ContatoForm

def index(request):
    return render(request, 'advogado/index.html')

def advogado(request):
    return render(request, 'advogado/advogado.html')

def artigo(request):
    artigo_list = Artigo.objects.filter(categoria__categoria_nome='Jurídica')
    context = {'artigo_list': artigo_list}
    return render(request, 'advogado/artigo.html', context)

def detartigo(request, artigo_id):
    detartigo = get_object_or_404(Artigo, pk=artigo_id)
    return render(request, 'advogado/detArtigo.html', {'artigo': detartigo})

def direitocrianca(request):
    artigo_list = Artigo.objects.filter(categoria__categoria_nome='Criança')
    context = {'artigo_list': artigo_list}
    return render(request, 'advogado/direitoCrianca.html', context)

def detdireitocrianca(request, artigo_id):
    detdircrianca = get_object_or_404(Artigo, pk=artigo_id)
    return render(request, 'advogado/detDirCrianca.html', {'artigo': detdircrianca})

def poema(request):
    literatura_list = Poema.objects.all()
    context = {'poema_list': poema_list}
    return render(request, 'advogado/poema.html', context)

def detPoema(request, poema_id):
    detPoema = get_object_or_404(Poema, pk=poema_id)
    return render(request, 'advogado/detPoema.html', {'poema': detPoema})


def resultado(request, artigo_id):
    return render(request, 'advogado/resultado.html', artigo)

def categoria(request, categoria_id):
    return render(request, 'advogado/categoria.html', categoria)

def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato_item = form.save(commit=False)
            contato_item.save()
    else:
        form = ContatoForm()

    return render(request, 'advogado/contato.html', {'form': form})

def videos(request):
    full_list = Video.objects.all()
    context = {'full_list': full_list}
    return render(request, 'advogado/videos.html', context)

def videoview(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'advogado/videoView.html', {'video': video})

def video_me(request):
    full_list = VideoME.objects.all()
    context = {'full_list': full_list}
    return render(request, 'advogado/video_me.html', context)

def videoview_me(request, video_me_id):
    video_me = get_object_or_404(VideoME, pk=video_me_id)
    return render(request, 'advogado/videoView_me.html', {'video_me': video_me})

def video_ek(request):
    full_list = VideoEK.objects.all()
    context = {'full_list': full_list}
    return render(request, 'advogado/video_ek.html', context)

def videoview_ek(request, video_ek_id):
    video_me = get_object_or_404(VideoEK, pk=video_ek_id)
    return render(request, 'advogado/videoView_ek.html', {'video_me': video_ek})

def juri(request):
    juris_list = Juri.objects.all()
    context = {'juris_list': juris_list}
    return render(request, 'advogado/juris.html', context)

def detJuris(request, juris_id):
    juris = get_object_or_404(Juris, pk=juris_id)
    return render(request, 'advogado/detJuris.html', {'juris': juris})

def plast(request):
    plast_list = Plast.objects.all()
    context = {'plast_list': plast_list}
    return render(request, 'advogado/plast.html', context)

def detPlast(request, plast_id):
    plast = get_object_or_404(Plast, pk=plast_id)
    return render(request, 'advogado/detPlast.html', {'plast': plast})

def rasc(request):
    rasc_list = Rasc.objects.all()
    context = {'rasc_list': rasc_list}
    return render(request, 'advogado/rasc.html', context)

def detRasc(request, rasc_id):
    rasc = get_object_or_404(Rasc, pk=rasc_id)
    return render(request, 'advogado/detRasc.html', {'rasc': rasc})

def quadrinho(request):
    quadrinho_list = Quadrinho.objects.all()
    context = {'quadrinho_list': quadrinho_list}
    return render(request, 'advogado/quadrinho.html', context)

def detQuadrinho(request, quadrinho_id):
    quadrinho = get_object_or_404(Quadrinho, pk=quadrinho_id)
    return render(request, 'advogado/detQuadrinho.html', {'quadrinho': quadrinho})

def tira(request):
    tira_list = Tira.objects.all()
    context = {'tira_list': tira_list}
    return render(request, 'advogado/tira.html', context)

def deTira(request, tira_id):
    tira = get_object_or_404(Tira, pk=tira_id)
    return render(request, 'advogado/deTira.html', {'tira': tira})

def ilustracao(request):
    ilustracao_list = Ilustracao.objects.all()
    context = {'ilustracao_list': ilustracao_list}
    return render(request, 'advogado/ilustracao.html', context)

def detIlustracao(request, ilustracao_id):
    ilustracao = get_object_or_404(Ilustracao, pk=ilustracao_id)
    return render(request, 'advogado/detIlustracao.html', {'ilustracao': ilustracao})

def ilustracao(request):
    ilustracao_list = Ilustracao.objects.all()
    context = {'ilustracao_list': ilustracao_list}
    return render(request, 'advogado/ilustracao.html', context)

def detIlustracao(request, ilustracao_id):
    ilustracao = get_object_or_404(Ilustracao, pk=ilustracao_id)
    return render(request, 'advogado/detIlustracao.html', {'ilustracao': ilustracao})

def poema(request):
    poema_list = Poema.objects.all()
    context = {'poema_list': poema_list}
    return render(request, 'advogado/poema.html', context)

def detIPoema(request, poema_id):
    poema = get_object_or_404(Poema, pk=poema_id)
    return render(request, 'advogado/detPoema.html', {'poema': poema})

def conto(request):
    conto_list = Conto.objects.all()
    context = {'conto_list': conto_list}
    return render(request, 'advogado/conto.html', context)

def detconto(request, conto_id):
    conto = get_object_or_404(Conto, pk=conto_id)
    return render(request, 'advogado/detConto.html', {'conto': conto})

def microconto(request):
    microconto_list = Microconto.objects.all()
    context = {'microconto_list': microconto_list}
    return render(request, 'advogado/microconto.html', context)

def detmicroconto(request, microconto_id):
    microconto = get_object_or_404(Microconto, pk=microconto_id)
    return render(request, 'advogado/detMicroconto.html', {'microconto': microconto})

def desenho_ek(request):
    desenho_ek_list = DesenhoEK.objects.all()
    context = {'desenho_ek_list': desenho_ek_list}
    return render(request, 'advogado/desenho_ek.html', context)

def detDesenho_ek(request, desenho_ek_id):
    desenho_ek = get_object_or_404(DesenhoEK, pk=desenho_ek_id)
    return render(request, 'advogado/detDesenho_ek.html', {'desenho_ek': desenho_ek})

def estoria_ek(request):
    estoria_ek_list = EstoriaEK.objects.all()
    context = {'estoria_ek_list': estoria_ek_list}
    return render(request, 'advogado/estoria_ek.html', context)

def detestoria_ek(request, estoria_ek_id):
    conto = get_object_or_404(EstoriaEK, pk=estoria_ek_id)
    return render(request, 'advogado/detEstoria_ek.html', {'estoria_ek': estoria_ek})