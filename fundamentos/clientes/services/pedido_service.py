from ..models import Pedido

def cadastrar_pedido(pedido):
    Pedido.objects.create(cliente=pedido.cliente, data_pedido=pedido.data_pedido, valor=pedido.valor,status=pedido.status, observacoes=pedido.observacoes)

def listar_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos

def listar_pedido_id(id):
    pedido = Pedido.objects.get(id=id)
    return pedido

def editar_pedido(pedido_antigo, pedido_novo):
    pedido_antigo.cliente = pedido_novo.cliente
    pedido_antigo.observacoes = pedido_novo.observacoes
    pedido_antigo.data_pedido = pedido_novo.data_pedido
    pedido_antigo.valor = pedido_novo.valor
    pedido_antigo.status = pedido_novo.status
    pedido_antigo.save(force_update=True)