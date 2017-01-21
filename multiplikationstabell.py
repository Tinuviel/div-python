# beräknar och skriver ut produkterna i en multiplikationstabell
# @author Lovisa Colérus 
# 2015

def multiplikationstabell(antalKolumner, antalRader):
	# x och y är heltal som används upprepat för att köra while-looparna
	# x används för kolumnerna och y för raderna
	x = 0
	y = 0
	
	# tre tomma listor som byggs upp i while-looparna
	kolumnSiff = []
	radSiff = []
	produktMatris = []
	
	# lägger till faktorerna i horisontellt led
	while x < antalKolumner:
		x = x+1
		kolumnSiff.append(x)
	
	# lägger till faktorerna i vertikalt led
	while y < antalRader:
		y = y+1
		radSiff.append(y)
		
	# nollställer y för att återanvända den	
	y = 0
	# går igenom varje faktor mindre än vår högsta faktor för raderna
	while y < antalRader:
		
		# skapar en tom lista som ska användas lokalt i den nästlade while-loopen
		ls = []
		# nollställer x inuti denna while-loop för att den ska återanvändas för den nästlade while-loopen
		x = 0
		# går igenom varje faktor för kolumnerna och multiplicerar den med den aktiva rad-siffran
		while x < antalKolumner:
			temp = kolumnSiff[x] * radSiff[y]
			# lägger till produkten i en temporär lista
			ls.append(temp)
			x = x+1
		# lägger till den temporära listan för att skapa en matris	
		produktMatris.append(ls)
		y = y + 1
	
	# skriver ut den översta raden med faktorer
	print("  ", "  ".join(str(x) for x in kolumnSiff))
	
	x = 0
	# skriver ut matrisen över produkterna
	for i in produktMatris:
		x = x+1
		print(x, end=" ")
		for j in i:
			print("%2d" %j, end=" ")
		print()

# tar in den högsta faktorn i multiplikationstabellens horisontella led
antalRader = int(input("Ange antal rader: "))

# tar in den högsta faktorn i multiplikationstabellens vertikala led
antalKolumner = int(input("Ange antal kolumner: "))
		
# kör funktionen med de värden användaren har fått skriva in	
multiplikationstabell(antalKolumner, antalRader)
