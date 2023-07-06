#Calculando o imc peso sobre a altura.

peso = float(input("Digite seu peso:"))


altura = float(input("Digite sua altura:"))

imc = peso / (altura**2)
print("O seu imc é:%.2f"%imc)

if imc < 18.5:
  print("Voce esta abaixo do normal.")
elif imc >= 18.5 and imc <= 24.9:
  print("Voce esta com o peso normal")
elif imc >= 25.0 and imc <= 29.9:
  print("Voce esta com excesso de peso")
elif imc >= 30.0 and imc <= 34.9:
  print("voce esta com obesidade classe 1")
elif imc >= 35.0 and imc <= 39.9:
  print("Voce esta com obessidade classe 2")
else:
  print("Voce esta com obessidade classe 3")
