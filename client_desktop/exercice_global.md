# Exercice global QGIS/QField/QGIS server

# Inventaire et analyse des infrastructures de mobilité douce  
*(pistes cyclables, parkings vélos, bornes de recharge e-bike)*

L’idée est de créer une base pour améliorer l’accessibilité et l’usage du vélo en ville ou en zone rurale.

---

### 1. Préparation des données de base

Importer des données de **swisstopo** pertinentes :  
- *Swiss Boundaries 3D* (communes, limites)  
- *Swiss TLM3D* ou *Swiss Map Vector 25* pour le réseau routier.  

Créer un **GeoPackage (GPKG)** avec les couches suivantes :  
- `pistes_cyclables` (lignes)  
- `parkings_velos` (points)  
- `bornes_recharge` (points)  

**Champs proposés :**  
- `pistes_cyclables` : `nom`, `type` (piste séparée/bande cyclable), `etat` (bon/moyen/mauvais).  
- `parkings_velos` : `capacite`, `abri` (oui/non), `photo`.  
- `bornes_recharge` : `operateur`, `puissance_kw`, `payant` (oui/non).  

---

### 2. Configuration des formulaires

Créer des formulaires ergonomiques avec widgets adaptés :  
- Menu déroulant pour `type`, `etat`, `payant`.  
- Widget photo pour `photo`.  
- Slider pour `capacite`.  

Organisation par onglets : **Infos générales / Détails techniques / Photos**.  

---

### 3. Numérisation dans QGIS

- Tracer un tronçon de `pistes_cyclables` à partir du réseau routier swisstopo.  
- Placer quelques points de `parkings_velos` et `bornes_recharge` d’après des connaissances locales ou des images de fond.  

---

### 4. Export vers QField et saisie simulée

- Préparer le projet avec **QFieldSync**.  
- Collecter de nouvelles données terrain (simulation dehors).  
- Ajouter une photo sur un parking vélo ou une borne.  
- Synchroniser les ajouts dans le projet QGIS.  

---

### 5. Analyse spatiale

Exemples de traitements avec le modeleur ou les requêtes spatiales :  
- Trouver les `parkings_velos` à moins de **100 m** d’une `piste_cyclable`.  
- Identifier les tronçons de `pistes_cyclables` à plus de **500 m** d’une `borne_recharge`.  
- Évaluer la **densité de parkings vélos** par quartier (jointure spatiale avec limites communales).  

Créer un **modeleur simple** automatisant :  
- **Entrée** = `bornes_recharge`  
- **Sortie** = tronçons de `pistes_cyclables` éloignés > 500 m  

---

### 6. Publication via QGIS Server
- Styliser les couches (ex. : pictogramme vélo, borne de recharge électrique, parking).  
- Paramétrer le projet pour publication **WMS** (titres, échelles, légendes).  
- Déployer sur **QGIS Server** (VM déjà prête).  
- Vérifier l’affichage dans un client externe (QGIS ou navigateur).  

---

## Résultats attendus

- **GeoPackage thématique mobilité douce.**  
- **Formulaires QField adaptés** à la collecte terrain.  
- **Données saisies et enrichies** sur le terrain et au bureau.  
- **Analyses spatiales automatisées** (distances, densités, proximité).  
- **Service WMS disponible** avec styles lisibles.  


