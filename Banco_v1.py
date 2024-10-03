import textwrap

def menu():
    menu = '''\n
    ========= MENU PRINCIPAL =========
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ [valor:.2f]\n"
        print('\n=== Depósito Concluído ===')
    else:
        print('\n=== Depósito Não Aprovado ===')

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, n_saques, lim_saque):
    sem_saldo = valor > saldo
    sem_limite = valor > limite
    sem_saques = n_saques >= lim_saque

    if sem_saldo:
        print('\n=== Saldo insuficiente ===')
    elif sem_limite:
        print('\n=== Limite de saque Bloqueado ===')
    elif sem_saques:
        print('\n=== N° de saques alcançado ===')
    elif valor > 0:
        saldo -= valor
        extrato +=f"Saque:\tR$ {valor:.2f}\n"
        n_saques += 1
        print('\n=== Saldo Concluído ===')
    else:
        print('\n=== Operação inválida ===')

    return saldo, extrato

def mostra_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print('==========================================')

def criar_user(usuarios):
    cpf = input('Informe seu CPF (apenas números)')
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print('\n=== CPF já cadastrado ===')
        return
    
    nome = input('Informe o nome')
    data_nascimento = input('Informe data de nascimento')
    endereco = input('Informe o endereço')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_user(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe seu CPF')
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada ===')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print('\n=== Usuário não encontrado ===')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('='* 100)
        print(textwrap.dedent(linha))

def main():
    LIM_SAQUE = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input('Informe o valor depositado:'))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input('Informe o valor do saque:'))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                n_saques=n_saques,
                lim_saque=LIM_SAQUE,
            )
        elif opcao == "3":
            mostra_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            criar_user(usuarios)
        elif opcao == "7":
            break
        else:
            print('Operação inválida')

main()
