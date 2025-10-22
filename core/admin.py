"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'passage_id')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Usuario)
admin.site.register(models.Bebida)
admin.site.register(models.Carrinho)
admin.site.register(models.CarrinhoItem)
admin.site.register(models.Combo)
admin.site.register(models.Endereco)
admin.site.register(models.ItemPedido)
# admin.site.register(models.Pedido)
@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'total', 'status', 'pagamento_status', 'criado_em')
    list_filter = ('status', 'pagamento_status', 'criado_em')
    search_fields = ('usuario__email', 'usuario__username', 'items')
    readonly_fields = ('criado_em', 'atualizado_em')
admin.site.register(models.Pizza)
admin.site.register(models.Produto) 
admin.site.register(models.Reserva)
admin.site.register(models.Feedback)
admin.site.site_header = 'Administração do Sistema'