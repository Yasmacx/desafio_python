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

    cursor.execute("""
        INSERT INTO medicos (nome, especialidade, crm)
        VALUES (?, ?, ?)
    """, (nome, especialidade, crm))

    conectar.commit()
    medico_id = cursor.lastrowid
    conectar.close()

    return {"sucesso": True, "id": medico_id, "mensagem": "Médico cadastrado com sucesso."}