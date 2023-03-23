kg=input(("Escribe tu peso en kilogramos: "))
m=input(("Escribe tu estatura en metro:"))

imc= round(float(kg)/float(m)**2)

print("Tu indice de masa corporal(IMC) es de: " +str(imc))