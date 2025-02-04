# Exercice 3 - Tri radix  
- Une fois l'exercice 2 complété : 

## Réorganisation des fichiers  
- Placez-vous dans la branche "main" et fusionnez "merge" la branche de developpement
- À partir de cette branche main -> faites une branche "Tri"
    - Réorganisez vos fichiers de façon à ce que :  
    - Dans une classe Tris il y ait -> bubble, insertion, selection et radix  
    - radix va lancer l'exception de non implémentation pour le moment.  
    - La classe Tris va être dans les namespace Outils_9999999.Tris  
    - Faites la classe OutilsTableaux et déplacez y les méthodes nécessaires.
    - Les méthodes qui ne sont pas utiles à l'extérieure de la classe doivent être "private" 
 
##  Programmation  

- Avec des méthode de niveau privé de cette classe Tri:
    - Craquez le problème ExtraireNombre(nombre, position) avec (nombre/10^pos)%10 :
    - Créer un dossier dans votre projet nommé "StructureDeDonnee"
    - Faites la classe File  
    - La classe File doit contenir :
        - Un tableau de int  
        - Une variable membre index représentant le début de file  
        - Une variable membre index représentant la fin de file
        - Un constructeur qui reçoit en paramètre une longueur.
        - Une méthode void Enfiler(int)
        - Une méthode int Defiler()
        - Une méthode int Observer()
        - Un accesseur Vide
        - Un accesseur Plein

##  
- [x] Les vérifications sanitaires doivent être faites pour chaque méthode.
- [x] Les résumés doivent être présents pour chaque méthode.
- [x] On ne laisse pas traîner d'espace blanc pour rien.
- [x] Si on a du code qui se duplique, on le factorise dans une méthode à part.
- [x] Le code dupliqué doit être factorisé.
- [x] Un "commit" par version qui compile.
