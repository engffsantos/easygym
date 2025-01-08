# config.py

import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


class Config:
    """
    Configurações da aplicação EasyGym para uso com MySQL no XAMPP.
    """
    # Configurações principais do Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')

    # Configuração do banco de dados MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost/easygym')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa track para melhorar performance

    # Configuração da API de WhatsApp
    WHATSAPP_API_KEY = os.getenv('WHATSAPP_API_KEY', '')

# Configurações adicionais podem ser criadas para diferentes ambientes:
# class DevelopmentConfig(Config):
#     DEBUG = True
#
# class ProductionConfig(Config):
#     FLASK_ENV = 'production'
#     DEBUG = False
