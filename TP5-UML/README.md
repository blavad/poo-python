# TP 5 : UML

Dans ce TP, on s'intéresse à la conception de logiciels avec UML. Ce TP est en grande partie à réaliser sur papier.

Les compétences travaillées durant cette activité sont les suivantes :

- Comprendre une description textuel d'un système logiciel
- Comprendre une description UML d'un système logiciel
- Décrire un système logiciel dans ses premières phases de conception

En particulier:

- Comprendre et réaliser un **diagramme de cas d'utilisation**
- Comprendre et réaliser un **modèle du domaine**
- Comprendre et réaliser un **diagramme de classe participantes**
- Comprendre et réaliser un **diagramme de séquences**

## Partie I : Classes et relations

30 min

1. Représenter une classe décrivant des livres électroniques. Les informations spécifiques à chaque livre sont : son titre, son nombre de page et le nom de l'auteur. Les actions possibles sont _pageSuivante_ et _pagePrécédente_.

1. Décrire en UML un diagramme de classes illustrant la description suivante : une personne possède un ou plusieurs livres électronique.

1. Décrire en UML un diagramme de classes illustrant la description suivante : les disquettes, les clés USB et les disques durs sont des périphériques de stockage.

1. Un message électronique comporte un titre ainsi que l'adresse du destinataire. Il est composé d'un en-tête et d'un corps. Il peut contenir éventuellement une ou plusieurs pièces jointes. Tracez le diagramme de classes correspondant à cette description.

## Partie II : Commerce électronique

1h15

Voici la description d'un système de commerce électronique :

- Un utilisateur (client) qui se connecte à un site de commerce électronique choisit parmi les produits proposés.
- Il remplit au fur et à mesure un panier virtuel comportant les produits à acheter.
- A tout moment, il peut ajouter ou supprimer un produit au panier.
- Le paiement s'effectue à l'aide d'une carte de crédit. Celle-ci n'appartient pas nécessairement à l'utilisateur.
- A la fin de la transaction, l'utilisateur peut soit valider sa commande ou l'annuler.

**1.** Décrivez le système à l'aide d'un diagramme de cas d'utilisation.

**2.** Décrivez le système à l'aide d'un diagramme de classes.

**3.** Complétez le diagramme en ajoutant le concept de client premium. Ce type de clients bénéficie d'une réduction pour ses achats et les informations de ses cartes de crédit sont sauvegardées par le système.

**4.** Décrivez l'ajout d'un article dans le panier à l'aide d'un diagramme de séquences.

## Partie III :

30min

L'école GEMA a besoin de connaître les moyennes pour ses 3 filières (IASchool, CyberManagement et ...) pour toutes les matières et pour tous les étudiants.

On suppose que les filières ont le même nombre de matières.

1. Identifier les classes et décrire le diagramme de classe
2. Etablir un scénario (=diagramme de séquences) pour effectuer la moyenne de GEMA

## Partie IV : Donner le diagramme de classes correspondant au TP 3

30min

<!--

## Partie V: Emprunt d'un livre dans une bibliothèque

On considère la procédure d'emprunt d'un livre dans une bibliothèque par un adhérent connaissant le titre de l'ouvrage :

"L'adhérent présente sa carte d'abonné au préposé qui enregistre son passage. L'adhérent indique le titre du livre souhaité. Le préposé effectue une recherche automatique dans sa base pour vérifier l'existence et la disponibilité de l'ouvrage". Lorque la réponse est positive, il demande confirmation à l'adhérent. Celui-ci confirme. Le préposé va alors chercher le livre en tenant compte de sa localisation et le remet à l'adhérent. Le préposé valide l'emprunt et valide la carte mégnétique l'adhérent. Celui-ci récupère le livre et sa carte puis sort de la bibliothèque après avoir présenté l'ouvrage et la carte à un lecteur magnétique qui ouvre le portillon après vérification et retourne la carte et le livre.

1. Identifier les divers scénarios et les événements les déclenchant
2. Reformuler le texte en utilisant des diagrammes d'envoi de messages entre les objets de votre choix. Préciser les classes nécessaires et donner leur spécifications. -->
