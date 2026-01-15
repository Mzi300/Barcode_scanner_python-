
import cv2
from pyzbar import pyzbar

# Initialize WebCam
video_capture = cv2.VideoCapture(0)

print("Barcode Scanning in Progress. Press Q to Quit")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Detect barcodes
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x,y), (x + y + h + w), (0,255,0), 2)

    barcode_data = barcode.data.decode("utf-8")
    barcode_type = barcode.type

    # Display Barcode Info
    text = f"{barcode_data} {barcode_type}"
    cv2.putText(name, text, (x + 6, y - 6), cv2.FONT_HERSHEY_SIMPLEX, (0,255,0), 0.5, 2)

    print(f" Detected: {barcode_data}{barcode_type}")

    cv2.imshow("Barcode Scanner", frame)

    if cv2.waitKey(1) & 0*FF == ord("q"):
        break

    video_capture.release()
    cv2.destroyAllWindows()




































