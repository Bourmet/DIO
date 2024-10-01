'''Operações: depósito, saque e extrato'''
menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

'''

saldo = 0
limite = 500
extrato = " "
n_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor de depósito: ') )
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print('Operação concluída com sucesso.')
        else:
            print('Valor de depósito inválido.')

    elif opcao == '2':
        qntd_sacada = float(input('Informe o valor do saque: ') )
        if n_saques <= LIMITE_SAQUES:
            if qntd_sacada <= 500 and qntd_sacada <= saldo:
                saldo -= qntd_sacada
                extrato += f"Saque: R$ {qntd_sacada:.2f}\n"
                n_saques += 1
                print('Operação concluída com sucesso.')
            else:
                print('Operação inválida. Saldo ou limite por saque ultrapassado')
        else:
            print('Operação inválida. Limite de saques ultrapassado')

    elif opcao == '3':
        print('\n####################### EXTRATO #######################')
        print("Não houve movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == '4':
        break

    else:
        print('Operação inválida. Tente novamente')
