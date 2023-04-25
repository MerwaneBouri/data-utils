# Vectorisation 

Concept clé pour l'optimisation de code, remplacer des 
boucles traditionnelles par des opérations sur des matrices/vecteurs.

Au lieu d'itérer avec une opération à la fois, on parallèlise avec des 
fonctions vectorielles. Numpy et Scipy sont faits pour ça.

## Exemple Faster cloud Diameter 

Ce que fait le script :
- récupère 2 listes à partir d'un zip, qui représente les coordonnées x,y de points dans un repère 2D cartésien.
- le but est de trouver la distance la plus grande entre 2 points

La méthode la plus intuitive (brute) est pour chaque point, calculer les distances avec tous les autres points, et garder la plus grande distance.

La vectorisation permet de regrouper tous ces calculs en une seule fois. On va reshape l'array en une colonne et une ligne, numpy permet de créer une matrice automatiquement. Chaque élément dans la matrice correspond à une distance entre 2 points. 

TODO: faire un dessin pour avoir une intuition (notebook ?)
