quantidade_excelente = 0
quantidade_ruim = 0
quantidade_bom = 0
for i in range(1, 51):
    print(f"--- Entrevistado {i} ---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    print("Opinião: 1-EXCELENTE | 2-BOM | 3-RUIM")
    opcao = input("Digite a sua opção (1, 2 ou 3): ")
    
    if opcao == "1":
        quantidade_excelente = quantidade_excelente + 1
    elif opcao == "2":
        quantidade_bom = quantidade_bom + 1
    elif opcao == "3":
        quantidade_ruim = quantidade_ruim + 1

print("\n=== RESULTADO ===")
print("a) Respostas EXCELENTE:", quantidade_excelente)
print("b) Respostas RUIM:", quantidade_ruim)

