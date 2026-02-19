# Projet "DUNGEON-GUARD 3000"

## Le Contexte
Le Seigneur Noir **Malphas** en a assez que des héros entrent dans son donjon comme dans un moulin. Il vous commissionne pour créer le système de gestion de sa Garde de Porte. Il veut automatiser la surveillance des couloirs et la gestion de ses monstres de garde.  

## Cahier des Charges

### Les Couloirs
Chaque couloir possède :  
- Un **nom** (ex: "Couloir des Soupirs")  
- Une **longueur** en mètres  
- Un **Niveau d'Alerte** (un chiffre de 1 à 5)  
- Une **capacité maximale** de gardes  

### Les Gardes
Un garde possède :  
- Un **nom**  
- Un **matricule**  
- Une **Puissance de Combat**  
- Une **Énergie** (maximum 100)  
- Un **Type de Monstre** (Squelette, Orc, Chevalier Noir)  
- Un état **Épuisé** (booléen)  

### Les Règles du Donjon
1. **Affectation** : On assigne des gardes à un couloir. On ne peut pas dépasser la capacité maximale du couloir.  
2. **Patrouille** : Lors d'une patrouille, un garde consomme de l'énergie selon la formule :  
   `EnergiePerdue = LongueurDuCouloir * NiveauAlerte`  
3. **Sécurité** : Si l'énergie d'un garde tombe à 0, il devient "Épuisé". Un garde épuisé ne peut plus patrouiller et sa puissance de combat tombe à 0 (sauf exception).  
4. **Logique de Défense** : La puissance défensive totale d'un couloir est la somme des puissances de tous les gardes **non-épuisés** présents.  

!!! info "Le Petit Plus (Optionnel)"  
    Les **Chevaliers Noirs** ne deviennent jamais "Épuisés", même à 0 d'énergie, mais leur puissance est divisée par 2 quand ils sont fatigués (énergie à 0).  

## Modélisation UML

Voici le diagramme de classes représentant la structure du système :  

```csharp mermaid
classDiagram
    direction LR
    class Couloir {
        - nom: String
        - longueur: double
        - niveauAlerte: int
        - capaciteMaximale: int
        + «get» Nom: String
        + «get» Longueur: double
        + «get»-«set» NiveauAlerte: int
        + «get» CapaciteMaximale: int

        + «create» Couloir(nom: String, longueur: double, niveauAlerte: int, capaciteMaximale: int)
        + AjouterGarde(garde: Garde) bool
        + CalculerPuissanceDefensiveTotale() int
        + FairePatrouille() void
    }

    class Garde {
        - nom: String
        - matricule: String
        - puissanceCombat: int
        - energie: int
        - estEpuise: bool
        + «get» Nom: String
        + «get» Matricule: String
        + «get» PuissanceCombat: int
        + «get»-«set» Energie: int
        + «get» EstEpuise: bool

        + «create» Garde(nom: String, matricule: String, puissanceCombat: int, energie: int, type: TypeMonstre)
        + Patrouiller(longueur: double, niveauAlerte: int) void
        + Dormir() void
    }

    class TypeMonstre {
        <<enumeration>>
        SQUELETTE
        ORC
        CHEVALIER_NOIR
    }

    Couloir "1" *-- "0..*" Garde : surveillé par
    Garde --> "1" TypeMonstre : possède un
```

## Mission

### Objectif
Concevoir le module `Donjon.Securite`.  

### Instructions
1. **Encapsulation Stricte** : Aucun attribut ne doit être public.  
2. **Validation** : Le `NiveauAlerte` doit être validé à l'entrée (entre 1 et 5).  
3. **Logique Métier** : Implémentez la méthode `FairePatrouille()` qui met à jour l'énergie de tous les gardes du couloir.  

## Test de Validation
Pour vérifier votre implémentation, suivez ce scénario :  
1. Créez un couloir de **20m** avec un niveau d'alerte de **3**.  
2. Ajoutez un **Squelette** (Puissance 10, Énergie 50).  
3. Faites patrouiller le garde une fois via `FairePatrouille()`.  
    - Il perd 60 d'énergie (20 x 3).  
    - Son énergie tombe à 0 et il devient **épuisé**.  
4. Vérifiez que la **Puissance Défensive Totale** du couloir est maintenant de **0** via `CalculerPuissanceDefensiveTotale()`.  

??? success "Solution suggérée (C#)"
```csharp
using System;
using System.Collections.Generic;

namespace Donjon.Securite
{
    /// <summary>
    /// Représente les différents types de monstres pouvant être des gardes.
    /// </summary>
    public enum TypeMonstre
    {
        SQUELETTE,
        ORC,
        CHEVALIER_NOIR
    }

    /// <summary>
    /// Représente un garde chargé de surveiller les couloirs du donjon.
    /// </summary>
    public class Garde
    {
        private string _nom;
        private string _matricule;
        private int _puissanceCombat;
        private int _energie;
        private TypeMonstre _type;

        /// <summary>
        /// Initialise une nouvelle instance de la classe <see cref="Garde"/>.
        /// </summary>
        /// <param name="nom">Le nom du garde.</param>
        /// <param name="matricule">Le matricule unique du garde.</param>
        /// <param name="puissanceCombat">La puissance de combat de base.</param>
        /// <param name="energie">Le niveau d'énergie initial (max 100).</param>
        /// <param name="type">Le type de monstre.</param>
        public Garde(string nom, string matricule, int puissanceCombat, int energie, TypeMonstre type)
        {
            Nom = nom;
            Matricule = matricule;
            _puissanceCombat = puissanceCombat;
            Energie = energie;
            Type = type;
        }

        /// <summary>
        /// Effectue une patrouille et consomme de l'énergie.
        /// </summary>
        /// <param name="longueur">La longueur du couloir parcouru.</param>
        /// <param name="niveauAlerte">Le niveau d'alerte du couloir.</param>
        public void Patrouiller(double longueur, int niveauAlerte)
        {
            if (EstEpuise)
            {
                return;
            }

            int energiePerdue = (int)(longueur * niveauAlerte);
            int nouvelleEnergie = Energie - energiePerdue;

            if (nouvelleEnergie < 0)
            {
                Energie = 0;
            }
            else
            {
                Energie = nouvelleEnergie;
            }
        }

        /// <summary>
        /// Redonne toute son énergie au garde.
        /// </summary>
        public void Dormir()
        {
            Energie = 100;
        }

        /// <summary>
        /// Obtient le nom du garde.
        /// </summary>
        public string Nom
        {
            get => _nom;
            private set => _nom = value;
        }

        /// <summary>
            /// Obtient le matricule du garde.
        /// </summary>
        public string Matricule
        {
            get => _matricule;
            private set => _matricule = value;
        }

        /// <summary>
        /// Obtient la puissance de combat effective du garde.
        /// </summary>
        public int PuissanceCombat
        {
            get
            {
                if (EstEpuise)
                {
                    return 0;
                }

                if (Type == TypeMonstre.CHEVALIER_NOIR && Energie == 0)
                {
                    return _puissanceCombat / 2;
                }

                return _puissanceCombat;
            }
        }

        /// <summary>
        /// Obtient ou définit l'énergie du garde.
        /// </summary>
        /// <exception cref="ArgumentOutOfRangeException">Lancée si l'énergie est hors limites.</exception>
        public int Energie
        {
            get => _energie;
            set
            {
                if (value < 0 || value > 100)
                {
                    throw new ArgumentOutOfRangeException(nameof(value), "L'énergie doit être comprise entre 0 et 100.");
                }
                _energie = value;
            }
        }

        /// <summary>
        /// Obtient le type de monstre.
        /// </summary>
        public TypeMonstre Type
        {
            get => _type;
            private set => _type = value;
        }

        /// <summary>
        /// Indique si le garde est épuisé et ne peut plus agir.
        /// </summary>
        public bool EstEpuise
        {
            get
            {
                // Les Chevaliers Noirs ne sont jamais épuisés selon la règle optionnelle
                if (Type == TypeMonstre.CHEVALIER_NOIR)
                {
                    return false;
                }

                return Energie == 0;
            }
        }
    }

    /// <summary>
    /// Représente un couloir du donjon contenant des gardes.
    /// </summary>
    public class Couloir
    {
        private string _nom;
        private double _longueur;
        private int _niveauAlerte;
        private int _capaciteMaximale;
        private List<Garde> _gardes;

        /// <summary>
        /// Initialise une nouvelle instance de la classe <see cref="Couloir"/>.
        /// </summary>
        /// <param name="nom">Le nom du couloir.</param>
        /// <param name="longueur">La longueur en mètres.</param>
        /// <param name="niveauAlerte">Le niveau d'alerte (1 à 5).</param>
        /// <param name="capaciteMaximale">La capacité maximale de gardes.</param>
        public Couloir(string nom, double longueur, int niveauAlerte, int capaciteMaximale)
        {
            Nom = nom;
            Longueur = longueur;
            NiveauAlerte = niveauAlerte;
            CapaciteMaximale = capaciteMaximale;
            _gardes = new List<Garde>();
        }

        /// <summary>
        /// Tente d'ajouter un garde au couloir.
        /// </summary>
        /// <param name="garde">Le garde à ajouter.</param>
        /// <returns>True si le garde a été ajouté, sinon False.</returns>
        public bool AjouterGarde(Garde garde)
        {
            if (_gardes.Count >= CapaciteMaximale)
            {
                return false;
            }

            _gardes.Add(garde);
            return true;
        }

        /// <summary>
        /// Calcule la puissance défensive totale du couloir.
        /// </summary>
        /// <returns>La somme des puissances de combat des gardes.</returns>
        public int CalculerPuissanceDefensiveTotale()
        {
            int puissanceTotale = 0;
            foreach (Garde garde in _gardes)
            {
                puissanceTotale += garde.PuissanceCombat;
            }
            return puissanceTotale;
        }

        /// <summary>
        /// Déclenche une patrouille pour tous les gardes du couloir.
        /// </summary>
        public void FairePatrouille()
        {
            foreach (Garde garde in _gardes)
            {
                garde.Patrouiller(Longueur, NiveauAlerte);
            }
        }

        /// <summary>
        /// Obtient le nom du couloir.
        /// </summary>
        public string Nom
        {
            get => _nom;
            private set => _nom = value;
        }

        /// <summary>
        /// Obtient la longueur du couloir.
        /// </summary>
        public double Longueur
        {
            get => _longueur;
            private set => _longueur = value;
        }

        /// <summary>
        /// Obtient ou définit le niveau d'alerte du couloir (1-5).
        /// </summary>
        /// <exception cref="ArgumentOutOfRangeException">Lancée si le niveau est hors limites.</exception>
        public int NiveauAlerte
        {
            get => _niveauAlerte;
            set
            {
                if (value < 1 || value > 5)
                {
                    throw new ArgumentOutOfRangeException(nameof(value), "Le niveau d'alerte doit être entre 1 et 5.");
                }
                _niveauAlerte = value;
            }
        }

        /// <summary>
        /// Obtient la capacité maximale de gardes.
        /// </summary>
        public int CapaciteMaximale
        {
            get => _capaciteMaximale;
            private set => _capaciteMaximale = value;
        }
    }
}
```
  
