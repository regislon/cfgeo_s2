# Installation de python 
-  Télécharger l'Installateur [python 3.9.9](https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe)
- Installer python dans le répertoire C:\Python\python-3.9.9-amd64

Vidéo complète de l'installation [ici](https://github.com/regislon/cfgeo_s2/raw/main/ressources/python/videos/install.mkv).

### Installation des libraries python
1.	Démarrer l’invite de commande windows (taper CMD dans la barre de recherche)
1. Se rendre dans le répertoire d’installation de python en tapant la commande suivante :``cd C:\Python\python-3.9.9-amd64\Scripts``
1. Installer ipython-sql  en tapant la commande suivante : ``pip install ipython-sql``
1. Installer jupyter en tapant la commande suivante : ``pip install jupyter``
1. Installer psycopg2 en tapant la commande suivante : ``pip install psycopg2``
1. Installer requests en tapant la commande suivante : ``pip install requests``

Vidéo de l'installation de la première librairie [ici](https://github.com/regislon/cfgeo_s2/raw/main/ressources/python/videos/pip.mkv).


### Installation des jupyter notebooks
1.	Créer un répertoire C:\Python_projects\cfgeo\notebooks
1.	Dézipper le contenu de ce [fichier](https://github.com/regislon/cfgeo_s2/raw/main/ressources/python/notebooks/s2_2_python.zip) dans ce répertoire 

### Démarrage de Jupyter Notebook
1.	Démarrer l’invite de commande windows
1.	Se rendre dans le répertoire du projet python « C:\Python_projects\cfgeo »
``cd C:\Python_projects\cfgeo\notebooks``
1.	Entrer la ligne de commande suivante :
``python -m notebook``
1.	Jupyter notebook doit se démarrer dans la fenêtre du navigateur 