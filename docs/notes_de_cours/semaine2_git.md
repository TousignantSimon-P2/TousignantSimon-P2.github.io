## La commande ultime  
```csharp sh title="Console"
git status
```
## Création d'un projet git local  
```csharp sh title="Console"
git init
```
## Création d'une branche  
```csharp sh title="Console"
git branch [le nom de la branche]  
```

## Changement de branche 
```csharp sh title="Console"
git checkout [le nom de la branche]  
```
## Afficher toutes les branches  
```csharp sh title="Console"
git branch  
```
## Créer et changer de branche  
```csharp sh title="Console"
git checkout -b [le nom de la branche]  
```
## Faire une soumission de code  
```csharp sh title="Console"
git add [le fichiers ou le dossier]  
git commit -m "Le message significatif"  
```
## Revenir en arrière quand les fichiers sont en attente de la soumission (staged)
```csharp sh title="Console"
git restore --staged [le fichier ou le dossiers]  
```
## Restauration des fichiers 
 - Vous avez modifier de quoi mais vous voulez revenir au dernier commit et perdre vos modifications)
```csharp sh title="Console"
git reset --hard  
```
## Lister les soumissions
```csharp sh title="Console"
git log  
git log --graph  
git log --oneline  
```
## fusionner 2 branches
- Se placer dans la branche qui va recevoir (exemple main avec git checkout main)  
- faire git merge [nom de la branche à aller chercher]  
- Prier que rien n'explose.  



