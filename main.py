import funcoes, validacoes, idade_em_dias

#listas
ids = []
nomes = []
cpfs = []
datas_nasc = []

menu = '''
*********** SISTEMA DE CADASTRO ***********

Escolha uma opção:

1. Inserir novo cadastro
2. Alterar CPF
3. Trocar sobrenomes
4. Remover cadastro
5. Listar todos os cadastros
6. Encerrar
'''

while True:
  print(menu)
  opcao = input("Escolha uma opção: \n")
  if opcao == '1':
      funcoes.inserir_cadastros(ids, nomes, cpfs, datas_nasc)
  elif opcao == '2':
      funcoes.alterar_cpf(ids, cpfs)
  elif opcao == '3':
      funcoes.trocar_sobrenomes(ids, nomes)
  elif opcao == '4':
      funcoes.remover_cadastros(ids, nomes, cpfs, datas_nasc)
  elif opcao == '5':
      funcoes.listar_cadastros(ids, nomes, cpfs, datas_nasc)
  elif opcao == '6':
      print("Encerrando o programa...")
      break
  else:
      print("Opção inválida. Escolha uma opção válida.")
    



