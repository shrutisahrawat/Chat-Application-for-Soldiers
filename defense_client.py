import socket
from cryptography.fernet import Fernet

# Use the same key as the server (copy it from the server's output)
key = b'PxMnP_y0AQfmKzj1EzGtznLIQMwXG5pG90P9MQRW-pc='
cipher = Fernet(key)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9998))  # Connect to the server

    try:
        while True:
            # Take input from the user
            message = input("Enter message to send: ")
            
            # Encrypt the message before sending
            encrypted_message = cipher.encrypt(message.encode())
            client.sendall(encrypted_message)
            print(f"Encrypted message: {encrypted_message}")

            # Receive the encrypted response from the server
            encrypted_response = client.recv(1024)
            decrypted_response = cipher.decrypt(encrypted_response).decode()

            print(f"Server response: {decrypted_response}")

    except Exception as e:
        print("Error:", e)
    finally:
        client.close()

start_client()
