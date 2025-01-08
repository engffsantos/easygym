// Exibir mensagem de confirmação antes de excluir
document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.btn-danger');

    deleteButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const confirmDelete = confirm('Tem certeza que deseja excluir este item?');
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });
});

// Exemplo de lógica para exibir notificações
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.textContent = message;

    document.body.prepend(notification);

    setTimeout(() => {
        notification.remove();
    }, 3000);
}
