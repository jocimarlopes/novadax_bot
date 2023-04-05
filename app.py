from time import sleep
from datetime import datetime
from account_novadax import listar_dados_moeda_id, ordem_de_compra, ordem_de_venda, quantia_ids_carteira, quantia_brl_carteira
from utils import verifica_carteira
# quantia minima ID = 12 id coins
# quantia minima BRL = 25 reais
ORDEM_ID_MINIMO = 12
ORDEM_BRL_MINIMO = 25
VALOR_TAXAS = 0.25

status = ''


def iniciar():
    qtd_brl_inicial = quantia_brl_carteira()
    qtd_ids_inicial = quantia_ids_carteira()
    global status
    qtd_parado = 0
    while True:
        result = listar_dados_moeda_id()
        date_result = datetime.fromtimestamp(result['timestamp'] / 1000)
        valor_compra = float(result['lastPrice'])
        valor_final = float(result['ask'])
        ratio = valor_final / valor_compra
        if qtd_parado > 20:
            status = ''
            qtd_parado = 0
        verify_data(ratio, date_result, valor_final)
        if ratio > 0.99 and ratio < 1.01:
            print('\nMédia: ', ratio)
            print('-> Não fazer nada')
            qtd_parado = qtd_parado + 1
        sleep(10)


def verify_data(ratio, date_result, valor_final):
    global status
    if ratio >= 1.03:
        print('\nMédia: ', ratio)
        print('Data: ', date_result)
        if status != 'VENDIDO' or ratio > 1.03:
            qtd_ids_carteira = quantia_ids_carteira()
            if qtd_ids_carteira >= ORDEM_ID_MINIMO:
                print('-> Vendendo em alta')
                status = 'VENDIDO'
                quantia_venda = verifica_carteira(
                    qtd_ids_carteira, ORDEM_ID_MINIMO)
                ordem_de_venda(valor_final, quantia_venda)
            else:
                print('\n-> Carteira não possui IDS suficientes')
    if ratio <= 0.98:
        print('\nMédia: ', ratio)
        print('Data: ', date_result)
        if status != 'COMPRADO' or ratio < 0.8:
            qtd_brl_carteira = quantia_brl_carteira()
            if qtd_brl_carteira >= ORDEM_BRL_MINIMO:
                print('-> Comprando em baixa')
                status = 'COMPRADO'
                quantia_compra = verifica_carteira(
                    qtd_brl_carteira, ORDEM_BRL_MINIMO)
                ordem_de_compra(quantia_compra)
            else:
                print('\n-> Carteira não possui BRL suficientes')


if __name__ == '__main__':
    iniciar()
