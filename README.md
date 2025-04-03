# Progetto-Uni-Sistemi-Informativi-SGI-
Progetto di fine corso
Ho iniziato prendendo come base un progetto fatto in aula sulla sentiment analisis e modificandolo.
-Ho lasciato invariato run_pipeline ( dato che richiama solamente le varie funzioni non è stato necessario modificarla.)
-Load_data.py:
dopo aver caricvato le varie librerie apriamo la funzione load_data in qui:
Leggiamo il nostro file togliamo la prima colonna (trattandosi di un indice) e lo inseriamo all'interno del nostro database.

-preprocess.py:
dopo aver importato le diverse librerie cominciamo con la funzione:
Ho lasciatop questa fuinzione più che altro per possibiliutà di ampiamento future Noi avendo solo dati qualitativi ed utilizzando una Random Forest come modello non necessitiamo di Preprocessing. Hop comunque controllato lòa preesenta dio collinearità tra le variabili al'interno del file Controllo Multicollinearità.ipynb e unico dato che attirava l'attenzione era la Latitudine ma dato che non era esageratamente Preoccupante ed era una delle covariate da utilizzare nell'esercizio ho voluto tenerla.

-make_model.py:
In questo file creaiamo in se per se il modello. 