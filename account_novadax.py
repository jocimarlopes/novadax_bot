from novadax import RequestClient as NovaClient
from utils import get_credentials
def init_novadax():
    config = get_credentials()
    client = NovaClient(config['ACCESS_KEY'], config['SECRET_KEY'])
    return client

def listar_dados_moeda_id():
    client = init_novadax()
    res = client.get_ticker('ID_BRL')
    return res['data']

def ordem_de_compra(quantia):
    client = init_novadax()
    res = client.create_order('ID_BRL', 'MARKET', 'BUY', value=quantia)
    print(res)
    print('----> COMPRA \n')

def ordem_de_venda(preco_para_vender, quantia):
    client = init_novadax()
    res = client.create_order('ID_BRL', 'MARKET', 'SELL', price=str(preco_para_vender), amount=quantia)
    print(res)
    print('----> VENDA \n')
    
def quantia_ids_carteira():
    client = init_novadax()
    res = client.get_account_balance()
    ids = 0
    for item in res['data']:
        if 'ID' in item['currency']:
            print('IDs na Carteira: ', item['available'])
            ids = float(item['available'])
    return ids

def quantia_brl_carteira():
    client = init_novadax()
    res = client.get_account_balance()
    brl = 0
    for item in res['data']:
        if 'BRL' in item['currency']:
            print('BRLs na Carteira: ', item['available'])
            brl = float(item['available'])
    return brl
