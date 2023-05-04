import operacao
numero1= int(input("Digit um numero: "))
numero2= int(input("Digite outro numero: "))
operacao_escolhida= input ('Digite a operação: ex: +-*/ : ')

if operacao_escolhida == '+' or "soma":
    operacao.soma(int(numero1),int(numero2))

elif operacao_escolhida == "-" or "subtracao":   
    operacao.sub(numero1,numero2)

elif operacao_escolhida == "*" or "multiplicacao":
    operacao.multiplicacao (numero1,numero2)

elif operacao_escolhida == '/' or "divisao":
    operacao.divisao (numero1,numero2)
else: 
    print ("Erro, tente novamente")
    