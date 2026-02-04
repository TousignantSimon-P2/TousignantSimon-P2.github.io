# TP : Intégration et Gestion de Versions chez "MathTech Solutions"

**Contexte :**
Vous rejoignez l'équipe de développement de **MathTech Solutions**. Votre responsable technique, **Sarah**, vous envoie vos tâches par courriel au fil de la journée.

??? note "Règles d'or de l'entreprise"
    1.  **Langue :** Tous les noms de branches (sauf `main`) et tous les messages de commit doivent être **en français**.
    2.  **Workflow :** On ne touche jamais directement à `main` pour le code. Tout passe par une branche d'intégration nommée `dev`.

**Prérequis :**
* Le dépôt a été créé pour vous via **GitHub Classroom**.
* Vous devez avoir l'URL de votre dépôt sous la main.

---

## Démarrage - La propreté avant tout

> **De :** Sarah Connor (Tech Lead)
>
> **Objet :** Démarrage - La propreté avant tout
>
> Bienvenue ! Ton dépôt est prêt.  
> Avant même d'écrire une ligne de code C#, on doit s'assurer que le dépôt restera propre. On ne veut surtout pas versionner les fichiers temporaires de Visual Studio (`bin`, `obj`, `.vs`).

### Tes tâches :

??? Solution "Solution"
    1.  Ouvre ton terminal (Git Bash ou PowerShell) et clone ton dépôt :
        ```bash
        git clone <L_URL_DE_TON_DEPOT>
        ```
    2.  Entre dans le dossier créé : `cd TP_MathTech_VotreNom` (ou le nom exact du dossier).
    3.  **Le .gitignore :**
        * Va sur Google, cherche "github gitignore visual studio".
        * Prends le contenu du fichier officiel (souvent un lien "Raw").
        * Crée un fichier nommé `.gitignore` **à la racine du dossier** (là où se trouve le dossier caché `.git`) et colle le contenu dedans.
    4.  Fais le **tout premier commit** du projet (c'est une bonne pratique de commencer par ça) :
        ```bash
        git add .gitignore
        git commit -m "Config : Ajout du gitignore pour Visual Studio"
        ```

---

## Création de l'architecture

> **De :** Sarah Connor (Tech Lead)
>
> **Objet :** Création de l'architecture
>
> Parfait, le dépôt est sécurisé contre les fichiers inutiles. On peut créer la solution.  
> J'aimerais que tu crées une solution Visual Studio contenant une **Bibliothèque de classes** nommée `Bibliotheque-git-<da>` et un projet **Console** nommé `Console-git-<da>`. Une fois que c'est fait, **envoie-moi une capture d'écran de l'explorateur de solutions dans Visual Studio pour confirmer la structure, et la sortie de `git status` pour vérifier que `bin`, `obj` et `.vs` ne sont pas suivis.**

### Tes tâches :

??? Solution "Solution"
    1.  Lance **Visual Studio 2026**.
    2.  Crée une nouvelle solution dans ton dossier cloné :
        * Nom de la Solution : `[NOM_SOLUTION]`
        * Ajoute un projet **Bibliothèque de classes** nommé `Bibliotheque-git-<da>`.
        * Ajoute un projet **Console** nommé `Console-git-<da>`.
    3.  Dans la librairie, renomme `Class1.cs` en `Calculatrice.cs` (et mets la classe `public static`).
    4.  Vérifie avec `git status` que les dossiers `bin` et `obj` n'apparaissent pas (grâce à ton travail précédent).
    5.  Valide la structure sur la branche principale :
        ```bash
        git add .
        git commit -m "Initialisation : Structure de la solution C#"
        ```
    6.  **Création de la branche de développement :**
        À partir de maintenant, `main` est sacré. Crée la branche `dev` et place-toi dessus :
        ```bash
        git checkout -b dev
        ```

---

## Attention à tes fichiers personnels !

> **De :** Sarah Connor (Tech Lead)
>
> **Objet :** URGENT - J'ai fait une gaffe avec un fichier perso !
>
> Oh là là, j'ai fait une grosse bêtise !  
> J'étais en train de prendre des notes rapidement dans un fichier `note_personnelle.txt` et, sans faire attention, je l'ai ajouté à l'index de Git (`git add .`) !  
> Je ne veux absolument pas que ce fichier finisse sur le dépôt. Je sais qu'il faut l'enlever du staging, mais je ne me souviens plus de la commande exacte.
>
> **Tu lui répondrais quoi ? Comment ferait-on pour retirer ce fichier de l'index sans le supprimer de mon ordinateur ?**

### Scénario à reproduire :
Après avoir lu le courriel de Sarah, voici comment tu pourrais l'aider :

??? Solution "Solution"
    1.  Crée un fichier texte nommé `note_personnelle.txt` à la racine du projet.
    2.  Ajoute-le à l'index par erreur (oups !) :
        ```bash
        git add .
        ```
    3.  Vérifie le statut (il doit être vert, prêt à être commité) :
        ```bash
        git status
        ```
    4.  **Correction :** Pour garder le fichier sur ton ordi et l'enlever de Git de l'index :
        ```bash
        git rm --cached note_personnelle.txt
        ```
        (Note: La commande `git rm --cached <fichier>` désindexe le fichier et le supprime du suivi Git. Une alternative plus sécuritaire, `git restore --staged <fichier>`, désindexe le fichier sans le supprimer du suivi et sans toucher à votre copie locale, réduisant ainsi le risque d'effacement accidentel. Nous utiliserons ici `git rm --cached` comme demandé, mais gardez l'alternative `git restore --staged` en tête.)
    5.  Pour éviter de refaire l'erreur, ajoute `note_personnelle.txt` à la fin de ton fichier `.gitignore`.
    6.  Valide la mise à jour du gitignore sur la branche `dev` :
        ```bash
        git add .gitignore
        git commit -m "Config : Ignorer les notes personnelles"
        ```

---

## Dev de l'addition

> **De :** Sarah Connor (Tech Lead)
>
> **Objet :** Dev de l'addition - Implémentation de la fonction d'addition
>
> C'est parti pour développer une nouvelle fonctionnalité !  
> N'oublie pas que l'on part toujours de la branche `dev` pour créer une fonctionnalité.  
> J'ai besoin que tu implémentes la méthode d'addition suivante dans `Calculatrice.cs` :
> ```csharp
> public static int Additionner(int a, int b)
> {
>     return a + b;
> }
> ```
> Une fois que tu as intégré cette méthode et fusionné ta branche de fonctionnalité dans `dev`, **envoie-moi la sortie de `git log --graph --oneline` pour que je voie l'historique des commits.**

### Tes tâches :
??? Solution "Solution"
    1.  Crée une branche nommée `fonctionnalite/addition` (depuis `dev`).
    2.  Implémente la méthode `Additionner` dans `Calculatrice.cs` selon les spécifications de Sarah.
    3.  Valide ton travail :
        ```bash
        git add .
        git commit -m "Fonctionnalité : Ajout de la méthode Additionner"
        ```
    4.  **Intégration :**
        * Reviens sur la branche `dev` (`git checkout dev`).
        * Fusionne ta fonctionnalité :
            ```bash
            git merge fonctionnalite/addition
            ```
        * Vérifie l'historique avec :
            ```bash
            git log --graph --oneline
            ```

---

## URGENT - Conflit à gérer

> **De :** Sarah Connor (Tech Lead)
>
> **Objet :** URGENT - Conflit à gérer : Ta tâche de division !
>
> Attention !  
> Pendant que tu travaillais sur l'addition, j'ai déjà poussé ma propre version de la méthode `Diviser` sur la branche `dev` pour ajouter une vérification de division par zéro.  
> Voici le code que j'ai mis en place dans `Calculatrice.cs` :
> ```csharp
> public static double Diviser(int a, int b)
> {
>     if (b == 0) throw new Exception("Division par zéro impossible");
>     return (double)a / b;
> }
> ```
> Maintenant, c'est à ton tour ! Crée une nouvelle branche depuis `dev`, implémente TA version de la méthode `Diviser` (même si elle est simple et ne gère pas encore la division par zéro), puis fusionne ta branche dans `dev`.  
> Je m'attends à ce que tu rencontres un conflit. Tu devras le résoudre manuellement. Une fois la fusion et la résolution du conflit terminées, **envoie-moi le code final de `Calculatrice.cs` et la sortie de `git log --graph --oneline` pour que je valide la résolution.**

### Tes tâches :

??? Solution "Solution"
    1.  Assure-toi d'être sur la branche `dev` (`git checkout dev`).
    2.  Crée une nouvelle branche pour ta fonctionnalité de division, par exemple `fonctionnalite/ma-division` (`git checkout -b fonctionnalite/ma-division`).
    3.  Dans le fichier `Calculatrice.cs`, ajoute ta version de la méthode `Diviser` (une simple division sans gestion d'erreur) :
        ```csharp
        public static double Diviser(int a, int b)
        {
            return (double)a / b;
        }
        ```
    4.  Valide ton travail sur ta branche :
        ```bash
        git add .
        git commit -m "Fonctionnalité : Ajout de ma version de la méthode Diviser"
        ```
    5.  Retourne sur la branche `dev` (`git checkout dev`).
    6.  Tente de fusionner ta branche `fonctionnalite/ma-division` dans `dev` :
        ```bash
        git merge fonctionnalite/ma-division
        ```
        💥 **Un conflit devrait être détecté !**
    7.  **Résolution du conflit :**
        *   Ouvre `Calculatrice.cs` dans ton éditeur de texte.
        *   Tu verras des marqueurs de conflit (`<<<<<<<`, `=======`, `>>>>>>>`) indiquant les différences entre ta version et celle de Sarah sur `dev`.
        *   Modifie le fichier pour combiner les deux versions. L'objectif est de garder la fonctionnalité de division tout en intégrant la vérification de division par zéro de Sarah. Le code final devrait ressembler à ceci :
            ```csharp
            public static double Diviser(int a, int b)
            {
                if (b == 0) throw new Exception("Division par zéro impossible");
                return (double)a / b;
            }
            ```
        *   **Attention :** Assure-toi de supprimer tous les marqueurs de conflit !
    8.  Marque le conflit comme résolu et finalise la fusion :
        ```bash
        git add Calculatrice.cs
        git commit -m "Fusion : Résolution de conflit sur la méthode Diviser (intégration des deux versions)"
        ```

---

## Version 1.0

> **De :** Sarah Connor (Tech Lead)
>
> **Objet :** Version 1.0
>
> Excellent travail !  
> Le développement est terminé. La branche `dev` est stable et testée.  
> C'est le moment de déployer ! Une fois que `dev` est fusionnée dans `main`, **envoie-moi la sortie complète de `git log --graph --oneline --all` pour que je puisse valider l'historique final de toutes les branches.**

### Tes tâches :
??? Solution "Solution"
    1.  Reviens sur la branche `main`.
    2.  Fusionne le travail de `dev` vers `main`.
        ```bash
        git merge dev
        ```
    3.  Admire ton graphe final et appelle-moi pour la validation :
        ```bash
        git log --graph --oneline --all
        ```
