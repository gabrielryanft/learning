def numeroInteiro(msg):
    while True:
        try:
            numero = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[31mDigite um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mInfelizmente você se recusou a preencher o bagulho.\033[m')
            return 0
        else:
            return numero
        
def numeroReal(msg):
    while True:
        try: 
            numero = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mValor invalido, tente de novo. (Digite um número por favor.)\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mInfelizmente alguém se recuso a responder o formulário.\033[m')
            return 0
        else:
            return numero