---
name: markdown-csharp-normalizer
description: Normalise les fichiers Markdown contenant des blocs de code C#. Alignement à gauche (colonne 0), standardisation des marqueurs ```csharp, passage au format de fin de ligne Unix (LF) et nettoyage de l'indentation intérieure des extraits de code. Utiliser pour corriger des problèmes d'affichage web sur MkDocs ou GitHub Pages.
---

# Normalisation Markdown C#

Cette compétence permet de standardiser l'apparence des blocs de code C# dans les fichiers Markdown.

## Fonctionnalités

1. **Alignement :** Ramène tous les marqueurs de blocs de code (` ``` `) à la colonne 0 (bord gauche).
2. **Langage :** Remplace systématiquement ` ```c# ` ou ` ``` ` par ` ```csharp ` lorsqu'un bloc est détecté.
3. **Indentation :** Supprime l'indentation commune superflue à l'intérieur des blocs de code pour assurer un affichage propre.
4. **Fins de ligne :** Convertit systématiquement les fichiers au format Unix (LF), éliminant les caractères CRLF (`^M`).

## Utilisation

Pour normaliser un ou plusieurs fichiers, ou un dossier entier de notes de cours :

```bash
python3 scripts/normalize.py <chemin_du_fichier_ou_dossier>
```

### Exemples d'exécution

- Normaliser tout un répertoire : `python3 markdown-csharp-normalizer/scripts/normalize.py docs/notes_de_cours/`
- Normaliser un fichier spécifique : `python3 markdown-csharp-normalizer/scripts/normalize.py docs/notes_de_cours/Semaine_1.md`

## Recommandations

- Toujours exécuter sur des fichiers de documentation avant un déploiement MkDocs.
- Préférable d'exécuter globalement sur un dossier pour maintenir une cohérence visuelle sur tout le site.