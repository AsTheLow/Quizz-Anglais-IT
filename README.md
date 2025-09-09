QCM Interactif Python
=====================

Un petit programme Python pour s’entraîner à des questions à choix multiples (QCM). 
Il permet de : 
- Faire le quiz complet
- Faire un quiz aléatoire de n questions
- Refaire uniquement les questions ratées pour réviser

Fonctionnalités
---------------

1. Quiz complet
   - Parcourt toutes les questions de la liste.
   - Affiche votre score final à la fin.

2. Quiz aléatoire
   - Permet de choisir un nombre n de questions au hasard.
   - Affiche votre score final à la fin.

3. Questions ratées
   - Les questions auxquelles vous avez répondu incorrectement sont mémorisées.
   - Vous pouvez refaire uniquement ces questions pour vous entraîner.

4. Menu interactif
   - Choisissez l’action à effectuer depuis un menu clair.
   - Le programme continue de tourner jusqu’à ce que vous décidiez de quitter.

Comment l’utiliser
------------------

1. Exécuter le script
   python qcm_interactif.py

2. Choisir une option dans le menu :
   1. Faire le test complet
   2. Faire un quiz aléatoire
   3. Refaire uniquement les questions ratées
   4. Quitter

3. Répondre aux questions
   - Tapez a, b, c ou d pour répondre.
   - Le script vous dira immédiatement si vous avez répondu correctement 
     et affichera la bonne réponse si vous vous êtes trompé.

4. Réviser les erreurs
   - Les questions ratées sont stockées automatiquement.
   - En choisissant l’option 3 du menu, vous pouvez les refaire pour vérifier si vous avez appris.

Personnalisation
----------------

- Ajouter des questions :
  Les questions sont stockées dans une liste "questions". Chaque question est un dictionnaire avec les champs :

  {
      "question": "Texte de la question",
      "options": ["a. option1", "b. option2", "c. option3", "d. option4"],
      "answer": "a",  # lettre de la bonne réponse
      "full_answer": "Réponse complète correcte"
  }

- Modifier le nombre maximum de questions aléatoires :
  Le script limite automatiquement le nombre choisi au nombre total de questions disponibles.

Exemple de fonctionnement
-------------------------

Bienvenue au QCM interactif !
1. Faire le test complet
2. Faire un quiz aléatoire
3. Refaire uniquement les questions ratées
4. Quitter
Votre choix (1/2/3/4) : 1

1. Quelle est la traduction de 'Infrastructure de systèmes' en anglais ?
a. System infrastructure
b. Système infrastructure
c. Systemes infrastructure
d. Systems infrastructure
Votre réponse (a/b/c/d) : a
✅ Correct ! +1 point

Votre score final est 1 / 1
