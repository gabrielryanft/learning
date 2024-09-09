p = float(input('Preço do produto: R$'))
print('Modos de pagamento disponiveis:\n -[ 1 ] À vista/cheque: ;\n -[ 2 ] À vista no cartão: ;\n -[ 3 ] 2x no cartão: ;\n -[ 4 ] 3x ou mais no cartão: .')
r = int(input('Modo de pagamento escolhido: '))
if r == 1:
    d = p - p / 100 * 10
    print('Se você pagar à vista em dinheiro ou cheque, terá 10% de desconto. Ficando: R${:.2f}'.format(d))
elif r == 2:
    d = p - p / 100 * 5
    print('Se você pagar à vista no cartão, terá 5% de desconto. Ficando: R${:.2f}'.format(d))
elif r == 3:
    print('pagando à vista no cartão não tem desconto e nem juros. O preço fica: R${:.2f}'.format(p))
elif r == 4:
    v = int(input('Em quantas vezes você pretende pagar? '))
    d = p + p / 100 * 20
    dm = d / v
    print('Você pagará R${:.2f} todo mês durante {} meses. Preço total com juros de 20%: R${:.2f}'.format(dm, v, d))
else: print('Seu burro! Só tem 4 opções! Escolha uma delas, por favor.')