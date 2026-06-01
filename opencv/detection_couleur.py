import cv2
import numpy as np

def detecter_dechet(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("ERREUR : image non trouvee")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    masque_vert = cv2.inRange(hsv, (40, 50, 50), (80, 255, 255))
    masque_bleu = cv2.inRange(hsv, (100, 50, 50), (130, 255, 255))
    masque_gris = cv2.inRange(hsv, (0, 0, 50), (180, 30, 200))

    if cv2.countNonZero(masque_vert) > 1000:
        resultat = "VERRE --> Bac vert"
        masque = masque_vert
    elif cv2.countNonZero(masque_bleu) > 1000:
        resultat = "PLASTIQUE --> Bac bleu"
        masque = masque_bleu
    elif cv2.countNonZero(masque_gris) > 1000:
        resultat = "METAL --> Bac gris"
        masque = masque_gris
    else:
        resultat = "Inconnu --> Bac general"
        masque = None

    print("RESULTAT :", resultat)

    if masque is not None:
        contours, _ = cv2.findContours(masque, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            contour_max = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(contour_max)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(image, resultat, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imwrite("resultat.jpg", image)
    print("Image sauvegardee : resultat.jpg")

if __name__ == '__main__':
    detecter_dechet("dechet.jpg")
