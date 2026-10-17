import sender_stand_request

print("Conectando con el servidor...")
token = sender_stand_request.get_new_user_token()
print(f"¡Éxito! El token obtenido es: {token}")