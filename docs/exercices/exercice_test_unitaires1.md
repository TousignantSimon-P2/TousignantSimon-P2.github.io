# Exercice Test unitaires

# Pour la file, les tests à trouver pour les cas d'utilisation suivants : 
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