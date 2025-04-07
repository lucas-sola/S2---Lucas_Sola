#-*- coding: UTF-8 -*-

#validando a opção
def saudacao(nome): 
    print(f"Olá, {nome}! Bem-vindo ao programa.")

def menu():
    print("Escolha uma opção:")
    print("1 - Ver uma mensagem motivacional")
    print("2 - Ver a hora atual (fictícia)")
    print("3 - Sair")

#pegando o nome do usuario
nome_usuario = input("Digite seu sua idade: ")
saudacao(nome_usuario)

#sistema de repetição até o usuário decidir sair
while True:
    menu()
    escolha = input("Digite o número da opção: ")

