# butlletins-de-notes
Extreu els diferents fitxers individuals de notes per cada alumne a partir del fitxer PDF de notes generat per SAGA per a un grup.
Cada fitxer inclou el nom de l'alumne.

L'script necessita que hi sigui a la mateixa carpeta que el pdf amb els butlletins descarregats del SAGA. Com a sortida, ens crea una carpeta anomenada butlletins on desarà tots els diferents PDFs corresponents al butlletí de notes de cada alumne amb el format "N.Nom Cognom1 Cognom2.pdf".

Exemple:

1.Pere Abad García.pdf

2.Marta Batllori López.pdf

3.Gerard Pérez Martorell.pdf

...

 

Si s'executa per línia de comandes, admet com a paràmetre el nom del fitxer amb tots els butlletins:

    **$ python3 creabutlletins.py fitxerambbutlletins.pdf**

si no s'especifica el nom del fitxer (per exemple quan no s'executa des de línia de comades) llavors assumeix que el nom del fitxer és butlletins.pdf.

Per poder-se executar, es necessita tenir instal·lat Python3 a la màquina i el mòdul PyPDF2:

    **$ pip3 install PyPDF2**
