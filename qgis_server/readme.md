# 🗺️ Mise en place de QGIS Server sur un Windows Server 2022 (AWS)

## 🎯 Objectif

Déployer QGIS Server sur une instance **Windows Server 2022 EC2 (AWS)**, sans passer par WSL, pour servir des cartes via **WMS/WFS** à partir de projets QGIS.

---

## 📦 Prérequis

- Compte AWS avec droits pour lancer une instance EC2
- Notions de QGIS (projets, couches, etc.)
- Savoir se connecter à une instance Windows via RDP
- QGIS Desktop et QGIS Server via OSGeo4W
- Serveur web (Apache via OSGeo4W)

---

## ☁️ Étape 1 – Créer une instance Windows Server 2022 sur AWS

1. Connectez-vous à la console AWS
2. Allez dans **EC2 > Lancer une instance**
3. Choisissez l’AMI : `Microsoft Windows Server 2022 Base`
4. Instance type : `t2.medium` ou mieux
5. Stockage : minimum 30 Go
6. Groupe de sécurité :
   - Autoriser **RDP (3389)** pour accès
   - Autoriser **HTTP (80)** pour QGIS Server
7. Lancer l’instance
8. Se connecter via Bureau à distance (RDP)

---

## 🛠️ Étape 2 – Installer QGIS Server et Apache

### 1. Télécharger OSGeo4W (Advanced Installer)

- Lien : [https://qgis.org/en/site/forusers/download.html](https://qgis.org/en/site/forusers/download.html)
- Télécharger **OSGeo4W Network Installer (Advanced Install)**

### 2. Lancer le setup :

1. Choisir : `Advanced Install`
2. Sélectionner :
   - `qgis-ltr-full`
   - `qgis-ltr-server`
   - `apache` (via `httpd` package)
3. Laissez le reste par défaut
4. Installer (peut prendre plusieurs minutes)

### 3. Vérifier l’installation

- Apache : `C:\OSGeo4W\apps\apache\bin\httpd.exe`
- QGIS Server : `C:\OSGeo4W\bin\qgis_mapserv.fcgi.exe`

---

## 🔧 Étape 3 – Configurer Apache avec QGIS Server

### 1. Modifier le fichier `httpd.conf`

Fichier : `C:\OSGeo4W\apps\apache\conf\httpd.conf`

Ajouter à la fin :

```apache
ScriptAlias /qgis/ "C:/OSGeo4W/bin/qgis_mapserv.fcgi.exe/"

<Directory "C:/OSGeo4W/bin">
    SetHandler fcgid-script
    Options +ExecCGI
    AllowOverride None
    Require all granted
</Directory>
```

> 💡 Attention aux slashs `/` au lieu des antislashs `\`.

### 2. Ajouter le support FastCGI (si manquant)

Dans le `httpd.conf`, vérifier que ces modules sont chargés :

```apache
LoadModule fcgid_module modules/mod_fcgid.so
LoadModule alias_module modules/mod_alias.so
```

---

## 📁 Étape 4 – Créer et préparer un projet QGIS

1. Ouvrir **QGIS Desktop**
2. Créer un projet `.qgs` avec les couches nécessaires
3. Enregistrer le projet dans un dossier accessible :
   ```
   C:\qgis_projects\monprojet.qgs
   ```

---

## 🌐 Étape 5 – Tester QGIS Server (WMS)

### 1. Démarrer Apache

- Exécuter :
  ```
  C:\OSGeo4W\apache-install.bat
  ```
- Ou manuellement :
  ```
  C:\OSGeo4W\apps\apache\bin\httpd.exe
  ```

### 2. Construire l’URL WMS

```
http://<IP_DU_SERVEUR>/qgis/qgis_mapserv.fcgi.exe?MAP=C:/qgis_projects/monprojet.qgs&SERVICE=WMS&REQUEST=GetCapabilities
```

### 3. Tester dans QGIS

- QGIS Desktop > Ajouter une couche WMS/WMTS
- Coller l’URL ci-dessus

---

## 🔐 Étape 6 – Sécurisation et options

- **Limiter l’accès** avec des règles de sécurité AWS (IP autorisées)
- **SSL** possible via un reverse proxy (ex : Apache avec Certbot sous Linux)
- **Authentification HTTP Basic** via `.htaccess` si besoin
- **Optimiser les performances** avec cache (ex : QGIS Server + MapProxy)

---

## ✅ Résultat attendu

Vous pouvez maintenant servir vos projets QGIS sous forme de services WMS/WFS depuis un serveur Windows 2022 sur AWS, consultables depuis un navigateur, QGIS Desktop, ou une application web.

---

## 📎 Exemple de lien WMS fonctionnel

```
http://<IP_DU_SERVEUR>/qgis/qgis_mapserv.fcgi.exe?MAP=C:/qgis_projects/test.qgs&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities
```
