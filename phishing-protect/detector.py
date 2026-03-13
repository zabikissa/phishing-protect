import re

MOTS_SUSPECTS = [
    "urgent", "verifier", "password", "mot de passe", "compte",
    "login", "banque", "click", "cliquez"
]

def analyze_mail(sender, subject, body):
    score = 0
    raisons = []

    sender = sender.lower()
    subject = subject.lower()
    body = body.lower()

    # Vérification mots suspects
    for mot in MOTS_SUSPECTS:
        if mot in subject or mot in body:
            score += 10
            raisons.append(f"mot suspect : {mot}")

    # Détection liens
    urls = re.findall(r'https?://\S+', body)
    if urls:
        score += 20
        raisons.append("lien détecté")

    # Expéditeur suspect
    if "support" in sender or "no-reply" in sender:
        score += 10
        raisons.append("expéditeur suspect")

    # Définition du niveau
    if score >= 50:
        niveau = "ÉLEVÉ"
    elif score >= 30:
        niveau = "MOYEN"
    else:
        niveau = "FAIBLE"

    return score, niveau, raisons
