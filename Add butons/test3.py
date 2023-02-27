
from emails import send_email


def test_send_email():
   
    assert send_email("ejemplo@gmail.com", "Prueba", "Este es un mensaje de prueba") == "Correo electrónico enviado correctamente"

   
    assert send_email("ejemplo", "Prueba", "Este es un mensaje de prueba") == "Error: dirección de correo electrónico inválida"

    
    assert send_email("ejemplo@gmail.com", "", "Este es un mensaje de prueba") == "Error: asunto vacío"

    
    assert send_email("ejemplo@gmail.com", "Prueba", "") == "Error: mensaje vacío"
