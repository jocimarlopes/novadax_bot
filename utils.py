
def create_credentials_file():
    try:
        open('credentials.json', 'r').read()
    except:
        open('credentials.json', 'w').read()

def verifica_carteira(quantia_carteira, quantia_minima):
    if quantia_carteira > quantia_minima:
        return quantia_minima
    else:
        return quantia_carteira