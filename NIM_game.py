def partida():
	print(" ")

	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	is_computer_turn = True

	if n % (m+1) == 0: 
		is_computer_turn = False
		print("Você começa!")
	else:
		print("Computador começa!")

	while n > 0:
		if is_computer_turn:
			partida = computador_escolhe_jogada(n, m)
			is_computer_turn = False
			print("O computador tirou {} peças.".format(partida))
		else:
			partida = usuario_escolhe_jogada(n, m)
			is_computer_turn = True
			print("Você tirou {} peças.".format(partida))


		n = n - partida
	
		print("Restam apenas {} peças no tabuleiro.\n".format(n))

	if is_computer_turn:
		print("Você ganhou!")
		return 1
	else:
		print("O computador ganhou!")
		return 0


def campeonato():	
	usuario = 0
	computador = 0
	for _ in range(3):
		vencedor = partida()
		if vencedor == 1:
			usuario = usuario + 1
		else:
			computador = computador + 1
	print("Placar final: Você {} x {} Computador". format(usuario,computador))


def computador_escolhe_jogada(n, m):
	if n <= m:
		return n
	else:
		quantia = n % (m+1)
		if quantia > 0:
			return quantia
		
		return m



def usuario_escolhe_jogada(n, m):
	jogada = 0
	while jogada == 0:
		jogada = int(input("Quantas peças você vai tirar? "))              
		if jogada > n or jogada < 1 or jogada > m:
			jogada = 0
			
	return jogada


jogo = 0

while jogo == 0:
	print("Bem vindo ao jogo NIM! Escolha:")
	print(" ")
	print("1 - Para jogar uma partida isolada")
	print("2 - Para jogar um campeonato")

	jogo = int(input("Sua opção:"))
	print(" ")

	if jogo == 1:
		print("Você escolheu partida isolada")
		partida()
		break
	elif jogo == 2:
		print("Você escolheu campeonato")
		campeonato()
		break
	else:
		print("opção inválida")
		jogo = 0






