
##  Prérequis

Windows 10 ou 11

Python 3.10+

PowerShell ou terminal

(Optionnel) VSCode pour modifier les mails exemples

## Structure du projet

main.py : interface graphique

detector.py : analyse des mails et calcul du score

logs/ : historique des mails analysés

quarantine/ : mails mis en quarantaine

samples/ : mails exemples pour tester



## Utilisation

Cloner le projet :

git clone https://github.com/zabikissa/phishing-protect.git

cd phishing-protect

Lancer l’application :

python main.py

Saisir un mail ou choisir un mail exemple dans samples/

Cliquer Analyser le mail → Score et niveau de risque s’affichent

Cliquer Mettre en quarantaine si nécessaire

Vérifier logs/log.txt pour l’historique

## Public cible

Conçu pour Mr Toutlemonde, pédagogique, simple et interactif, pour sensibiliser au phishing et à la cybersécurité.~

