from ..forms.pedido_forms import *
from django.shortcuts import redirect, render
from ..entidades import pedido
from ..services import pedido_service

def inserir_pedido(request):
    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        if form_pedido.is_valid():
            cliente = form_pedido.cleaned_data['cliente']
            observacoes = form_pedido.cleaned_data['observacoes']
            data_pedido = form_pedido.cleaned_data['data_pedido']
            valor = form_pedido.cleaned_data['valor']
            status = form_pedido.cleaned_data['status']
            produtos = form_pedido.cleaned_data['produtos']

            pedido_novo = pedido.Pedido(cliente=cliente, observacoes=observacoes, 
            data_pedido=data_pedido, valor=valor, status=status, produtos=produtos)
            pedido_service.cadastrar_pedido(pedido_novo)
            return redirect('listar_pedidos')
    else:
        form_pedido = PedidoForm()
    return render(request, 'pedidos/form_pedido.html', {'form_pedido': form_pedido})

def listar_pedidos(request):
    pedidos = pedido_service.listar_pedidos()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

def listar_pedido_id(request, id):
    pedido = pedido_service.listar_pedido_id(id)
    return render(request, 'pedidos/lista_pedido.html', {'pedido': pedido})

def editar_pedido(request, id):
    pedido_antigo = pedido_service.listar_pedido_id(id)
    form_pedido = PedidoForm(request.POST or None, instance=pedido_antigo)

    if form_pedido.is_valid():
        cliente = form_pedido.cleaned_data['cliente']
        observacoes = form_pedido.cleaned_data['observacoes']
        data_pedido = form_pedido.cleaned_data['data_pedido']
        valor = form_pedido.cleaned_data['valor']
        status = form_pedido.cleaned_data['status']
        produtos = form_pedido.cleaned_data['produtos']

        pedido_novo = pedido.Pedido(cliente=cliente, observacoes=observacoes, 
        data_pedido=data_pedido, valor=valor, status=status, produtos=produtos)
        pedido_service.editar_pedido(pedido_antigo, pedido_novo)
        return redirect('listar_pedidos')

    return render(request, 'pedidos/form_pedido.html', {'form_pedido': form_pedido})