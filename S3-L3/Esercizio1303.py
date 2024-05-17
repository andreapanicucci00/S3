def perimetro():
	print("Questo programma calcola il perimetro di una figura geometrica")
	print("""
	-Quadrato: >>1
	-Rettangolo: >>2
	-Cerchio: >>3
	""")

	print('inserire la scelta:')
	scelta = int(input(">>> "))
	if scelta == 1:
		print("Hai selezionato il perimetro del Quadrato")
		lato = float(input('Inserire valore del lato: '))
		print("Il perimetro del quadrato, avente lato", lato, "è:", lato *4)
	elif scelta == 2:
		print("Hai selezionato il perimetro del Rettangolo")
		base = float(input('Inserire il valore della base:'))
		altezza = float(input('Inserire il valore della base:'))
		print("Il perimetro del Rettangolo di base", base, "e altezza", altezza, " è: ",base*2 + 2*altezza)
	elif scelta == 3:
		print("Hai selezionato il perimetro del Cerchio")
		r = float(input('Inserire il valore del Raggio:'))
		print("Il perimetro del Cerchio di raggio", r,"é:", 2* r* 3.14)
	else:
		print("Non hai scelto uno dei numeri sopra elencati! MALE ")



perimetro();

