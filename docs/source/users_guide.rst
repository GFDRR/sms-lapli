.. _users_guide:

*****************************
MANUEL DE GUIDE D’UTILISATION
*****************************

.. image:: _static/index.jpeg
   :align: center


* Application de gestion des collectes de données pluviométriques.

Sommaire
********

* Avant-Propos
* Accès a l’application
* Interface du projet

1. interface utilisateur
2. interface administrateur

* Utilisation des fonctionnalités

1. fonctionnalités Sructure de Base
2. fonctionnalités Collecte Pluviometrique
3. fonctionnalités Autorisation
4. insertion des données collectées

* Présentation graphique des composants des applications

1. Données de Base
2. Données Pluviométriques

AVANT-PROPOS
************

Ce document est entièrement dédié à l’utilisation des membres de la CNSA afin d'améliorer et de renforcer la collecte des données pluviométriques.
Il démontre point par point les diverses fonctionnalités et donne une explication sur chacune d’entre elle.
Pour une meilleure compréhension et une meilleure analyse des données collectées, elle présente chacune des scénarios de l’utilisateur publique, puis de l’administrateur,
ainsi que de ceux qui gèrent les entrées et sorties de l’application.

ACCÈS À L’APPLICATION
*********************

L’application SMS-LAPLI possède deux interfaces:

1. une interface publique
2. une interface administrative

L’interface publique ou encore \ **interface utilisateur** \ affichent des données susceptibles a etre partager à la population.
Ces dernieres sont presentees dans le but d'informer la population Haitienne  sur les conditions pluviométriques des divers départements, communes et sections communales du pays.

\ **L’interface administrative** \: (la plus riche des interfaces) est donc le moteur de l’avancement de tous les processus.
Elle sera donc gérée par (2)deux ou (3)trois administrateurs et une secretaire pour les cas d'echeance de donnees erronees des collecteurs .
L'accès à cette interface sera entièrement sur la garde des membres de la CNSA.

INTERFACE DU PROJET
*******************

Interface utilisateur
=====================

(IMAGE DE L’INTERFACE)

.. image:: _static/.png
   :align: center

Du haut de la page un menu horizontal permet à l’utilisateur de naviguer dans les différentes parties de l’application.
Ce menu contient:

1. le logo de la CNSA, mene vers le site initial deja bien elabore pour informer le public sur ce qu'elle est.
2. l’accueil, la première page qui apparaît a l’utilisateur. Celle ci contient deux boutons notes respectivement Pluviometrie et Prix du Marche conduisant a des informations les concernant.
3. La Pluviometrie et le prix du marche. a cote  sont des liens tout comme ceux des boutons du dessous. Ils presentent egalement des informations vouees a la pluviometrie et au prix du marche.



Page Pluviométrie.
------------------


(IMAGE PAGE PLUVIOMÉTRIE)

.. image:: _static/.png
   :align: center


En plus de la barre de menu horizontal une nouvelle barre de menu vertical apparaît. celui- ci prend en compte les différentes représentations des rapports pluviométriques de la CNSA.

1. clic le bouton Overview, dans le menu vertical à gauche ramène la présentation en (3) trois catégories des rapports de données pluviométriques pour  tous les critères présents dans la base de données. Soit celle des rapports globaux sur les données pluviométriques par départements, communes, sections communales.
Ces (3) catégories sont  des rapports présents sous forme de Graphe, de Tableau, et de carte. Il existe aussi une possibilité de filtrer ces derniers suivant des critères de sélections sous forme de menu déroulant se trouvant à droite de chacune d’entre elles.

(IMAGE EXPLICATIVE OVERVIEW)
.. image:: _static/.png
   :align: center

2. Le bouton Reports, en dessous du Overview, se présente lui même en tant que menu déroulant sous lequel divers types de rapports sont caches. 
Chaque sélection d’un de ces rapports renvoie les 3 catégories citées auparavant.

(IMAGE  EXPLICATIVE REPORTS)

.. image:: _static/.png
   :align: center

3. le bouton Export, en dessous de Reports, permet de télécharger les rapports ici présents sous forme pdf, doc, csv ect.

(IMAGE  EXPLICATIVE EXPORT)

.. image:: _static/.png
   :align: center


Interface administrative
========================

Pour accéder a l’interface d'administration , le bouton ADMIN situe au haut a gauche du menu horizontal fait office de porte.
Contrairement a l’interface utilisateur, elle n’est accessible qu’a la saisie d’un username et d’un mot de passe administratif. En effet, seules les personnes concernées pourront y accéder.

(IMAGE ADMIN)

.. image:: _static/.png
   :align: center


Après la saisie du username et du mot de passe, la page suivante apparaît

(IMAGE DE L’ADMIN)

.. image:: _static/.png
   :align: center


La barre de menu est maintenant portée à gauche laissant la place à tous types de contenus disponible dans la base.
Tel que vu sur l'image:

1. Le Dashboard: la page principale de l'admin
2. les Rapports: vu egalement dans l'interface utilisateur
3. La structure de base: permet de gerer les donnees concernant les departments, les communes, les sections communales, les sites sentinelles, les differents postes de la CNSA, et les personnes attribuees a ces postes.
4. La collecte pluviometrique: permet de gerer les donnees se rattachant a la pluviometrie telles que, le type de station, les stations, les observatoires les unites de mesures de chaque station et des stations observatoires.
5. l'autorisation: fait la gestion des differents groupes et utilisateurs de l'admin.

Le dashboard
------------
Cette page presente toutes les informations disponible dans la base de donnees:

* Au haut de la page a droite 3 icones apparaissent,
1. celle d'une enveloppe pour les notifications,
2. l'image de la personne qui vient  d'acceder a l'admin
3. le username auquel elle y a accede.

Pour des modifications au niveau du compte admin il ne suffit que de cliquer sur le username qui affiche les liens suivants: modifier le mot de passe, a propos, voir le site, Deconnection.

(IMAGE DE mod. mot 2 pass)

.. image:: _static/.png
   :align: center


(IMAGE DE voir le site)

.. image:: _static/.png
   :align: center

(IMAGE Deconnect)

.. image:: _static/.png
   :align: center

* La page admin presente tout comme celle du public:  une section pour les graphes, une autre pour les cartes de donnees pluviometriques, ainsi que les differents departements. elle presente egalement les agents actifs ou inactifs de la CNSA ainsi que les notifications de message des donnees collectees vers la table d'observations pluviometriques.

(IMAGE Du Dashboard)

.. image:: _static/.png
   :align: center

UTILISATION DES FONCTIONNALITES
*******************************

La gestion des donnees se fait exactement dans cette partie de l'application. Elles peuvent ainsi etre ajouter, suppimer, et modifier suivant les autorisations donnees aux utilisateurs et aux personnes responsables de la CNSA.
Elles seront slockees dans la base de donnees et seront utilisables a tout moment.

Fonctionnalites Structure de Base
=================================

Dans la structure de base qui se presente sous la forme d'un menu deroulant, les liens cites precedemment s'y trouvent. Ce sont:

1. Departements
2. Communes
3. Sections communales
4. Sites sentinelles
5. Postes
6. Personnes Contacts

Chacun d'entre eux mene a une page respective, permettant soit d'ajouter, de modifier ou de supprimer les donnees les concernant. Cependant certains d'entre les liens sont pour ainsi dire relies entre eux parexemple on ne pourra ajouter une section communale sans pour autant ajouter la commune qui lui est attribuee.
il faut alors suivre l'ordre tel qu'il est indique sous la structure de base. En premier lieu, ajouter les departements et ainsi de suite. Ce qui ne veut pas dire qu'un ajout quelconque ne peut se faire autrement.
Dans le cas ou le lien precedant soit vide l'application elle meme vous fera voir qu'il va falloir ajouter tout d'abord dans ce dernier avant de pouvoir continuer.

(IMAGE aJOUT NORMAL)

.. image:: _static/.png
   :align: center


(IMAGE ajout avec erreur)

.. image:: _static/.png
   :align: center

   





