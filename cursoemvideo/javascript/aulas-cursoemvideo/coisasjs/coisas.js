console.log('Teaching the world how to code'.length)// .length = conta o numero de caracteres em uma palavra, frase e etc. conta os espaços!!! rerposta = 30

console.log('Codecademy'.toUpperCase());// .toUpperCase() = deixa o texto em maiusculo. resposta = CODECADEMY

console.log('    Remove whitespace   '.trim());// .trim = tira os espaços do fim e do começo. resposta = Remove whitespace

var m = 1545.5//1545.5 é dinheiro.

console.log(m)

console.log(m.toFixed(2))// resposta = 1545.50 

console.log(m.toFixed(2).replace('.',','))// troca o ponto ('.') por virgula(',').

console.log(m.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'}))//tranforma o numero normal em um numero de dinheiro = R$ 1,545.50 ( em real)

console.log(m.toLocaleString('pt-BR', {style: 'currency', currency: 'USD'}))// em dolar.

console.log(m.toLocaleString('pt-BR', {style: 'currency', currency: 'EUR'}))//em euro

console.log(5 + 2)// = 7

console.log(5 - 2)// = 3

console.log(5 * 2)// = 10

console.log(5 / 2)// = 2.5

console.log(5 % 2)// = 1 ( o resto da divisãõ intteira.)

console.log(5 ** 2)// = 25

/*
os operadores são resolvidos igual na matematica normal(parenteses, potencia, divisão multiplicação e resto de divisão, soma subtração).
*/

var n = 3

console.log(n = n + 4)// n agora é igual a 7

console.log(n = n - 5)// já que agora o n vale 7, a resposta é = 2

console.log(n = n * 4)// 2 vezes 4 = 8

console.log(n = n / 2)// 8 dividido para 2 = 4

console.log(n = n ** 2)// 4 ao quadrado = 16

console.log(n = n % 6)// resto de 16 dividido para 5 = 4

/*
simplificando as variaveir a cima: (essa regra so vale se um valor for adicionado à propria variavel: se for por exemplo: n = x + 4 aí n vale.)
*/

console.log(n += 4)

console.log(n -= 5)

console.log(n *= 4)

console.log(n /= 2)

console.log(n **= 2)

console.log(n %= 5)

/*
como simplificar o var - ou + 1 ( precisa ser um. outro numero não comta.):
*/

console.log(n++) // (n + 1) também pode ser representado como: ++n (há diferença entre um e outro.)

console.log(n--) // (n - 1) também pode ser representado como: --n (há diferença entre um e outro.)

