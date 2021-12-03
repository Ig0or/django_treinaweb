from ..models import Cliente


def listar_clientes():
    clientes = Cliente.objects.filter().all()
    return clientes


def listar_cliente_id(id):
    cliente = Cliente.objects.get(id=id)
    return cliente


def remover_cliente(cliente):
    cliente.delete()


def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, sobrenome=cliente.sobrenome, sexo=cliente.sexo, data_nascimento=cliente.data_nascimento, email=cliente.email, profissao=cliente.profissao,
    endereco=cliente.endereco)


def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.sobrenome = cliente_novo.sobrenome
    cliente.sexo = cliente_novo.sexo
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.email = cliente_novo.email
    cliente.profissao = cliente_novo.profissao
    cliente.endereco = cliente_novo.endereco
    cliente.save(force_update=True)
