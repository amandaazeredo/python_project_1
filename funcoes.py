import validacoes, idade_em_dias

def listar_cadastros(ids, nomes, cpfs, datas_nasc):
  if not ids:#se a lista de ids estiver vazia
    print("Não há cadastros armazenados.")
    return
  #imprimindo dados
  print("***********Lista de Cadastros***********")
  for id in range(len(ids)):#itera sobre os indices da lista ids para imprimir cada dado cadastrado em ordem
    #imprime o dado de acordo com o ID - indice
    print("\nID:", ids[id])
    print("Nome:", nomes[id])
    print("CPF:", cpfs[id])
    print("Data de Nascimento:", datas_nasc[id])
    idade_em_dias.imprime_idade_em_dias(datas_nasc)

def inserir_cadastros(ids, nomes, cpfs, datas_nasc):
  #input do usuario
  print("***********Cadastro de dados***********")    
  op = int(input("Deseja criar ID? (1 - Sim, 2 - Não): "))
  #verifica opção
  if op == 1:
      id = int(input("Digite o ID: "))
      while validacoes.valida_id(ids, id):  #chamando verificação de id, se retorna verdadeiro entra no bloco while
        print("ID já está em uso. Por favor, escolha outro.")
        id = int(input("Digite o ID: "))
  elif op == 2:
      if not ids:  # se a lista ids estiver vazia, atribui 1 como o primeiro ID
          id = 1
      else:
        id = 1
        while id in ids:  # Encontra o menor ID disponível para atribuir automaticamente
          id += 1 #incrementa +1 ao menor id disponivel
  else:
    print("Opção inválida, implementado o id automaticamente.")
    id = 1
    while id in ids:  #encontra o menor ID disponível
      id += 1


  nome = input("Nome completo: ")
  cpf = input("CPF sem pontos e traços (EX.: 12345678900): ")
  data_nasc = input("Data de nascimento (EX.: 01/01/1900): ")

  # Insere os dados nas posição correta de acordo com o id
  insert_position = id - 1  # Posição na lista será o ID - 1 (pois as listas começam do índice 0)
  ids.insert(insert_position, id)

  nome_validado = validacoes.validar_nome(nome)
  if nome_validado is not None:  # Verifica se o nome é válido
    nomes.insert(insert_position - 1, nome_validado)#insere o nome validado na posição correta da lista
  else:
    print("Nome inválido")
    exit()

  cpf_validado = validacoes.valida_cpf(cpf)
  if cpf_validado: 
    cpfs.insert(insert_position, cpf)
  else:
    exit()

  data_validada = validacoes.valida_data(data_nasc)
  if data_validada: 
    datas_nasc.insert(insert_position, data_nasc)
  else:
    exit()

def remover_cadastros(ids, nomes, cpfs, datas_nasc):
  #input do usuario
  print("***********Remover cadastro***********")
  id = int(input("Digite o ID do cadastro a ser removido: "))

  #verificando se o ID existe
  while not validacoes.valida_id(ids, id):  #se retorna falso entra no bloco while
      id = int(input("ID não encontrado, digete um ID válido:"))

  #removendo os dados correspondentes do ID
  index = ids.index(id)#var que recebe o indice do id
  nomes.pop(index)#removendo nome do index
  cpfs.pop(index)#removendo cpf do index
  datas_nasc.pop(index)#removendo data de nascimento do index
  ids.remove(id)#removendo id

  print("Cadastro removido com sucesso.")

def alterar_cpf(ids, cpfs):
  print("***********Alterar CPF***********")
  id = int(input('Entre com o ID do CPF que deseja alterar: '))
  if id in ids: #se o id existe na lista
    index = ids.index(id)
    cpf_novo = input('Entre com o novo CPF: ')
    if validacoes.valida_cpf(cpf_novo):#se for valido
      cpfs[index] = cpf_novo#cpf inserido no index
      print('CPF alterado com sucesso!')
    elif not validacoes.valida_cpf(cpf_novo):
      exit()
    else:
      print(f'O ID {id} não foi encontrado!')

def trocar_sobrenomes(ids, nomes):
    print("***********Troca de Sobrenomes***********")
    id1 = int(input("Digite o ID do primeiro sobrenome a ser trocado: "))
    id2 = int(input("Digite o ID do segundo sobrenome a ser trocado: "))

    if id1 not in ids or id2 not in ids:#se algum dos ids não for encontrado o erro ocorre
        print("IDs inválidos. Pelo menos um dos IDs não foi encontrado.")
        return
  #variaveis que recebem o indice dos ids escolhidos
    index1 = ids.index(id1)
    index2 = ids.index(id2)

  #separando nome do sobrenome e pegando o último item
    sobrenome_1 = nomes[index1].split(' ')[-1]  
    sobrenome_2 = nomes[index2].split(' ')[-1]  

  #substituindo sobrenomes
    nome1 = nomes[index1].replace(sobrenome_1, sobrenome_2)  
    nome2 = nomes[index2].replace(sobrenome_2, sobrenome_1) 

  #atribuindo novos nomes
    nomes[index1] = nome1
    nomes[index2] = nome2

    print("Sobrenomes trocados com sucesso!")
