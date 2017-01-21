# tar in informationen om temperaturerna över åren användaren vill använda sig av och 
# beräknar medeltemperaturen för varje år samt bestämmer högsta temperaturen för varje år och högsta temperaturen för alla år
#
# @author Lovisa Colérus
# 2015
#
def temperaturMedel(antalÅr):
	# sätter lägsta värdet på AHT eftersom vi inte kan ha temperaturer under absoluta nollpunkten
	AHT = -300
	lsÅr = []
	lsMånad = []
	HTÅLista = []
	gns = []
	
	antalÅrUppr = 0
	# körs lika många gånger som antalet år användaren vill mata in
	# tar in information om varje år och beräknar genomsnittet, HTÅ och AHT
	while antalÅrUppr < antalÅr:
		år = int(input("Vilket är år nr %d?: " %(antalÅrUppr+1)))
		lsÅr.append(år)
		lsMånadtemp = []
		HTÅ = -300
		månadUppr = 0
		årUppr = 0
		antalÅrUppr = antalÅrUppr+1
		# Låter användaren skriva in varje månads medeltemperamur
		for månadUppr in range(12):
			månadUppr = månadUppr+1
			temp = int(input("månad %d: " %månadUppr))
			lsMånadtemp.append(temp)
			
			# ändrar HTÅ för att den ska vara högsta för ett år
			if temp > HTÅ:
				HTÅ = temp
			# ändrar AHT till att vara det största av HTÅ	
			if HTÅ > AHT:
				AHT = HTÅ
		
		# lägger till alla HTÅ-värden i en lista för att ??
		#HTÅLista.append(HTÅ)
		
		# beräknar årets genomsnittstemperatur
		genomsnitt = sum(lsMånadtemp)/12
		
		# lägger till i en lista för utskriftens skull
		gns.append(genomsnitt)
		lsMånad.append(lsMånadtemp)
		
	årUppr = 0
	# skriver ut alla år och månader med temp och genomsnittlig temp per år samt vilka som är HTÅ och AHT
	for i in lsÅr:
		print("År %d" %i)
		
		for månadUppr in range(12):
			print("månad %d:" %(månadUppr+1), "%d" %lsMånad[årUppr][månadUppr], end=" ")
			
			if lsMånad[årUppr][månadUppr] == AHT:
				print("(AHT)", end = "")
				
			if lsMånad[årUppr][månadUppr] == HTÅLista[årUppr]:
				print("(HTÅ)")
			else:
				print()
				
		print("Genomsnitt för året är %d" %gns[årUppr])
		print("")
		årUppr = årUppr+1

# tar in antalet år användaren vill mata in som ett heltal
antalÅr = int(input("Hur många år vill du mata in? "))
		
# kör funktionen med den input användaren gett	
temperaturMedel(antalÅr)	
		