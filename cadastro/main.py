import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            tel TEXT NOT NULL,
            sexo TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL,
            curso TEXT NOT NULL,
            picture TEXT NOT NULL)''')
        self.conn.commit()

    def register_student(self, estudante):
        self.c.execute('''INSERT INTO estudantes 
            (nome, email, tel, sexo, data_nascimento, endereco, curso, picture) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', estudante)
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Registro concluído')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()
        return dados
        

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()
        return dados

    def update_student(self, novos_valores):
        query = '''UPDATE estudantes SET 
            nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? 
            WHERE id=?'''
        self.c.execute(query, novos_valores)
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID {novos_valores[8]} foi atualizado')

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f'Estudante com ID {id} foi deletado')

# Criar instância para testes
sistema_de_registro = SistemaDeRegistro()

#informações
#estudante = ('elena', 'elena@hotmail.com', '123', 'F', '01/07/2005', 'Angola,/luanda', 'medicina', 'imagem2.png')

#sistema_de_registro.register_student(estudante)


# ver estudantes
#deletar_aluno = sistema_de_registro.delete_student(3)
#todos_alunos = sistema_de_registro.view_all_students()
#procurar aluno
#aluno = sistema_de_registro.search_student(1)
#atualizar aluno
#estudante = ('elena', 'elena@hotmail.com', '123', 'F', '01/08/2005', 'Angola,/luanda', 'medicina', 'imagem2.png','4')
#aluno = sistema_de_registro.update_student(estudante)






