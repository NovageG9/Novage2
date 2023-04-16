# Novage2

Nouvelle version de Nouvage.
Web dynamique
Groupe 9


<img src="https://github.com/NovageG9/Novage2/blob/main/static/assets/images/logo2.png" alt="Your logo" title="Your logo"  />
<h1>Le nom du projet : NOVAGE</h1>




<H2>Background </H2>
Nous sommes une équipe entièrement constituée de 5 étudiants de l'Université de Toulouse 1 Capitole.<BR>

Le  but de ce projet est de faciliter l’utilisateur à trouver un lieu en France. <BR>

Les utilisateurs font une inscription et se connectent aussi sur ce site.<BR>

Chez Novage, les utilisateurs peuvent chercher avec facilité des lieux ou activités pour chaque région. ils peuvent partager les commentaires pour chaque lieu, ils peuvent  cliquer sur le like pour chaque lieu et aussi  rajouter de lieu favorable dans votre liste favorable.<BR>

Novage se  soucie d’offrir un service de qualité, des relations de confiance avec les utilisateurs et un sens de la communauté qui relie les utilisateurs et son équipe les uns aux autres. <BR>

Le lien ver le dossier Google Drive<BR>
<a href="https://docs.google.com/document/d/1yaC2_GxFr_GqfbpzW52bTUE6nbzf5xGNFtNh3AwWcWk/edit">Projet intégratif PMP</a><BR>
<a href="https://docs.google.com/presentation/d/1v5jUCV6jYN82gGwspAWEhQjGHpqWLswcL1h73yc1RMg/edit#slide=id.g1b9369e2784_2_82">Présentation Site web</a><BR>
<BR>

<H2>Related Efforts</H2>

Schéma entité-association:<BR>



Commentaire: <BR>

Dans le cadre d’une création de site web dont le thème est le voyage dans les régions françaises.
Un utilisateur possède un id, un pseudo, un mail, et un mot de passe. Il peut écrire plusieurs commentaires ou aucun. Un commentaire possède un id, une description et une note. Un commentaire est écrit par un unique utilisateur. Un commentaire est écrit par rapport à un seul lieu. Un lieu possède un id, un nom et une description. Les utilisateurs ont aussi la possibilité d’ajouter et liker des lieux favoris. Un lieu appartient à une ville qui possède un id et un nom. Dans une ville, il peut y avoir un ou plusieurs lieux à visiter. Une ville correspond à une région. Une région possède un id, un nom et une spécialité gastronomique. Le site donne aussi la durée conseillée de visite d’un lieu pour exercer une activité. Une activité possède un id, un nom et une description. <BR>

Schéma relationnel:<BR>

Utilisateur (idUti, pseudo, mailUti, mdpUti)
Commentaire (idCo, descCo, note, idUti*,idLieu*)<BR>
Lieu (idLieu, nomLieu, descLieu, idVille*)<BR>
Ajouter(idUti*, idLieu*)<BR>
Liker (idUti*, idLieu*)<BR>
Activite(idActivite, nomActivite, descActivite)<BR>
Exercer(idLieu*, idActivite*, dureeConseillee)<BR>
Recommander(idLieu*, idSaison*)<BR>
Saison (idSaison, nomSaison, moisSaison)<BR>
Ville(idVille, nomVille, idRegion*)<BR>
Region(idRegion, nomRegion)

<BR>
Afin de rendre le site dynamique, nous comptons utiliser MySQL pour stocker les données (à faire au second semestre).  
<BR>

<H2>Maintainers</H2><BR>

Scrum Master: Xiaoyun Tang<BR>
Product Owner: Anne Ndjeng<BR>
Les membres: Britney Rangith, Yinchen Wang<BR>

<H2>License</H2>
<BR>
MIT License
<BR>
Copyright (c) 2022 Novage
<BR>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
<BR>
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
<BR>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.








