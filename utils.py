from json import loads

def get_credentials():
    config = '{"ACCESS_KEY": "ACCESS_KEY_AQUI","SECRET_KEY": "SECRET_KEY_AQUI"}'
    try:
        return loads(open('credentials.json', 'r').read())
    except:
        f = open('credentials.json', 'a')
        f.write(config)
        f.close()
        print('Arquivo credentials.json criado, adicione as credenciais da NovaDax')
        exit()

def verifica_carteira(quantia_carteira, quantia_minima):
    if quantia_carteira > quantia_minima:
        return quantia_minima
    else:
        return quantia_carteira