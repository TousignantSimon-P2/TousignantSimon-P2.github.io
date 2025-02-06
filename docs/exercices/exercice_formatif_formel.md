## Exercice formatif formel.

### Vous devez tracer votre progression en utilisant git

### Question 1 - Organisation de solution multi-projet

    - Faites une solution visual studio FormatifFormel contenant   
        - Une projet console nommé ProgramPrincipal  
        - Une bibliothèque de classes nommée FormatifFormel-9999999 (*votre DA)  

### Question 2 - Création d'une méthode

    - Faites une classe OutilsFormatifFormel avec :  
        - Une méthode statique AFaire qui prends en paramètre un tableau de string nommé phrase  
        - La méthode n'est pas implémentée.  

### Question 3 - Connexion inter-projet 
    - Faites en sorte que le programme principal puisse appeller la méthode AFaire  
    - Il est souhaité que le programme principal plante lors que la méthode est appellée.

### Question 4 - Algorithmie

    - Importez votre bibliothèque de classe pour la gestion des tableaux que vous avez faites en classe.  
    - Vous pouvez utiliser les méthodes de cette dernière pour résoudre le problème suivant :  
    - Dans la classe OutilsFormatifFormel faites l'implémentation de la méthode avec la signature string Fusion(string[])  
    - La méthode prend chacun des mots dans le tableau de tableau de string et fusionne les mots avec des espaces pour faire une phrase exemple {"Bonjour", "," "très","appréciés", "étudiants"}  
        - Particularité, si c'est une virgule, la syntaxe c'est "mot, " (mot virgule espace)  
        - Si c'est deux mots la syntaxe c'est "mot mot" (mot espace mot)  

## Question 5 - Appel avec arguments.
    - Faites les modifications nécessaires pour que la sources des mots soit passée en paramètre  
    par l'utilisateur à l'appel du programme. :  
    Exemple : ProjetConsole.exe bonjours , très chers étudiants

## Vérification et continuation
Pour les zigotos qui sont plus avancés. La liste de vérification est dans la boite cachée ci-bas.  
Si votre solution est aux normes, voici ce que vous pouvez faire. Comme à l'habitude je ne vous  
fais pas coder quelque chose pour rien...

??? "Question 7, 8 - Exigeance supplémentaire pour nourrir l'âme affamés"
    **Question 7**  
    - Faites une méthode avec la signature suivante "int[] Fusion(int[] a, int[] b)  
    - La méthode assume que les 2 tableaux sont déjà triés en ordre croissant.  
    - La méthode fusionne les 2 tableaux en 1 seul tableau :  
        - Exemple {1, 3, 5, 7, 9} et {0, 2, 4, 6, 8} va retourner un tableau contenant : {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  
        - {4, 5, 6} {1, 2, 3, 7, 8, 9} va retourner {1, 2, 3, 4, 5, 6, 7, 8, 9}  
    - Astuce : placez vous 2 curseurs: 1 sur chacun des tableaux à l'index 0 :)    
    **Question 8**  
    - Si toi, padawan expérimenté, a réussi à dominer ce problème...  
    - Voici la nouvelle méthode -> Fusion(int[] espaceDeTravail, int indexLimiteBasse, int mid, indexLimiteHaute)  
    - Définition : On ne travail plus qu'avec un tableau...  
    - Donc : tableau = {7,8,9,1,2,3} -> on appelle Fusion avec Fusion(tableau, 0, 3, 5)  
    - l'algorithme compare en premier l'index 0 et l'index 3 et interverti si nécessaire. le but est de fusionner en place et en ordre ;)  
    - le résultat reste {1, 2, 3, 7, 8, 9}  

??? "Liste de vérification"
    - Une branche de developpement 
        - git log permet de voir qu'un commit est fait pour chacune des méthodes.  
        
    - Les summarys sont présents pour chacune des classes et chacune des méthodes incluant:  
        - La description de la méthode (même pour celle "AFaire")  
        - Les paramètres sont bien définis et expliqué en ce qui attrait à leurs limite de valeurs possibles  
    - Les classes commencent par une majuscule. (Casse chameau)  
    - Les méthodes commencent par une majuscule. (Casse chameau)  
    - Toutes les variables sont en minuscule  
    - L'appel de la méthode AFaire lance l'exception "NotImplementedExeption"  
        - Un message d'erreur significatif est lancé  
    - Les vérifications sanitaires sont faites pour la chaine de paramètre pour s'assurer qu'elle n'est pas vide ni null  
    - Les dépendances entre les projets sont présentes.  
    - Les using nécessaires sont déclarés.  
    
