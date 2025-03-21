while True:
    nota1bim = float(input("digite a nota 1 bim: "))
    if (nota1bim <= 10) and (nota1bim >= 0):
        break

 
while True:
    nota2bim = float(input("digite a nota 2 bim: "))
    if (nota2bim <= 10) and (nota2bim >= 0):
        break

while True:
    nota3bim = float(input("digite a nota 3 bim: "))
    if (nota3bim <= 10) and (nota3bim >= 0):
      break

while True:
    nota4bim = float(input("digite a nota 4 bim: "))
    if (nota4bim <= 10) and (nota4bim >= 0):
        break

media = (nota1bim + nota2bim + nota3bim + nota4bim) / 4 
print(f"sua media é {media:,.2f}")

if (media >= 5):
    print("Aluno A P R O V A D O !!!!")

elif (media >= 3):
    print("Aluno em recuperação")

else:
    print("Aluno R E P R O V A D O !!!")

print("fim do ano letivo")