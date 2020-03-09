# ELEF

> Authors: Adrien JACQUIER ([@adrien-jk](https://github.com/adrien-jk)), Clément LEMASSON ([@Orelfeu](https://github.com/Orelfeu)), Julien MARTIN-PRIN ([@Flexiboy](https://github.com/Flexiboy)), Léo LAMBERT ([@LeoDPlouc](https://github.com/LeoDPlouc)), Pierre-Victor LANDEZ ([@Tulbius](https://github.com/Tulbius))

# French version (English version below)

*Ce projet est réalisé dans le cadre du Projet PING (Projet d'ingénieur numérique généraliste) de 3ème année à l'ESILV*

## Description du projet

Elef est un assistant connecté visant à aider les patients atteints de la maladie d'Alzheimer. Pour cela, nous allons d'abord concevoir une enceinte doté d'un assistant vocal. Cet assistant restera limité et l'entrée utilisateur ne se fera que par écrit au travers d'une console dans un premier temps. Notre but est, à termes, de doter cet assistant d'une intelligence artificielle capable de reconnaitre la voix. L'enceinte communiquera cependant par oral avec son utilisateur.

Cet assistant embarquera des fonctions basiques, que l'on attend d'un assistant vocal, comme la gestion d'un calendrier ou des rappels. Mais comme nous nous adressons à des personnes atteintes de la maladie d'Alzheimer, nous allons aussi rappeler certains gestes du quotidien au patient comme le fait de ne pas mettre de métaux au micro-ondes par exemple ou rappeler une date d'anniversaire.

## Cible du projet

La cible de ce projet est les personnes atteintes de la maladie d'Alzheimer, c'est-à-dire une tranche assez agée de la population, n'étant pas forcément à l'aise avec les nouvelles technologies.

## Solution apportée

Comme présenté lors de la description du projet, nous allons concevoir un assistant vocal. Cet assistant communiquera par voie vocal et écrite avec son utilisateur. La voix humaine étant assez compliquée à reconnaître, nous avons choisi de nous contenter d'une entrée utilisateur par voie écrite pour notre prototype. Notre but est bien évidemment, à termes, de nous affranchir de l'interface console et de passer directement par voie orale.

La sortie sera cependant par voie orale car la voix humaine est bien plus simple à synthétiser.

Il faut cependant garder à l'esprit que nous nous adressons à une partie agée de la population n'étant pas forcément à l'aise avec la technologie. Il faudra donc penser à ne pas avoir une approche trop brute avec le patient.Pour cela, nous allons utiliser une voix féminine plutôt douce et nous allons surtout rappeler le fait que c'est une enceinte connectée avant chaque communication.

Pour le côté technique, nous allons utiliser une Raspberry PI 3 (4) ainsi que des haut-parleurs. L'alimentation sera gérée sur secteur et l'enveloppe esthétique de l'enceinte sera conçue par nos soins à l'aide de logiciels de modélisation et d'une imprimante 3D.

## OMT Diagram

<img src="images/OMT_Diagram.png" width=1000>

## Description des fonctions

**InputBase**

Cette classe est l'interface tampon entre l'entrée utilisateur est le programme. Elle fait la liaison entre l'interface de l'input et l'interface de la gestion de cette entrée. Cette classe est composée d'une seule fonction `int execute();` qui renvoie 0 si tout s'est bien déroulé.

**Input**

Cette classe est l'interface gérant l'entrée utilisateur. Elle recoit l'entrée utilisateur et la transmet au parseur qui se charge de séparer les mots pour une meilleure lisibilité au niveau de l'algorithme. elle est composée de deux fonctions, `void parse();` et `void execute();` qui ne retournent rien toutes les deux.

**InputParse**

C'est la classe qui parse notre entrée utilisateur. Elle prend toute l'entrée utilisateur en entrée et sépare chaque mot pour pouvoir faire une reconnaissance par mots clés. Elle est composée d'une seule méthode `vector<string> parse();` qui se charge de parser notre entrée utilisateur et renvoie un vecteur de chaines de caractères.

**KeywordRecognition**

Cette classe va nous permettre de reconnaitre les mots clés présents dans notre entrée utilisateur. Elle va prendre en entrée `vector<InputBase *> inp;` notre entrée parsée. Cette classe comporte une seule méthode `int execute();` qui retourne 0 si tout s'est bien passé.

**AppKeyword**

Cette classe va nous permettre d'orienter le flux d'instructions en reconnaissant le mot clé lié à l'application que l'on souhaite utiliser (calendrier, rappels, etc...). Cela va nous permettre de faire appel à différentes fonctions qui seront liées à l'application. Elle est composé d'une seule méthode `int execute();` qui renvoie 0 si tout s'est bien passé.

* **Calendar**: C'est la fonction calendrier de notre assistant elle comporte les méthodes `void create();` et `void consult();` qui permettent respectivement de créer un évènement ou de le consulter. La méthode `int execute();` vérifie que tout se passe bien et renvoie 0 si c'est le cas.
* **Reminders**: C'est la fonction qui gère les rappels. Elle agit comme la fonction calendrier
* **Weather**: C'est la fonction qui donne la météo. Elle agit comme la fonction calendrier à l'exception que l'on ne peut pas créer d'évènement.

**Watchout**

Cette classe est la classe gérant les rappels du quotidien. C'est à elle que l'on va faire appel quand il va s'agir de rappeler des gestes simples comme le fait de ne pas mettre de métaux dans le micro-ondes, ou de rappeler des emplacements d'affaires... Elle prend en entrée une liste prédéfinies de rappels qui se trouveront dans un fichier texte. Cette classe ne comporte qu'une seule méthode `void execute();` qui n'est là que pour exécuter la tâche.

**Timer**

Les rappels du quotidiens étants répétés à intervalle régulière, nous avons besoin d'un timer pour pouvoir les annoncer. Cette méthode aide donc à gérer la diffusion des rappels et ne comporte qu'une seule méthode: `void execute();`

**Output**

Cette classe est l'interface qui gère la sortie. Elle va créer une réponse à l'entrée utilisateur ou va créer la requête permettant la diffusion des rappels du quotidien. Elle n'est composée que d'une seule méthode `void execute();`

**OutputToVoice**

Cette méthode va convertir la sortie texte en sortie vocale, ce qui va permettre à l'enceinte de diffuser un son plutôt qu'un texte. Elle n'est composé que d'une seule fonction `void execute();` et prend en entrée la sortie déjà générée.

## Roadmap

# English version

*This project is realized as a student project only, through the PING project (Projet d'ingénieur généraliste numérique / Numeric generalist engineering project) in the 3rd year of engineering studies at ESILV*

## Project description

## Target of the project

## Solution brought

## OMT Diagram

<img src="images/OMT_Diagram.png" width=1000>

## Roadmap
