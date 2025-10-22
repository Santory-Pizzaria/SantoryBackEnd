from rest_framework import serializers
from core.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Pedido
        fields = [
            'id', 'usuario', 'items', 'total',
            'cep', 'rua', 'bairro', 'cidade', 'uf',
            'status', 'pagamento_status', 'criado_em', 'atualizado_em',
            'tempo_entrega_min', 'tempo_entrega_max', 'observacoes'
        ]
        read_only_fields = ['id', 'usuario', 'criado_em', 'atualizado_em']

    def create(self, validated_data):
        request = self.context.get('request')
        user = None
        if request and hasattr(request, 'user') and request.user and request.user.is_authenticated:
            user = request.user
        elif 'usuario' in self.initial_data:
            # permitir passar user por id (opcional)
            user = self.initial_data.get('usuario')

        if not user:
            raise serializers.ValidationError('Usuário é obrigatório')

        # itens podem vir como lista; calcular total se não informado
        items = validated_data.get('items', [])
        total = validated_data.get('total')
        if total in (None, 0):
            # tenta calcular soma a partir dos itens (espera-se item.preco e quantidade)
            try:
                calc = 0
                for it in items:
                    preco = float(str(it.get('preco', 0)).replace('R$', '').replace(',','.'))
                    qtd = int(it.get('qtd', it.get('quantidade', 1)))
                    calc += preco * qtd
                total = round(calc, 2)
            except Exception:
                total = 0

        pedido = Pedido.objects.create(
            usuario=user if hasattr(user, 'pk') else None,
            items=items,
            total=total,
            cep=validated_data.get('cep'),
            rua=validated_data.get('rua'),
            bairro=validated_data.get('bairro'),
            cidade=validated_data.get('cidade'),
            uf=validated_data.get('uf'),
            status=validated_data.get('status', 'confirmado'),
            pagamento_status=validated_data.get('pagamento_status', 'pendente'),
            tempo_entrega_min=validated_data.get('tempo_entrega_min'),
            tempo_entrega_max=validated_data.get('tempo_entrega_max'),
            observacoes=validated_data.get('observacoes', ''),
        )
        return pedido