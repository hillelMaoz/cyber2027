from collections import Counter
import itertools

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
    
    score = 0
    for char, freq in ENGLISH_FREQS.items():
        observed_freq = (counts.get(char, 0) / total) * 100
        score += observed_freq * freq  # ככל שההתאמה טובה יותר, הציון גבוה יותר
        
    return score

def decrypt_caesar(ciphertext):
    best_score = -1
    best_text = ""
    best_shift = 0
    
    for shift in range(26):
        plain = []
        for c in ciphertext:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                plain.append(chr((ord(c) - base - shift) % 26 + base))
            else:
                plain.append(c)
        decoded = "".join(plain)
        score = english_score(decoded)
        
        if score > best_score:
            best_score = score
            best_text = decoded
            best_shift = shift
            
    return best_shift, best_text

def decrypt_transposition(ciphertext):
    best_score = -1
    best_text = ""
    best_key = None
    
    n = len(ciphertext)
    for key_len in range(2, min(16, n)):
        num_rows = n // key_len
        if n % key_len != 0:
            num_rows += 1
            
        for perm in itertools.permutations(range(key_len)):
            grid = [''] * key_len
            extra = n % key_len
            
            idx = 0
            col_lengths = [num_rows if i < extra or extra == 0 else num_rows - 1 for i in range(key_len)]
            
            cols = {}
            for col_idx in range(key_len):
                c_len = num_rows if (extra == 0 or col_idx < extra) else num_rows - 1
                pass

    for cols_count in range(2, min(12, len(ciphertext))):
        for p in itertools.permutations(range(cols_count)):
            rows = len(ciphertext) // cols_count + (1 if len(ciphertext) % cols_count != 0 else 0)
            pass
            
    return "Optimal Key Found", "Decrypted Text"
