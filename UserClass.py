import sqlite3
import qrcode

class User:
    def __init__(self, uid, name, age):
        self.uid = uid
        self.name = name
        self.age = age

    def save_to_db(self):
        conn = sqlite3.connect("users.db")  # Connect to database
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uid TEXT PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        """)

        # Insert user data
        cursor.execute("INSERT INTO users (uid, name, age) VALUES (?, ?, ?)", (self.uid, self.name, self.age))
        conn.commit()
        conn.close()
        print(f"User {self.name} saved to database.")

    def generate_qr_code(self):
        """Generate a QR code with UID as the data."""
        qr = qrcode.make(self.uid)  # Create QR with UID
        qr.save(f"{self.uid}.png")  # Save as PNG file
        print(f"QR Code saved as {self.uid}.png")

# Take user input
if __name__ == "__main__":
    uid = input("Enter a unique User ID: ")
    name = input("Enter the User's Name: ")
    age = input("Enter the User's Age: ")

    # Create a new user object
    user = User(uid, name, int(age))
    user.save_to_db()
    user.generate_qr_code()
