from app import create_app

# Cria a instância da aplicação
app = create_app()

if __name__ == '__main__':
    # Executa a aplicação
    app.run(debug=True)
