 
limite = 0 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite1 = 500

mensagem = """
      
B ====================== BN - Banco Neto ========================== N
|================================================================== |    
|                       Escolhe a opcao desejada                    |
|================================================================== |                                                              
|                       [1] - Depositar                             |
|                       [2] - Sacar                                 |
|                       [3] - Extrato                               |
|                       [0] - Sair                                  |
B ====================== BN - Banco Neto ========================== N    
      ==> """ 

opcao = int(input(mensagem))

while True:
    
    if opcao == 0:
        print(" Obrigado por utilizar nosso BN - Banco Neto, volte sempre!!!")
        break
    elif  opcao == 1:
        print()
        mensagem1 = """
B ======================== BN - Banco Neto ======================== N
|================================================================== |    
|                   Deseja fazer um depoosito                       |
|================================================================== |                                                                
|         [4] - Dinheiro                                            |
|         [5] - cheque                                              |
|                                                                   |
B ========================= BN - Banco Neto ======================= N  
         ==> """
        opcao = int(input(mensagem1))
        print()

    elif opcao == 4:
        dinheiro = float(input("Informa o valor a ser depositado em dinheiro: R$ "))

        if dinheiro > 0: 
            limite += dinheiro 
            extrato += f"Depósito: R$ {dinheiro:.2f}\n"
            print()
            print(f"Deposito realizado com sucesso!!")
            print()
            opcao = int(input(mensagem))
            print()
        else:
            print("Operação falhou! O valor informado é inválido.")   


    elif opcao == 5:
        cheque = float(input("Informa o valor a ser depositado do cheque: R$ "))

        if cheque > 0: 
            limite += cheque 
            extrato += f"Cheque compensado: R$ {cheque:.2f}\n"
            print()
            print(f"Deposito realizado com sucesso!!")
            print()
            opcao = int(input(mensagem))
            print()
        else:
            print("Operação falhou! O valor informado é inválido.")   
        
        
    elif opcao == 2:
        saque = float(input("Informe o valor do saque: "))
        

        excedeu_saldo = saque > limite

        excedeu_limite = saque > limite1

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            opcao = int(input(mensagem))
            

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            opcao = int(input(mensagem))

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            opcao = int(input(mensagem))

        elif saque > 0:
            limite -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            opcao = int(input(mensagem))
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        

    elif opcao == 3:

        print("\n================ EXTRATO BN ================")

        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {limite:.2f}")
        print("====================BN======================")
        opcao = int(input(mensagem))

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        opcao = int(input(mensagem))