# 🌳 Préparation d’un projet QGIS pour un levé avec QField

Mise en place d’un projet simple destiné au relevé d’un parc urbain avec QField.

---

## 1. Création des couches

Créez un nouveau projet QGIS et ajoutez les couches suivantes dans un **GeoPackage**.

### Arbre
**Type :** Couche de points (Point)  
**Attributs :**  
- `espece` *(texte)*  
- `diametre` *(nombre décimal)*  
- `note` *(texte)*  
- `photo` *(texte)*  

### Surface_Fleurs
**Type :** Couche de polygones (Polygone)  
**Attributs :**  
- `type_fleurs` *(texte)*  
- `surface_m2` *(nombre décimal – calculé automatiquement plus tard)*  
- `note` *(texte)*  
- `photo` *(texte)*  

### Banc
**Type :** Couche de points (Point)  
**Attributs :**  
- `materiau` *(texte)*  
- `etat` *(texte – valeurs possibles : "bon", "moyen", "mauvais")*  
- `photo` *(texte)*  

### Poubelle
**Type :** Couche de points (Point)  
**Attributs :**  
- `type` *(texte – valeurs possibles : "tri", "ordinaire")*  
- `capacite_litres` *(nombre entier)*  
- `photo` *(texte)*  

### Place_de_jeux
**Type :** Couche de polygones (Polygone)  
**Attributs :**  
- `nom` *(texte)*  
- `note` *(texte)*  
- `photo` *(texte)*  

---

## 2. Ajouter un fond de plan
Ajoutez un fond de plan adapté (ex. **OpenStreetMap** ou orthophoto) pour faciliter le repérage sur le terrain.

---

## 3. Configuration des formulaires

Pour simplifier la saisie sur le terrain :  
1. **Clic droit sur la couche** → *Propriétés* → *Formulaire d’attributs*.  
2. Pour les champs à valeurs prédéfinies (`etat` pour Banc, `type` pour Poubelle), définissez une liste de valeurs.  
3. Pour `surface_m2` :  
   - Décocher **Editable**  
   - Définissez la valeur par défaut avec :  

     ```qgis
     round($area, 2)
     ```

4. Enregistrez le projet avec un nom explicite, par exemple :  leve_parc_urbain.qgz

---

## 4. Préparation pour QField

### Avec QFieldSync
- Dans QGIS : `QFieldSync → Packager pour QField`  
- Un dossier contenant toutes les données nécessaires est créé, prêt à être transféré sur l’appareil mobile.

---

## Méthodes de transfert

### 1. Synchronisation manuelle (projet seul, sans Cloud)
1. Connectez l’appareil mobile à l’ordinateur.  
2. Copiez le dossier (**projet .qgz + GeoPackage .gpkg**) sur l’appareil.  
3. Ouvrez le projet dans QField.

### 2. Travail en équipe (synchronisation manuelle, sans Cloud)
1. Packager le projet avec QFieldSync.  
2. Copier le dossier sur chaque appareil.  
3. Au retour du terrain : `QFieldSync → Synchroniser depuis QField`.

### 3. Synchronisation via QFieldCloud
1. Dans QGIS : `QFieldSync → Créer un nouveau projet`.  
2. Sur QField : *Projets QFieldCloud → Télécharger le projet*.  
3. Synchroniser les modifications directement via le Cloud.

---

# 🗺️ Relevés sur le terrain

## Ouvrir et naviguer
- Ouvrir le projet `leve_parc_urbain.qgz` dans QField.  
- Naviguer : zoom, déplacement sur la carte.

## Ajouter un point (ex. : Banc)
1. Sélectionner la couche **Banc**.  
2. Appuyer sur **"+"** pour ajouter une entité.  
3. Le GPS positionne automatiquement le point.  
4. Remplir les attributs (`materiau`, `etat`).  
5. Sauvegarder.

## Ajouter un polygone (ex. : Surface_Fleurs)
1. Sélectionner la couche **Surface_Fleurs**.  
2. Appuyer sur **"+"** et tracer la zone en ajoutant des sommets.  
3. Fermer le polygone.  
4. Remplir les attributs.  
5. La surface est calculée automatiquement.

## Prendre une photo
- Dans le formulaire d’attributs, appuyer sur l’icône appareil photo.  
- Prendre la photo : elle sera automatiquement liée à l’entité.

---

## Sauvegarde et retour au bureau

- Sauvegarder régulièrement pendant le relevé.  

### Méthodes possibles :
- **Manuelle (projet seul)** : copier le dossier des levés sur l’ordinateur.  
- **Manuelle en équipe** : copier les données puis `QFieldSync → Synchroniser depuis QField`.  
- **QFieldCloud** : ouvrir le projet dans l’explorateur QGIS via QFieldCloud puis `QFieldSync → Synchroniser depuis QField`.
