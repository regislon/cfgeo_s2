# Module S2 "SIT systèmes" 

## Introduction
![ ](/ressources/planning/images/plan.png) 

## Installations
### Préambule
Merci d'installer les différents composants en suivant scrupuleusement les chemins d'accès et les nommages.

### Machine virtuelle
Vous disposez toutes et tous d'une machine virtuel sur Amazon. 
 - Ne pas oublier de stopper la machine après utilisation 
 
### Installation de PostgreSQL et PostGIS
Pour installer cette base de données avec son extention spatiale, veuillez procéder ainsi :
- Télécharger l'Installateur [PostgreSQL 14](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- Laisser les répertoire tels que proposés par défaut 
- User = "postgres"
- Mot de passe = "postgres" (A ne jamais faire dans la vraie vie, mais la on a le droit :-))
- Démarrer le stack buider pour installer postGIS (à la fin de l'installation)
- Démarrer PgAdmin pour vérifier que l'on peut se connecter à cette nouvelle base installée

Vidéo complète de l'installation [ici](https://github.com/regislon/cfgeo_s2/raw/main/ressources/postgres/videos/install.mkv).


### Installation de QGIS et QGIS server
Pour installer Qgis, nous allons utiliser OSGeo4W. OSGeo4W est une distribution de binaire d'un grand nombre de logiciels open source geospatial pour les environnements Windows

-  Télécharger l'Installateur [OSGEo4W](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe)
- Choisir l’option « Advanced Install »
- Répertoire d’installation : C:\OSGeo4W64
- Choisir qgis-lrt et qgis-lrt-server

Vidéo complète de l'installation [ici](https://github.com/regislon/cfgeo_s2/raw/main/ressources/qgis/videos/install.mkv).

### Création d'un premier projet QGIS
- Créer un projet QGIS, enregistrer-le sous C:\OSGeo4W64\apps\qgis-ltr\bin\cfgeo.qgz
- Ajouter ces [données](https://github.com/regislon/cfgeo_s2/raw/main/ressources/qgis/data/initial_load.gpkg).


### Installation d'Apache
-  Télécharger l'Installateur [XAMPP](https://www.apachefriends.org/download.html)
- Sélectionner uniquement que :

![ ](/ressources/apache/images/1.png) 

- Remplacer le fichier C:\xampp\apache\conf\httpd.conf par celui ci : ![httpd.conf](/ressources/apache/conf/httpd.conf)
- Ne pas oublier de redémarrer Apache à la fin de l'installation.

Vidéo complète de l'installation [ici](https://github.com/regislon/cfgeo_s2/raw/main/ressources/apache/videos/install.mkv).

### Test de la configuration GIS server + Apache
- Placer un projet QGIS nommé "cfgeo.qgz" dans
- Depuis un navigateur web sur la machine virtuelle (Edge par exemple), entrer :  [localhost/cgi-bin/qgis_mapserv.fcgi.exe?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities&map=cfgeo.qgz](localhost/cgi-bin/qgis_mapserv.fcgi.exe?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities&map=cfgeo.qgz)

### Installation de python 
-  Télécharger l'Installateur [python 3.9.9](https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe)
- Installer python dans le répertoire C:\Python\python-3.9.9-amd64

Vidéo complète de l'installation [ici](https://github.com/regislon/cfgeo_s2/raw/main/ressources/python/videos/install.mkv).

### Installation des libraries python
1.	Démarrer l’invite de commande windows (taper CMD dans la barre de recherche)
1. Se rendre dans le répertoire d’installation de python en tapant la commande suivante :``cd C:\Python\python-3.9.9-amd64\Scripts``
1. Installer ipython-sql  en tapant la commande suivante : ``pip install ipython-sql``
1. Installer jupyter en tapant la commande suivante : ``pip install jupyter``
1. Installer psycopg2 en tapant la commande suivante : ``pip install psycopg2``

### Installation des jupyter notebooks
1.	Créer un répertoire C:\Python_projects\cfgeo\notebooks
1.	Dézipper le contenu de ce [fichier](https://github.com/regislon/cfgeo_s2/raw/main/ressources/python/notebooks/s2_4_python_conditions.zip) dans ce répertoire 

### Démarrage de Jupyter Notebook
1.	Démarrer l’invite de commande windows
1.	Se rendre dans le répertoire du projet python « C:\Python_projects\cfgeo »
``cd C:\Python_projects\cfgeo\notebooks``
1.	Entrer la ligne de commande suivante :
``python -m notebook``
1.	Jupyter notebook doit se démarrer dans la fenêtre du navigateur 

