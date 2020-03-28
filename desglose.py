valor= float(input("Ingrese valor:"))

resto_con_quinientos= valor%500
con_quinientos= valor//500
resto_con_doscientos= resto_con_quinientos%200
con_doscientos= resto_con_quinientos//200
con_cien= resto_con_doscientos//100
resto_con_cien= resto_con_doscientos%100
resto_con_cincuenta= resto_con_cien%50
con_cincuenta= resto_con_cien//50
con_veinte= resto_con_cincuenta//20
resto_con_veinte= resto_con_cincuenta%20
con_diez= resto_con_veinte//10
resto_con_diez=resto_con_veinte%10
con_cinco= resto_con_diez//5
resto_con_cinco= resto_con_diez%5
con_dos= resto_con_diez//2
resto_con_dos= resto_con_diez%2


print ("El desglose es:", con_quinientos, "billete(s) de 500,", con_doscientos, "billete(s) de 200,", con_cien, "billete(s) de 100,", con_cincuenta, "billete(s) de 50,", con_veinte, "billete(s) de 20,",con_diez, "billete(s) de 10,", con_cinco, "billete(s) de 5,",con_dos, "billete(s) de 2 y",resto_con_dos, "billete(s) de 1.")

