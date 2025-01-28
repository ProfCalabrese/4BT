# 4BT
ProgettoPokemon

0.5)Ogni studente vada nella sezione Projects e ne crei uno con il proprio nome e cognome

1.0)
Creare la classe mosse, in cui abbiamo il tipo di mossa, nome, attacco, precisione e descrizione. Di questa classe avremo solo costruttori set e get.
Creare una classe Pokemon, che presenti il numero, il nome, il tipo1, il tipo2, la razza del pokemon, psmax, psattuali, velocità.
Il Pokemon sarà anche in grado di breedare. Dato per un pokemon della stessa razza, restituirà un oggetto pokemon le cui statistiche sono la media dei due pokemon genitori.
Poi creare 3 classi "figlie" di pokemon, base, fase1 e fase2.
Ognuna di queste classi avrà un range di livello in cui è il pokemon (ad esempio un pokemon si evolve in fase1 a partire dal livello 18 e poi si evolve in fase 2 al livello 32, oppure se non vi sono ulteriori evoluzioni arriverà al 100).
Tranne la fase 2, le altre classi avranno il metodo "evolviPokemon", che creerà un oggetto della fase successiva, copiando il nome del pokemon di partenza. Ovviamente sarà possibile solo se il range non arriva al 100.
Ogni pokemon poi avrà un arraylist di massimo 4 mosse. Ogni pokemon avrà i metodi di 
- fuga: si genera un numero casuale, il numero casuale più la velocità del proprio pokemon devono superare la veocità del pokemon avversario (passata per parametro) per riuscire a fuggire
- attacca: nel quale si mostra l'elenco di mosse e si fa scegliere all'utente quale usare
- cura: usate una pozione per curare il pokemon di 50ps
- imparaMossa: si passa per parametro un oggetto mossa dato in input dall'utente e la si fa imparare al pokemon sostituendo una mossa già esistente.
- cheatMossa: si aggiunge una mossa barando e togliendo il limite delle 4 mosse
- dimenticaMossa: si mostra all'utente la lista delle mosse del pokemon e sceglie quale eliminare delle 4.
Creare un'eccezione personalizzata in impara mossa. Il pokemon deve poter imparare mosse che corrispondano solo ad uno dei suoi due tipi.
