tamanhoDoArquivo = float (input ('Qual o tamanho do arquivo que deseja realizar o download? (Em MB)'))
velociade = float (input ('Qual a velocidade de download do link? (Em MBps)'))

tempoDeDownload = (tamanhoDoArquivo / velociade) / 60

print(f'Seu download demorará {tempoDeDownload} minutos')

