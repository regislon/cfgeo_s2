---
marp: true
paginate: true
header: "CFGEO - S2 - QGIS - Installation"
theme: default
---

<style>
table th {
  font-size: 0.75em;
}
table td {
  font-size: 0.7em;
}
</style>


# QGIS - Installation
- Doc : [https://github.com/regislon/cfgeo_s2/tree/main/client_desktop](https://github.com/regislon/cfgeo_s2/tree/main/client_desktop)
- Slides : [https://regislon.github.io/cfgeo_s2/client_desktop/README.html](https://regislon.github.io/cfgeo_s2/client_desktop/README.html)
- PDF : [https://github.com/regislon/cfgeo_s2/blob/gh-pages/client_desktop/README.pdf](https://github.com/regislon/cfgeo_s2/blob/gh-pages/client_desktop/README.pdf)



---


# Installation de QGIS et QGIS server
Pour installer Qgis, nous allons utiliser OSGeo4W. OSGeo4W est une distribution de binaire d'un grand nombre de logiciels open source geospatial pour les environnements Windows

-  Télécharger l'Installateur [OSGEo4W](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe)
- Choisir l’option « Advanced Install »
- Répertoire d’installation : C:\OSGeo4W64
- Choisir qgis-lrt et qgis-lrt-server

Vidéo complète de l'installation [ici](https://github.com/regislon/cfgeo_s2/raw/main/client_desktop/videos/install.mkv).


---


### Création d'un premier projet QGIS
- Créer un projet QGIS, enregistrer-le sous C:\OSGeo4W64\apps\qgis-ltr\bin\cfgeo.qgz
- Ajouter ces [données](https://github.com/regislon/cfgeo_s2/raw/main/client_desktop/data/initial_load.gpkg).



---

## 1. Interface de QGIS
L’interface de QGIS se compose de plusieurs éléments principaux :

- **Barre de menu** : accès aux fonctions principales (Projet, Édition, Vue, Couche, etc.).  
- **Barres d’outils** : outils accessibles rapidement, activables/désactivables.  
- **Panneaux** : par exemple le panneau des couches ou l’explorateur. Ils sont modulables et peuvent être affichés ou masqués.  
- **Vue cartographique (map canvas)** : zone principale d’affichage des couches.  
- **Barre d’état** : messages, coordonnées, SCR courant, indicateurs et recherche.

---

## 2. Configuration de QGIS
La configuration se fait via **Paramètres → Options** et inclut :

- **Options générales** : apparence, thèmes, langue, gestion des fichiers temporaires.  
- **Système et Profils utilisateur** : possibilité de créer plusieurs profils pour conserver des environnements distincts (plugins, barres d’outils, préférences).  
- **Propriétés du projet** : paramètres spécifiques à un projet (SCR, métadonnées, couleurs, variables, relations, macros, etc.).  
- **Personnalisation** : activer/désactiver des éléments de l’interface.  
- **Raccourcis clavier** : entièrement personnalisables.  
- **Ligne de commande et variables d’environnement** : pour les usages avancés et le déploiement.

---

## 3. Création d’un GeoPackage (gpkg) via le panneau Explorateur
Le **GeoPackage (GPKG)** est un format OGC qui stocke dans un seul fichier :  
- des couches vecteurs et rasters,  
- des styles (symbologie),  
- éventuellement un projet QGIS.

**Étapes pour créer un GeoPackage depuis le panneau Explorateur** :  

1. Ouvrir le **panneau Explorateur** (si besoin, activer via `Vue → Panneaux → Explorateur`).  
2. Dans l’arborescence, **clic droit sur "GeoPackage"** → choisir **Nouvelle base de données…**  
3. Donner un **nom** et un **emplacement** au fichier `.gpkg`.  
4. Une fois créé, le fichier apparaît dans le panneau Explorateur.  
5. Pour ajouter une couche dans ce GeoPackage :  
   - clic droit sur le GeoPackage,  
   - choisir **Nouvelle couche** (vecteur ou raster),  
   - définir les champs et géométries (point, ligne, polygone).  

---

## 4. Symbologie
La symbologie détermine l’apparence des couches vectorielles et rasters.

- **Accès** : clic droit sur une couche → *Propriétés* → onglet *Symbologie*, ou directement via le **panneau de style (Layer Styling Panel)**.  
- **Types de rendu disponibles** :  
  - Symbole unique,  
  - Valeurs catégorisées,  
  - Valeurs graduées,  
  - Symboles proportionnels,  
  - Rendu par règles,  
  - Heatmap (densité),  
  - Cluster,  
  - 2.5D et autres styles avancés.  
- **Options supplémentaires** : niveaux de symbole, transparence, effets de dessin, animation, styles sauvegardables dans le GeoPackage.

---