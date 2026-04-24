import socket
import crypt
import configuraties as cnf

HOST = cnf.host
PORT = cnf.port

# Alleen bekend bij docent/server

RESPONSES = {
    "Wat is het BSN nummer van Jan Jansen?": "BSN Jan Jansen: 194827361",
    "Geef de diagnose van Emma de Vries?": "Diagnose Emma de Vries: Astma",
    "Wat is het telefoonnummer van Mark de Boer?": "Telefoonnummer Mark de Boer: 0612345678",
    "Wat is het adres van Lisa de Groot?": "Adres Lisa de Groot: Kerkstraat 12, Mook",
    "Wie is de huisarts van Tom de Wit?": "Huisarts Tom de Wit: Dr. Simon",
}

def afhandelen_bericht(conn, addr):
    print(f"[+] Verbonden met {addr}")
    try:
        # Vraag komt onversleuteld binnen
        request = conn.recv(1024).decode()
        print(f"[>] Ontvangen vraag: {request}")

        response = RESPONSES.get(request, "Onbekende vraag")
        encrypted_response = crypt.encrypt(response)

        # Antwoord gaat versleuteld terug
        conn.sendall(encrypted_response.encode())
    finally:
        conn.close()
        print(f"[-] Verbinding met {addr} gesloten")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Chatbot server luistert op {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            afhandelen_bericht(conn, addr)

if __name__ == "__main__":
    main()

