---
marp: true
paginate: true
header: "CFGEO - S2 - VM"
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

# Bases de données en géomatique

## PostgreSQL, PostGIS et fichiers géographiques

https://regislon.github.io/cfgeo_s2/base_donnees/

---

![alt text](image.png)

 Canada Land Inventory (CLI), which is often recognized as one of the first major GIS initiatives in the world

---

## Pourquoi une base de données en géomatique ?

* Gérer de grands volumes de données spatiales
* Garantir l’intégrité, la cohérence et la traçabilité
* Faciliter les requêtes spatiales complexes
* Travailler en équipe, sur des données partagées

---

## Fichiers géographiques vs base de données

| Fichiers SIG (ex: Shapefile, GeoPackage)     | Base de données (PostGIS) |
| -------------------------------------------- | ------------------------- |
| Stockage local                               | Stockage centralisé       |
| Accès séquentiel                             | Requêtes dynamiques (SQL) |
| Limité pour la mise à jour multi-utilisateur | Collaboration simplifiée  |
| Pas d’index spatial performant               | Index spatial performant  |


---

La majorité de la diffusion des données géographiques s’effectue via des bases de données. Toutefois, les données statiques, pour des raisons de performance, sont souvent diffusées sous forme de fichiers tuilés, comme le format MBTiles, par exemple. 

De nouveaux formats, tels que GeoParquet, permettent désormais un enregistrement efficace et une accessibilité accrue sans nécessiter de base de données ni de serveur de diffusion. Nous y reviendrons plus en détail dans la suite du cours.

---

# Bases de données spatiales : panorama

## Les principaux SGBD spatiaux

* **PostgreSQL/PostGIS** : open source, très utilisé en géomatique, riche en fonctions spatiales.
* **Oracle Spatial** : solution propriétaire, très puissante, intégrée à Oracle Database.
* **Microsoft SQL Server (avec extension spatiale)** : supporte les types geometry et geography, utilisé dans de nombreux environnements professionnels.

---

* **MySQL (Spatial Extensions)** : supporte les objets géométriques, moins avancé que PostGIS ou Oracle.
* **SpatiaLite** : extension spatiale pour SQLite, idéale pour des usages légers ou embarqués.
* **MongoDB (GeoJSON)** : base NoSQL avec support des requêtes spatiales simples.

---

## Comparatif des coûts de licence (estimation)

| SGBD Spatial                | Licence / Coût estimé                |
|-----------------------------|--------------------------------------|
| PostgreSQL/PostGIS          | Gratuit (open source)                |
| Oracle Spatial              | $$$$ (plusieurs milliers €/an/util.) |
| SQL Server (édition Entreprise) | $$$ (plusieurs milliers €/an/serveur) |
| MySQL (Spatial Extensions)  | Gratuit (open source)                |
| SpatiaLite                  | Gratuit (open source)                |
| MongoDB (GeoJSON)           | Gratuit (open source, offre cloud payante) |

Quelle est la limite de votre carte de crédit ? 

---

## Historique de PostgreSQL

* **1986** : Début du projet POSTGRES à l’Université de Californie, Berkeley, sous la direction de Michael Stonebraker (suite au projet Ingres).
* **1996** : Le projet devient PostgreSQL, ajout du support SQL.
* **Années 2000** : Adoption croissante dans le monde open source et en entreprise, enrichissement des fonctionnalités (transactions, index avancés, extensibilité).
* **Aujourd’hui** : PostgreSQL est reconnu comme l’un des SGBD open source les plus robustes, évolutifs et riches en fonctionnalités, avec une forte communauté et de nombreux contributeurs.

---

## Historique de PostGIS

* **2001** : Début du développement de PostGIS par Refractions Research pour ajouter des capacités spatiales à PostgreSQL.
* **2003** : Première version stable (1.0), ajout des types `geometry` et des fonctions spatiales de base.
* **2005** : Certification OGC (Open Geospatial Consortium) pour la conformité avec les standards spatiaux.
* **Années 2010** : Intégration de nouvelles fonctionnalités comme le support des types `geography`, des index GiST améliorés, et des fonctions avancées (ST_Cluster, ST_3D).
* **Aujourd’hui** : PostGIS est l’une des extensions spatiales les plus utilisées, avec un large écosystème d’outils compatibles (QGIS, GeoServer, etc.).

---

**PostGIS & Spatial Database History**


https://www.youtube.com/watch?v=ZO5ZAXtW0MU


---

## PostgreSQL + PostGIS

* **PostgreSQL** : Système de gestion de base de données relationnelle (SGBDR)
* **PostGIS** : Extension spatiale de PostgreSQL

  * Ajoute le type `geometry` et `geography`
  * Fonctions spatiales : distances, intersections, buffers, etc.
  * Indexation spatiale avec **GiST**

---


## Le modèle relationnel + spatial

```sql
CREATE TABLE batiments (
  id SERIAL PRIMARY KEY,
  nom TEXT,
  geom GEOMETRY(POLYGON, 2056)
);
```

* Chaque ligne représente un **objet géographique**
* La colonne `geom` contient la **géométrie**
* Le SRID (ex: 2056) indique le **système de projection**

---

## Requêtes spatiales avec PostGIS

```sql
-- Rechercher tous les bâtiments dans une zone
SELECT * FROM batiments
WHERE ST_Within(geom, ST_GeomFromText('POLYGON(...)', 2056));
```

* Requêtes puissantes grâce aux fonctions `ST_`
* Compatible avec QGIS, GeoServer, etc.

---

## Index spatial : accélérer les requêtes

```sql
CREATE INDEX batiments_geom_idx
ON batiments
USING GIST(geom);
```

* L’index GiST permet des recherches rapides
* Obligatoire pour les projets de grande envergure

---

## Intégration SIG + BDD

* QGIS peut se connecter directement à PostGIS
* Possibilité d’éditer, visualiser et filtrer les données
* Un seul lieu de vérité pour toutes les équipes

---

**Qgis est-il le seul à pouvoir se connecter à PostGIS ?**

Non, d'autres outils comme Pgadmin, GeoServer, MapServer, et même des langages de programmation comme Python (avec psycopg2) ou R (avec RPostgreSQL) peuvent se connecter à PostGIS.

---

## Qu'est-ce que PgAdmin ?

PgAdmin est un outil graphique open source pour gérer et administrer les bases de données PostgreSQL. Il offre une interface utilisateur intuitive pour :

* Créer, modifier et supprimer des bases de données, tables, et autres objets.
* Exécuter des requêtes SQL et visualiser les résultats.
* Gérer les utilisateurs et les permissions.
* Superviser les performances et surveiller l'activité de la base de données.


⚠️ : PgAdmin n'est pas une base de données, mais un SGBD.


---


## Résumé

* PostGIS transforme PostgreSQL en base spatiale puissante
* Idéal pour des projets collaboratifs et évolutifs
* Remplace avantageusement les fichiers plats (shapefile, etc.)
* Outil central dans une **Infrastructure de Données Spatiales (IDS)**

---
## Installation de PostgreSQL/PostGIS + PGAdmin

🛠️ Exercice : Installation de la base de données
📋 Instructions : à consulter ci-dessous
⏱️ Durée estimée : 20 minutes

---
## Procédure d'installation de PostgreSQL, PostGIS et PgAdmin

### 1. Installation de PostgreSQL
1. Rendez-vous sur le site officiel de PostgreSQL : [https://www.postgresql.org/download/](https://www.postgresql.org/download/).
2. Sélectionnez votre système d'exploitation (Windows).
3. Téléchargez et installez le programme d'installation approprié.
4. Pendant l'installation :
  - Configurez un mot de passe pour l'utilisateur `postgres`.
  - Notez le port par défaut (5432) et le chemin d'installation.

---

### 2. Installation de PostGIS
1. PostGIS est généralement inclus dans les distributions PostgreSQL modernes.
2. Si ce n'est pas le cas, installez-le via l'outil de gestion des extensions :
  ```sql
  CREATE EXTENSION postgis;
  ```
3. Vérifiez que PostGIS est bien installé :
  ```sql
  SELECT PostGIS_Full_Version();
  ```

### 3. Installation de PgAdmin
1. Téléchargez PgAdmin depuis [https://www.pgadmin.org/download/](https://www.pgadmin.org/download/).
2. Installez le logiciel en suivant les instructions pour votre système d'exploitation.
3. Lancez PgAdmin et connectez-vous à votre instance PostgreSQL en utilisant les informations configurées lors de l'installation.

### 4. Vérification de l'installation
1. Connectez-vous à PostgreSQL via PgAdmin.
2. Créez une nouvelle base de données.
3. Activez PostGIS dans cette base de données :
  ```sql
  CREATE EXTENSION postgis;
  ```
4. Testez une requête spatiale simple pour valider le bon fonctionnement.

### 5. Ressources supplémentaires
- Documentation PostgreSQL : [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- Documentation PostGIS : [https://postgis.net/documentation/](https://postgis.net/documentation/)
- Tutoriels PgAdmin : [https://www.pgadmin.org/docs/](https://www.pgadmin.org/docs/)

---
