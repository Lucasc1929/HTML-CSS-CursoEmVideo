import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

videocapture = cv2.VideoCapture(0) # Qual camera usar

videocapture.set(10,50)    # ID 10 = BRILHO e medida


#videocapture.set(3,1920)    # ID 3 = WIDTH, e medida em pixeis
#videocapture.set(4,900)     # ID 4 = HEIGHT, medida em pixeis


while True:      # Várias imagens que formaram o vídeo
    ret, frame = videocapture.read() # Coletar imagens da camera
    faces = face_cascade.detectMultiScale(frame, 1.5, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        eyes = eye_cascade.detectMultiScale(frame, 1.1, 5)
        for (x1,y1,w1,h1) in eyes:
            cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 3)
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) == ord("q"): # Tecla para pressionar para finalizar
        break   # Se apertar a tecla, finaliza

videocapture.release() # Mostra o vídeo