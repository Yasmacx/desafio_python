from gerenciamento_medico import (
    cadastrar_medico,
    validar_crm
)

# 1. Cadastrar médico
resultado = cadastrar_medico(
    "Carlos Silva",
    "Cardiologia",
    "CRM12345"
)

print(resultado)