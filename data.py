# data.py

# Cuerpo para crear un usuario nuevo (necesario para obtener el token)
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

# --- Cuerpos para crear KITS (los 9 casos de la lista de comprobación) ---

# Prueba 1: 1 carácter permitido
kit_body_1_character = {
    "name": "a"
}

# Prueba 2: 511 caracteres (máximo permitido)
kit_body_511_characters = {
    "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
}

# Prueba 3: 0 caracteres (string vacío)
kit_body_empty = {
    "name": ""
}

# Prueba 4: 512 caracteres (uno más del máximo)
kit_body_512_characters = {
    "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
}

# Prueba 5: caracteres especiales
kit_body_special_chars = {
    "name": "\"№%@\","
}

# Prueba 6: espacios
kit_body_spaces = {
    "name": " A Aaa "
}

# Prueba 7: números (como string)
kit_body_numbers = {
    "name": "123"
}

# Prueba 8: sin el parámetro name
kit_body_no_name = {}

# Prueba 9: tipo de dato incorrecto (número en lugar de string)
kit_body_number_type = {
    "name": 123
}