import socket

HOST = "10.99.4.167"      # aanpassen naar server-IP indien nodig
PORT = 4242     # aanpassen naar server-poort indien nodig

QUESTIONS = [
    "Wat is het BSN nummer van Jan Jansen?",
    "Geef de diagnose van Emma de Vries?",
    "Wat is het telefoonnummer van Mark de Boer?",
    "Wat is het adres van Lisa de Groot?",
    "Wie is de huisarts van Tom de Wit?",
]

def main():
    print("Kies een vraag:")
    for i, q in enumerate(QUESTIONS, start=1):
        print(f"{i}. {q}")

    choice = int(input("Nummer: ")) - 1
    question = QUESTIONS[choice]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Vraag onversleuteld versturen
        s.sendall(question.encode())

        # Versleuteld antwoord ontvangen
        encrypted_response = s.recv(1024).decode()

    print("Encrypted response ontvangen:")
    print(encrypted_response)

if __name__ == "__main__":
    main()
