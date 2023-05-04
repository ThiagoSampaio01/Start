import os 

def login():
    while True:
        usuario = input("Digite seu Login: ")
        senha = input("Digite sua senha: ")
        if (usuario == "Victor" or usuario == "Thiago") and senha == "1234":
            print("Bem-vindo, ", usuario, "! Você entrou no xvideos.")
            os.system ("start wwww.xvideos.com")
            break
        else:
            print("Tente novamente, punheteiro.")

login()
