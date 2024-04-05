from datetime import date

def eh_bissexto(ano: int) -> bool:#verifica se o ano é bissexto
    cond1 = ano % 4 == 0
    cond2 = ano % 100 != 0
    cond3 = ano % 400 == 0
    return (cond1 and cond2) or cond3

def conta_dias(dia_hoje, mes_hoje, ano_hoje, dia_nasc, mes_nasc, ano_nasc):
    dias = 0
    for ano in range(ano_nasc, ano_hoje + 1):
        lista_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#meses do ano
        if eh_bissexto(ano):
            lista_meses[1] = 29#se for bissexto o mês 2 tem seus dias alterados para 29
        total_dias_ano = sum(lista_meses)#soma os dias do ano
        if ano not in (ano_nasc, ano_hoje):#se não estamos no ano do nascimento
            dias += total_dias_ano #dias recebe a soma dos dias do ano
        else:
            mes_inicial = 1
            if ano == ano_nasc:
                mes_inicial = mes_nasc
            mes_final = 12
            if ano == ano_hoje:
                mes_final = mes_hoje
            for mes in range(mes_inicial, mes_final + 1):
                total_dias_mes = lista_meses[mes - 1]
                dia_inicial = 1
                if (mes, ano) == (mes_nasc, ano_nasc):
                    dia_inicial = dia_nasc
                dia_final = total_dias_mes
                if (mes, ano) == (mes_hoje, ano_hoje):
                    dia_final = dia_hoje
                dias += dia_final - dia_inicial + 1
    return dias

def imprime_idade_em_dias(datas_nasc):
  hoje = date.today()
  dia_hoje, mes_hoje, ano_hoje = hoje.day, hoje.month, hoje.year

  idades_calculadas = []  #armazena as idades calculadas para output

  for data_nasc in datas_nasc:  # itera sobre cada data de nascimento na lista
      partes_data = data_nasc.split('/')  #divide a data de nascimento em partes
    #convertendo partes em numero inteiro
  dia_nasc = int(partes_data[0])  
  mes_nasc = int(partes_data[1]) 
  ano_nasc = int(partes_data[2]) 
  idade = conta_dias(dia_hoje, mes_hoje, ano_hoje, dia_nasc, mes_nasc, ano_nasc)  #chama funao de calculo de idade em dias
  idades_calculadas.append(idade)  # adiciona a idade calculada à lista de idades
  print('Calculada: ', idade, 'dia(s)')
