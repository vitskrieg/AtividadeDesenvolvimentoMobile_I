import os


class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Agenda:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.contatos = self.ler_contatos()

    def ler_contatos(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                linhas = f.readlines()
                contatos = [Contato(*linha.strip().split(";")) for linha in linhas]
                return contatos
        else:
            return []

    def salvar_contatos(self):
        with open(self.arquivo, "w") as f:
            for contato in self.contatos:
                f.write(f"{contato.nome};{contato.email};{contato.telefone}\n")

    def inserir_contato(self, contato):
        self.contatos.append(contato)
        self.salvar_contatos()

    def apagar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                self.salvar_contatos()
                return True
        return False

    def listar_contatos(self):
        for contato in self.contatos:
            print(f"{contato.nome}: {contato.email} | {contato.telefone}")

    def atualizar_contato(self, nome, novo_email, novo_telefone):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.email = novo_email
                contato.telefone = novo_telefone
                self.salvar_contatos()
                return True
        return False


pessoa = Contato("Vilson", "vilson.filho@gmail.com", 03242097)
agenda = Agenda("contatos")
agenda.inserir_contato(pessoa)
agenda.ler_contatos()
agenda.salvar_contatos()
agenda.apagar_contato("Vilson")
