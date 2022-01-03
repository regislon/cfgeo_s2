# Module S2 "SIT systèmes" 

## Introduction

## Installations
### Préambule
Merci d'installer les différents composants en suivant scupuleusement les chemains d'accès et les nomages.

### Machine virtuelle
Vous disposez toutes et tous d'une machine virtuel sur exoscale. 
 - Ne pas oublier de stopper la machine après utilisation 
 - Ne pas oublier de de faire un snapshots et de le télécharger (au cas où)
 ![ ](/ressources/exoscale/images/snapshot.png)
- Une fois le snapshot effectué, il faut créer un template en utilisant les informations suivantes :
 ![ ](/ressources/exoscale/images/snapshot2.png)
 le template se crée icc :
  ![ ](/ressources/exoscale/images/snapshot3.png)
- Finalement, il faut "destroyer" la machine pour ne pas payer des frais de licence windows inutilement. 


 

### Installation de QGIS et QGIS server
Pour installer Qgis, nous allons utiliser OSGeo4W. OSGeo4W est une distribution de binaire d'un grand nombre de logiciel open source geospatial pour les environnements Windows

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




