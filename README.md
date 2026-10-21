# MuJoCo Robotique

Projet d'apprentissage de la robotique avec le simulateur [MuJoCo](https://mujoco.org/) : de la simulation d'un bras robotique jusqu'au pick-and-place, en passant par la cinématique, la commande, la perception et l'apprentissage.

Ce dépôt documente ma progression étape par étape, dans le cadre de mon master en robotique.

## Qu'est-ce que MuJoCo ?

MuJoCo (*Multi-Joint dynamics with Contact*) est un moteur physique open source développé par Google DeepMind. Il est très utilisé en recherche en robotique et en apprentissage par renforcement, car il est rapide, précis et gère bien les contacts.

Une simulation MuJoCo repose sur deux objets :

- **`model`** (`MjModel`) : ce qui ne change pas — géométrie, masses, articulations, moteurs. Il est chargé depuis un fichier XML (format MJCF).
- **`data`** (`MjData`) : l'état courant — positions (`qpos`), vitesses (`qvel`), commandes moteurs (`ctrl`).

Chaque pas de simulation suit la même boucle : lire l'état → calculer une commande → `mj_step` → afficher.

## Installation

Testé sur macOS avec Python 3.

```bash
# 1. Cloner ce dépôt
git clone https://github.com/TON_PSEUDO/mujoco-robotique.git
cd mujoco-robotique

# 2. Créer et activer un environnement virtuel
python3 -m venv mujoco-env
source mujoco-env/bin/activate

# 3. Installer les dépendances
pip install mujoco numpy matplotlib

# 4. Récupérer les modèles de robots (MuJoCo Menagerie)
git clone https://github.com/google-deepmind/mujoco_menagerie.git
```

Vérifier l'installation :

```bash
python -m mujoco.viewer --mjcf=mujoco_menagerie/franka_emika_panda/scene.xml
```

## Utilisation

```bash
mjpython premier_test.py
```

> Sur macOS, les scripts qui ouvrent le visualiseur (`launch_passive`) doivent être lancés avec `mjpython` au lieu de `python`. Sur Linux et Windows, `python` suffit.

## Contenu

| Fichier | Description |
|---|---|
| `premier_test.py` | Charge le bras Franka Panda et fait osciller son premier axe avec une consigne sinusoïdale. |

## Feuille de route

- [x] Installer MuJoCo et faire bouger un robot par code
- [ ] **Cinématique** : cinématique directe et inverse (Jacobienne, moindres carrés amortis)
- [ ] **Commande** : PD articulaire, compensation de gravité, couple calculé, commande dans l'espace opérationnel
- [ ] **Trajectoires** : polynômes quintiques, profils trapézoïdaux, machine à états de pick-and-place
- [ ] **Perception** : caméra simulée, détection d'objet, estimation de position 3D
- [ ] **Apprentissage** : apprentissage par renforcement et par imitation
- [ ] **Réel** : transfert sur un bras physique (SO-101)

## Ressources

- [Documentation MuJoCo](https://mujoco.readthedocs.io/)
- [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) — collection de modèles de robots
- [Tutoriel Python officiel (Colab)](https://github.com/google-deepmind/mujoco#getting-started)
