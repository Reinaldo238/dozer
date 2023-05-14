import requests
import json
import time
import urllib3
import os
import pandas as pd
from datetime import datetime
import os.path
import openpyxl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

soma4 = 0
numeros_somados4 = set()
moedas4 = 0
maior_valor4= 0

soma7 = 0
numeros_somados7 = set()
moedas7 = 0
maior_valor7= 0

soma8 = 0
numeros_somados8 = set()
moedas8 = 0
maior_valor8= 0

soma9 = 0
numeros_somados9 = set()
moedas9 = 0
maior_valor9= 0

soma12 = 0
numeros_somados12 = set()
moedas12 = 0
maior_valor12= 0

soma13 = 0
numeros_somados13 = set()
moedas13 = 0
maior_valor13= 0

soma14 = 0
numeros_somados14 = set()
moedas14 = 0
maior_valor14= 0

soma15 = 0
numeros_somados15 = set()
moedas15 = 0
maior_valor15= 0

soma16 = 0
numeros_somados16 = set()
moedas16 = 0
maior_valor16= 0

soma17 = 0
numeros_somados17 = set()
moedas17 = 0
maior_valor17= 0

soma18 = 0
numeros_somados18 = set()
moedas18 = 0
maior_valor18= 0

soma19 = 0
numeros_somados19 = set()
moedas19 = 0
maior_valor19 = 0


def mesa_quatro():

    global soma4 # usar a variável global
    global numeros_somados4 # usar o conjunto global
    global moedas4
    global maior_valor4


    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=4", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 250000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados4: # verificar se o número já foi somado

            valor = item ['payout']

            soma4 += item['payout'] # somar o número à soma
            moedas4 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas4], "valor_total_pago":[soma4/1000000000], "valor_total_gasto": [moedas4*0.05]})], ignore_index=True)

            

            if item['payout'] > maior_valor4:
                maior_valor4 = item['payout']


            numeros_somados4.add(gameid) # adicionar o número ao conjunto de números já somados
    
    if os.path.isfile("dados_mesa_4.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_4.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_4.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_4.xlsx", index=False)
            
    print("---------------------------------")
    print("ANÁLISE MESA 4")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma4/1000000000}")
    print(f'Valor gasto:           {moedas4 * 0.05}')
    print(f"Nº de moedas jogadas:: {moedas4}")
    print(f"Maior valor pago:      {maior_valor4/1000000000}")
    print("---------------------------------")  
def mesa_sete():

    global soma7 # usar a variável global
    global numeros_somados7 # usar o conjunto global
    global moedas7
    global maior_valor7

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=7", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 500000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados7: # verificar se o número já foi somado

            valor = item ['payout']

            soma7 += item['payout'] # somar o número à soma
            moedas7 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas7], "valor_total_pago":[soma7/1000000000], "valor_total_gasto": [moedas7*0.1]})], ignore_index=True)
            

            if item['payout'] > maior_valor7:
                maior_valor7 = item['payout']


            numeros_somados7.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_7.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_7.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_7.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_7.xlsx", index=False)

    
    print("---------------------------------")
    print("ANÁLISE MESA 7")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma7/1000000000}")
    print(f'Valor gasto:           {moedas7 * 0.1}')
    print(f"Nº de moedas jogadas:: {moedas7}")
    print(f"Maior valor pago:      {maior_valor7/1000000000}")
    print("---------------------------------")
def mesa_oito():

    global soma8 # usar a variável global
    global numeros_somados8 # usar o conjunto global
    global moedas8
    global maior_valor8

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=8", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 500000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados8: # verificar se o número já foi somado

            valor = item ['payout']

            soma8 += item['payout'] # somar o número à soma
            moedas8 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas8], "valor_total_pago":[soma8/1000000000], "valor_total_gasto": [moedas8*0.05]})], ignore_index=True)
            

            if item['payout'] > maior_valor8:
                maior_valor8 = item['payout']


            numeros_somados8.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_8.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_8.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_8.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_8.xlsx", index=False)

    
    print("---------------------------------")
    print("ANÁLISE MESA 8")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma8/1000000000}")
    print(f'Valor gasto:           {moedas8 * 0.05}')
    print(f"Nº de moedas jogadas:: {moedas8}")
    print(f"Maior valor pago:      {maior_valor8/1000000000}")
    print("---------------------------------")
def mesa_nove():

    global soma9 # usar a variável global
    global numeros_somados9 # usar o conjunto global
    global moedas9
    global maior_valor9

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=9", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])
    valor_referencia = 1000000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados9: # verificar se o número já foi somado

            valor = item ['payout']

            soma9 += item['payout'] # somar o número à soma
            moedas9 += item['coins']
            
            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas9], "valor_total_pago":[soma9/1000000000], "valor_total_gasto": [moedas9*0.05]})], ignore_index=True)
            

            if item['payout'] > maior_valor9:
                maior_valor9 = item['payout']


            numeros_somados9.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_9.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_9.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_9.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_9.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 9")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma9/1000000000}")
    print(f'Valor gasto:           {moedas9 * 0.05}')
    print(f"Nº de moedas jogadas:: {moedas9}")
    print(f"Maior valor pago:      {maior_valor9/1000000000}")
    print("---------------------------------")
def mesa_doze():

    global soma12 # usar a variável global
    global numeros_somados12 # usar o conjunto global
    global moedas12
    global maior_valor12

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=12", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])
    valor_referencia = 1000000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados12: # verificar se o número já foi somado

            valor = item ['payout']

            soma12 += item['payout'] # somar o número à soma
            moedas12 += item['coins']
            
            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas12], "valor_total_pago":[soma12/1000000000], "valor_total_gasto": [moedas12*0.25]})], ignore_index=True)
            

            if item['payout'] > maior_valor12:
                maior_valor12 = item['payout']


            numeros_somados12.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_12.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_12.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_12.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_12.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 12")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma12/1000000000}")
    print(f'Valor gasto:           {moedas12 * 0.25}')
    print(f"Nº de moedas jogadas:: {moedas12}")
    print(f"Maior valor pago:      {maior_valor12/1000000000}")
    print("---------------------------------")
def mesa_treze():

    global soma13 # usar a variável global
    global numeros_somados13 # usar o conjunto global
    global moedas13
    global maior_valor13

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=13", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])
    valor_referencia = 1000000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados13: # verificar se o número já foi somado

            valor = item ['payout']

            soma13 += item['payout'] # somar o número à soma
            moedas13 += item['coins']
            
            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas13], "valor_total_pago":[soma13/1000000000], "valor_total_gasto": [moedas13*0.05]})], ignore_index=True)
            

            if item['payout'] > maior_valor13:
                maior_valor13 = item['payout']


            numeros_somados13.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_13.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_13.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_13.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_13.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 13")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma13/1000000000}")
    print(f'Valor gasto:           {moedas13 * 0.05}')
    print(f"Nº de moedas jogadas:: {moedas13}")
    print(f"Maior valor pago:      {maior_valor13/1000000000}")
    print("---------------------------------")
def mesa_cartoze():

    global soma14 # usar a variável global
    global numeros_somados14# usar o conjunto global
    global moedas14
    global maior_valor14

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=14", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 1000000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados14: # verificar se o número já foi somado

            valor = item ['payout']

            soma14 += item['payout'] # somar o número à soma
            moedas14 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas14], "valor_total_pago":[soma14/1000000000], "valor_total_gasto": [moedas14*0.05]})], ignore_index=True)


            

            if item['payout'] > maior_valor14:
                maior_valor14 = item['payout']


            numeros_somados14.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_14.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_14.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_14.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_14.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 14")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma14/1000000000}")
    print(f'Valor gasto:           {moedas14 * 0.05}')
    print(f"Nº de moedas jogadas:: {moedas14}")
    print(f"Maior valor pago:      {maior_valor14/1000000000}")
    print("---------------------------------")
def mesa_quinze():

    global soma15 # usar a variável global
    global numeros_somados15 # usar o conjunto global
    global moedas15
    global maior_valor15

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=15", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 1000000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados15: # verificar se o número já foi somado

            valor = item ['payout']

            soma15 += item['payout'] # somar o número à soma
            moedas15 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas15], "valor_total_pago":[soma15/1000000000], "valor_total_gasto": [moedas15*0.1]})], ignore_index=True)

            
            if item['payout'] > maior_valor15:
                maior_valor15 = item['payout']


            numeros_somados15.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_15.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_15.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_15.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_15.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 15")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma15/1000000000}")
    print(f'Valor gasto:           {moedas15 * 0.1}')
    print(f"Nº de moedas jogadas:: {moedas15}")
    print(f"Maior valor pago:      {maior_valor15/1000000000}")
    print("---------------------------------")
def mesa_dezesseis():

    global soma16 # usar a variável global
    global numeros_somados16 # usar o conjunto global
    global moedas16
    global maior_valor16

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=16", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 5000000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados16: # verificar se o número já foi somado

            valor = item ['payout']

            soma16 += item['payout'] # somar o número à soma
            moedas16 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas16], "valor_total_pago":[soma16/1000000000], "valor_total_gasto": [moedas16*0.25]})], ignore_index=True)


            if item['payout'] > maior_valor16:
                maior_valor16 = item['payout']


            numeros_somados16.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_16.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_16.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_16.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_16.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 16")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma16/1000000000}")
    print(f'Valor gasto:           {moedas16 * 0.25}')
    print(f"Nº de moedas jogadas:: {moedas16}")
    print(f"Maior valor pago:      {maior_valor16/1000000000}")
    print("---------------------------------")
def mesa_dezessete():

    global soma17 # usar a variável global
    global numeros_somados17 # usar o conjunto global
    global moedas17
    global maior_valor17

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=17", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 1000000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados17: # verificar se o número já foi somado

            valor = item ['payout']

            soma17 += item['payout'] # somar o número à soma
            moedas17 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas17], "valor_total_pago":[soma17/1000000000], "valor_total_gasto": [moedas17*0.1]})], ignore_index=True)

            
            if item['payout'] > maior_valor17:
                maior_valor17 = item['payout']


            numeros_somados17.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_17.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_17.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_17.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_17.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 17")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma17/1000000000}")
    print(f'Valor gasto:           {moedas17 * 0.1}')
    print(f"Nº de moedas jogadas:: {moedas17}")
    print(f"Maior valor pago:      {maior_valor17/1000000000}")
    print("---------------------------------")
def mesa_dezoito():

    global soma18 # usar a variável global
    global numeros_somados18 # usar o conjunto global
    global moedas18
    global maior_valor18

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=18", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])

    valor_referencia = 2500000000

    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados18: # verificar se o número já foi somado

            valor = item ['payout']

            soma18 += item['payout'] # somar o número à soma
            moedas18 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas18], "valor_total_pago":[soma18/1000000000], "valor_total_gasto": [moedas18*0.25]})], ignore_index=True)

            
            if item['payout'] > maior_valor18:
                maior_valor18 = item['payout']


            numeros_somados18.add(gameid) # adicionar o número ao conjunto de números já somados
            
    if os.path.isfile("dados_mesa_18.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_18.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_18.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_18.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 18")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma18/1000000000}")
    print(f'Valor gasto:           {moedas18 * 0.25}')
    print(f"Nº de moedas jogadas:: {moedas18}")
    print(f"Maior valor pago:      {maior_valor18/1000000000}")
    print("---------------------------------")
def mesa_dezenove():


    global soma19 # usar a variável global
    global numeros_somados19 # usar o conjunto global
    global moedas19
    global maior_valor19

    request = requests.get(f"https://www.degenpusher.com:8080/api/pusher/status?machineId=19", verify=False)
    todos = json.loads(request.content)
    jogadas = todos['finished']

    df = pd.DataFrame(columns=["data_hora", "valor", "carteira", "moedas_jogadas", "valor_total_pago", "valor_total_gasto"])
    valor_referencia = 10000000000


    for item in jogadas:
        gameid = item ['gameId']

        if gameid not in numeros_somados19: # verificar se o número já foi somado

            valor = item ['payout']

            soma19 += item['payout'] # somar o número à soma
            moedas19 += item['coins']

            if valor >= valor_referencia:
                data_hora = datetime.now()
                carteira = item['userName']
                valor_atualizado = valor/1000000000
                df = pd.concat([df, pd.DataFrame({"valor": [valor_atualizado], "data_hora": [data_hora], "carteira":[carteira], "moedas_jogadas":[moedas19], "valor_total_pago":[soma19/1000000000], "valor_total_gasto": [moedas19*0.5]})], ignore_index=True)

            
            if item['payout'] > maior_valor19:
                maior_valor19 = item['payout']


            numeros_somados19.add(gameid) # adicionar o número ao conjunto de números já somados
            

    if os.path.isfile("dados_mesa_19.xlsx"):
        df_antigo=pd.read_excel("dados_mesa_19.xlsx")
        df_novo = pd.concat([df_antigo, df])
        df_novo.to_excel("dados_mesa_19.xlsx", index=False)

    else:
        df.to_excel("dados_mesa_19.xlsx", index=False)
    
    print("---------------------------------")
    print("ANÁLISE MESA 19")
    print("---------------------------------")
    print(f"Total de pagamento:    {soma19/1000000000}")
    print(f'Valor gasto:           {moedas19 * 0.5}')
    print(f"Nº de moedas jogadas:: {moedas19}")
    print(f"Maior valor pago:      {maior_valor19/1000000000}")
    print("---------------------------------")

escolher = []
escolher = input('Quais mesas deseja verificar? ')

while True:
   
    try:
     
        if "4" in escolher:
            mesa_quatro()
        if "7" in escolher:
            mesa_sete()
        if "8" in escolher:
            mesa_oito()
        if "9" in escolher:
            mesa_nove()
        if "12" in escolher:
            mesa_doze()
        if "13" in escolher:
            mesa_treze()
        if "14" in escolher:
            mesa_cartoze()
        if "15" in escolher:
            mesa_quinze()
        if "16" in escolher:
            mesa_dezesseis()
        if "17" in escolher:
            mesa_dezessete()
        if "18" in escolher:
            mesa_dezoito()
        if "19" in escolher:
            mesa_dezenove()
        if "0" in escolher:
            mesa_quatro()
            mesa_sete()
            mesa_oito()
            mesa_nove()
            mesa_doze()
            mesa_treze()
            mesa_cartoze()
            mesa_quinze()
            mesa_dezesseis()
            mesa_dezessete()
            mesa_dezoito()
            mesa_dezenove()
        time.sleep(30)
        os.system("cls")

    except requests.exceptions.RequestException as e:
            time.sleep(1)
