import string

#Các hàm xử lý bao gồm hàm decrypt caesar,ROTN,ROT 13
def caesar_encrypt(text: str, k: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + k) % 26 + base)
            result += new_char
        else:
            result += char

    return result


def caesar_decrypt(text: str, k: int) -> str:
    return caesar_encrypt(text, -k)


def rot_n(text: str, n: int) -> str:
    return caesar_encrypt(text, n)


def rot13(text: str) -> str:
    return caesar_encrypt(text, 13)


# Brute force, hàm xử lý Brute force

def brute_force(text: str):
    print("\n=== Brute Force ===")
    for k in range(26):
        print(f"[Key {k:2}] {caesar_decrypt(text, k)}")


# =========================
# Auto detect
# =========================
COMMON_WORDS = [
    "THE", "AND", "HELLO", "YOU", "IS", "ARE",
    "FLAG", "CTF", "PICO", "THIS"
]


def score_text(text: str) -> int:
    text_upper = text.upper()
    score = 0

    for word in COMMON_WORDS:
        if word in text_upper:
            score += 1

    return score


def auto_detect(text: str):
    best_score = -1
    best_key = 0
    best_text = ""

    for k in range(26):
        decrypted = caesar_decrypt(text, k)
        score = score_text(decrypted)

        if score > best_score:
            best_score = score
            best_key = k
            best_text = decrypted

    print("\n=== Auto Detect ===")
    print(f"Best key: {best_key}")
    print(f"Decrypted: {best_text}")


# =========================
# Menu system
# =========================
def menu():
    while True:
        print("\n===== Caesar Cipher Tool =====")
        print("1. Encrypt (Caesar)")
        print("2. Decrypt (Caesar)")
        print("3. ROT N")
        print("4. ROT13")
        print("5. Brute Force")
        print("6. Auto Detect")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "0":
            print("Bye!")
            break

        text = input("Enter text: ")

        if choice in ["1", "2", "3"]:
            k = int(input("Enter key (number): "))

        if choice == "1":
            print("Result:", caesar_encrypt(text, k))

        elif choice == "2":
            print("Result:", caesar_decrypt(text, k))

        elif choice == "3":
            print("Result:", rot_n(text, k))

        elif choice == "4":
            print("Result:", rot13(text))

        elif choice == "5":
            brute_force(text)

        elif choice == "6":
            auto_detect(text)

        else:
            print("Invalid choice!")


# =========================
# Run
# =========================
if __name__ == "__main__":
    menu()