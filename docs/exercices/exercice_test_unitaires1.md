# Exercice Test unitaires

# Pour la file, les tests à trouver pour les cas d'utilisations suivants : 
File doit avoir / faire.

- Constructeur
	- Création avec une longueur définie
	- Création sans limite -> on peut insérer jusqu'à l'explosion.
	- Création d'une File avec un tableau ex. 1 2 3 4 5 doit sortir en ligne 1 2 3 4 5
	  De facto, le premier à sortir est la valeur à l'index 0.
	- N'est pas permise une telle abération zigotienne que de faire une file de
	  longueur 0.
	  -> Donc, un tableau null ou de longueur 0 proscrit.

- Opérations

	- Enfiler à la fin de la file d'attente
		- Si la file est pleine -> InvalidOperationException("file pleine");
		- Si la file est pleine.... mais de longueur non définie...
		- Si la file est défini à partir d'un tableau.... 

	- Défiler
		- Retirer/effacer l'élément au début de la File
		- Retourne l'élément retiré
		- Défiler une file vide -> InvalidOperationException("file vide");

	- Observer
	    - Retourne le premier élément. Sans effacer de la File
		- Observer une file vide -> InvalidOperationException("file vide");

	- Reinitialiser 
		- Retirer toutes les données de la file
		- Ne retourne rien

Accesseurs 

	- Taille de la file
	- Nombre d'éléments dans la file
	- Vide ? booléen
	- Pleine ? booléen.

## Définition des tests    
Définition des test pour la classe File  

// ----------- Constructeurs -------------------//

Constructeur avec un parametre de taille. 

	  Je dois tester que :  
	- * Une taille négative ou de longueur 0 doit lancer ArgumentOutOfRangeException  
	- Pour une file crée de taille N la propriété capacité doit être de N  
	- La propriété vide doit être true  
	- La propriété pleine doit être false  
	- Le nombre d'élément doit être 0   
	- La propriété infinie doit être false  
	
Constructeur avec un parametre tableau (capacité == longueur du tableau)

	  Je dois tester que :  
	- * Passer un tableau null lance ArgumentNullException  
	- * Passer un tableau avec une longueur de 0 doit lancer ArgumentException  
	- La file doit avoir capacité N pour un tableau de N de long  
	- Le nombre d'éléments pour un tableau de N de long doit être de N  
	- La propriété vide est à false  
	- La propriété pleine est à true  
	- La propriété infinie est à false  
	- Observer retourne l'élément au tableau[0]  
	- La modification de tableau[0] après le new de la file ne change pas la valeur  
	  retourné par Observer();  
	  
Constructeur sans paramètre (noter : capacité infinie)

	  Je dois tester que :
	- La propriété vide doit être true
	- La propriété pleine doit être false
	- Le nombre d'élément doit être 0 
	- La propriété infinie doit être true
	  

// ----------- Méthodes -----------//

Pour une file de longueur définie  
File vide

	- Ajouter un élément change l'état de la file de la façon suivante :
	- Vide devient false
	- Pleine reste false
	- Nombre d'élément == 1
	- Observer retourne l'élément Enfilé
	- Infini est à false
	- La capacité ne change pas.
	
File pas vide

	- Le nombre d'élément devient nombre d'élément + 1
	- capacité change pas
	- plein est faux
	- vide est faux
	- infini est faux
	- observer retourne le premier élément d'origine. (après création : pour tester que l'insertion n'est pas inversé)

File presque pleine -> nombre d'élément == capacité - 1  

	- Le nombre d'élément devient nombre d'élément + 1
	- capacité change pas
	- plein devient true
	- vide reste faux
	- infini reste faux
	- observer retourne le premier élément d'origine. (après création : pour tester que l'insertion n'est pas inversé)

File pleine

	- Ajouter un élément dans une file pleine lance InvalidOperationException

File infinie 

	- Nombre d'élément : 0
    - Plein : false
    - Vide : True
    - Capacité : -1
    - On peut insérer un nombre conséquent (10k éléments) et vérifier que ça fonctionne bien.
  

Défiler

File pleine

    - Observer retourne X
	- Défiler retourne X et observer subséquemment retourne le prochain.
	- Nombre d'élément = nombre d'élément -1
	- capacité change pas
	- vide false
	- plein passe de true à false

File vide

	- Lance InvalidOperationException

   ~50% plein

    - Observer retourne X  
	- Défiler retourne X et observer subséquemment retourne le prochain.  
	- Nombre d'élément = nombre d'élément -1  
	- capacité change pas  
	- vide est à false   
	- infini reste true si c'est file infinie, sinon reste à false.  