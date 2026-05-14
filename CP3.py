temperaturas = [
    [28, 31, 34, 33], #sala 1
    [25, 27, 29, 28],  #sala 2
    [32, 35, 36, 34],  # sala 3
    [24, 26, 25, 27] # sala 4
    ]


maior_criticos = -1
sala_maior_risco = 0

num_sala = len(temperaturas)
num_medicoes = len(temperaturas[0])


for i in range(num_sala):
    soma_sala = 0
    contador = 0
    

    for j in range(num_medicoes):
        soma_sala = soma_sala + temperaturas[i][j]
        if temperaturas[i][j] >= 33:
            contador = contador + 1
    
    media_sala = soma_sala / num_medicoes
    

    print(f"Sala {i + 1}")
    print(f"Média: {media_sala}")
    print(f"Registros críticos: {contador}")
    print() # Linha em brancos para separar as sala
    
   
    if contador > maior_criticos:
        maior_criticos = contador
        sala_maior_risco = i + 1


print(f"Sala com maior risco: Sala {sala_maior_risco}")
