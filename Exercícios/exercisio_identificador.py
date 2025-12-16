salario = float (input("Qual o seu salário mensal?"))
if salario <= 3000:
        print("Seu salário é baixo.")
elif salario > 3000 and salario <= 5500:
        print ("seu salário é medio, e é bom!")
elif salario > 5500 and salario <= 10000:
        print ("Seu saário é bem alto!") 
elif salario > 10000 and salario <= 90000:
        print ("Seu salário é demasiadamente alto!")
elif salario > 90000 and salario <= 150000:
        print ("Seu salário já paga a sua vida!")
else:
        print ("Você é um ser imensuradamente abastado!") 
