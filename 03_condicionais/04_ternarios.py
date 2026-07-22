idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira :
  print("Voce pode dirigir")

mensagem = "Pode dirigir" if idade >= 18 and tem_carteira else "Voce nao pode dirigir"
print(mensagem)