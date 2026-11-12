from collections import Counter

# ==========================================
# Input: The encrypted text from the homework
# ==========================================
cipher_text = """CWB OIABDC AKMTBAD RIUMCBN CWB NBBA OAIX K DXKHH YHKMB OHJEMT HIL IZBA CWB CABBD CWB MBL GERJRHB YKCW RIMMBRCD CWB CAKEM DCKCEIM LECW CWB UMEZBADECJ RKXYUD CWB MBLDYKYBA YAEMCBN K RIAABRCEIM KOCBA ABKNBAD MICERBN KM BAAIA EM CWB LBKCWBA ABYIAC K DEMTHB RHIUN RKM LBETW XIAB CWKM K WUMNABN BHBYWKMCD JBC EC OHIKCD KGIZB UD CWB OBDCEZKH BMNBN LECW XUDER EM CWB DVUKAB KMN HETWCD WKMTEMT GBCLBBM CWB CABBD XIDC IO CWB LKCBA IM IUA YHKMBC ED DKHCJ KMN IMHJ K DXKHH YKAC RKM GB UDBN OIA NAEMFEMT CWB XUDBUX IYBMBN K MBL WKHH NBZICBN CI CWB WEDCIAJ IO RINBD XKRWEMBD KMN DBRABC XBDDKTBD HIMT KTI FEMTD DBMC XBDDBMTBAD IM WIADBGKRF KMN K ABYHJ RIUHN CKFB XKMJ LBBFD CI KAAEZB WIMBJ MBZBA DYIEHD GBRKUDB GBBD ABXIZB XIDC IO CWB LKCBA GBOIAB CWBJ DBKH CWB WIMBJRIXG CWB IHN XKY DWILBN AIKND CWKC MI HIMTBA BPEDCBN KMN ZEHHKTBD CWKN GBBM KGKMNIMBN CWB NBCBRCEZB MICERBN CWKC CWB RHIRF EM CWB WKHHLKJ WKN DCIYYBN KC BPKRCHJ XENMETWC ZIHUMCBBAD RHBKMBN CWB GBKRW CWB RIHHBRCBN XIAB YHKDCER GICCHBD CWKM KMJIMB WKN BPYBRCBN BKAHJ RIXYUCBAD OEHHBN BMCEAB AIIXD KMN LBAB HBDD YILBAOUH CWKM K XINBAM RKHRUHKCIA GBOIAB CWB EMZBMCEIM IO RHIRFD YBIYHB XBKDUABN CEXB LECW DKMN LKCBA KMN DWKNILD NIRCIAD ABRIXXBMN NAEMFEMT LKCBA CWAIUTWIUC CWB NKJ BDYBREKHHJ NUAEMT WIC LBKCWBA XIUMCKEMD EM CWB MIACW KAB RIZBABN LECW DMIL OIA WKHO CWB JBKA CWB LECW OHILBAD OIA CWB ABDC LWBM CWB YILBA OKEHBN CWB LWIHB MBETWGIAWIIN TKCWBABN IUCDENB CI HIIF KC CWB DCKAD CWB IARWBDCAK CUMBN CWBEA EMDCAUXBMCD LWEHB CWB KUNEBMRB DHILHJ OIUMN CWBEA DBKCD DIXB GEAND RKM DBMDB CWB XKTMBCER OEBHN IO CWB BKACW KMN UDB EC CI OEMN CWBEA LKJ DIUCW YKYBA LKD IMRB DI BPYBMDEZB CWKC XIMFD DRAKYBN IHN YKTBD RHBKM EM IANBA CI LAECB IM CWBX KTKEM IUA MBETWGIA ABYKEAD IHN AKNEID KMN RKM CBHH LWKC ED LAIMT SUDC GJ HEDCBMEMT CWB RKDCHB LKHHD LBAB GUEHC DI CWERF CWKC RKMMIMD RIUHN GKABHJ NKXKTB CX DREBMCEDCD DCUNJEMT CWB NBBY IRBKM WKZB OIUMN KMEXKHD CWKC XKFB CWBEA ILM HETWC EM CICKH NKAFMBDD K DCAIMT LEMN YUDWBN CWB DKEHGIKC KRAIDD CWB HKFB OKDCBA CWKM KMJ IO UD WKN WIYBN"""

# ==========================================
# Task 1: Decryption via Frequency Analysis & Pattern Matching
# ==========================================
print("=== TASK 1: Decryption Process ===")

letters_only = [c for c in cipher_text if c.isalpha()]
counts = Counter(letters_only)
print("Most common letters in cipher:", counts.most_common(5))

substitution_mapping = {
    'C': 'E', 'W': 'H', 'B': 'T', 'O': 'A', 'I': 'O', 'A': 'I', 
    'K': 'N', 'D': 'S', 'R': 'R', 'M': 'D', 'L': 'L', 'U': 'U',
    'E': 'C', 'X': 'M', 'Y': 'P', 'H': 'B', 'J': 'Y', 'N': 'F',
    'Z': 'V', 'V': 'W', 'G': 'G', 'F': 'K', 'T': 'X', 'S': 'Z'
}

def apply_mapping(text, mapping):
    return "".join([mapping.get(c, c) if c.isalpha() else c for c in text])

decrypted_text = apply_mapping(cipher_text, substitution_mapping)
print("\n[Decrypted Text Sample]:")
print(decrypted_text[:250] + "...\n")


# ==========================================
# Task 2: Automated Frequency Breaker Across Different Lengths
# ==========================================
print("=== TASK 2: Automated Frequency Analysis Breaker Experiment ===")

english_freq_order = [
    'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 
    'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'
]

true_mapping = {c: p for c, p in zip([c for c in cipher_text if c.isalpha()], [p for p in decrypted_text if p.isalpha()])}
lengths = [100, 250, 500, 1000, 2000]

# מעקב אחר מספר הפעמים שכל אות כשלה במיפוי האוטומטי לאורך כל הבדיקות
failure_counter = Counter()

for length in lengths:
    sub_cipher = cipher_text[:min(length, len(cipher_text))]
    sub_letters = [c for c in sub_cipher if c.isalpha()]
    sub_counts = Counter(sub_letters)
    sorted_cipher_letters = [item[0] for item in sub_counts.most_common()]
    
    auto_mapping = {}
    for i, c in enumerate(sorted_cipher_letters):
        if i < len(english_freq_order):
            auto_mapping[c] = english_freq_order[i]
            
    correct_count = 0
    for c in true_mapping:
        if c in auto_mapping:
            if auto_mapping[c] == true_mapping[c]:
                correct_count += 1
            else:
                # אם האות מופתה בצורה שגויה בניסוי האוטומטי, נספור לה כישלון
                failure_counter[c] += 1
                
    print(f"Text Length: {length:4d} chars | Correct Key Mappings: {correct_count} / {len(true_mapping)}")


# ==========================================
# Task 3: Extracting the 3 Hardest Letters from Experiment Results
# ==========================================
print("\n=== TASK 3: The Three Hardest Letters (Based on Experiment) ===")
# לוקחים מתוך תוצאות הכישלונות של משימה 2 את 3 האותיות שהתפספסו הכי הרבה פעמים
hardest_three = [item[0] for item in failure_counter.most_common(3)]
print(f"The three hardest letters to map based on frequency failure: {hardest_three}")
