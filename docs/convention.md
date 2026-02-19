# Convention de nommage C#


## Gardez en tête

- C# est sensible à la casse  

## Règles générales

- Pensez approche K.I.S.S.  
- Toujours : Les summarys  
- Toujours commencer une méthode par une lettre majuscule (PascalCase)  
- Toujours commencer une variable membre par _  
- Toujours garder en tête de mettre privé par défaut et public seulement si nécessaire  
- Toujours en français lorsque possible.  

## Modélisation UML

- Utilisez `«create»` pour les constructeurs.  
- Utilisez `«get»` et `«set»` pour les accesseurs (propriétés).  
- Utilisez `+«get»-«set»` pour indiquer un getter public avec un setter privé.  

## Définition des classes

- Commence par un summary  
- Comence par une majuscule  
- Doit avoir une visibilité définie  
- Aucun _ dans le nom  
- Doit être en francais  

    > :memo: ** L'ordre des choses est la suivante **  
    >  
    > - Déclaration de la classe  
    > - Déclaration des variable membres  
    > - Déclaration des constructeurs  
    > - Déclaration des méthodes  
    > - Déclaration des implémentations d'interface  
    > - Déclaration des "overrides"  
    > - Déclaration de la méthode ToString()  
    > - Déclaration des accesseurs get/set  
    > - Déclaration des variables static avec s_  



## Définition des méthodes.
- Commence par un summary  
- Comence par une majuscule  
- Doit avoir une visibilité définie  
- Aucun _ dans le nom  

## Noms des variables
- Variable membre  
    - Commence par un _ si c'Est une variable membre  
    - Casse chameau  
    - Commentaire si la variable nécessite une précision sur ces limites de valeurs, rôle, etc.  
- Variable standard  
    - Casse chameau  
    - Pas de _ dans le nom de la variable  

## Commentaires

- Nécessaire pour les entête de classe et de méthode sous la forme de summary  
