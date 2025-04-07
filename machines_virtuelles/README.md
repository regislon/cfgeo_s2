---
theme : "simple"
transition: "slide"
highlightTheme: "monokai"
logoImg: "logo.png"
slideNumber: true
title: "VSCode Reveal intro"
center: false
mouseWheel: true
---

# Système d'information géographique

--

## Définition 

Un système d’information géographique (SIG) est un outil permettant de collecter, gérer, analyser et visualiser des données géographiques pour mieux comprendre et prendre des décisions sur l’espace.

--

À votre avis, quels sont les composants d’un système d’information géographique ?

Par exemple :
- map.geoadmin.ch
- le guichet cartographique de votre canton ou commune
- celui de votre entreprise



--



--

Voici le schéma de notre SIG que nous allons mettre en place 🤘 

![alt text](image.png)


--

<!-- .slide: style="font-size: 0.6em" -->
 Cette liste présente de manière non exhaustive les différents éléments qui composent un système d'information géographique.

**Composants de base :**


| **Composant**                | **Rôle**                                                                 | **Exemples concrets**                              |
|------------------------------|--------------------------------------------------------------------------|----------------------------------------------------|
| **Base de données spatiale** | Stockage structuré des données géographiques et attributaires            | PostgreSQL + PostGIS, MSSQL,                    |
| **Serveur d’application**    | Traitement des requêtes, logique métier                                  | Apache, NGINX, Node.js, Gunicorn                   |
| **Serveur de diffusion SIG** | Publication des couches spatiales via des services web                   | GeoServer, MapServer, QGIS Server                  |
| **Système de fichiers / stockage** | Stockage de fichiers sources, tuiles, logs, backups              | Amazon S3, EBS, disque local, GCS                  |
| **API / Web services**       | Points de communication entre front-end et back-end, accès aux données            | REST, WFS, WMS, WMTS, GeoJSON API                  |


Les composants de base d’un système d’information géographique sont installés sur un serveur (physique, virtuel ou dans le cloud), et peuvent être déployés individuellement ou sous forme de conteneurs Docker pour une installation plus rapide, modulaire et reproductible.


--

Un serveur physique est un ordinateur dédié, puissant et généralement installé dans un centre de données, conçu pour faire fonctionner des services en continu, comme une base de données, un site web ou un système d’information géographique.

--


Un **serveur virtuel** est une machine simulée par un logiciel (hyperviseur) qui fonctionne comme un vrai serveur, mais partage les ressources (CPU, RAM, disque) d’un serveur physique avec d'autres machines virtuelles.


--

Un **serveur cloud** est un serveur virtuel hébergé dans un centre de données distant, accessible via Internet, et fourni à la demande par un prestataire (comme AWS, Azure ou Google Cloud), avec une grande flexibilité de ressources et de coûts.



---

<!-- .slide: style="font-size: 0.6em" -->
# Clients


Une telle infrastructure peut être utilisée par une entreprise, une administration publique ou un particulier pour gérer des données géographiques, créer des applications web, réaliser des analyses spatiales, etc.




| **Composant**                | **Rôle**                                                                 | **Exemples concrets**                              |
|------------------------------|--------------------------------------------------------------------------|----------------------------------------------------|
| **Client web**   | Interface utilisateur pour l’exploration et l’interaction avec les données | Leaflet, OpenLayers, MapLibre, React + Mapbox      |
| **Client desktop**      | Utilisation des données via un page web                                          | Qgis ArcGIS Pro    |
| **Client mobile**      | Utilisation des données via une application                                          | Qfield, ESRI Survey123   |



---

<!-- .slide: style="font-size: 0.6em" -->
# Distinction entre le backend et le frontend

Dans le développement d'applications web ou de systèmes d'information, on distingue généralement deux parties principales :

--

## 🖥️ Front-End

Le **front-end** correspond à la partie **visible par l'utilisateur**. C'est l'interface graphique avec laquelle l'utilisateur interagit directement, via un navigateur web.



--


## 🗄️ Back-End

Le **back-end** est la partie **invisible** pour l'utilisateur. Il gère la logique métier, les calculs, les accès aux bases de données, et les communications avec le front-end.

<center>
<iframe width="560" height="315" 
src="https://www.youtube.com/embed/3aGi-5kdM9g" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen>
</iframe>
</center>


--



## 🔁 Interaction entre Front-End et Back-End

Le front-end envoie des **requêtes** au back-end, qui traite les données et renvoie une **réponse** (souvent au format JSON).  
Cela permet de construire des applications web interactives et dynamiques.




---


# Machine virtuelle
Vous disposez toutes et tous d'une machine virtuel sur Amazon. 











### Divers
 - Depuis votre machine virtuelle, tapper "firewall" dans la recherche Windows et désactiver le firewall du private network
 ![ ](/ressources/aws/images/firewall.png)
