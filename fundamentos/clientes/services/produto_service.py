from ..models import Produto

def inserir_produto(produto):
    Produto.objects.create(nome=produto.nome, descricao=produto.descricao, valor=produto.valor)

def listar_produtos():
    return Produto.objects.all()

def listar_produto_id(id):
    return Produto.objects.get(id=id)