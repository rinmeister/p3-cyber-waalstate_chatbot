from crypt import decrypt, bruteforce

def looks_plausible(data: int) -> bool:
    try:
        text = data
    except UnicodeDecodeError:
        return False
    allowed = all(("a" <= b <= "z") or ("A" <= b <= "Z") or (b in (".", ",", " ", ":")) or ("0" <= b <= "9") for b in data)
    return allowed and len(text) > 5

def brute_force(ciphertext):
    print("begin brute-force attack...")
    print(type(ciphertext))
    for key_int in range(512):
        candidate = bruteforce(ciphertext, key_int)
        if looks_plausible(candidate):
            print(f"Mogelijke sleutel: {key_int} {candidate}")

if __name__ == "__main__":
    input = input("Plak hier de response van de server: ")
    print(input)
    brute_force(input)

