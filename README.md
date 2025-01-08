# EasyGym - Sistema de Gestão para Academia

O **EasyGym** é um sistema de gestão completo para academias de pequeno e médio porte, desenvolvido em **Flask**. O foco do projeto é oferecer um gerenciamento eficiente de clientes, treinos, pagamentos, medições corporais e envio de mensagens de forma integrada, com uma estrutura organizada que facilite manutenções e novas funcionalidades.

---

## Sumário
1. [Principais Funcionalidades](#principais-funcionalidades)  
2. [Requisitos](#requisitos)  
3. [Instalação](#instalação)  
4. [Execução](#execução)  
5. [Estrutura de Diretórios](#estrutura-de-diretórios)  
6. [Testes](#testes)  
7. [Contribuições](#contribuições)  
8. [Licença](#licença)  
9. [Considerações Finais](#considerações-finais)  

---

## Principais Funcionalidades

- **Gestão de Clientes**  
  - Cadastro completo de dados (nome, contato, status de pagamento)  
  - Histórico de medições corporais, comentários e evolução  
  - Observações personalizadas  

- **Treinos Personalizados**  
  - Criação de treinos com associação de exercícios por cliente  
  - Registro de séries, repetições, e cargas para cada exercício  
  - Organização por grupo muscular e nível de dificuldade  

- **Exercícios**  
  - Cadastro e gerenciamento de exercícios, incluindo descrição detalhada  
  - Agrupamento por grupos musculares e objetivos  

- **Pagamentos**  
  - Registro de pagamentos com datas, valores e formas de pagamento  
  - Histórico de pagamentos, status (Pago, Atrasado, Em Aberto)  
  - Possibilidade de integração com gateways e envio de comprovantes  

- **Integração com WhatsApp**  
  - Envio de notificações automáticas: lembretes de pagamento, motivação e avisos gerais  
  - Serviço para envio massivo de mensagens, caso necessário  

- **Scheduler (APScheduler)**  
  - Agendamento de tarefas para cobranças ou avisos periódicos  
  - Gatilhos configuráveis (pagamento atrasado, renovação de planos, etc.)  

- **Autenticação e Segurança**  
  - Gerenciamento de usuários via **Flask-Login**  
  - Proteção de rotas sensíveis e acesso restrito ao painel administrativo  

---

## Requisitos

- **Python 3.8+**  
- **Flask**  
- **SQLAlchemy**  
- **Flask-SQLAlchemy**  
- **Flask-Migrate**  
- **Flask-Login**  
- **APScheduler**  
- **python-dotenv**  

Caso deseje executar testes unitários e de integração:
- **pytest**  

---

## Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/usuario/easygym.git
cd easygym
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/MacOS:
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Crie o arquivo `.env` na raiz do projeto** (exemplo de conteúdo):

```env
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=sqlite:///academia.db
SECRET_KEY=sua_chave_secreta
WHATSAPP_API_KEY=sua_chave_api_whatsapp
```

5. **Configure o banco de dados (se aplicável):**

```bash
flask db init
flask db migrate
flask db upgrade
```

Esses comandos criarão as tabelas no banco de dados informado na variável `DATABASE_URL`.

---

## Execução

Para rodar a aplicação em modo de desenvolvimento:

```bash
flask run
```

A aplicação estará acessível em [http://localhost:5000](http://localhost:5000).

---

## Estrutura de Diretórios

Abaixo está a estrutura completa de pastas e arquivos do **EasyGym**, incluindo arquivos de configuração da IDE e do ambiente virtual:

```plaintext
EasyGym/
├── .env                  # Variáveis de ambiente (chaves, configs)
├── .gitignore            # Ignora arquivos/pastas desnecessários no Git
├── EasyGym.iml           # Arquivo de configuração do projeto (IDE)
├── profiles_settings.xml # Configurações de perfil de IDE
├── misc.xml              # Metadados de configuração (IDE)
├── modules.xml           # Configurações de módulos (IDE)
├── sqldialects.xml       # Configurações de dialetos SQL (IDE)
├── workspace.xml         # Configurações gerais do workspace (IDE)
│
├── .venv/
│   └── .gitignore        # Arquivo de exclusão específico do ambiente virtual
│
├── app/
│   ├── controllers/
│   │   ├── cliente_controller.py     # Lógica de clientes
│   │   ├── exercicio_controller.py   # Lógica de exercícios
│   │   ├── medida_controller.py      # Lógica de medidas corporais
│   │   ├── pagamento_controller.py   # Lógica de pagamentos
│   │   ├── treino_controller.py      # Lógica de treinos
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── base.py       # Classe base para modelos (SQLAlchemy)
│   │   ├── cliente.py    # Modelo de Cliente
│   │   ├── exercicio.py  # Modelo de Exercício
│   │   ├── medida.py     # Modelo de Medida (histórico de medidas)
│   │   ├── mensagem.py   # Modelo de Mensagem (enviadas/registradas)
│   │   ├── pagamento.py  # Modelo de Pagamento
│   │   ├── treino.py     # Modelo de Treino
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── email_service.py     # Serviço para envio de e-mails
│   │   ├── whatsapp_service.py  # Serviço de integração com WhatsApp
│   │   └── __init__.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── bootstrap.min.css
│   │   │   └── style.css
│   │   ├── img/
│   │   │   └── logo.png
│   │   └── js/
│   │       ├── bootstrap.min.js
│   │       └── main.js
│   │
│   ├── templates/
│   │   ├── base.html         # Template base (layout)
│   │   ├── dashboard.html    # Painel principal
│   │   ├── login.html        # Tela de login
│   │   ├── clientes/
│   │   │   ├── detalhes.html
│   │   │   ├── editar.html
│   │   │   ├── lista.html
│   │   │   └── novo.html
│   │   ├── exercicios/
│   │   │   ├── editar.html
│   │   │   ├── lista.html
│   │   │   └── novo.html
│   │   ├── pagamentos/
│   │   │   ├── lista.html
│   │   │   └── novo.html
│   │   ├── treinos/
│   │   │   ├── editar.html
│   │   │   ├── lista.html
│   │   │   └── novo.html
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── database.py   # Configurações de conexão e inicialização do DB
│   │   ├── helpers.py    # Funções auxiliares gerais
│   │   ├── validators.py # Validações para formulários e dados
│   │   └── __init__.py
│   │
│   ├── views/
│   │   ├── clientes/
│   │   │   └── cliente_views.py    # Rotas/Views de clientes
│   │   ├── exercicios/
│   │   │   └── exercicio_views.py  # Rotas/Views de exercícios
│   │   ├── pagamentos/
│   │   │   └── pagamento_views.py  # Rotas/Views de pagamentos
│   │   ├── treinos/
│   │   │   └── treino_views.py     # Rotas/Views de treinos
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── config.py               # Configurações gerais (Flask, etc.)
├── database/
│   └── criar_db.sql        # Script de criação inicial do banco (SQL)
├── docs/
│   ├── api.md              # Documentação da API
│   ├── manual.md           # Manual de utilização
│   └── setup.md            # Guia de setup do projeto
├── logs/
│   ├── access.log          # Log de acessos
│   └── error.log           # Log de erros
├── migrations/
│   └── versions/           # Scripts gerados de migração do DB
├── README.md               # Documentação principal (este arquivo)
├── requirements.txt        # Lista de dependências do projeto
├── run.py                  # Arquivo principal para executar a aplicação
├── tests/
│   ├── test_controllers.py # Testes de controladores
│   ├── test_models.py      # Testes de modelos
│   ├── test_services.py    # Testes de serviços
│   └── __init__.py
└── __init__.py (opcional)  # Caso seja necessário inicializar em nível raiz
```

### Descrição Resumida dos Diretórios Principais
- **app/**: contém toda a lógica da aplicação (controllers, models, services, views, static, templates).
- **config.py**: define configurações globais (ex.: Flask, banco de dados).
- **database/**: armazena scripts SQL.
- **docs/**: documentação extra (API, manuais, guias).
- **logs/**: arquivos de log para auditoria e troubleshooting.
- **migrations/**: scripts de migração de banco (Flask-Migrate).
- **tests/**: testes unitários e de integração.

---

## Testes

Se desejar executar testes (unitários e de integração), utilize o comando:

```bash
pytest
```

---

## Contribuições

Sinta-se à vontade para contribuir com o **EasyGym**:

1. Faça um **fork** do projeto.  
2. Crie uma **branch** para sua feature ou correção (`git checkout -b minha-feature`).  
3. Faça o **commit** das suas alterações (`git commit -am 'Minha nova feature'`).  
4. Faça o **push** para a branch (`git push origin minha-feature`).  
5. Crie um **pull request** para o repositório principal.

---

## Licença

O projeto **EasyGym** está licenciado sob a [MIT License](LICENSE). Consulte o arquivo `LICENSE` para mais detalhes.

---

## Considerações Finais

O **EasyGym** foi desenvolvido para simplificar e profissionalizar a gestão de academias, trazendo uma interface moderna e intuitiva, além de integrações úteis (e-mail, WhatsApp) para automatizar comunicações. Sua **arquitetura em Flask** e **estrutura de diretórios organizada** tornam o projeto escalável e de fácil manutenção.

Esperamos que o EasyGym contribua para otimizar processos na sua academia e ofereça uma ótima experiência de uso. Se tiver dúvidas ou sugestões, fique à vontade para abrir uma issue ou contribuir diretamente no repositório!