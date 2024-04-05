def validar_nome(nome):
  nome_parts = nome.split(' ')#dividindo o nome em partes por espaço
  if len(nome_parts) != 2:
      print("Há apenas uma palavra/primeiro nome")
      return nome_parts[0].capitalize()#retorna o nome com a primeira letra maiúscula
  else:
    primeiro_nome = nome_parts[0].capitalize()#primeira letra maiuscula no primeiro nome
    sobrenome = nome_parts[1].capitalize() #primeira letra maiuscula no sobrenome
    nome_completo = primeiro_nome + " " + sobrenome #concatenando nome
    return nome_completo

def valida_id(ids, id_informado):
#bloco serve para qualquer função pois retorna apenas um booleano que será interpretado na função a ser implementado
  if id_informado in ids:
      return True
  elif not str(id_informado).isdigit() or int(id_informado) <= 0:#tranformando o id em string para verificar se é digito inteiro e depois em int para verificar se é maior que 0
      return print("ID inválido, ele precisa ser um número inteiro positivo")
  else:
      return False

def valida_cpf(cpf):
  if len(cpf) != 11 or not cpf.isdigit():#verifica se não cpf tem exatos 11 digitos
      print("CPF inválido. Deve conter exatamente 11 dígitos.")
      return False

  nono_digito = int(cpf[8])#nono digito - região de emissão
  regioes = [7, 8, 9, 0] #regioes sudeste
  
  if nono_digito in regioes:#verifica se o nono dígito corresponde a uma região fiscal da Região Sudeste
      print("CPF inválido. Não pode ser emitido na Região Sudeste.")
      return False
  
  print("CPF válido.")#se ele não foi pego em nenhum if ele é válido retorna True
  return True

def valida_data(data_nasc):
  formato = data_nasc.split('/')#divindo os campos da data pela /
  if len(formato) != 3: #deve ser dividida em 3 partes, possuindo 2 /
      print("Data inválida. Utilize o formato dd/mm/aaaa.")
      return False#invalido
  
  for parte in formato:
      if not parte.isdigit():#verificando se cada parte do formato possui apenas digitos
          print("Data de nascimento inválida. Cada parte deve ser um número.")
          return False#invalido
  
  #se ele não caiu em nenhuma condição os valores são atribuidos a variaveis
  dia = int(formato[0])
  mes = int(formato[1])
  ano = int(formato[2])
  
  if mes < 1 or mes > 12:#verifica mês
      print("Data de nascimento inválida. O mês deve estar entre 1 e 12.")
      return False
  
  if mes in [1, 3, 5, 7, 8, 10, 12]:#meses com 31 dias
      num_dias = 31
  elif mes == 2:#mês variante no ano bissexto
      if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:#bissexto
          num_dias = 29
      else:#ano comum
          num_dias = 28
  else:#outos meses
      num_dias = 30
  
  if dia < 1 or dia > num_dias:#dependendo do numero de dias da condição anterior
      print(f"Data de nascimento inválida. O dia deve estar entre 1 e {num_dias}.")
      return False
  
  from datetime import date
  hoje = date.today()#verificando se a data de nascimento é menor que a data atual
  if ano > hoje.year:
    if ano == hoje.year and mes > hoje.month: 
      if mes == hoje.month and dia > hoje.day:
        print("Entrada invalida, data inserida é futura.")
        return False
  
  print("Data de nascimento válida.")#se não caiu em nenhuma condição a data é válida
  return True

