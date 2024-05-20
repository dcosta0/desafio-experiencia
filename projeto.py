seunome = input("Qual o seu nome?") #pergunta o nome
exp = eval(input("Quantos pontos de experiência você tem?")) #pergunta quanto de experiencia voce tem e transforma em um numero para calcular
nivel = 0 #variavel para dizer o nivel
if exp < 1000: #confere qual o nivel de acordo com a experiencia
    nivel = "Ferro"
elif exp >= 1000 and exp < 2000:
    nivel = "Bronze"
elif exp >= 2000 and exp < 5000:
    nivel = "Prata"
elif exp >= 5000 and exp < 7000:
    nivel = "Ouro"
elif exp >= 7000 and exp < 8000:
    nivel = "Platina"
elif exp >= 8000 and exp < 9000:
    nivel = "Ascendente"
elif exp >= 9000 and exp < 10000:
    nivel = "Imortal"
elif exp >= 10000:
    nivel = "Radiante" 
print("O Herói de nome",seunome,"está no nível",nivel)