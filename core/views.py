from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic
from core.models import Cliente, Veiculo, Parametro, Mensalista, Movimento
from core.forms import FormCliente, FormVeiculo, FormMensalista, FormMovimento, FormParametro


# ******************VIEWS HOME**************************
def home(request):
    contexto = {'acao': 'ACGcar: Estacionamento'}
    return render(request, 'core/index.html', contexto)


# ******************VIEWS REGISTRAR**************************
class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


# ******************VIEWS CLIENTE**************************
@login_required
def cadastro_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro Cliente', 'titulo': 'Cadastrar'}
    if form.is_valid():
        form.save()
        messages.success(request, "Clente cadastrado com sucesso!")
        return redirect('url_listagem_clientes')
    else:
        return render(request, 'core/cadastro_cliente.html', contexto)


@login_required
def listagem_clientes(request):
    if request.POST:
        if request.POST['nome']:
            clientes = Cliente.objects.filter(nome=request.POST['nome'])
        else:
            clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.all()
    contexto = {'clientes': clientes, 'acao': 'Lista Cliente', 'titulo ': 'lista_cliente'}
    return render(request, 'core/listagem_clientes.html', contexto)


@login_required()
def atualiza_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualiza Cliente', 'titulo': 'Atualizar'}
    if form.is_valid():
        form.save()
        messages.success(request, "Clente atualizado com sucesso!")
        return redirect('url_listagem_clientes')
    else:
        return render(request, 'core/cadastro_cliente.html', contexto)


@login_required
def exclui_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    contexto = {'valor': obj.nome, 'acao': 'Exclui Cliente', 'titulo ': 'exclui_cliente'}
    if request.POST:
        obj.delete()
        return redirect('url_listagem_clientes')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


# ******************VIEWS VEICULO**************************
@login_required
def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro Véiculo', 'titulo': 'Cadastrar'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculos')
    else:
        return render(request, 'core/cadastro_veiculo.html', contexto)


@login_required
def listagem_veiculos(request):
    if request.POST:
        if request.POST['placa']:
            veiculos = Veiculo.objects.filter(placa=request.POST['placa'])
        else:
            veiculos = Veiculo.objects.all()
    else:
        veiculos = Veiculo.objects.all()
    contexto = {'veiculos': veiculos, 'acao': 'Lista Veiculos', 'titulo ': 'lista_veiculo'}
    return render(request, 'core/listagem_veiculos.html', contexto)


@login_required
def atualiza_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form, 'acao': 'Atualiza Veiculo', 'titulo': 'Atualizar'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculos')
    else:
        return render(request, 'core/cadastro_veiculo.html', contexto)


@login_required
def exclui_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    contexto = {'acao': obj.placa, 'redirect': 'url_listagem_parametros', 'acao': 'Lista Veiculo', 'titulo ': 'exclui_veiculo'}
    if request.POST:
        obj.delete()
        return redirect('url_listagem_veiculos')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


# ******************VIEWS PARAMETRO**************************
@login_required
def cadastro_parametro(request):
    form = FormParametro(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de Parametro', 'titulo': 'Cadastrar'}
    if form.is_valid():
        form.save()

        return redirect('url_listagem_parametros')
    else:
        return render(request, 'core/cadastro_parametro.html', contexto)


@login_required
def listagem_parametros(request):

    dados = Parametro.objects.all()
    contexto = {'parametros': dados, 'acao': 'Lista Parametros', 'titulo ': 'lista_parametro'}
    return render(request, 'core/listagem_parametros.html', contexto)


@login_required()
def atualiza_parametro(request, id):
    try:
        obj = Parametro.objects.get(id=id)
        form = FormParametro(request.POST or None, request.FILES or None, instance=obj)
        contexto = {'form': form, 'acao': 'Atualiza Parametro', 'titulo': 'Atualizar'}
        if form.is_valid():
            form.save()
            return redirect('url_listagem_parametros')
        else:
            return render(request, 'core/cadastro_parametro.html', contexto)
    except Exception as erro:
        contexto = {'erro':erro, 'acao': 'Mensagem do sistema'}
        return redirect(request, 'core/erro.html', contexto)


@login_required
def exclui_parametro(request, id):
    try:
        obj = Parametro.objects.get(id=id)
        contexto = {'acao': obj.descricao, 'redirect': 'url_listagem_parametros'}
        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_parametros')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_parametros')


# ******************VIEWS MENSALISTA**************************
@login_required
def cadastro_mensalista(request):
    form = FormMensalista(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de Mensalista', 'titulo': 'Cadastrar'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_mensalistas')
    else:
        return render(request, 'core/cadastro_mensalista.html', contexto)


@login_required
def listagem_mensalistas(request):
    dados = Mensalista.objects.all()
    contexto = {'mensalistas': dados, 'acao': 'Lista Mensalistas', 'titulo ': 'lista_mensalista'}
    return render(request, 'core/listagem_mensalistas.html', contexto)


@login_required()
def atualiza_mensalista(request, id):
    try:
        obj = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, request.FILES or None, instance=obj)
        contexto = {'form': form, 'acao': 'Atualiza Mensalista', 'titulo': 'Atualizar'}
        if form.is_valid():
            form.save()
            return redirect('url_listagem_mensalistas')
        else:
            return render(request, 'core/cadastro_mensalista.html', contexto)
    except Exception as erro:
        contexto = {'erro': erro, 'acao': 'Mensagem do sistema'}
        return redirect(request, 'core/erro.html', contexto)


@login_required
def exclui_mensalista(request, id):
    try:
        obj = Mensalista.objects.get(id=id)
        contexto = {'acao': obj.id_veiculo.placa, 'redirect': 'url_listagem_mensalistas'}
        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_mensalistas')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_mensalistas')


# ******************VIEWS MOVIMENTO**************************
@login_required
def cadastro_movimento(request):
    if request.user.is_staff:
        form = FormMovimento(request.POST or None)
        contexto = {'form': form, 'titulo': 'cad:Movimento', 'acao': 'Cadastro de Movimento'}
        if form.is_valid():
            form.save()
            return redirect('url_listagem_movimentos')
        return render(request, 'core/cadastro_movimento.html', contexto)
    else:
        contexto = {'erro': 'Você não tem permissão para executar'}
        return render(request, 'core/erro.html', contexto)


@login_required
def listagem_movimentos(request):

    dados = Movimento.objects.all()
    contexto = {'movimentos': dados, 'acao': 'Lista Movimentos', 'titulo ': 'lista_movimento'}
    return render(request, 'core/listagem_movimentos.html', contexto)


@login_required()
def atualiza_movimento(request, id):
    try:
        if request.user.is_staff:
            obj = Movimento.objects.get(id=id)
            form = FormMovimento(request.POST or None, instance=obj)
            contexto = {'form': form, 'acao': 'Atualiza Movimento', 'titulo': 'Atualizar'}
            if form.is_valid():
                if obj.calcula_total() >= 0.0:
                    form.save()
                    return redirect('url_listagem_movimentos')
                else:
                    contexto = {'erro': 'Operação não concluida! Horario de saída é menor que o da entrada'}
                    return render(request, 'core/erro.html', contexto)
            else:
                return render(request, 'core/cadastro_movimento.html', contexto)
        else:
            contexto = {'erro': 'Você não tem permissão para executar'}
            return render(request, 'core/erro.html', contexto)
    except Exception as erro:
        contexto = {'erro': erro, 'acao': 'Mensagem do sistema'}
        return redirect(request, 'core/erro.html', contexto)


@login_required()
def exclui_movimento(request, id):
    try:
        obj = Movimento.objects.get(id=id)
        contexto = {'acao': obj.id_veiculo.placa, 'redirect': 'url_listagem_movimentos'}
        if request.method == 'POST':
            obj.delete()
            return redirect('url_listagem_movimentos')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as erro:
        return redirect('url_listagem_movimentos')
