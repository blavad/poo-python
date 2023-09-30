# TP 4 : UML

Dans ce TP, on s'intéresse à la conception de logiciels en utilisant la modélisation UML. 

Les compétences travaillées durant cette activité sont les suivantes : 

- Comprendre une description textuel d'un système logiciel
- Comprendre une description UML d'un système logiciel
- Décrire un système logiciel dans ses premières phases de conception

En particulier:
- Comprendre et réaliser un **diagramme de cas d'utilisation** 
- Comprendre et réaliser un **modèle du domaine** 
- Comprendre et réaliser un **diagramme de classe participantes** 
- Comprendre et réaliser un **diagramme de séquences** 


## Partie 1 : Comprendre UML (30 min)

<img src="assets/exo-uml1-graphical-shapes.png" alt="drawing" width="300"/>

Etant donné le diagramme de classes ci-dessus représentant des objets graphiques, répondre aux questions suivantes :
1. L'attribut **diameter** est-il accessible pour un objet **Square** ?
1. Un objet **Circle** possède-t-il un attribut **color** 
1. Peut-on appliquer la méthode **move** à un objet **Point** ?
1. Grâce à quelle notion de l'approche objet, la méthode **rotate** peut-elle être présente dans toutes les classes du diagramme et à quoi sert cette notion ?
1. a. Quelle hypothèse doit-on considérer pour rendre la classe **GraphicalShape** abstraite ?
    
    b. Quel est l'intérêt d'éviter que cette surclasse soit concrète ?
    
    c. Quelle modification doit-on apporté au diagramme de classes ?

1. Proposez une extension du modèle permettant d'obtenir un objet graphique composé de plusieurs autres objets graphiques.

## Partie 2 : Classes et relations (30 min)

1. Représenter une classe décrivant des livres électroniques. Les informations spécifiques à chaque livre sont : son titre, son nombre de page et le nom de l'auteur. Les actions possibles sont *pageSuivante* et *pagePrécédente*.

1. Décriver en UML un diagramme de classes illustrant la description suivante : une personne possède un ou plusieurs livres électronique.

1. Décriver en UML un diagramme de classes illustrant la description suivante : les disquettes, les clés USB et les disques durs sont des périphériques de stockage.

1. Un message électronique comporte un titre ainsi que l'adresse du destinataire. Il est composé d'un en-tête et d'un corps. Il peut contenir éventuellement une ou plusieurs pièces jointes. Tracez le diagramme de classes correspondant à cette description.


## Partie 3 : Commerce électronique
Voici la description d'un système de commerce électronique :
- Un utilisateur (client) qui se connecte à un site de commerce électronique choisit parmi les produits proposés.
- Il remplit au fur et à mesure un panier virtuel comportant les produits à acheter.
- A tout moment, il peut ajouter ou supprimer un produit au panier.
- Le paiement s'effectue à l'aide d'une carte de crédit. Celle-ci n'appartient pas nécessairement à l'utilisateur.
- A la fin de la transaction, l'utilisateur peut soit valider sa commande ou l'annuler.


**1.** Décrivez le système à l'aide d'un diagramme de cas d'utilisation.

**2.** Décrivez le système à l'aide d'un diagramme de classes.

**3.** Complétez le diagramme en ajoutant le concept de client premium. Ce type de clients bénéficie d'une réduction pour ses achats et les informations de ses cartes de crédit sont sauvegardées par le système.

**4.** Décrivez le système à l'aide d'un diagramme de séquences.