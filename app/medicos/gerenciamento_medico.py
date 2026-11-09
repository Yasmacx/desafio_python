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
    #valida se nao tem crm e str, considera como invalido se nao for letra e nem def

    crm_limpo = crm.strip()
    #stip tira espaços em branco

    if len(crm_limpo) == 0:
        return {"valido": False, "mensagem": "O CRM não pode ser vazio."}
    #deixa sem espaços e valida se tiver nada

    conectar = conectar_db()
    cursor = conectar.cursor()

    cursor.execute("SELECT id FROM medicos WHERE crm = ?", (crm_limpo,))
    medico_existente = cursor.fetchone()

    conectar.close()

    if medico_existente:
        return {"valido": False, "mensagem": "CRM já cadastrado no sistema."}

    return {"valido": True, "mensagem": "CRM disponível para cadastro."}


def consultar_medico(termo_busca=None):
                        #none é usado para se o usuario nao colocar oq ele quer procurar, ele coloca todas as infos
    conectar = conectar_db()
    cursor = conectar.cursor()

    if termo_busca is None or str(termo_busca).strip() == "":
        cursor.execute("""
            SELECT id, nome, especialidade, crm
            FROM medicos
        """)
        medicos_encontrados = cursor.fetchall()
        conectar.close()

        lista_medicos = []
        for medico in medicos_encontrados:
            lista_medicos.append({
                "id": medico[0],
                "nome": medico[1],
                "especialidade": medico[2],
                "crm": medico[3]
            })

        return {"sucesso": True, "dados": lista_medicos}

    termo_formatado = f"%{str(termo_busca).strip()}%"

    cursor.execute("""
        SELECT id, nome, especialidade, crm
        FROM medicos
        WHERE nome LIKE ? OR especialidade LIKE ? OR crm LIKE ? OR id = ?
    """, (termo_formatado, termo_formatado, termo_formatado, termo_busca))

    medicos_encontrados = cursor.fetchall()
    conectar.close()

    lista_medicos = []
    for medico in medicos_encontrados:
        lista_medicos.append({
            "id": medico[0],
            "nome": medico[1],
            "especialidade": medico[2],
            "crm": medico[3]
        })

    return {"sucesso": True, "dados": lista_medicos}