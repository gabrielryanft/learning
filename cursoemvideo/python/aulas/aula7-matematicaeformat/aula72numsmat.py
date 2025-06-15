n1 = int(input('Digite um número! '))
n2 = int(input('Digite outro número! '))

so = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print('a soma ({} + {}) é = {}'.format(n1, n2, so), end=' E ')#end=''sugnifica que noi final de=a linha não vai nada(ela não vai quebrar) eu botei ' e ' então ao invés de nada 
print('a subtração ({} - {}) é = {}'.format(n1, n2, su), end=' E ')
print('a multiplicção ({} x {}) é = {}'.format(n1, n2, m), end=' E ')
print('a divisão ({} / {}) é = {:.3f}'.format(n1, n2, d), end=' E ')#na terceira chave o :.3f sifnifica que eu quero 3 casas decimaos(:.3) depois do ponto flutuante(f)
print('a divisão inteira ({} // {}) é = {}'.format(n1, n2, di), end=' E ')
print('a potencia ({} ** {}) é = {}'.format(n1, n2, p), end=' E ')