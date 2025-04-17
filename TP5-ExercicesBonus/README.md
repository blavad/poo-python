# TP n°5 : Exercices complémentaires

Dans un python notebook.

### Exercice 1 : Logiciel de gestion d'une école

1. Créer une classe `Etudiant` qui permet de gérer et créer des étudiants. Cette classe devra contenir les méthodes ci-dessous et les attributs adéquats à l'exécution des méthodes :

   - méthode `ajouter_note` qui ajoute une note à la liste des notes de l'étudiants (la liste est initialement vide)
   - méthode `calculer_moyenne` qui calcule la note moyenne de étudiant et la retourne (on suppose qu'il n'y a pas de coefficient pour les notes)
   - méthode `afficher` qui affiche le nom, le prénom et l'école de l'étudiant (exemple: `Alan Turing de l'école IASchool`)

   ```
   Puis créer plusieurs objets du type `Etudiant` pour tester vos méthodes.
   ```

2. Créer une classe `Ecole` qui permet de gérer les étudiants d'une école. Cette classe doit contenir les méthodes suivantes et les attributs adéquats à leur exécution :

   - méthode `ajouter_etudiant` qui ajoute un étudiant à l'école (la liste d'étudiants est initialement vide)
   - méthode `retirer_etudiant` qui retire l'étudiant de l'école
   - méthode `calculer_moyenne` qui calcule la moyenne de l'école
   - méthode `afficher` qui affiche le nom de l'école et le nombre d'étudiants (exemple : `L'école IASchool compte 34 étudiants`)
   - méthode `afficher_liste_etudiants` qui affiche la liste de tous les étudiants de l'école
