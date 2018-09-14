#importa  uma biblioteca
import sqlite3
 ######## FUNÇOES ##########

def criar_tabela_usuario(conexao):
    #cria o cursor para operar o banco
    cursor = conexao.cursor()


    #mota o sql a ser executado
    sql = """
    CREATE TABLE IF NOT EXISTS usuario(
    nome text,
    login text,
    senha text
    );

    """

    # executa um sql
    cursor.execute(sql)

def inserir_usuario(conexao):
    #cria o cursor para operar o banco
    cursor = conexao.cursor()

    #################################################
    nome = input("Digite seu nome : ")
    login = input("Digite seu nome1 :")
    senha = input("Digite sua senha :")
    sql = """
    INSERT INTO usuario VALUES(
    '{}',
    '{}',
    '{}'
    );

    """.format(nome, login, senha)

    #executa o sql
    cursor.execute(sql)

    #salvar as modificações.
    #o commit sempre deve ser feito depois do insert ou select
    conexao.commit()



def listar_usuarios(conexao):
    #cria o cursor para operar o banco
    cursor = conexao.cursor()

    #monta o sql
    sql = "SELECT rowid,* FROM usuario;"

    #executa o sql
    cursor.execute(sql)

    #armazena os dados (registro) do SELECT
    #toda a vez que executa o select, precisa
    usuarios = cursor.fetchall()# buscar todos

    for usr in usuarios:
        print("{}-{}".format(usr[0], usr[1]) )




#############  PRINCIPAL #################
print("conectando no banco...\n\n")
#1
conexao = sqlite3.connect("aula28.sqlite")

# inserir_usuario(conexao)
listar_usuarios(conexao)




















print("\n\nfechando conexao..........")
#fechando a conexao (ligação)
conexao.close()
