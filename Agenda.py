class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def __str__(self):
        favorito_texto = " (Favorito)" if self.favorito else ""
        return f"{self.nome}{favorito_texto} - Telefone: {self.telefone}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self):
        print("Adicionar novo contato")
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        favorito = input("Marcar como favorito? (s/n): ").strip().lower() == 's'
        contato = Contato(nome, telefone, email, favorito)
        self.contatos.append(contato)
        print("Contato adicionado com sucesso.\n")

    def listar_contatos(self):
        print("\nLista de contatos:")
        if not self.contatos:
            print("Nenhum contato cadastrado.\n")
            return
        for idx, contato in enumerate(self.contatos, start=1):
            print(f"{idx}. {contato}")
        print()

    def editar_contato(self):
        self.listar_contatos()
        if not self.contatos:
            return
        try:
            escolha = int(input("Digite o número do contato para editar: "))
            if escolha < 1 or escolha > len(self.contatos):
                print("Número inválido.\n")
                return
            contato = self.contatos[escolha - 1]
            print(f"Editando contato: {contato.nome}")
            nome = input(f"Novo nome ({contato.nome}): ").strip()
            telefone = input(f"Novo telefone ({contato.telefone}): ").strip()
            email = input(f"Novo email ({contato.email}): ").strip()
            if nome:
                contato.nome = nome
            if telefone:
                contato.telefone = telefone
            if email:
                contato.email = email
            print("Contato atualizado com sucesso.\n")
        except ValueError:
            print("Entrada inválida, digite um número.\n")

    def apagar_contato(self):
        self.listar_contatos()
        if not self.contatos:
            return
        try:
            escolha = int(input("Digite o número do contato para apagar: "))
            if escolha < 1 or escolha > len(self.contatos):
                print("Número inválido.\n")
                return
            contato = self.contatos.pop(escolha - 1)
            print(f"Contato '{contato.nome}' apagado com sucesso.\n")
        except ValueError:
            print("Entrada inválida, digite um número.\n")

    def alternar_favorito(self):
        self.listar_contatos()
        if not self.contatos:
            return
        try:
            escolha = int(input("Digite o número do contato para marcar/desmarcar favorito: "))
            if escolha < 1 or escolha > len(self.contatos):
                print("Número inválido.\n")
                return
            contato = self.contatos[escolha - 1]
            contato.favorito = not contato.favorito
            status = "favorito" if contato.favorito else "não favorito"
            print(f"Contato '{contato.nome}' agora é {status}.\n")
        except ValueError:
            print("Entrada inválida, digite um número.\n")

    def listar_favoritos(self):
        favoritos = [c for c in self.contatos if c.favorito]
        print("\nContatos favoritos:")
        if not favoritos:
            print("Nenhum contato favorito.\n")
            return
        for contato in favoritos:
            print(contato)
        print()

def menu():
    agenda = Agenda()
    while True:
        print("----- AGENDA DE CONTATOS -----")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Editar contato")
        print("4. Apagar contato")
        print("5. Marcar/Desmarcar favorito")
        print("6. Listar favoritos")
        print("0. Sair")
        escolha = input("Escolha uma opção: ").strip()
        print()
        if escolha == '1':
            agenda.adicionar_contato()
        elif escolha == '2':
            agenda.listar_contatos()
        elif escolha == '3':
            agenda.editar_contato()
        elif escolha == '4':
            agenda.apagar_contato()
        elif escolha == '5':
            agenda.alternar_favorito()
        elif escolha == '6':
            agenda.listar_favoritos()
        elif escolha == '0':
            print("Encerrando a agenda. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()

