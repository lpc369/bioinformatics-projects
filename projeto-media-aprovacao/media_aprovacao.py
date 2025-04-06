# Solicitar para inserir a nota 1 do aluno 
#Ler a nota 1
#Solicitar para inserir nota 2
# Ler a nota 2
#Solicitar  insirir nota 3
# Ler a nota 3
# Solicitar  insirir nota 4
# Ler a nota 4
#somar as notas e dividir por 4 para média
# Se a média > ou = a 6.0 então
# print mensagem "Aprovado"
# Senão
# print6
# mensagem "Reprovado"

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

# Calcule a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# print a média
print(f"A média do aluno é: {media}")

# o aluno foi aprovado ou reprovado?
if media >= 6.0:
    print("Aprovado")
else:
    print("Reprovado")
