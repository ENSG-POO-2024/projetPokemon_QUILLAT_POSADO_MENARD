from PyQt5.QtCore import QTimer

# Créer un objet QTimer
timer = QTimer()

# Définir une fonction à exécuter après 2 secondes
def on_timeout():
    print("Attente de 2 secondes terminée")
    # Insérez ici le code à exécuter après l'attente

# Connecter la fonction à exécuter au signal timeout du QTimer
timer.timeout.connect(on_timeout)

# Démarrer le QTimer pour une attente de 2 secondes
timer.start(2000)
