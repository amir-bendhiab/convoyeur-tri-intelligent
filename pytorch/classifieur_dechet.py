import torch
import torch.nn as nn
import torch.optim as optim

class ClassifieurDechet(nn.Module):
    def __init__(self):
        super().__init__()
        self.couche1 = nn.Linear(3, 8)
        self.activation = nn.ReLU()
        self.couche2 = nn.Linear(8, 3)

    def forward(self, x):
        x = self.couche1(x)
        x = self.activation(x)
        x = self.couche2(x)
        return x

# Donnees d'entrainement : couleurs RGB normalisees (0 a 1)
# 0 = plastique (bleu), 1 = verre (vert), 2 = metal (gris)
couleurs = torch.tensor([
    [0.0, 0.0, 1.0],
    [0.1, 0.1, 0.9],
    [0.0, 1.0, 0.0],
    [0.1, 0.9, 0.1],
    [0.5, 0.5, 0.5],
    [0.6, 0.6, 0.6],
], dtype=torch.float32)

etiquettes = torch.tensor([0, 0, 1, 1, 2, 2])

modele = ClassifieurDechet()
fonction_perte = nn.CrossEntropyLoss()
optimiseur = optim.Adam(modele.parameters(), lr=0.05)

print("Debut de l'entrainement...")
for epoque in range(200):
    optimiseur.zero_grad()
    sortie = modele(couleurs)
    perte = fonction_perte(sortie, etiquettes)
    perte.backward()
    optimiseur.step()

    if epoque % 50 == 0:
        print(f"Epoque {epoque} - Perte : {perte.item():.4f}")

print("Entrainement termine !")

test_bleu = torch.tensor([[0.05, 0.05, 0.95]])
prediction = modele(test_bleu)
classe = torch.argmax(prediction).item()
noms = ["PLASTIQUE", "VERRE", "METAL"]
print(f"Prediction pour une couleur bleue : {noms[classe]}")
