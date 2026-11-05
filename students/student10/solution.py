from collections import Counter

ENGLISH_FREQS = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95,
    'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88,
    'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
    'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11,
    'J': 0.10, 'Z': 0.07
}

def english_score(text):
    text = text.upper()
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0.0
    counts = Counter(letters)
    total = len(letters)
    score = 0.0
    for char, freq in ENGLISH_FREQS.items():
        observed_freq = (counts.get(char, 0) / total) * 100
        score += observed_freq * freq
    return score

def decrypt_caesar(ciphertext, shift):
    plain = []
    for c in ciphertext:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            plain.append(chr((ord(c) - base - shift) % 26 + base))
        else:
            plain.append(c)
    return "".join(plain)

def break_caesar(ciphertext):
    best_score = -1
    best_text = ""
    best_shift = 0
    for shift in range(26):
        decoded = decrypt_caesar(ciphertext, shift)
        score = english_score(decoded)
        if score > best_score:
            best_score = score
            best_text = decoded
            best_shift = shift
    return best_shift, best_text

def decrypt_transposition(ciphertext):
    best_score = -1
    best_text = ""
    best_key_len = 0
    n = len(ciphertext)
    for key_len in range(2, n):
        num_rows = (n + key_len - 1) // key_len
        extra = n % key_len
        col_lens = [num_rows if (i < extra or extra == 0) else num_rows - 1 for i in range(key_len)]
        cols = {}
        curr = 0
        for col_idx in range(key_len):
            c_len = col_lens[col_idx]
            cols[col_idx] = ciphertext[curr:curr + c_len]
            curr += c_len
        plain_chars = []
        for r in range(num_rows):
            for c in range(key_len):
                if r < len(cols[c]):
                    plain_chars.append(cols[c][r])
        candidate = "".join(plain_chars)
        score = english_score(candidate)
        if score > best_score:
            best_score = score
            best_text = candidate
            best_key_len = key_len
    return best_key_len, best_text

if __name__ == "__main__":
    caesar_cipher = "ZNK ZKGS CUT ZNK SGZIN OT ZNK RGYZ SOTAZK GLZKX G RUTM GTJ JOLLOIARZ YKIUTJ NGRL YZAJKTZY CNU VXGIZOIK G ROZZRK KBKXE JGE AYAGRRE"
    transposition_cipher = "WHHN HN ETRINEMGOSNETRNCHTHHETTTI SSHELIVO LH DHBDKEHEE S HLTT E  GERTDEW EO E ENL OEDOOB UMHRNH RAT RCDWR IWU RLRYFNITYIEFMLOH H E TGETCEDI ITD  N IAK AAETAT"

    shift, caesar_plain = break_caesar(caesar_cipher)
    print(f"Caesar Shift: {shift}")
    print(f"Caesar Plaintext: {caesar_plain}\n")

    key_len, trans_plain = decrypt_transposition(transposition_cipher)
    print(f"Transposition Key Length: {key_len}")
    print(f"Transposition Plaintext: {trans_plain}")
