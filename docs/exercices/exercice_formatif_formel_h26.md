# Évaluation Formative Pratique : Système de Station Météo

## Objectif
Démontrer la compétence en encapsulation, gestion d'erreurs et architecture logicielle en C#.

---

## Mise en situation
Vous devez créer un module de gestion pour une station météo. Ce module doit valider les données de température et d'humidité avant de les traiter par le reste du système.

---

## Tâche 1 : Architecture de la Solution
1. Créez une solution Visual Studio nommée `SolutionStationMeteo`.
2. Ajoutez un projet de type **Bibliothèque de classes (.NET)** nommé `StationMeteo.Metier`.
3. Ajoutez un projet de type **Application Console** nommé `StationMeteo.App`.
4. Configurez le projet `StationMeteo.App` pour qu'il puisse utiliser les classes du projet `Metier` (Ajout de référence).

---

## Tâche 2 : Conception de la classe `CapteurMeteo`
Dans le projet `Metier`, créez la classe `CapteurMeteo` en respectant les critères suivants :

### A. Attributs (Champs privés)
- Déclarez les champs privés pour le `_nom`, la `_temperature` et l' `_humidite`. Respectez la convention de nommage C# (`_casseChameau`).

### B. Méthode de validation privée
- Créez une méthode **privée** nommée `ContientDesChiffres(string texte)` qui retourne `true` si la chaîne passée en paramètre contient au moins un chiffre, et `false` sinon.
- *Indice : Utilisez une boucle `foreach` pour tester chaque caractère avec `char.IsDigit(c)`.*

### C. Propriétés (Encapsulation)
- **`Nom`** : 
    1. Ne peut pas être nul ou vide (utilisez `string.IsNullOrWhiteSpace`).
    2. Ne doit pas contenir de chiffres (utilisez votre méthode privée `ContientDesChiffres`).
    3. Si une de ces conditions n'est pas respectée, lancez une `ArgumentException` avec un message clair.
- **`Temperature`** : Doit être **bornée** entre -60.0 et 60.0. Si la valeur reçue dépasse ces limites, ramenez-la à la limite la plus proche (ne pas lancer d'exception).
- **`Humidite`** : Doit être entre 0 et 100 %. Si la valeur est hors limite, lancez une `ArgumentOutOfRangeException`.

### D. Constructeurs
- Créez un constructeur qui accepte uniquement le `nom`.
- Créez un second constructeur qui accepte les 3 paramètres. 
- **Important :** Vos constructeurs doivent passer par les **Propriétés** (Majuscules) pour garantir que les validations s'exécutent dès l'instanciation.

---

## Tâche 3 : Utilisation dans le Main
Dans le projet `App`, instanciez les objets suivants en entourant vos appels de blocs `try-catch` appropriés :
1. Un capteur valide : `"Capteur_Nord"`, `12.5`, `45`.
2. Un capteur invalide : `"Capteur123"` (doit lever une exception à cause du chiffre).
3. Un capteur invalide : Humidité de `-10` (doit lever une exception).

---

## Tâche 4 : Gestion de versions (Git)
1. Initialisez un dépôt Git et faites un commit initial de votre structure.
2. Créez une branche nommée `test-unitaire`.
3. Dans cette branche, ajoutez une ligne dans le `Main` qui affiche le résultat de la lecture du capteur.
4. Effectuez un commit sur votre branche, puis **fusionnez** (merge) la branche dans `main`.
