

# Server Cartographique
- Doc : [https://github.com/regislon/cfgeo_s2/tree/main/serveur_cartographique](https://github.com/regislon/cfgeo_s2/tree/main/server_cartographique)
- Slides : [https://regislon.github.io/cfgeo_s2/serveur_cartographique/README.html](https://regislon.github.io/cfgeo_s2/server_cartographique/readme.html)
- PDF : [https://github.com/regislon/cfgeo_s2/blob/gh-pages/serveur_cartographique/README.pdf](https://github.com/regislon/cfgeo_s2/blob/gh-pages/server_cartographique/readme.pdf)




> :speech_balloon: Dans cette partie, nous allons créer un projet QGIS, le placer à l'emplacement précis sur la machine virtuelle, puis il sera servi par le serveur cartographique QGIS Server pour diffuser les données.




### Création de la structure du projet

- Créez un répertoire à la racine du disque nommé `qgis`.
- À l'intérieur de ce dossier, placez un projet QGIS nommé `cfgeo.qgz`.
- Cette organisation facilitera la gestion et la diffusion du projet par QGIS Server.



### Ajout des données au projet QGIS

- Les données ont déjà été **chargées dans la base PostgreSQL/PostGIS**.
- Créez une **connexion locale** à la base `localhost`.
- Ajoutez les couches nécessaires au projet `cfgeo.qgz`.
- Appliquez un **style minimal** (couleurs, transparence, légende) pour faciliter la diffusion via QGIS Server.

> :art: Un style clair et lisible améliore la compréhension des cartes publiées.




### Paramétrage du projet QGIS pour QGIS Server

- Ouvrez le menu **Project > Properties...** pour accéder aux paramètres du projet QGIS.

![height:400](images_documentation/image.png)





- Activez **Enable Service Capabilities** dans l’onglet `QGIS Server`.

![height:500](images_documentation/image-1.png)



- Complétez les métadonnées principales :  
  - Titre, Organisation, Contact, URL.  


- Configurez les capacités :  
  - **WMS** : étendue, options de rendu, taille max. des images.  
    ![height:400](images_documentation/image-2.png)



  - **WFS / OAPIF** : couches publiées, droits de mise à jour/insertion.  

![height:400](images_documentation/image-3.png)


> :bulb: Ces paramètres alimentent les documents *GetCapabilities* (interopérabilité et sécurité).  



## OGC : Open Geospatial Consortium

- **Fondé en 1994**
- **Objectif** : *Faciliter les échanges dans le domaine de la géomatique (formats de données et services)*
- Mise en place de **standards ouverts** :
  - Formats de fichiers (KML, NetCDF, ...)
  - Services web (WMS, WFS, ...)
  - API (GeoAPI)
  - ...
- Ces standards assurent l’interopérabilité entre logiciels et plateformes SIG.




## Web Map Service (WMS)

- **Norme OGC** permettant de diffuser des cartes **sous forme d’images**.  
- Principales requêtes :  
  - **GetCapabilities** : description du service.  
  - **GetMap** : génération d’une carte (image PNG/JPEG).  
  - **GetFeatureInfo** : info sur un objet en cliquant.  
- Utilisation : visualiser des couches **sans télécharger les données**.  

> :framed_picture: Exemple : afficher une carte communale en JPEG depuis QGIS Server.  






## Web Map Tile Service (WMTS)

- Variante de WMS qui diffuse des **tuiles prédécoupées**.  
- Avantage :  
  - Chargement rapide (cache de tuiles).  
  - Compatible avec de nombreux clients web (Leaflet, OpenLayers).  
- Principales requêtes :  
  - **GetCapabilities** : métadonnées du service.  
  - **GetTile** : récupération d’une tuile.  
  - **GetFeatureInfo** : info sur un objet (optionnel).  

> :rocket: Idéal pour les applications web nécessitant de la **performance**.  




## Web Feature Service (WFS)

- **Norme OGC** permettant d’accéder aux données vectorielles.  
- Diffuse les **géométries et attributs** (pas seulement une image).  
- Principales requêtes :  
  - **GetCapabilities** : description du service.  
  - **GetFeature** : récupération des objets (en GML, GeoJSON, etc.).  
  - **DescribeFeatureType** : structure des données.  
  - **Transaction (WFS-T)** : mise à jour / insertion / suppression (si autorisé).  

> :bar_chart: Permet une **analyse SIG complète côté client**.  


## Vector Tile Service (MVT)

- **Vector tiles** : tuiles contenant des données vectorielles (géométries + attributs), généralement au format **MVT (Mapbox Vector Tile)**.
- Avantages :
  - Affichage **rapide et fluide** même avec de grandes quantités de données.
  - **Personnalisation du style** côté client (couleurs, symboles, etc.).
  - Moins de bande passante qu’avec des images.
- Utilisation :
  - Compatible avec des bibliothèques web modernes (MapLibre, OpenLayers, etc.).
  - Permet des applications interactives et dynamiques.


> :triangular_ruler: Idéal pour des cartes web interactives et personnalisables à grande échelle.




## File-based (analyse & stockage)

* **GeoParquet** 🟢 (GDAL, OGC)
  ➝ Extension de Parquet pour données géospatiales (colonnaire, big data, analytique).
* **FlatGeobuf** 🟢 (GDAL, non-OGC)
  ➝ Format binaire compact, optimisé transfert rapide & web/mobile.

💡 Idéal pour l’**analyse** (requêtes attributaires/spatiales), mais pas pensé pour la visualisation directe.


## Tiled-based (visualisation & diffusion)

* **COMTiles** (2022)
  ➝ Archive streamable pour tuiles, cloud-optimisé (S3, Azure).
* **PMTiles** (2021) 🟢 (GDAL)
  ➝ Archive unique de tuiles (vecteur/raster), hébergeable “serverless” (S3, GitHub Pages).
* **Mapbox Vector Tiles (MVT)** 🟢 (OGC Community Std)
  ➝ Format binaire standard pour diffusion web des vecteurs, interactif & rapide.

💡 Idéal pour la **visualisation web** (MapLibre, Leaflet, OpenLayers).





## Tester la publication du projet

- Une fois le projet QGIS paramétré, vous pouvez tester sa diffusion via QGIS Server.
- Ouvrez dans votre navigateur l’URL suivante :

```url
http://localhost/cgi-bin/qgis_mapserv.fcgi.exe?MAP=C:\qgis\cfgeo.qgz&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities
````

* Si la configuration est correcte, vous obtenez le **document XML GetCapabilities** décrivant :

  * Les couches publiées.
  * Les systèmes de coordonnées.
  * Les options disponibles pour le service WMS.

> \:mag\_right: Ce test permet de vérifier que QGIS Server **répond bien** et que votre projet est accessible.



## Comparaison WMS / WMTS / WFS

| Service | Diffuse quoi ? | Format de sortie | Points forts | Limites |
|---------|----------------|------------------|--------------|---------|
| **WMS** | Images (cartes rendues) | PNG, JPEG | Simple, standard, supporté partout | Moins performant, pas d’accès aux données |
| **WMTS** | Tuiles d’images | PNG, JPEG | Rapide (cache de tuiles), idéal web | Pré-découpage → moins flexible |
| **WFS** | Données vectorielles (géométries + attributs) | GML, GeoJSON, etc. | Accès aux données, analyse possible côté client | Plus lourd, performances limitées sur gros volumes |





## Tester l’affichage d’une couche (GetMap)

- Après le test *GetCapabilities*, on peut vérifier le rendu d’une couche précise.  
- Exemple avec la couche **`bf`** :  

```url
http://localhost/cgi-bin/qgis_mapserv.fcgi.exe?MAP=C:\qgis\cfgeo.qgz&LAYERS=bf&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&CRS=EPSG:2056&WIDTH=400&HEIGHT=200&BBOX=2534472,1176780,2541983,1182660
````

* Paramètres principaux :

  * **LAYERS** : nom de la couche à afficher (`bf`).
  * **CRS** : système de coordonnées (`EPSG:2056`).
  * **BBOX** : emprise de la carte.
  * **WIDTH / HEIGHT** : dimensions de l’image.

> \:framed\_picture: Le résultat est une **image générée par QGIS Server**, confirmant que la couche est bien publiée.

