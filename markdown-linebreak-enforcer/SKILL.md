---
name: markdown-linebreak-enforcer
description: Assure que les sauts de ligne dans les fichiers Markdown sont précédés de deux espaces (standard Markdown pour les retours à la ligne forcés). Ignore les blocs de code, les tableaux, les en-têtes et les lignes vides.
---

# Enforceur de sauts de ligne Markdown

Cette compétence permet de forcer l'ajout de deux espaces avant chaque saut de ligne pour assurer un rendu correct dans les environnements Markdown.

## Fonctionnalités

1. **Ajout d'espaces :** Ajoute exactement deux espaces à la fin de chaque ligne de texte.
2. **Respect des structures :** Ignore intelligemment les blocs de code (` ``` `), les en-têtes (`#`), les tableaux (`|`) et les lignes déjà vides pour ne pas briser le formatage spécial.
3. **Idempotence :** Nettoie les espaces existants avant d'en ajouter deux, évitant ainsi l'accumulation d'espaces lors de passages répétés.

## Utilisation

Pour traiter des fichiers ou des dossiers :

```bash
python3 markdown-linebreak-enforcer/scripts/enforce_linebreaks.py <chemin_du_fichier_ou_dossier>
```

### Exemples d'exécution

- Traiter tout le dossier docs : `python3 markdown-linebreak-enforcer/scripts/enforce_linebreaks.py docs/`
- Traiter un fichier spécifique : `python3 markdown-linebreak-enforcer/scripts/enforce_linebreaks.py docs/notes_de_cours/Semaine_1.md`