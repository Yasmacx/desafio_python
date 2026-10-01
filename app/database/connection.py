import sqlite3


def conectar_db():
    conectar = sqlite3.connect('smartclinic.db')

    conectar.execute("PRAGMA foreign_keys = ON;")
    return conectar

def create_table():
    conectar = conectar_db()
    cursor = conectar.cursor()

    cursor.execute("""
        CREATE TABLE pacientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        data_nascimento TEXT NOT NULL
    );
""")
    cursor.execute("""
        CREATE TABLE medicos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especialidade TEXT NOT NULL,
        crm TEXT NOT NULL UNIQUE
        );
""")
    cursor.execute("""
        CREATE TABLE consultas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        medico_id INTEGER NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('confirmada', 'cancelada', 'realizada')),
        FOREIGN KEY(medico_id)REFERENCES medicos(id),
        FOREIGN KEY(paciente_id)REFERENCES pacientes(id)
        );
""")
        
    conectar.commit() #grava alterações para sempre no banco de dados, igual github
    conectar.close() #ppara de conectar o banco de dados no arquivo, por contado uso da memoria temporario

if __name__=="__main__":
    create_table()
    print("Tabela criada com sucesso!")