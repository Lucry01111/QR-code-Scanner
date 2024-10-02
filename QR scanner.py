import cv2

def scan_qr_code_live():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    # Store the last read QR code
    last_qr_code = None
    while True:
        # Read the frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error capturing the frame.")
            break
        # Decode the QR code from the frame
        data, bbox, _ = detector.detectAndDecode(frame)

        # If a QR code is detected and it's not the same as the last one read
        if data and data != last_qr_code:
            print(f"QR Code found: {data}")
            last_qr_code = data  # Update the last read QR code

        # If the bounding box has been detected, draw a rectangle
        if bbox is not None:
            bbox = bbox.astype(int)  # Convert the bounding box values to integers
            for i in range(len(bbox[0])):
                cv2.line(frame, tuple(bbox[0][i]), tuple(bbox[0][(i+1) % len(bbox[0])]), (255, 0, 0), 3)
        cv2.imshow("Real-time QR Code Scanner", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the webcam and close the windows
    cap.release()
    cv2.destroyAllWindows()

scan_qr_code_live()
