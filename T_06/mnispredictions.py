import sys
import os

# Usar el entorno virtual
python_env = r"C:\Users\maryo\Desktop\python\mnist_env\Scripts\python.exe"

if os.path.abspath(sys.executable).lower() != os.path.abspath(python_env).lower():
    os.execv(python_env, [python_env] + sys.argv)

# Librerías
import cv2
import tensorflow as tf
import numpy as np

# Cargar modelo
ruta_modelo = r"C:\Users\maryo\Desktop\python\mnist_model.keras"
model = tf.keras.models.load_model(ruta_modelo)

print("Modelo cargado correctamente")

# Buscar cámara USB
cap = None
camara_usada = None

for i in [1, 2, 3, 4, 0]:
    cam = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    if cam.isOpened():
        ret, frame = cam.read()

        if ret:
            cap = cam
            camara_usada = i
            break

    cam.release()

# Verificar cámara
if cap is None:
    print("No se encontró ninguna cámara")
    sys.exit()

print("Cámara encontrada:", camara_usada)

# Captura
while True:

    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer la cámara")
        break

    # Pantalla de predicción
    image_prediction = np.zeros(
        (250, 200, 3),
        dtype=np.uint8
    )

    # Escala de grises
    frame_gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Imagen binaria
    _, binary = cv2.threshold(
        frame_gray,
        127,
        255,
        cv2.THRESH_BINARY_INV
    )

    # Buscar contornos
    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # 5 contornos más grandes
    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )[:5]

    # Revisar contornos
    for cnt in contours:

        # Ignorar contornos pequeños
        if cv2.contourArea(cnt) > 3000:

            x, y, w, h = cv2.boundingRect(cnt)

            # Buscar formas verticales
            if h > 0 and w / h < 1:

                # Ampliar recorte
                y_ini = y - h // 10
                y_fin = y + h + h // 10

                # Margen horizontal
                w_portion = (
                    int(y_fin - y_ini) - w
                ) // 2

                x_ini = x - w_portion
                x_fin = x + w + w_portion

                # Validar límites
                if (
                    y_ini >= 0
                    and x_ini >= 0
                    and y_fin <= frame.shape[0]
                    and x_fin <= frame.shape[1]
                ):

                    # Recortar número
                    crop_image = binary[
                        y_ini:y_fin,
                        x_ini:x_fin
                    ]

                    if crop_image.size == 0:
                        continue

                    # Convertir a 28x28
                    crop_resize_image = cv2.resize(
                        crop_image,
                        (28, 28)
                    )

                    # Normalizar
                    input_image = (
                        crop_resize_image.astype("float32")
                        / 255.0
                    )

                    # Convertir a 784
                    input_image = input_image.reshape(
                        1,
                        28 * 28
                    )

                    # Predicción
                    prediction = model.predict(
                        input_image,
                        verbose=0
                    )

                    # Clase predicha
                    predicted_class = np.argmax(
                        prediction,
                        axis=1
                    )[0]

                    # Porcentaje
                    porcentaje = (
                        prediction[0][predicted_class]
                        * 100
                    )

                    print(
                        "Predicción:",
                        predicted_class,
                        f"- {porcentaje:.1f}%"
                    )

                    # Rectángulo original
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + w, y + h),
                        (255, 0, 0),
                        2
                    )

                    # Rectángulo ampliado
                    cv2.rectangle(
                        frame,
                        (x_ini, y_ini),
                        (x_fin, y_fin),
                        (0, 255, 0),
                        2
                    )

                    # Mostrar recorte
                    cv2.imshow(
                        "Numero detectado",
                        crop_image
                    )

                    cv2.imshow(
                        "Numero 28x28",
                        crop_resize_image
                    )

                    # Mostrar porcentaje
                    cv2.putText(
                        image_prediction,
                        f"Prediccion: {porcentaje:.1f}%",
                        (5, 25),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 255),
                        1
                    )

                    # Mostrar número
                    cv2.putText(
                        image_prediction,
                        str(predicted_class),
                        (35, 210),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        6,
                        (0, 255, 255),
                        3
                    )

    # Mostrar ventanas
    cv2.imshow("Camara USB", frame)
    cv2.imshow("Prediccion", image_prediction)
    cv2.imshow("Binaria", binary)

    # ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cerrar
cap.release()
cv2.destroyAllWindows()

