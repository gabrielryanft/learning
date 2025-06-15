import urllib.request

try:
    requisicao = urllib.request.urlopen('https://gabrielryanft.github.io/gabrielgostosao/')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('O site está ascessivel.')