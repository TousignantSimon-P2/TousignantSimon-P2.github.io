## Les interfaces  

Les interfaces sont essentiellement des contrats pour s'assurer qu'une classe implémente une ou plusieurs méthodes / accesseurs.  

Le standard au niveau du nom des interface est "I majuscule" suivit du nom de l'interface, qui commence également par une lettre majuscule.  
Exemple : "IEquatable" ou "ICompatable"  

### Exemple de déclaration
```csharp title="IUneInterface.cs"

public interface IUneInterface
{  

}
```

### Déclaration du "contrat"

Dans l'interface on déclare uniquement les signatures de méthodes.  
Bref, on termine pas un point-virgule à la fin de la déclaration.
```csharp title="IUneInterface.cs"

public interface IUneInterface
{  
    public void Methode();
    public int Methode(int variable);
}
```

### Les interfaces "standards" de C#

Dans c# il y a moulte interfaces déjà toutes prêtes, dont deux très connues  
- IEquatable  
- IComparable

### IEquatable

Permet de savoir si deux objets sont identiques (pareil) en fonction des données de l'objet et non parce que les 2 objets sont identiques au niveau de la mémoire (c'est la même référence).

Généralement on utiise IEquatable avec la mécanique générique

```csharp title="IUneInterface.cs"

public class UneClasse : IEquatable<UneClasse> //déclare que la classe UneClasse va avoir Equals(UneClasse other)
{  
    public bool Equals(UneClasse other)
    {

    }
}
```

### Les grand principe de IEquatable.
- Si other est null, nous sommes différents -> retourne faux
- Ensuite on compare les objets sur les règles métiers. Exemple est-ce que les noms sont identiques, est-ce que le kilométrage est identique, etc.
  
  
```csharp title="UneClasse.cs"
Exemple :   
public class UneClasse : IEquatable<UneClasse> //déclare que la classe UneClasse va avoir Equals(UneClasse other)
{  
    private int _uneValeur = 8;

    public bool Equals(UneClasse other)
    {
       if (other is null)
          return false;

       return (_uneValeur == other._uneValeur);

    }
}
```

Autre exemple : 


```csharp title="Personne.cs"
public class Personne : IEquatable<Personne>
{
    public string Nom { get; set; }

    public bool Equals(Personne other)
    {
        if (other is null) return false;
        return this.Nom == other.Nom;
    }
}
```

[Référence microsoft](https://learn.microsoft.com/fr-ca/dotnet/api/system.iequatable-1?view=net-9.0)   


### IComparable

IComparable permet de comparer des objets entre eux, mais également de les ordonner.  
Par exemple on compare 2 âges entre eux. 20 et 25 ans, on peut déduire qu'il y a une différence de 5 entre les deux.  

Détails important de vision. Si on regarde à l'inverse on voit qu'il peut aussi avoir une différence de -5 entre les deux âges.

Si on a 25 et 25 on a une différence de 0, donc les âges sont identiques.

Dans l'implémentation, les lignes directrice. Si on compare avec un objet null on retourne 1. Signifiant que nous sommes plus grand que "other".

Autrement c'est toujours "nous" comparé à l'autre. Si nous somme plus grand, le nombre est positif. Autrement, zéro si nous sommes égaux, sinon un nombre négatif. Souvent, une soustraction est impliquée.  

Exemple : une personne de 25 ans et de 20 ans... 25 - 20 = 5 donc nous sommes plus grand.  
Inversement, si la personne à 20 ans et que other a 25... 20 - 25 = -5 donc moins âgée.

En code : 


```csharp title="Etudiant.cs"
   public class Etudiant : IComparable<Étudiant>
{
    public string Nom { get; set; }
    public double Moyenne { get; set; }

    public int CompareTo(Étudiant other)
    {
        if (other == null) return 1;

        return this.Moyenne - other.Moyenne;
    }
} 
```

À noter qu'une implémentation d'interface n'est pas exclusive, une classe peut implémenter plusieurs interfaces.

Exemple :

```csharp title="Etudiant.cs"
public class Personne : IEquatable<Personne>, IComparable<Personne>
{
    public string Nom { get; set; }
    public int Âge { get; set; }

    // Implémentation de IEquatable<Personne>
    public bool Equals(Personne other)
    {
        if (other is null) return false;
        return Nom == other.Nom && Âge == other.Âge;
    }

    // override de Equals de object -> on fait la passe sur la palette de Equals qui reçoit une personne en paramètre.
    public override bool Equals(object obj) => Equals(obj as Personne);

    // méthode qui retourne un nombre "unique" pour identifier l'objet (requis par CompareTo)
    public override int GetHashCode() => HashCode.Combine(Nom, Age);

    // Implémentation de IComparable<Personne>
    public int CompareTo(Personne other)
    {
        if (other == null) return 1;

        // Exemple : tri par âge croissant, puis par nom
        int comparaisonÂge = Age.CompareTo(other.Age);
        if (comparaisonÂge != 0) return comparaisonÂge;

        return string.Compare(Nom, other.Nom, StringComparison.Ordinal); // une méthode de comparaison.
    }

    public override string ToString() => $"{Nom} ({Age} ans)";
}
```


Note sur le "Ordinal"

StringComparison.Ordinal effectue une comparaison binaire stricte des caractères, basée uniquement sur leurs valeurs Unicode. 

## Pourquoi utiliser `StringComparison.Ordinal` ?

| Critère                      | `StringComparison.Ordinal`                                      | Autres comparaisons (`CurrentCulture`, etc.)                         |
|------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------|
| **Vitesse**                  | ✅ Très rapide (pas de traitement culturel)                      | ❌ Plus lent (dépend de la culture de l'environnement)              |
| **Prédictibilité**           | ✅ Identique sur toutes les machines                             | ❌ Peut varier selon la langue ou le système                        |
| **Sensibilité à la casse**   | ✅ Oui (ex. `"abc"` ≠ `"ABC"`)                                   | ⚠️ Dépend de l'option (IgnoreCase)                                 |
| **Tri technique**            | ✅ Idéal pour tris binaires, noms techniques, clés de dictionnaire | ❌ Peut donner des résultats inattendus (ex. tri alphabétique français) |
| **Indépendant de la culture**| ✅ Oui                                                           | ❌ Non                                                              |
| **Utilisation recommandée**  | Comparaison de chaînes techniques : identifiants, fichiers, etc. | Affichage utilisateur, recherche en texte selon la langue          |

