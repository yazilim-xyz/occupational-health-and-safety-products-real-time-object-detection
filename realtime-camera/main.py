#occupational health and safety equipment detection

import cv2

# Kameraya bağlan (0: Varsayılan kamera, 1 veya 2: USB kameralar)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    # Kameradan kare yakala
    ret, frame = cap.read()
    
    if not ret:
        print("Görüntü alınamadı!")
        break

    # Görüntüyü göster
    cv2.imshow('Webcam', frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
