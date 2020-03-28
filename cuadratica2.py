from math import*

Coef_principal=float(input("Ingrese coeficiente principal: "))
Coef_variable_lineal=float(input("Ingrese coeficiente de variable lineal: "))
Coef_independiente=float(input("Ingrese coeficiente de variable independiente: "))
Determinante=Coef_variable_lineal**2-4*Coef_principal*Coef_independiente


if Coef_principal==0:
	if Coef_variable_lineal!=0:
		print ("El resultado es:", -Coef_independiente/Coef_variable_lineal)
	else:
		print ("El resultado es:", Coef_independiente)
else:
	if Determinante>=0:
		raiz=sqrt(Determinante)

		Resultado_1=(-Coef_variable_lineal+raiz)/(2*Coef_principal)
		Resultado_2=(-Coef_variable_lineal-raiz)/(2*Coef_principal)

		print ("Los resultados son: X1=",Resultado_1, "y X2=", Resultado_2)
	
	else:
		print ("No son raíces reales")




