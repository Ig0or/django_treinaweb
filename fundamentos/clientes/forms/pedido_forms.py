from django import forms
from django import forms
from ..models import Cliente, Pedido

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    class Meta:
        model = Pedido
        fields = ['cliente', 'observacoes', 'data_pedido', 'valor', 'status']