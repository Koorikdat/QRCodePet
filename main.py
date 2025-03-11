import cv2
from pyzbar.pyzbar import decode
import sqlite3

def get_user_by_uid(uid):
    """Fetch user details from SQLite using UID."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE uid = ?", (uid,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return {"uid": user[0], "name": user[1], "age": user[2]}
    else:
        return None

def scan_qr():
    """Scan QR code and fetch user details from database."""
    cap = cv2.VideoCapture(0)  # Open webcam

    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            uid = barcode.data.decode("utf-8")  # Decode QR Code data
            print(f"Scanned UID: {uid}")

            # Fetch user info from database
            user_info = get_user_by_uid(uid)
            if user_info:
                print("User Info:", user_info)
            else:
                print("User not found.")

            cap.release()
            cv2.destroyAllWindows()
            return user_info

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    user_data = scan_qr()
    print("Fetched User Info:", user_data)
