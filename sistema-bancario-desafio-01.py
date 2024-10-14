
def mostrarMenu(nome):
    global opcao
    menu = f"""OI {nome}! 
               QUAL OPERAÇÃO DESEJA REALIZAR ? 
               DIGITE: 
                    1 - DEPÓSITO 
                    2 - SAQUE 
                    3 - EXTRATO
                    4 - SAIR """
    opcao = int(input(menu))
    return opcao

nome = input('DIGITE SEU NOME    \n')
mostrarMenu(nome)

global saldo
extrato=[]
global qtdSaqueDiario
qtdSaqueDiario=0
saldo=0

while opcao != 4:
    if opcao == 1:
        valorDep = float(input('INFORME O VALOR A SER DEPOSITADO:  R$'))
        if valorDep > 0:
            saldo+=valorDep
            extrato = extrato + [f"DEPÓSITO DE R${valorDep},  SALDO TOTAL R${saldo}"]
        else:
            print('VALOR INVÁLIDO')
        mostrarMenu(nome)
        
    elif opcao == 2:
        valorSaque = float(input('INFORME O VALOR A SER SACADO:  R$'))        
        if valorSaque>500 :
           print('NÃO EH POSSÍVEL SACAR ACIMA DE R$5OO')
        if qtdSaqueDiario >=3:
           print('NÃO EH POSSÍVEL SACAR + DE 3 SAQUES POR DIA')
        if valorSaque > saldo:
            print('SALDO INDISPONIVEL')
        if (valorSaque <= saldo) & (qtdSaqueDiario<3):
           qtdSaqueDiario+=1
           saldo-=valorSaque
           extrato = extrato + [f"SAQUE DE R${valorSaque},  SALDO TOTAL R${saldo}"]
        mostrarMenu(nome)

    elif opcao == 3:
        for e in extrato:
            print(e)
        mostrarMenu(nome)

    elif opcao == 4:
        print('SAINDOOOOOO')

    else:
        print('OPÇÃO INVÁLIDA')
        mostrarMenu(nome)