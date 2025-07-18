# Programme du Cours QGIS

## Jour 1

### Accueil et Introduction (30 min)
- Qui êtes-vous et qui suis-je?

- À propos de QGIS :
  - QGIS : Historique, philosophie (open-source), avantages et place dans le monde de la géomatique.
- Objectifs du cours : Maîtriser les bases de QGIS pour l'acquisition, la gestion, la visualisation et la production de cartes.

### Prise en main de l'interface et sources de données (1h)
- Présentation de l'interface utilisateur de QGIS :
  - Zone de carte, panneau des couches, explorateur, barres d'outils, panneaux d'outils.
  - Comprendre la structure d'un projet QGIS (.qgs/.qgz).
- Extensions (plugins) indispensables pour la Suisse :
  - Introduction et installation des plugins **Swiss Downloader** et **Swiss Locator**.
  - *Exercice pratique* : installation des extensions.
- Sources de données géographiques :
  - Formats de données courants : Shapefile (.shp), GeoPackage (.gpkg), TIFF.
  - Services web (WMS, WMTS, WFS) via url (getcapabilities) et Swiss Locator : utilité pour accéder à des données en ligne sans les télécharger.
  - Acquisition de données suisses avec Swiss Downloader :
    - *Démonstration et exercice* : téléchargement d’orthophotos (SWISSIMAGE) et de données vectorielles (limites communales, bâtiments) pour une zone d’étude (ex: Yverdon-les-Bains).
  - Ajouter des couches vectorielles et raster au projet QGIS.

### Pause café (15 min)

### Gérer et explorer les données (1h45)
- Gérer les données dans un projet QGIS :
  - Organisation des couches : ordre d'affichage, groupes.
  - Systèmes de Coordonnées de Référence (SCR) : focus sur CH1903+/LV95.
  - Reprojection "à la volée" et des couches.
- Symbologies et étiquettes :
  - Modifier l’apparence des couches : couleur, taille, épaisseur.
  - Symbolisation simple, catégorisée et graduée (ex : types de bâtiments).
  - Configurer l’étiquetage des entités : taille, couleur, position, masque.
- Configurer un formulaire d'attributs :
  - Accès à la table d'attributs.
  - Types de champs : texte, numérique, date.
  - Personnalisation du formulaire (onglets, glisser/déposer, widgets).
- Expressions simples :
  - Introduction au générateur d'expressions.
  - Utilisation pour la symbologie, l'étiquetage, les sélections.

### Pause midi (1h15)

### 13h00 - 14h30 : Sélection, filtrage et édition (1h30)
- Sélectionner et filtrer des données :
  - Sélection manuelle, par attribut (requêtes SQL), par localisation.
  - Filtrage de couches avec des requêtes.
  - Localisation rapide avec Swiss Locator (adresse, parcelle, lieu-dit).
- Saisir et éditer des géométries et attributs :
  - Création de nouvelle couche vectorielle (point, ligne, polygone) + champs attributaires.
  - Mode édition.
  - Outils de numérisation : ajout, suppression, déplacement de sommets.
  - Utiliser l'accrochage (snap).
  - Modification via le formulaire d’attributs.
  - *Exercice pratique* : numériser de nouvelles entités (ex : bâtiment ou limite temporaire).

### Pause (15 min)

### 14h45 - 16h15 : Traitement et analyse simple (1h30)
- Introduction aux outils de traitement :
  - Présentation de la Processing Toolbox.
  - Exploration d’algorithmes courants (géotraitement, gestion des données).
- Analyse simple de données vectorielles :
  - **Buffer (tampon)** : créer des zones tampon (ex : autour d’un cours d’eau).
  - **Intersection** : croisement de couches (ex : parcelles dans une zone d’affectation).
  - **Dissolution** : fusion d’entités similaires (ex : parcelles d’un même propriétaire).
  - *Exercice pratique* : identifier les bâtiments à moins de 20m d'une route principale.

---

## Jour 2

### 8h30 - 10h00 : Créer une mise en page et Conclusion (1h30 min)
- Réalisation de cartes pour l’impression :
  - Créer une nouvelle mise en page.
  - Ajouter les éléments essentiels : carte principale, vue d’ensemble, titre, légende, échelle, flèche du Nord, cadre.
  - Ajouter texte et images (logo de l’école/entreprise).
  - Grilles de coordonnées (CH1903+/LV95).
  - *Exercice pratique* : créer une carte finale intégrant les données téléchargées, numérisées et analysées.
- Exportation de la carte : PDF, JPG, PNG.

### Conclusion et ressources
- Récapitulatif des compétences acquises.
- Session Questions / Réponses.
- Ressources complémentaires :
  - Documentation QGIS
  - Forums
  - Portails de données suisses (Swisstopo, cantons, communes)

---

