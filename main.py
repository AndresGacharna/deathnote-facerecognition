from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np

app = FastAPI()

# Cargar el clasificador de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectar_rostros(imagen_bytes):
    # Convertir los bytes de la imagen en un array de NumPy
    np_arr = np.frombuffer(imagen_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if img is None:
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    return len(faces) > 0

@app.post("/detectar-humano")
async def detectar_humano(file: UploadFile = File(...)):
    imagen_bytes = await file.read()  # Leer el archivo de imagen
    resultado = detectar_rostros(imagen_bytes)  # Procesar la imagen
    return {"hay_humano": resultado}  # Retornar el resultado






# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cap= cv2.VideoCapture(0)

# while True:
#     _, img = cap.read()
#     gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1,4)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)
#     cv2.imshow('img', img)
#     k = cv2.waitKey(30)
#     if k == 27:
#         break
# cap.release()