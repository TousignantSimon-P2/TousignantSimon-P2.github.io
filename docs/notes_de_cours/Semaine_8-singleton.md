# Patron de conception : Singleton en C#

## Définition

Le **Singleton** est un patron de conception qui garantit qu'une classe ne possède **qu'une seule instance**, tout en fournissant un **point d'accès global** à cette instance.

Il est souvent utilisé pour gérer des ressources partagées comme une connexion à une base de données, un fichier de log, ou une configuration centrale.

## Objectifs

- Empêcher la création multiple d'objets.
- Fournir un accès global à l'instance unique.

## Implémentation simple en C#

Voici une version **non thread-safe** du Singleton en C# :

```csharp
public class ExempleSingleton
{
    private static ExempleSingleton instance;

    // Propriété publique d'accès à l'instance
    public static ExempleSingleton Instance
    {
        get
        {
            if (instance == null)
            {
                instance = new ExempleSingleton();
            }
            return instance;
        }
    }

    // Constructeur privé pour empêcher l'instanciation externe
    private ExempleSingleton()
    {
        // Initialisation de l'objet
    }

    // Exemple de méthode
    public void FaireQuelquechose()
    {
        Console.WriteLine("Singleton actif !");
    }
}
```

Autre exemple pour l'accesseur si toutefois vous la croiseriez  

```csharp
// C'est un "get" static avec la notion ?? qui veut dire si c'est null fait un new ExempleSingleton

public static ExempleSingleton Instance => instance ?? (instance = new ExempleSingleton());

```
  
  
```csharp

//Décomposé en plusieurs lignes on retrouverait

public static ExempleSingleton Instance 
{
    get 
    { 
        // instance n'est pas null, donc instance = instance. Sinon on fait un nouveau singleton
        instance = instance ?? new ExempleSingleton(); 
        return instance;
    }
}
```

Dans l'exemple précédent, il ya redondance, on assigne instance à instance...  
Si l'instance n'est pas null on mets instance égal à instance...  
Donc, vous allez souvent voir la version condensée.  

```csharp
// C'est un "get" static avec la notion ?? qui veut dire si c'est null fait un new ExempleSingleton

public static ExempleSingleton Instance => instance ?? (instance = new ExempleSingleton());

//Décomposé en plusieurs lignes on retrouverait

public static ExempleSingleton Instance
{
    get
    {
        return instance ?? new ExempleSingleton();
    }
}
```

Mais souvent dans la documentation ou le code de .Net on va voir littéralement la version lambda
```csharp
public static ExempleSingleton Instance => instance ?? (instance = new ExempleSingleton());
```

