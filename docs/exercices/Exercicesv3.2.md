# Exercices v3.2

Changez votre identifiant git pour Victo-[votreDA]
Important de se conformer aux standards

Vous devez utiliser git. 1 commit / push par exercice QUI FONCTIONNE
Commentaire requis lors du push

## Conventions et Bonnes Pratiques

### Majuscules / Minuscules

En P1, vous avez utilisé des minuscules pour le nom des méthodes. Fred vous a habitué à cela pour éviter la confusion entre le nom des classes et les méthodes.

En C# le standard est que les **Classes** et les **Méthodes** ont des noms commençant par une lettre **Majuscule**.

**Exemple :**
```csharp
Console.WriteLine
Random rnd = new Random();
rnd.Next();
```
`WriteLine`, `Next` ont des majuscules.

### Documentation (Commentaires)

Vous devez utiliser `//` pour les commentaires simples.
Vous devez utiliser `/*` et `*/` pour ouvrir et fermer un commentaire de plusieurs lignes.

#### Summary

Vous devez faire des summarys en haut de chaque classe, constructeur et méthode.
Vous tapez votre entête de méthode avec les bons noms de paramètres et type de retour. Ensuite, en haut de la méthode, tapez `///`.

**Exemple :**

```csharp
    /// <summary>
    /// Cette classe contient des exemples de documentation.
    /// </summary>
    public class ExempleDocumentation
    {
        /// <summary>
        /// Additionne deux nombres entiers.
        /// </summary>
        /// <param name="a">Le premier nombre à additionner.</param>
        /// <param name="b">Le deuxième nombre à additionner.</param>
        /// <returns>La somme des deux nombres.</returns>
        /// <exception cref="ArgumentException">Le résultat de l'addition dépasse la capacité d'un entier.</exception>
        public int Additionner(int a, int b)
        {
            // Vérifier si le résultat de l'addition dépasse la capacité d'un entier.
            if ((a > 0 && b > int.MaxValue - a) || (a < 0 && b < int.MinValue - a))
            {
                throw new ArgumentException("Le résultat de l'addition dépasse la capacité d'un entier.");
            }

            // Effectuer l'addition et retourner le résultat.
            return a + b;
        }
    }
```

Les summary servent à documenter le code, à savoir à quoi sert le bloc de code.
Il permet de savoir ce qui est valide comme paramètre (exemple `random.Next(2,5)`, est-ce que le 5 est inclusif ou exclusif).
Il permet de bien faire les tests, si le summary dit que c'est entre 0 et 10 inclusif. Alors les tests doivent se faire en fonction que les paramètres sont entre 0 et 10 inclusif.

**Les summarys sont maintenant essentiels et obligatoires pour Programmation 2.**

### Signature de méthode

Une **signature** est un mot qui désigne le type de retour, le nom de la méthode et les types des paramètres qui lui sont passés.

**Exemple :** la ligne suivante : `int a = Calculer(2,3)`
La signature de la méthode `Calculer` est `"int Calculer(int,int)"`.
La méthode retourne un `int`, elle s'appelle `Calculer` et elle reçoit 2 `int` en paramètre.

Le nom des variables, c'est à vous de les définir.

### Visibilité

Pour l'instant, toutes les méthodes et les attributs se veulent **publics**.

---

## Exercices - Semaine 1-2

Faites une classe "RevisionP1" avec une méthode au niveau `static` pour chacun des exercices suivants:

### Exercice 1

*   **Signature** : `void Exercice1()`
*   **La méthode doit** :
    *   Afficher "Allô p2";

### Exercice 2

*   **Signature** : `void Exercice2(int,int)`
*   **La méthode doit** :
    *   Afficher
        *   "premier entier : [le nombre 1]"
        *   "deuxième entier : [le nombre 2]"

### Exercice 3

*   **Signature** : `int Exercice3(int,int)`
*   **La méthode doit** :
    *   Prendre les deux nombres
    *   Les additionner
*   **La méthode retourne** :
    *   Le résultat du premier nombre et du deuxième
    *   \* Aucun affichage dans la méthode

### Exercice 4

*   **Signature** : `int Exercice4()`
*   **La méthode doit** :
    *   Demander à l'utilisateur un nombre
*   **La méthode retourne** :
    *   Le nombre
    *   \*On assume que l'utilisateur n'entre pas autre chose qu'un nombre

### Exercice 5

*   **Signature** : `int Exercice5()`
*   **La méthode doit** :
    *   Demander à l'utilisateur un nombre
    *   Valider que c'est un nombre supérieur à 0
*   **La méthode retourne** :
    *   -1 si le nombre n'est pas un nombre OU
    *   que le nombre est inférieur à 0 OU
    *   que l'utilisateur n'a fait que "entrer sans rien entrer"

### Exercice 6

*   **Signature** : `int Exercice6()`
*   **La méthode doit** :
    *   Demander à l'utilisateur un nombre tant que le nombre n'est pas un nombre supérieur à 10
*   **La méthode retourne** :
    *   Le nombre valide.

### Exercice 7

*   **Signature** : `int Exercice7(int,int)`
*   **La méthode doit** :
    *   Faire la division du premier par le deuxième nombre
*   **La méthode retourne** :
    *   0 si la division est par 0
    *   Le résultat de la division

### Exercice 8

*   **Signature** : `int[] Exercice8(int)`
*   **La méthode doit** :
    *   Générer un tableau d'une longueur passée en paramètre initialisé à 0
*   **La méthode retourne** :
    *   Le tableau généré à 0 de la longueur passée en paramètre

### Exercice 9

*   **Signature** : `int[] Exercice9(int,int,int)`
*   **La méthode doit** :
    *   Générer un tableau de longueur égale au premier entier
    *   Le tableau doit être rempli d'un ensemble de données aléatoire entre la valeur du deuxième paramètre et du troisième paramètre
    *   Les données ne doivent pas comprendre le troisième paramètre.
*   **On assume que** :
    *   Le 2ème paramètre est toujours inférieur au 3ème.

### Exercice 10

*   **Signature** : `int[] Exercice10(int,int,int)`
*   **La méthode doit** :
    *   Générer un tableau de longueur égale au premier entier
    *   Le tableau doit être rempli d'un ensemble de données aléatoire entre la valeur du deuxième paramètre et du troisième paramètre
*   **On assume que** :
    *   Les données **PEUVENT CONTENIR** le troisième paramètre.
    *   Le 2ème paramètre est assumé comme inférieur au 3ème paramètre.

### Exercice 11

*   **Signature** : `int[] Exercice11(int,int,int)`
*   **La méthode doit** :
    *   Générer un tableau de longueur égale au premier entier
    *   Le tableau doit être rempli d'un ensemble de données aléatoire entre la valeur du deuxième paramètre et du troisième paramètre
    *   Les données **PEUVENT CONTENIR** le troisième paramètre.
*   **On assume que** :
    *   Le 3ème paramètre peut-être inférieur au 2ème et on doit pallier pour l'erreur.

### Exercice 12

*   **Signature** : `int[] Exercice12(int,int,int)`
*   **La méthode doit** :
    *   Générer un tableau de longueur égale au premier entier
    *   Le tableau doit être rempli d'un ensemble de données aléatoire entre la valeur du deuxième paramètre et du troisième paramètre
    *   Les données **PEUVENT CONTENIR** le troisième paramètre.
*   **On assume que** :
    *   La méthode peut-être appelée avec un premier paramètre négatif, dans lequel cas on retourne un tableau `null`.
    *   Le deuxième paramètre peut être négatif.
    *   Le deuxième paramètre peut, ou non, être inférieur ou égal au troisième.
    *   La méthode gère l'inversion des paramètres si `min > max`.

### Exercice 13

*   **Signature** : `int Exercice13(int[])`
*   **La méthode doit** :
    *   Retourner la somme de tous les nombres dans le tableau de `int`.
    *   Utiliser la boucle `for`.

### Exercice 14

*   **Signature** : `int Exercice14(int[])`
*   **La méthode doit** :
    *   Retourner la somme de tous les nombres dans le tableau de `int`.
    *   Utiliser la boucle `foreach`.

### Exercice 15

*   **Signature** : `int Exercice15(int[])`
*   **La méthode doit** :
    *   Retourner la somme de tous les nombres dans le tableau de `int`.
    *   Utiliser la boucle `while`.

### Exercice 16

*   **Signature** : `int Exercice16(int[])`
*   **La méthode doit** :
    *   Retourner la somme de tous les nombres dans le tableau de `int`.
    *   Utiliser la boucle `do while`.

### Exercice 17

*   **Signature** : `void Exercice17()`
*   **La méthode doit** :
    *   Afficher la forme suivante:
        ```
        ***
        ***
        ***
        ```

### Exercice 18

*   **Signature** : `void Exercice18(int)`
*   **La méthode doit** :
    *   Afficher une forme similaire à la forme de l'exercice 17.
    *   À la différence que la forme a une longueur/largeur définie par le paramètre.

### Exercice 19

*   **Signature** : `void Exercice19(int)`
*   **La méthode doit** :
    *   Afficher une forme similaire à la forme de l'exercice 17.
    *   À la différence que la première boucle est un `for` et la seconde est un `while`.
*   **On assume que** :
    *   Le paramètre peut être négatif ou positif, on prend la valeur absolue si la valeur est négative.

### Exercice 20

*   **Signature** : `void Exerice20(int,int)`
*   **La méthode doit** :
    *   Afficher une forme de largeur égale au premier paramètre
    *   De hauteur du second paramètre
        ```
        *******
        *******
        *******
        ```
*   **On assume que** :
    *   Les nombres sont invalides si inférieurs à 1.
    *   La méthode affiche "impossible d'afficher parce que [mettre un message pertinent]".

### Exercice 21

*   **Signature** : `void Exercice21(int, int, char)`
*   **La méthode doit** :
    *   Afficher une forme similaire à l'exercice 19.
    *   Le paramètre `char` est le caractère à afficher.
*   **On assume que** :
    *   Les nombres sont invalides si inférieurs à 1.
    *   La méthode affiche "impossible d'afficher parce que [mettre un message pertinent]".

### Exercice 22

*   **Signature** : `void Exercice22(int,int,int,char)`
*   **La méthode doit** :
    *   Afficher une forme similaire à l'exercice 20.
    *   Le paramètre 1 est la largeur.
    *   Le paramètre 2 est la hauteur.
    *   Le paramètre 3 est le nombre de fois que la forme doit être affichée.
    *   Le paramètre 4 est le caractère à utiliser.
*   **On assume que** :
    *   Les nombres sont invalides si inférieurs à 1.
    *   Il y a une ligne vide entre chacune des formes.

### Exercice 23

*   **Signature** : `void Exercice23(int)`
*   **La méthode doit** :
    *   Afficher une forme similaire à celle-ci dont la ligne la plus longue est égale au paramètre
        ```
        *
        **
        ***
        ****
        ```
*   **On assume que** :
    *   La méthode utilise 2 boucles `for`.
    *   Le paramètre est valide.

**À partir de maintenant vous devez valider que les paramètres sont valides.**
Un message d'erreur doit être mis dans la console avec `Debug.WriteLine("le message d'erreur","le nom de l'exercice");`

### Exercice 24

*   **Signature** : `void Exercice24(int)`
*   **La méthode doit** :
    *   Afficher une forme similaire à celle-ci dont la ligne la plus longue est égale au paramètre
        ```
        ****
        ***
        **
        *
        ```
*   **On assume que** :
    *   La méthode utilise 2 boucles `while`.

### Exercice 25

*   **Signature** : `void Exercice25(int)`
*   **La méthode doit** :
    *   Afficher une forme similaire à celle-ci dont la ligne la plus longue est égale au paramètre
        ```
        ****
        ***
        **
        *
        ```
*   **On assume que** :
    *   La méthode utilise 2 boucles `do while`.

### Exercice 26

*   **Signature** : `void Exercice26(int)`
*   **La méthode doit** :
    *   Afficher une forme similaire à celle-ci dont la ligne la plus longue est égale au paramètre
        ```
        ****
        ***
        **
        *
        **
        ***
        ****
        ```
*   **On assume que** :
    *   La méthode utilise des méthodes existantes.

### Exercice 27

*   **Signature** : `string Exercice27(int)`
*   **La méthode doit** :
    *   Retourner une chaîne de caractères représentant une forme similaire à celle-ci dont la ligne la plus longue est de longueur du paramètre
        ```
            *
           * *
          * * *
         * * * *
        * * * * *
        ```
*   **On assume que** :
    *   La méthode utilise des boucles `for`.
    *   Qu'il n'y a pas d'espace inutile avant OU après les `*`.

### Exercice 28

*   **Signature** : `double Exercice28(int[])`
*   **La méthode doit** :
    *   Faire la moyenne des nombres dans le tableau.
*   **On assume que** :
    *   Le tableau peut-être `null` ou non `null`.
    *   Être de longueur `>=` à 0.

### Exercice 29

*   **Signature** : `double Exercice29(int[])`
*   **La méthode doit** :
    *   Calculer la moyenne.
    *   Reprendre chacun des nombres du tableau en paramètre et pour chacun des nombres:
        *   Calculer la différence à la moyenne.
        *   Si la différence est négative, la rendre positive.
        *   Faire la moyenne de ces différences.

    **Exemple :**
    Tableau d'origine : `1 2 3 -5 8 3`  
    La moyenne est de `2`  
    Pour chacun des nombres, la différence à la moyenne est de  
    `-1 (1-2) | 0 (2-2) | 1 (3-2) | -7 (-5-2) | 6 (8-2) et 1 (3-2)`  
    { -1, 0, 1, -7, 6, 1 }  
    On prend la valeur absolue de chacun des nombres  
    { 1, 0, 1, 7, 6, 1 }   
    On calcule la moyenne : 2.666...  
    En moyenne les nombres sont à 2.666 de la moyenne.  

---

## INTRODUCTION À L'ORIENTÉ OBJET

À partir de maintenant, nous allons introduire des structures de données (Classes) pour grouper les informations.
Vous continuerez à pratiquer la logique (boucles, tableaux) mais en manipulant \*parfois\* ces objets.

### Exercice 30

*   Faites une classe `Personne` dans un fichier `Personne.cs`.
*   **La classe contient** :
    *   Les membres suivants:
        *   `+nom:String`
        *   `+prenom:String`
        *   `+age:int`
    *   Le constructeur contient les 3 éléments en paramètres.
    *   Une méthode `Vieillir()` qui ajoute 1 année à la personne.

### Exercice 31 (Génération de données)

*   **Signature** : `Personne[] Exercice31(int, int, int, string[], string[])`
*   **Paramètres** :
    *   Le premier `int` est le nombre de personne qu'on veut générer.
    *   Le 2ème `int` est l'âge minimum des personnes à générer.
    *   Le 3ème `int` est l'âge maximum des personnes à générer.
    *   Le 1er tableau de `string` est un tableau de prénom.
    *   Le 2ème tableau de `string` est un tableau de nom.
*   **La méthode doit** :
    *   Retourner un tableau de personne.
    *   Le nombre de personnes défini dans les paramètres.
    *   L'âge est aléatoire entre les 2 nombres passés en paramètre (inclusif).
    *   Le nom et le prénom sont choisis aléatoirement dans les 2 tableaux de `string`.

### Exercice 32 (Moyenne d'âge)

*   **Signature** : `double Exercice32(Personne[])`
*   **La méthode doit** :
    *   Calculer la moyenne d'âge des personnes dans le tableau.

### Exercice 33 (Le Doyen)

*   **Signature** : `Personne Exercice33(Personne[])`
*   **La méthode doit** :
    *   Trouver la personne la plus âgée du tableau.
*   **La méthode retourne** :
    *   L'objet `Personne` complet qui est le plus âgé (le premier trouvé si égalité).

### Exercice 34 (Swap - Retour aux entiers)

*   **Signature** : `void Exercice34(int[], int, int)`
*   **La méthode doit** :
    *   Échanger la position des nombres aux index paramètre 2 et paramètre 3.
    *   `{5, 10, 15, 20, 25, 30}` avec les paramètres 0 et 3 vont renvoyer
    *   `0   1   3   2   3   4` (ce commentaire est un peu confus, je le laisse tel quel)
    *   `{25, 10, 15, 20, 5, 30}`
*   **On assume que** :
    *   \*Rappel : À partir de l'exercice 23 vous devez valider vos paramètres.

### Exercice 35

*   **Signature** : `void Exercice35(int[])`
*   **La méthode doit** :
    *   Inverser tout le tableau.
    *   Le premier élément devient le dernier.
    *   Le 2ème élément devient l'avant-dernier.
    *   etc.
*   **On assume que** :
    *   \*Rappel : À partir de l'exercice 23 vous devez valider vos paramètres.

### Exercice 36

*   **Signature** : `void Exercice36(int[])`
*   **La méthode doit** :
    *   Prendre la première moitié du tableau et la substituer à la seconde.
    *   **Exemple 1 :** `{1, 2, 3, 4, 5, 6}` devient `{4, 5, 6, 1, 2, 3}`.
    *   **Exemple 2 :** `{1, 2, 3, 4, 5}` devient `{4, 5, 3, 1, 2}`.

### Exercice 37

*   **Signature** : `int Exercice37(char[], char)`
*   **La méthode doit** :
    *   Trouver le caractère passé en paramètre dans le tableau.
*   **La méthode retourne** :
    *   L'index du caractère si trouvé, autrement -1.

### Exercice 38

*   **Signature** : `int Exercice38(int[])`
*   **La méthode doit** :
    *   Trouver dans le tableau s'il y a un doublon (un nombre en double).
*   **La méthode retourne** :
    *   L'index de la première occurrence d'un nombre qui est répété ailleurs dans le tableau.
    *   Si le tableau n'a pas de doublon on retourne -1.
    *   **Exemple :** `{1,2,3,*4,5,*4,5,6,6}`
    *   retourne 3 parce que 3 est l'index du premier 4 et, 4 et 4 sont les premiers doublons.

### Exercice 39

*   **Signature** : `int[] Exercice39(int[])`
*   **La méthode doit** :
    *   Trouver les index de tous les doublons et les mettre dans un tableau.
    *   **Note :** dans un tableau de 2 de longueur : Combien au maximum de doublons peut-il y avoir ?
    *   Dans un tableau de 4, au maximum combien de doublon peut-il y avoir ?
*   **La méthode doit retourner** :
    *   Un tableau contenant tous les index des premières occurrences des nombres dupliqués.

### Exercice 40 (Fusion simple)

*   **Signature** : `int[] Exercice40(int[], int[])`
*   **La méthode doit** :
    *   Fusionner les 2 tableaux dans un nouveau tableau créé.
*   **La méthode doit retourner** :
    *   Un tableau qui contient les éléments des 2 tableaux passés en paramètre.
    *   **Exemple :** Les tableaux en paramètre `{1,2,3}` et `{4,5,6}`.
    *   Le tableau de sortie doit être de longueur 6 et contenir `{ 1, 2, 3, 4, 5, 6 }`.

### Exercice 41

*   **Signature** : `int[] Exercice41(int[])`
*   **La méthode doit** :
    *   Faire la somme des éléments pairs et impairs.
*   **La méthode doit retourner** :
    *   Un tableau d'une longueur de 2 dont le premier index contient la somme des nombres pairs et le second index la somme des éléments impairs.

### Exercice 42

*   **Signature** : `int[] Exercice42(int)`
*   **La méthode doit** :
    *   Faire la création d'un tableau de longueur du paramètre.
    *   Doit faire un palindrome numérique pour remplir le tableau.
*   **La méthode retourne** :
    *   Un palindrome pour remplir un tableau de longueur du paramètre.
    *   **Exemple :** `Exercice(11)` retourne `{0,1,2,3,4,5,4,3,2,1,0}`.
    *   **Exemple 2 :** `Exercice(10)` retourne `{0,1,2,3,4,4,3,2,1,0}`.

### Exercice 43

*   **Signature** : `void Exercice43(int[], int)`
*   **La méthode doit** :
    *   Faire le décalage du tableau vers la droite (les éléments de gauche deviennent 0).
*   **La méthode retourne** :
    *   Rien.
    *   **Exemple :** `Exercice43(5)` avec `{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}`.
    *   Le tableau devient `{0,0,0,0,0,1,2,3,4,5,6,7,8,9,10}`.

### Exercice 44

*   **Signature** : `int[] Exercice44(int[],int)`
*   **La méthode doit** :
    *   Faire la même chose que l'exercice 43, mais les informations qui "disparaissent du tableau" doivent être placées dans un tableau de sortie.
*   **La méthode retourne** :
    *   Un tableau de longueur du 2ème paramètre qui contient les exclus du tableau.
    *   **Exemple :** avec le paramètre `5` et le tableau `{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}`.
    *   Le tableau de travail devient `{0,0,0,0,0,1,2,3,4,5,6,7,8,9,10}`.
    *   Le tableau retourné est `{11,12,13,14,15}`.

### Exercice 45

*   **Signature** : `int[] Exercice45(int[],int)`
*   **La méthode doit** :
    *   Faire la rotation des nombres dans le tableau pour une longueur équivalente au paramètre (les éléments qui sortent à droite reviennent à gauche).
*   **La méthode retourne** :
    *   Rien (probablement `void` ici, le `int[]` dans la signature est peut-être une erreur de frappe dans le texte original).
    *   **Exemple :** avec `5` et `{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}`.
    *   Le tableau devient `{11,12,13,14,15,1,2,3,4,5,6,7,8,9,10}`.

### Exercice 46 (Tableau de fréquence)

*   **Signature** : `int[] Exercice46(int[])`
*   **La méthode doit** :
    *   Créer un tableau de longueur égale à l'élément le plus grand du tableau + 1 case pour le 0.
    *   Compter combien il y a de duplicata des nombres dans le tableau.
*   **On assume que** :
    *   Le tableau ne contient que des entiers positifs et inférieurs à 200.
*   **Exemple :** `{1, 2, 1, 3, 2, 4}` doit retourner `{0,2,2,1,1}`.
    *   il n'y a aucun 0 -> `{0,`
    *   il y a 2 "1" -> `{0,2,0,0,0}`
    *   il y a 2 "2" -> `{0,2,2,0,0}`
    *   il y a 1 "3" -> `{0,2,2,1,0}`
    *   il y a 1 "4" -> `{0,2,2,1,1}`

### Exercice 47

*   **Signature** : `int Exercice47(int[])`
*   **La méthode doit** :
    *   Trouver l'élément unique dans le tableau s'il y en a 1.
*   **La méthode retourne** :
    *   -1 si aucun élément trouvé (ou si impossible à trouver).
    *   L'index de l'élément unique.
    *   **Exemple :** `{1,2,3,2,1}` retourne `2` parce que `3` est unique et à l'index `2`.

### Exercice 48 (Fibonacci)

*   **Signature** : `int[] Exercice48(int)`
*   **La méthode doit** :
    *   Faire un tableau de longueur du paramètre.
    *   Le tableau doit démarrer avec 0 et 1.
    *   Le 3ème élément est calculé en additionnant les nombres aux index 0 et 1.
    *   Le 4ème élément est calculé en additionnant 1 et 2.
    *   Le 5ème élément est calculé en additionnant 2 et 3.
    *   etc.
*   **La méthode retourne** :
    *   Une suite de Fibonacci d'une longueur passée en paramètre.
    *   **Exemple :** `Exercice48(10)` retourne `{0,1,1,2,3,5,8,13,21,34}`.

### Exercice 49 (Fusion triée)

*   **Signature** : `int[] Exercice49(int[],int[])`
*   **La méthode doit** :
    *   Fusionner les deux tableaux dans un seul.
    *   Le tableau fusionné doit être en ordre.
*   **La méthode retourne** :
    *   Un tableau de longueur égale à la longueur des 2 tableaux d'origine.
    *   Le tableau est trié lorsque sorti.
*   **On assume que** :
    *   Les tableaux sont triés.
    *   **Exemple :**
        *   `{1,3,5}` et `{2,4,6}`
        *   `{0,0,0,0,0,0}` //création du tableau de 6 (3+3)
        *   `{1,0,0,0,0,0}` // 1 du tableau 1 est inférieur à 2 du tableau 2
        *   `{1,2,0,0,0,0}` // 2 du tableau 2 est inférieur à 3 du tableau 1
        *   `{1,2,3,0,0,0}` // 3 du tableau 1 est inférieur à 4 du tableau 2
        *   `{1,2,3,4,0,0}` // 4 du tableau 2 est inférieur à 5 du tableau 1
        *   `{1,2,3,4,5,0}` // 5 du tableau 1 est inférieur à 6 du tableau 2
        *   `{1,2,3,4,5,6}` // 6 du tableau 2 est le seul élément restant.
    *   \*Indice : vous allez avoir besoin de 3 curseurs/index/compteurs :
        *   1 pour chaque tableau.
        *   où allez-vous écrire.
        *   où vous êtes rendu dans le tableau 1.
        *   où vous êtes rendu dans le tableau 2.

### Exercice 50 (Tri à bulle)

*   **Signature** : `void Exercice50(int[])`
*   **La méthode doit** :
    *   Trier avec l'algorithme du tri à bulle le tableau passé en paramètre.
*   **La méthode retourne** :
    *   Rien, le tableau est trié en place.

### Exercice 51 (Tri sélection)

*   **Signature** : `void Exercice51(int[])`
*   **La méthode doit** :
    *   Trier avec l'algorithme du tri par sélection le tableau passé en paramètre.
*   **La méthode retourne** :
    *   Rien, le tableau est trié en place.

### Exercice 52 (Tri Insertion)

*   **Signature** : `void Exercice52(int[])`
*   **La méthode doit** :
    *   Trier avec l'algorithme du tri par insertion le tableau passé en paramètre.
*   **La méthode retourne** :
    *   Rien, le tableau est trié en place.

### Exercice 53 (Tri Objet)

*   **Signature** : `void Exercice53(Personne[])`
*   **La méthode doit** :
    *   Trier le tableau de `Personne` selon l'âge (du plus petit au plus grand).
    *   Vous pouvez utiliser l'algorithme de tri de votre choix (Bulle, Sélection ou Insertion).
*   **La méthode doit** :
    *   Modifier le tableau passé en paramètre.

### Exercice 54 (Comparaison)

*   **Signature** : `int Exercice54(Personne, Personne)`
*   **La méthode doit** :
    *   Comparer deux personnes et déterminer laquelle est la plus âgée.
*   **La méthode reçoit** :
    *   Un nombre positif si la première personne est plus vieille que la seconde.
    *   Un nombre négatif si la première personne est plus jeune que la seconde.
    *   Zéro si les 2 âges sont identiques.
    *   Un nombre positif si la 2ème personne passée en paramètre est `null`.
*   **Comportement d'erreur** :
    *   Un message d'erreur via la création d'un `ArgumentNullException`.
    *   `https://learn.microsoft.com/fr-fr/dotnet/standard/exceptions/how-to-explicitly-throw-exceptions`
    *   La ligne "throw" est celle recherchée.
