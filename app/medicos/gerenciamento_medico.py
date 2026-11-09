import sqlite3
from database.connection import conectar_db


def cadastrar_medico(nome, especialidade, crm):
    conectar = conectar_db()
    cursor = conectar.cursor()

    cursor.execute("SELECT id FROM medicos WHERE crm = ?", (crm,))
    medico_existente = cursor.fetchone()

    if medico_existente:
        conectar.close()
        return {"sucesso": False, "mensagem": "CRM já cadastrado no sistema."}
                #sucesso: false: falso achou algo igual na tabela, ou seja, ja tem no sistema os dados da pessoa

    cursor.execute("""
        INSERT INTO medicos (nome, especialidade, crm)
        VALUES (?, ?, ?)
    """, (nome, especialidade, crm))
    #cursos.execute executa a comando sql q add novos dados para banco de dados

    conectar.commit()
    medico_id = cursor.lastrowid
    conectar.close()

    return {"sucesso": True, "id": medico_id, "mensagem": "Médico cadastrado com sucesso."}

def validar_crm(crm):
    if not crm or not isinstance(crm, str):
        return {"valido": False, "mensagem": "CRM inválido. O formato deve ser um texto preenchido."}

    crm_limpo = crm.strip()

    if len(crm_limpo) == 0:
        return {"valido": False, "mensagem": "O CRM não pode ser vazio."}

    conectar = conectar_db()
    cursor = conectar.cursor()

    cursor.execute("SELECT id FROM medicos WHERE crm = ?", (crm_limpo,))
    medico_existente = cursor.fetchone()

    conectar.close()

    if medico_existente:
        return {"valido": False, "mensagem": "CRM já cadastrado no sistema."}

    return {"valido": True, "mensagem": "CRM disponível para cadastro."}