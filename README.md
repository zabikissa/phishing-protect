# Analyseur de phishing

## Description
Projet pédagogique permettant de détecter des mails suspects et de les mettre en quarantaine. Accessible aux utilisateurs non-techniciens.

## Prérequis
- Windows 10 ou 11
- Python 3.10+
- PowerShell ou terminal
- (Optionnel) VSCode pour modifier les mails

## Structure
- `main.py` : interface graphique
- `detector.py` : analyse du mail et calcul du score
- `logs/` : historique des mails analysés
- `quarantine/` : mails mis en quarantaine
- `samples/` : mails exemples pour tester

## Utilisation
1. Ouvrir PowerShell et naviguer dans le dossier du projet
2. Lancer : `python main.py`
3. Saisir un mail ou choisir un mail exemple
4. Cliquer **Analyser le mail** → Score et niveau de risque affichés
5. Cliquer **Mettre en quarantaine** si nécessaire
6. Vérifier `logs/log.txt` pour l’historique

## Public
Conçu pour Mr Toutlemonde, pédagogique, simple et interactif
~
~

