import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from controllers.connection_controller import ConnectionController
from controllers.event_controller import EventController
from controllers.main_controller import MainController
from controllers.tag_controller import TagController
from controllers.user_controller import UserController
import random

# ---------- Mock 40 users ----------
app_controller = MainController()
user_controller = app_controller.user_controller

print("Iniciando a criação de 40 usuários mock...")
for i in range(1, 41):
    username = f'user{i:02}'
    password = username
    email = f'{username}@example.com'

    try:
        user_controller.register_user(
            username=username,
            password=password,
            email=email
        )
        print(f"Usuário '{username}' criado.")
    except ValueError as e:
        print(f"Erro ao criar usuário '{username}': {e}")

total_users = len(user_controller.users)
print(f"\nOperação concluída. Total de usuários no sistema: {total_users}")

# ---------- Mock 120 connections ----------
connection_controller = ConnectionController(app_controller)
all_users = user_controller.users
target_connections = 120
created_connections_count = 0

print(f"\nIniciando a criação de {target_connections} conexões mock...")

# Loop para garantir 120 conexões
while created_connections_count < target_connections:
    # Sorteia dois usuários diferentes da lista
    user1, user2 = random.sample(all_users, 2)

    # Tenta criar a conexão usando o controller
    new_connection = connection_controller.create_connection(user1, user2)

    # Se a conexão foi criada com sucesso (não era duplicada)
    if new_connection:
        created_connections_count += 1
        
        # Aceita a conexão com 70% de chance para ter dados mais realistas
        if random.random() < 0.7:
            connection_controller.accept_connection(new_connection.id, user2)

print(f"\n{created_connections_count} conexões criadas com sucesso.")
