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
> **Objet :** Démarrage - La propreté avant tout
>
> Bienvenue ! Ton dépôt est prêt. Avant même d'écrire une ligne de code C#, on doit s'assurer que le dépôt restera propre. On ne veut surtout pas versionner les fichiers temporaires de Visual Studio (`bin`, `obj`, `.vs`).

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
> **Objet :** Création de l'architecture
>
> Parfait, le dépôt est sécurisé contre les fichiers inutiles. On peut créer la solution.

### Tes tâches :

??? Solution "Solution"
    1.  Lance **Visual Studio 2026**.
    2.  Crée une nouvelle solution dans ton dossier cloné :
        * Nom de la Solution : `MathTechSolution`
        * Ajoute un projet **Bibliothèque de classes** nommé `MathTech.Librairie`.
        * Ajoute un projet **Console** nommé `MathTech.Console`.
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
> **Objet :** Attention à tes fichiers personnels !
>
> Je vois que tu as créé un fichier pour noter tes idées, mais tu as failli l'envoyer sur le serveur. Il faut corriger ça avant que ça ne pollue le projet.

### Scénario à reproduire :

??? Solution "Solution"
    1.  Crée un fichier texte nommé `mes_notes.txt` à la racine du projet.
    2.  Ajoute-le à l'index par erreur (oups !) :
        ```bash
        git add .
        ```
    3.  Vérifie le statut (il doit être vert, prêt à être commité) :
        ```bash
        git status
        ```
    4.  **Correction :** On veut garder le fichier sur ton ordi, mais l'enlever de Git. Utilise la commande magique :
        ```bash
        git rm --cached mes_notes.txt
        ```
    5.  Pour éviter de refaire l'erreur, ajoute `mes_notes.txt` à la fin de ton fichier `.gitignore`.
    6.  Valide la mise à jour du gitignore sur la branche `dev` :
        ```bash
        git add .gitignore
        git commit -m "Config : Ignorer les notes personnelles"
        ```

---

## Dev de l'addition

> **De :** Sarah Connor (Tech Lead)
> **Objet :** Dev de l'addition
>
> C'est parti. On part toujours de `dev` pour créer une fonctionnalité.

### Tes tâches :
??? Solution "Solution"
    1.  Crée une branche nommée `fonctionnalite/addition` (depuis `dev`).
    2.  Dans `Calculatrice.cs`, ajoute :
        ```csharp
        public static int Additionner(int a, int b)
        {
            return a + b;
        }
        ```
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
> **Objet :** URGENT - Conflit à gérer
>
> Pendant que tu codais l'addition, j'ai dû modifier le fichier sur la branche `dev`. Tu vas devoir gérer l'intégration de la division manuellement.

### Suis ces étapes PRÉCISÉMENT pour simuler le conflit :

??? Solution "Solution"
    **Étape A : Ton travail sur la division**
    1.  Assure-toi d'être sur `dev`, puis crée la branche `fonctionnalite/division`.
    2.  Dans `Calculatrice.cs`, ajoute cette méthode (en dessous de l'addition) :
        ```csharp
        public static double Diviser(int a, int b)
        {
            return (double)a / b;
        }
        ```
    3.  Valide ton code :
        ```bash
        git commit -am "Fonctionnalité : Ajout de la division simple"
        ```

    **Étape B : Simulation du travail d'un collègue (Le piège)**
    1.  Reviens sur la branche `dev` : `git checkout dev`.
    2.  Modifie **le même fichier** `Calculatrice.cs`. Ajoute cette méthode (au même endroit, en dessous de l'addition) :
        ```csharp
        // Méthode ajoutée par Sarah
        public static double Diviser(int a, int b)
        {
            if (b == 0) throw new Exception("Division par zéro impossible");
            return (double)a / b;
        }
        ```
    3.  Simule le commit du collègue sur `dev` :
        ```bash
        git commit -am "Correctif : Sécurisation de la division"
        ```

    **Étape C : La Fusion et la Résolution**
    Tu es sur `dev`. Tu veux récupérer ton travail qui est sur `fonctionnalite/division`.
    1.  Lance la fusion :
        ```bash
        git merge fonctionnalite/division
        ```
        💥 **CONFLIT DÉTECTÉ !**

    2.  **Résolution :**
        * Ouvre `Calculatrice.cs` dans Visual Studio.
        * Repère les marqueurs de conflit (`<<<<<<<`, `=======`, `>>>>>>>`).
        * **Consigne :** Garde la version sécurisée (celle avec le `if`) et supprime les marqueurs. Le code doit compiler.
    3.  Finalise la fusion :
        ```bash
        git add Calculatrice.cs
        git commit -m "Fusion : Résolution de conflit sur la division"
        ```

---

## Version 1.0

> **De :** Sarah Connor (Tech Lead)
> **Objet :** Version 1.0
>
> Le développement est terminé. La branche `dev` est stable et testée. On déploie !

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
