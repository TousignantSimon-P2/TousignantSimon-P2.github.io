# Création des tests unitaires

- Sur la classe on ouvre les actions rapides et les refactorisations  
- Sélectionner "Créer des tests unitaires"  
![](/images/ClasseEtProjet/14.png)  

- Si aucun projet de tests, on garde les options par défaut.  
![](/images/ClasseEtProjet/15.png)  

- Faire la section summary de la classe.
- On peut se faire des variables pour se faciliter la vie. 
- Pour chaque méthode / constructeur, on fait l'analyse des points de retour (throw new, return valeur);
- On fait une méthode de test pour chacun des points de retour (pour le moment)
- Dans l'exemple on test avec un [ExpectedException] en entête de méthode. 
- La création de l'étudiant se fait avec les variables définie en entête de classe, beaucoup plus lisible, beaucoup plus rapide
![](/images/ClasseEtProjet/16.png)  

- Exemple de test d'exception fait avec un Assert.ThrowsException. Je vous suggère de casser la ligne sur plusieurs lignes.  
  Beaucoup plus facile à lire.  
     
  "J'affirme que sera lancée l'exception "ArgumentException",  
   quand sera exécutée l'instruction "new étudiant(...)"  
   faute de quoi le message d'erreur sera "L'ArgumentException non lancé sur construction avec nom == string.Empty"  
![](/images/ClasseEtProjet/17.png)  

- Test valide, confirme, via ce qui est disponible, que l'étudiant est bien créé.  
![](/images/ClasseEtProjet/18.png)  
