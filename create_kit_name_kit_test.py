# create_kit_name_kit_test.py

import sender_stand_request
import data


# --- FUNCIONES AUXILIARES (ASSERTS) ---

def positive_assert(kit_body):
    """Comprueba que el kit se cree correctamente (código 201) y el nombre coincida."""
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201, f"Se esperaba 201, pero se recibió {response.status_code}"
    assert response.json()["name"] == kit_body["name"], "El nombre en la respuesta no coincide"


def negative_assert_code_400(kit_body):
    """Comprueba que el servidor rechace la solicitud con un error 400."""
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400, f"Se esperaba 400, pero se recibió {response.status_code}"


# --- LAS 9 PRUEBAS ---

# Prueba 1: 1 carácter permitido
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert(data.kit_body_1_character)


# Prueba 2: 511 caracteres permitidos
def test_create_kit_511_characters_in_name_get_success_response():
    positive_assert(data.kit_body_511_characters)


# Prueba 3: 0 caracteres (vacío) - Espera 400
def test_create_kit_0_characters_in_name_get_error_response():
    negative_assert_code_400(data.kit_body_empty)


# Prueba 4: 512 caracteres (excede el límite) - Espera 400
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert_code_400(data.kit_body_512_characters)


# Prueba 5: Caracteres especiales permitidos
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert(data.kit_body_special_chars)


# Prueba 6: Espacios permitidos
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(data.kit_body_spaces)


# Prueba 7: Números permitidos
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(data.kit_body_numbers)


# Prueba 8: Sin el parámetro name - Espera 400
def test_create_kit_no_name_get_error_response():
    negative_assert_code_400(data.kit_body_no_name)


# Prueba 9: Tipo de dato incorrecto (número en lugar de string) - Espera 400
def test_create_kit_number_type_in_name_get_error_response():
    negative_assert_code_400(data.kit_body_number_type)