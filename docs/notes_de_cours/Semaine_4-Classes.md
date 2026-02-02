## Création d'une classe dans une bibliothèque
- Créer une bibliothèque de classes vous fabrique par défaut Class1 que vous allez devoir renommer.
- (Ctrl+r Ctrl+r)  
![](/images/ClasseEtProjet/1.png)  
  
- Renomme également le fichier associé à la classe.  
![](/images/ClasseEtProjet/2.png)  

## Création des champs / attributs
- Faire la déclaration des variables membres.
- Attention : Toujours "private" toujours "_" et le nom en casse chameau.  
![](/images/ClasseEtProjet/3.png)  

## Accesseurs
- Création des accesseur avec les actions rapides.  
![](/images/ClasseEtProjet/4.png)  
  
- Prendre l'option d'encapsuler et d'utiliser la propriété.  
![](/images/ClasseEtProjet/5.png)  
  
- Faire un premier nettoyage des "get" et des "set" pour rendre ça plus propre.  
- Les "get" peuvent rester sur une seule ligne.  
![](/images/ClasseEtProjet/6.png)   
  
## Validation des valeurs passées dans les propriétés
- Les sections summarys sont essentiels  
- Dans les "set" on s'assure de valider le paramètre.
- Attention: Le paramètre prend le nom de "value". Typique à C#  
![](/images/ClasseEtProjet/7.png)  

### Validation par regex et foreach
- Exemple d'une validation sanitaire pour le numéro de DA
- Par regex et par boucle foreach.  
![](/images/ClasseEtProjet/8.png)  

### Valeurs nullable
- Pour les avertissement et les erreurs concernant les type "non-nullable"
- Placer un ? après le type pour rendre la valeur nullable.  
![](/images/ClasseEtProjet/9.png)  

## Génération du ou des constructeurs
- Une fois toutes les validations sanitaires complétées, procédez à la création des constructeurs
- Action rapides et factorisation sur la classe.  
![](/images/ClasseEtProjet/10.png)  
  
- Sélectionner "Générer le constructeur"  
![](/images/ClasseEtProjet/11.png)  

- Sélectionnez les propriétés et non les champs.  
![](/images/ClasseEtProjet/12.png)  

- Assurez vous de bien remplir la section summary 
- Attention les exceptions ne seront pas générées, vous devez compléter cette section manuellement.  
![](/images/ClasseEtProjet/13.png)  

