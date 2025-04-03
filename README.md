# Progetto-Uni-Sistemi-Informativi-SGI-
Progetto di fine corso
Ho iniziato prendendo come base un progetto fatto in aula sulla sentiment analysis e modificandolo.
-Ho lasciato invariato run_pipeline ( dato che richiama solamente le varie funzioni non è stato necessario modificarla.)
-Load_data.py:
dopo aver caricato le varie librerie apriamo la funzione load_data in cui:
Leggiamo il nostro file togliamo la prima colonna (trattandosi di un indice) e lo inseriamo all'interno del nostro database.


-preprocess.py:
dopo aver importato le diverse librerie cominciamo con la funzione:
Ho lasciato questa funzione più che altro per possibilità di ampliamento future Noi avendo solo dati qualitativi non la utilizziamo. In realtà c'è un processo di preprocessing che facciamo, lo scaling che facciamo però nel make_model poiché è meglio farlo solo sui dati di test e questi ultimi vengono creati nel file make_model.


-make_model.py:
In questo file creiamo in se per se il modello.  grazie al file Confronto Modelli.ipynb osserviamo che anche la Random Forest ha la miglior esplicatività è anche soggetta ad overfitting e dopo aver provato a ridurre l'impatto sono giunto alla conclusione che un KNN riesca a descrivere meglio i nostri dati.
all'interno del File make_model.py facciamo:
la funzione di scaling ( fatta qui e non nel preprocessing per non dover splittare in training e test il dataset in un altra funzione che diventava inutilmente complesso),
dopodichè creiamo il modello e creiamo il modello predittivo e lo salviamo.


UI: l'interfaccia grafica di questo progetto si divide in 2 parti, le colonne di inserimento manuale di latitudine e longitudine e la mappa cliccabile. avendo latitudine e longitudine mi è venuto subito in mente che una mappa cliccabile sarebbe stato un ottimo modo per far interagire l'utente con il programma.


-config.py:
utile per inserire dati in modo che siano facilmente modificabili in futuro, per esempio se volessi modificare il nome di una tabella non serve andare a cercarla in ogni file ma basta modificarla sul config.
