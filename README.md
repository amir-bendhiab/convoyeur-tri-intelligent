# Convoyeur de tri de déchets intelligent

Projet académique — École Polytechnique Sousse (EPS) | Avril 2026

## Description
Système de tri automatique de déchets combinant vision par ordinateur et architecture robotique ROS2.
Le convoyeur détecte la couleur de chaque déchet et commande le servo de tri vers le bon bac.

## Architecture
Caméra → OpenCV (détection couleur) → ROS2 (décision) → Arduino (commande servo)

## Technologies
- **Vision** : OpenCV / Python — détection colorimétrique en temps réel
- **Robotique** : ROS2 Jazzy — 3 noeuds Python communicant via topics
- **Automatisme** : TIA Portal Siemens S7-1200 — programmation Ladder
- **Embarqué** : Arduino / C++ — contrôle des servomoteurs
- **CAO** : SolidWorks — modélisation mécanique du convoyeur

## Structure
opencv/
      detection_couleur.py   # Détection couleur par masque HSV
ros2/
      capteur_couleur.py     # Noeud 1 : publie la couleur détectée
      decision_tri.py        # Noeud 2 : décide le bac de destination
      commande_servo.py      # Noeud 3 : commande l'angle du servo
README.md

## Résultats
- Détection de 3 catégories : Plastique (bleu), Verre (vert), Métal (gris)
- Communication inter-noeuds via topics ROS2 : `/couleur_dechet` et `/commande_servo`
- Validation via simulation Factory I/O

## Auteur
**Amir Mokhtar BEN DHIAB**  
Élève ingénieur Génie Électromécanique — EPS Sousse  
[LinkedIn](https://linkedin.com/in/amir-mokhtar-ben-dhiab-8465182b7)
