import cv2

def scan_qr_code_live():
    # Apri la webcam
    cap = cv2.VideoCapture(0)

    # Crea il rilevatore QR
    detector = cv2.QRCodeDetector()

    while True:
        # Leggi il frame dalla webcam
        ret, frame = cap.read()

        if not ret:
            print("Errore nell'acquisizione del frame.")
            break

        # Decodifica il QR code dal frame
        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            print(f"QR Code trovato: {data}")

        # Disegna un riquadro attorno al QR code, se rilevato
        if bbox is not None:
            for i in range(len(bbox)):
                cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), (255, 0, 0), 3)

        # Mostra il frame
        cv2.imshow("QR Code Scanner in tempo reale", frame)

        # Premi 'q' per uscire
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Rilascia la webcam e chiudi le finestre
    cap.release()
    cv2.destroyAllWindows()

# Avvia lo scanner in tempo reale
scan_qr_code_live()