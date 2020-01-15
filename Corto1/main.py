unidades = {'1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco'}
centenas = {}

def numer_to_text(n):
    text_number = ''
    for x in len(n):
        text_number = unidades[x]
    