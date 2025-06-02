#Manu principal do Sisteme 

import sqlite3

######################################################
#  Definicao de Variaveis Globais                    #
######################################################


### Definicao de funcoes




#######################################################
#  Definicao de Variaveis Globais                     #
#######################################################
def main_menu():
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2, lista de Aluno ")
    print("3, Atualizar Aluno")
    print("4, Excluir Aluno")
    print("5, Sair")

    opcao =("Escolha uma opcao:")
    return opcao
 
###########################################################
#  Objetivo: Conectar no Banco de Dados e Criar as Tabelas#
###########################################################

def CreateTable():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor() 


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aluno( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                idade INTEGER
                )
     """)
    conexao.commit()
    conexao.close()

def register(nome,email,idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    
    try:
        cursor.execute("INSERT INTO aluno(nome,email,idade) VALUES (?,?,?)",
                       (nome,email,idade))
        conexao.commit()
        print("Aluno cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("Email ja cadastrado")
    finally:
        conexao.close()

    conexao.commit()
    conexao.close()

def display():
    conexao = sqlite3.connect("escola.db") 
    cursor = conexao.cursor() 

    cursor.execute("SELECT * FROM aluno")
    aluno = cursor. fetchall()

    conexao.close() # fecho a conexao com o banco 

    print("Lista de Aluno cadastrados")
 
    for aluno in aluno:
        print(aluno)

if __name__ == "__main__":
    CreateTable()
        
    while True:
        opcao = main_menu()
        if opcao == "1":
            nome = input("Nome:")
            email = input("E-mail:")
            idade = int(input("Idade:"))
            register(nome,email,idade)
        elif opcao == "2":    
            display()
        elif opcao == "3":
             id = int(input("Informe o ID do Aluno que vc quer atualizar"))
            new_nome = input("Novo Nome")
            new_email = input("Novo Email")
            new_idade = int(input("Nova Idade"))
            update(id,new_nome,new_email,new_idade)
        elif opcao == "5":    
            break
        else:
            print("Opcao Invalida") 




