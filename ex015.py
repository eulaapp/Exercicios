km_percorridos = float(input('Informe a quantidade de km percorridos: '))
quantidade_dias = int(input('Informe a quantidade de dias que o carro foi alugado: '))

preco_pagar = float((quantidade_dias * 60) + (km_percorridos * 0.15))

print(f'O valor a pagar é de R${preco_pagar}')