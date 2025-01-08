from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.cliente import Cliente
from extensions import db
from datetime import date


# Ajuste no caminho do template_folder
cliente_views_bp = Blueprint(
    'cliente_views',
    __name__,
    template_folder='../../templates/'  # Caminho relativo correto
)

@cliente_views_bp.route('/')
def listar_clientes():
    # Filtra apenas os clientes ativos
    clientes = Cliente.query.filter_by(ativo=True).all()
    return render_template('clientes/lista.html', clientes=clientes)

@cliente_views_bp.route('/<int:id_cliente>')
def detalhes_cliente(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)
    return render_template('clientes/detalhes.html', cliente=cliente)
@cliente_views_bp.route('/novo', methods=['GET', 'POST'])
def novo_cliente():
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form.get('nome')
        whatsapp = request.form.get('whatsapp')
        plano = request.form.get('plano')
        dia_vencimento = request.form.get('dia_vencimento')
        ultima_mensalidade = request.form.get('ultima_mensalidade')
        observacoes = request.form.get('observacoes')

        # Validação básica
        if not nome or not whatsapp:
            flash('Nome e WhatsApp são obrigatórios!', 'danger')
            return render_template('clientes/novo.html')

        # Cria um novo cliente
        novo_cliente = Cliente(
            nome=nome,
            whatsapp=whatsapp,
            plano=plano,
            dia_vencimento=dia_vencimento,
            ultima_mensalidade=ultima_mensalidade,
            observacoes=observacoes,
            data_cadastro=date.today(),  # Define a data de cadastro como hoje
        )

        # Salva no banco de dados
        db.session.add(novo_cliente)
        db.session.commit()

        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('cliente_views.listar_clientes'))

    # Exibe o formulário de cadastro
    return render_template('clientes/novo.html')
# Rota para editar um cliente
@cliente_views_bp.route('/<int:id_cliente>/editar', methods=['GET', 'POST'])
def editar_cliente(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)

    if request.method == 'POST':
        # Obtém os dados do formulário
        cliente.nome = request.form.get('nome')
        cliente.whatsapp = request.form.get('whatsapp')
        cliente.plano = request.form.get('plano')
        cliente.dia_vencimento = request.form.get('dia_vencimento')
        cliente.ultima_mensalidade = request.form.get('ultima_mensalidade')
        cliente.observacoes = request.form.get('observacoes')

        # Validação simples
        if not cliente.nome or not cliente.whatsapp:
            flash('Nome e WhatsApp são obrigatórios!', 'danger')
            return render_template('clientes/editar.html', cliente=cliente)

        # Salva as alterações no banco de dados
        db.session.commit()
        flash('Cliente atualizado com sucesso!', 'success')
        return redirect(url_for('cliente_views.listar_clientes'))

    # Exibe o formulário com os dados do cliente
    return render_template('clientes/editar.html', cliente=cliente)

@cliente_views_bp.route('/<int:id_cliente>/excluir', methods=['POST'])
def excluir_cliente(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)

    # Marca o cliente como inativo
    cliente.ativo = False
    db.session.commit()

    flash('Cliente marcado como inativo.', 'warning')
    return redirect(url_for('cliente_views.listar_clientes'))

@cliente_views_bp.route('/<int:id_cliente>/reativar', methods=['POST'])
def reativar_cliente(id_cliente):
    cliente = Cliente.query.get_or_404(id_cliente)

    # Marca o cliente como ativo
    cliente.ativo = True
    db.session.commit()

    flash('Cliente reativado com sucesso.', 'success')
    return redirect(url_for('cliente_views.listar_clientes_inativos'))

@cliente_views_bp.route('/inativos')
def listar_clientes_inativos():
    # Filtra apenas os clientes inativos
    clientes = Cliente.query.filter_by(ativo=False).all()
    return render_template('clientes/lista_inativos.html', clientes=clientes)

