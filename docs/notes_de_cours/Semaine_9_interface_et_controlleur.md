# Gestion d'un Client via un Singleton dans un Projet Windows Forms

Ce document explique comment structurer un petit projet Windows Forms en C# pour gérer un client simple (ayant uniquement un nom) en utilisant le **patron de conception Singleton** pour le contrôleur.

---

## 1. Le formulaire (`FormClient`)

Dans le formulaire principal de l’interface graphique, en haut du constructeur, comme dans une classe normale  
nous avons une variable privée qui référence le contrôleur :

```csharp
private ControlleurClient _controlleurClient = ControlleurClient.Instance;
```

### Pourquoi faire cela ?

- On veut accéder à une **seule instance partagée** du contrôleur partout dans l’application.
- Cela évite de devoir instancier manuellement le contrôleur à chaque fois.
- Cela centralise la logique métier dans une classe dédiée.

---

## 2. Le contrôleur (`ControlleurClient`)

Le contrôleur contient toute la logique liée aux actions métiers sur les clients (ex. ajouter un nom, récupérer une liste).

Il est implémenté en **singleton**, c’est-à-dire que seule une instance de la classe sera créée et utilisée :

```csharp
public class ControlleurClient
{
    private static ControlleurClient instance;

    //version condensée du Singleton.
    public static ControlleurClient Instance => instance ?? (instance = new ControlleurClient());

    //Constructeur privé pour éviter l'instanciation.
    private ControlleurClient() { }

    // Action : Enregistrer un client (par nom)
    public void EnregistrerClient(string nom)
    {
        // Logique d’enregistrement (ex. stocker dans une liste)
    }

    // Action : Récupérer la liste des clients
    public List<string> RecupererListeClient()
    {
        //Logique de récupération de la liste
    }
}
```

---

## 3. Utilisation dans le formulaire

Voici comment le formulaire utilise le contrôleur via la variable `_controlleurClient` pour appeler les actions :

```csharp
private void btnEnregistrer_Click(object sender, EventArgs e)
{
    string nomClient = txtNomClient.Text;
    _controlleurClient.EnregistrerClient(nomClient);
}

private void btnAfficherClients_Click(object sender, EventArgs e)
{
    var liste = _controlleurClient.RecupererListeClient();
    lstClients.DataSource = liste;
}
```

## 4. Résumé

- `ControlleurClient` est un **singleton** accessible via `ControlleurClient.Instance`.
- Le formulaire déclare une variable `_controlleurClient` pour y accéder facilement.
- Les méthodes du contrôleur permettent d’**enregistrer un client** et de **récupérer une liste**.
- Le contrôlleur possède des opérations de hauts niveau pour séparer la logique d'interface de la logique métier.

