# -*- coding: utf-8 -*-
#Programma 1 del progetto di Linguistica Computazionale 2020/2021
#Di Giuseppe Calabrese 599365
import sys
import nltk

print("Programma 1: \n\n")
punt = [".",":",",",";","?","!","'",'"',"(",")"] #lista punteggiatura part-of-speech tags
agg = ["JJ","JJR","JJS"] #lista aggettivi part-of-speech tags
avv = ["RB","RBR","RBS","RP"] #lista avverbi part-of-speech tags
verb = ["VB","VBD","VBG","VBN","VBP","VBZ"] #lista verbi part-of-speech tags
sost = ["NN","NNS","NNP","NNPS"] #lista sostantivi part-of-speech


def Lunghezza_Frasi(frasi): #tokenizzazione corpus,calcolo lunghezza del corpus, calcolo lunghezza e media delle frasi
	Tokens = []           #lista tokens
	N_Frasi = 0.0 			#numero totale di frasi
	Lunghezza_C = 0.0 		#lunghezza del corpus
	N_char = 0.0  			#numero di caratteri
	C_no_punt = 0.0			#lunghezza corpus - punteggiatura
	for frase in frasi: 
		tokens = nltk.word_tokenize(frase)
		Tokens += tokens
		N_Frasi += 1
		Lunghezza_C += len(tokens) #numero di tokens nel corpus
		for token in tokens:
			if token not in punt:
				char_in_word = len(token) #caratteri per parola, calcolati come lunghezza dei tokens 
				N_char += char_in_word    #totale del numero di caratteri
				C_no_punt += 1            #corpus esclusi i segni di punteggiatura
	avg_words = (N_char * 1)/(C_no_punt*1)    #calcolo lunghezza media delle parole
	avg_phrases = (Lunghezza_C*1)/(N_Frasi*1) #calcolo lunghezza media delle frasi
	return N_Frasi, Lunghezza_C, avg_phrases, avg_words, Tokens


def Ricchezza_Lessicale(tokens,length):
	L_Tokens = tokens[0:5000] #selezione primi 5000 tokens
	Vocabolario = list(sorted(set(L_Tokens))) #lista tokens diversi fra loro in ordine alfabetico
	TTR = (len(Vocabolario)*1)/(len(L_Tokens)*1)

	return Vocabolario, TTR


def Classi_Frequenza (tokens, length):
	for x in range(0,len(tokens),500):
		L_Tokens_500 = tokens[0:x+500] #lista tokens da 0 a x+500
		Voc500 = list(set(L_Tokens_500)) 
		V1 = [] #lista hapax
		V5 = [] #lista classe di frequenza 5
		V10 = [] #lista classe di freqienza 10
		for token in Voc500: #scorro il token nel vocabolario (evito le ripetizioni)
			y = L_Tokens_500.count(token) #contatore frequenza del token selezionato
			if y == 1: #hapax
				V1.append(token)
			elif y == 5: #frequenza 5
				V5.append(token)
			elif y == 10: #frequenza 10
				V10.append(token)
		print("Nel testo, considerando la sezione da 0 a", len(L_Tokens_500),"le classi hanno frequenza\n","f|V1| = ",len(V1),"\n","f|V5| = ",len(V5),"\n","f|V10| = ",len(V10),"\n")


def AVG_Frasi(PosList,N_Frasi):
	N_S = 0.0
	N_V = 0.0
	for pos in PosList:
		if pos in sost:
			N_S += 1
		elif pos in verb:
			N_V += 1
	Avg_sost = (N_S*1)/(N_Frasi*1) #media sostantivi nelle frasi
	Avg_verb = (N_V*1)/(N_Frasi*1) #media verbi nelle frasi

	return Avg_sost, Avg_verb


def POS_Annotation(frasi): #annotazione part of speech e selezione singoli POS
	TotTokensPos = [] #tutti i token morfosintatticamente annotati
	PosList = [] #lista POS tags
	for frase in frasi: #scorro le frasi
		tokens = nltk.word_tokenize(frase) #tokenizzazione frase
		tokensPos = nltk.pos_tag(tokens) #annotazione tokens della frase
		TotTokensPos += tokensPos #inserisco nella lista di tutti i i token annotati quelli annotati nel ciclo
	AnalizedTextPos = TotTokensPos
	for bigramma in AnalizedTextPos: #scorro i bigrammi nel testo analizzato
		PosList.append(bigramma[1])  #inserisco nella lista dei pos solo la seconda parte del bigramma, ovvero il Part of Speech
	return PosList


def Densita_Lessicale(N_Parole,Seq_Pos):
	N_Agg = 0.0       #totale aggettivi
	N_Avv = 0.0       #totale avverbi
	N_V = 0.0         #totale verbi
	N_S = 0.0         #totale sostantivi
	N_punt = 0.0      #totale segni di punteggiatura
	for pos in Seq_Pos: #ciclo con if innestati che conta agg, avv, verbi, sostantivi e punteggiatura
		if pos in agg:
			N_Agg += 1   #se aggettivo aggiorno numero aggettivi
		elif pos in avv:
			N_Avv += 1   #se avverbio aggiorno numero avverbio
		elif pos in verb:
			N_V += 1     #se verbo aggiorno numero verbo
		elif pos in sost:
			N_S += 1     #se sostantivo aggiorno numero sostantivi
		elif pos in punt:
			N_punt += 1
	DL = (N_Agg + N_Avv + N_S + N_V) / (N_Parole - N_punt) #calcolo densità lessicale come totale di aggettivi, verbi, nomi e avverbi del testo, dividendolo per il numero di parole meno i segni di punteggiatura
	return DL


def main (file1,file2):
	Discorso1 = open(file1, mode='r', encoding="utf-8") #apertura file 1
	Discorso2 = open(file2, mode='r', encoding="utf-8") #apertura file 2
	raw1 = Discorso1.read() #lettura file 1
	raw2 = Discorso2.read() #lettura file 2
	split_token = nltk.data.load("tokenizers/punkt/english.pickle") # creazione tokenizzatore per sentence splitting
	frasi1 = split_token.tokenize(raw1) #tokenizzazione del file1 grezzo
	frasi2 = split_token.tokenize(raw2) #tokenizzazione del file2 grezzo
	print("Discorso 1 in inglese:\n", Discorso1,"\n") #stampa del discorso 1 grezzo in inglese
	print("Discorso 2 in inglese:\n", Discorso2,"\n") #stampa del discorso 2 grezzo in inglese
	N_Frasi1, Lunghezza_C1, avg_phrases1, avg_words1, Tokens1 = Lunghezza_Frasi(frasi1) #output funzione Lunghezza_Frasi, con numero di frasi e token, lunghezza media delle frasi in token e lunghezza media parole in caratteri per discorso 1
	N_Frasi2, Lunghezza_C2, avg_phrases2, avg_words2, Tokens2 = Lunghezza_Frasi(frasi2) #output funzione Lunghezza_Frasi, con numero di frasi e token, lunghezza media delle frasi in token e lunghezza media parole in caratteri per discorso 2
	print("Output dei due testi in base al numero di frasi, di tokens, e alla media di tokens per frasi e di caratteri per parole:\n")
	print(file1,"Numero di frasi discorso 1:",N_Frasi1,"\n") 
	print(file2,"Numero di frasi discorso 2:",N_Frasi2,"\n")
	print(file1,"Numero di tokens discorso 1:",Lunghezza_C1,"\n") 
	print(file2,"Numero di tokens discorso 2:",Lunghezza_C2,"\n")
	print(file1,"Media di tokens per frase nel discorso 1:",avg_phrases1,"\n")
	print(file2,"Media di tokens per frase nel discorso 2:",avg_phrases2,"\n")
	print(file1,"Media di caratteri per parole discorso 1:",avg_words1,"\n")
	print(file2,"Media di caratteri per parole discorso 2:",avg_words2,"\n")


	#Esercizio 1: confronto del numero di frasi e tokens tra i due testi
	print("Confronto numero di frasi:\n")
	if N_Frasi1>N_Frasi2:
		print(file1,"Il discorso 1 ha più frasi: ",N_Frasi1,"\n")
	elif N_Frasi1<N_Frasi2:
		print(file2,"Il discorso 2 ha più frasi: ",N_Frasi2,"\n")
	else:
		print("I due discorsi contengono lo stesso numero di frasi. \n")

	print("Confronto numero di tokens:\n")
	if Lunghezza_C1>Lunghezza_C2:
		print(file1,"Il discorso 1 ha più tokens: ",Lunghezza_C1,"\n")
	elif Lunghezza_C1<Lunghezza_C2:
		print(file2,"Il discorso 2 ha più tokens: ",Lunghezza_C2,"\n")
	else:
		print("I due discorsi contengono lo stesso numero di tokens. \n")


	#Esercizio 2: confronto della media di tokens per frase e caratteri per parola fra i due testi
	print("Confronto della media di tokens per frase:\n")
	if avg_phrases1>avg_phrases2:
		print(file1,"Il discorso 1 ha in media più tokens per frase: ",avg_phrases1,"\n")
	elif avg_phrases1<avg_phrases2:
		print(file2,"Il discorso 2 ha in media più tokens per frase: ",avg_phrases2,"\n")
	else:
		print("I due discorsi hanno la stessa media di tokens per frase. \n")

	print("Confronto della media di caratteri per parola:\n")
	if avg_words1>avg_words2:
		print(file1,"Il discorso 1 ha in media più caratteri per parola: ",avg_words1,"\n")
	elif avg_words1<avg_words2:
		print(file2,"Il discorso 2 ha in media più caratteri per parola: ",avg_words2,"\n")
	else:
		print("I due discorsi hanno la stessa media di caratteri per parola. \n")


	#Esercizio 3: Calcolo grandezza vocabolario e ricchezza lessicale, calcolata con TTR, per i due corpus entro i 5000 tokens
	Vocabolario1, TTR1 = Ricchezza_Lessicale(Tokens1,Lunghezza_C1) #Output di vocabolario e TTR discorso 1 dato dalla funzione Ricchezza_Lessicale
	Vocabolario2, TTR2 = Ricchezza_Lessicale(Tokens2,Lunghezza_C2) #Output di vocabolario e TTR discorso 2 dato dalla funzione Ricchezza_Lessicale 
	print("Calcolo del vocabolario del discorso 1: ",Vocabolario1, "\n") #Stampa del vocabolario discorso 1
	print("Calcolo del vocabolario del discorso 2: ",Vocabolario2, "\n") #Stampa del vocabolario discorso 2
	print("Calcolo della grandezza del vocabolario del discorso 1: ",len(Vocabolario1), "\n") #Stampa grandezza del vocabolario del discorso 1
	print("Calcolo della grandezza del vocabolario del discorso 2: ",len(Vocabolario2), "\n") #Stampa grandezza del vocabolario del discorso 2

	print("Confronto fra i due vocabolari.\n") 
	if len(Vocabolario1)>len(Vocabolario2): #Confronto della grandezza del vocabolari dei 2 discorsi
		print(file1,"Il discorso 1 ha un vocabolario maggiore: ",len(Vocabolario1),"\n")
	elif len(Vocabolario1)>len(Vocabolario2):
		print(file2,"Il discorso 2 ha un vocabolario maggiore: ",len(Vocabolario2),"\n")
	else:
		print("I due discorsi hanno la stessa grandezza del vocabolario. \n")

	print("Calcolo della TTR del discorso 1 entro 5000 tokens: ",TTR1, "\n") 
	print("Calcolo della TTR del discorso 2 entro 5000 tokens: ",TTR2, "\n")
	print("Confronto fra i due vocabolari.\n")
	if TTR1>TTR2: #Confronto della grandezza della TTR dei 2 discorsi
		print(file1,"Il discorso 1 ha una maggiore ricchezza lessicale: ",TTR1,"\n")
	elif len(Vocabolario1)>len(Vocabolario2):
		print(file2,"Il discorso 2 ha una maggiore ricchezza lessicale: ",TTR2,"\n")
	else:
		print("I due discorsi hanno la stessa ricchezza lessicale. \n")


	#Esercizio 4: calcolo distribuzione delle classi di frequenza |V1|, |V5|, |V10|, dei due discorsi considerando porzioni di testo di 500 in 500
	print("Distribuzione classi di frequenza |V1|, |V5| e |V10| del testo 1, considerando porzioni di testo di 500 in 500:\n")
	Classi_Frequenza (Tokens1, Lunghezza_C1)
	print("Distribuzione classi di frequenza |V1|, |V5| e |V10| del testo 2, considerando porzioni di testo di 500 in 500:\n")
	Classi_Frequenza (Tokens2, Lunghezza_C2)


	#Esercizio 5: calcolo media di sostantivi e verbi per frase
	print("Calcolo media verbi e sostantivi per frase e confronto tra i due discorsi:\n ")
	PosList1 = POS_Annotation(frasi1) #Output lista part of speech del discorso 1
	PosList2 = POS_Annotation(frasi2) #Output lista part of speech del discorso 2
	Avg_sost1, Avg_verb1 = AVG_Frasi(PosList1, N_Frasi1) #Output media sostantivi e verbi per frase del discorso 1
	Avg_sost2, Avg_verb2 = AVG_Frasi(PosList2, N_Frasi2) #Output media sostantivi e verbi per frase del discorso 2

	if Avg_sost1>Avg_sost2: #confronto media sostantivi per frase del discorso 1 e discorso 2 (discorso 1 ne ha di più)
		print("Il discorso 1 ha una media di sostantivi per frase maggiori del discorso 2 e ")
		if Avg_verb1>Avg_verb2: #confronto media verbi per frase del discorso 1 e discorso 2 (discorso 1 ne ha di più)
			print("una media di verbi per frase maggiore del discorso 2.\n")
		elif Avg_verb1<Avg_verb2: #confronto media verbi per frase del discorso 1 e discorso 2 (discorso 2 ne ha di più)
			print("una media di verbi per frasi minore del discorso 2.\n")
		elif Avg_verb1==Avg_verb2: #stessa media di verbi per frase
			print("una ugual media di verbi per frase.\n")

	elif Avg_sost2>Avg_sost1: #confronto media sostantivi per frase del discorso 1 e discorso 2 (discorso 2 ne ha di più)
		print("Il discorso 2 ha una media di sostantivi per frase maggiori del discorso 1 e ")
		if Avg_verb2>Avg_verb1: #confronto media verbi per frase del discorso 1 e discorso 2 (discorso 2 ne ha di più)
			print("una media di verbi per frase maggiore del discorso 1.\n")
		elif Avg_verb2<Avg_verb1: #confronto media verbi per frase del discorso 1 e discorso 2 (discorso 1 ne ha di più)
			print("una media di verbi per frasi minore del discorso 1.\n")
		elif Avg_verb1==Avg_verb2:
			print("una ugual media di verbi per frase.\n")

	else:  #in questo caso hanno ugual media sia di sostantivi che di verbi per frase
		print("I due discorsi hanno ugual media di sostantivi per frase e ")
		if Avg_verb1>Avg_verb2: #confronto media verbi per frase del discorso 1 e discorso 2 (discorso 1 ne ha di più)
			print("una media di verbi per frase maggiore del discorso 2.\n")
		elif Avg_verb1<Avg_verb2: #confronto media verbi per frase del discorso 1 e discorso 2 (discorso 2 ne ha di più)
			print("una media di verbi per frasi minore del discorso 2.\n")
		elif Avg_verb1==Avg_verb2: #stessa media di verbi per frase
			print("una ugual media di verbi per frase.\n")


	#Esercizio 6: Confronto fra i due testi per densità lessicale, considerando il numero totale di occorrenze di sostantivi, verbi, avverbi e aggettivi, numero totale di tokens, escludendo i segni di punteggiatura
	print("Calcolo e confronto densita' lessicale fra i due discorsi: \n")
	DL1 = Densita_Lessicale(Lunghezza_C1, PosList1) #Output funzione per il calcolo della densita lessicale considerando il discorso 1
	DL2 = Densita_Lessicale(Lunghezza_C2, PosList2) #Output funzione per il calcolo della densita lessicale considerando il discorso 2
	if DL1>DL2: #confronto densità lessicale fra i due discorsi (discorso 1 ha maggiore densità lessicale)
		print("La densita' lessicale del discorso 1 è maggiore rispetto a quella del discorso 2.\n")
	elif DL1<DL2: #confronto densità lessicale fra i due discorsi (discorso 2 ha maggiore densità lessicale)
		print("La densita' lessicale del discorso 2 è maggiore rispetto a quella del discorso 1.\n")
	else: #confronto densità lessicale fra i due discorsi (hanno ugual densità lessicale)
		print("La densita' lessicale relativa ai due testi è di ugual valore.\n")
main(sys.argv[1], sys.argv[2])