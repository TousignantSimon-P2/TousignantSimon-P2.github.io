# Exercice 2  
- Faire un dépôt Git dans un dossier de votre choix. (git init)
- Ajouter le .gitignore pour Visual Studio (sur Google VisualStudio.gitignore -> renommez-le)
- Créer une solution Visual Studio avec 2 projets à l'intérieur (Nommons-la Exercice2)
    - Un projet console .NET 8
    - Une bibliothèque de classes MesOutils-9999999 (avec votre DA)

## Découpage du problème  

- Dans une branche devParceQueSimonLeDemande, faites la codification des éléments suivants :
    - Une classe statique "OutilTableaux" avec les méthodes statiques suivantes :
    - Générer un tableau avec une taille donnée.
    - Générer un tableau avec une taille donnée, un minimum pour les valeurs inclus, un maximum __inclusif__.
    - Inverser un tableau nommé Inverser.
    - Décaler vers la droite un tableau __sans rotation__ d'un nombre d'éléments.
    - Décaler vers la gauche un tableau __sans rotation__ d'un nombre d'éléments.
    - Décaler vers la droite un tableau __avec rotation__ d'un nombre d'éléments.
    - Décaler vers la gauche un tableau __avec rotation__ d'un nombre d'éléments.
    - Copier un tableau à l'identique.
    - Extraire un sous-tableau d'un tableau à partir d'un index x à un index y et le recopier dans un tableau de destination à partir d'un index z.
    - Trier avec bulle, insertion et sélection doit être déplacé dans cette bibliothèque.
    - Faite la déclaration seulement de TriRadix avec les arguments et lever l'exception nécessaire.
    - Faites la déclaration de la classe File avec comme méthode "Enfiler, Defiler et Observer". Lever les exceptions nécessaires.
##  
- [x] Les vérifications sanitaires doivent être faites pour chaque méthode.
- [x] Les résumés doivent être présents pour chaque méthode.
- [x] On ne laisse pas traîner d'espace blanc pour rien.
- [x] Si on a du code qui se duplique, on le factorise dans une méthode à part.
- [x] Le code dupliqué doit être factorisé.