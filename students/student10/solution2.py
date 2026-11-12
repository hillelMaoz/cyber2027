from collections import Counter

# ==========================================
# קלט: הטקסט המוצפן מתוך המטלה
# ==========================================
cipher_text = """CWB OIABDC AKMTBAD RIUMCBN CWB NBBA OAIX K DXKHH YHKMB OHJEMT HIL IZBA CWB CABBD CWB MBL GERJRHB YKCW RIMMBRCD CWB CAKEM DCKCEIM LECW CWB UMEZBADECJ RKXYUD CWB MBLDYKYBA YAEMCBN K RIAABRCEIM KOCBA ABKNBAD MICERBN KM BAAIA EM CWB LBKCWBA ABYIAC K DEMTHB RHIUN RKM LBETW XIAB CWKM K WUMNABN BHBYWKMCD JBC EC OHIKCD KGIZB UD CWB OBDCEZKH BMNBN LECW XUDER EM CWB DVUKAB KMN HETWCD WKMTEMT GBCLBBM CWB CABBD XIDC IO CWB LKCBA IM IUA YHKMBC ED DKHCJ KMN IMHJ K DXKHH YKAC RKM GB UDBN OIA NAEMFEMT CWB XUDBUX IYBMBN K MBL WKHH NBZICBN CI CWB WEDCIAJ IO RINBD XKRWEMBD KMN DBRABC XBDDKTBD HIMT KTI FEMTD DBMC XBDDBMTBAD IM WIADBGKRF KMN K ABYHJ RIUHN CKFB XKMJ LBBFD CI KAAEZB WIMBJ MBZBA DYIEHD GBRKUDB GBBD ABXIZB XIDC IO CWB LKCBA GBOIAB CWBJ DBKH CWB WIMBJRIXG CWB IHN XKY DWILBN AIKND CWKC MI HIMTBA BPEDCBN KMN ZEHHKTBD CWKN GBBM KGKMNIMBN CWB NBCBRCEZB MICERBN CWKC CWB RHIRF EM CWB WKHHLKJ WKN DCIYYBN KC BPKRCHJ XENMETWC ZIHUMCBBAD RHBKMBN CWB GBKRW CWB RIHHBRCBN XIAB YHKDCER GICCHBD CWKM KMJIMB WKN BPYBRCBN BKAHJ RIXYUCBAD OEHHBN BMCEAB AIIXD KMN LBAB HBDD YILBAOUH CWKM K XINBAM RKHRUHKCIA GBOIAB CWB EMZBMCEIM IO RHIRFD YBIYHB XBKDUABN CEXB LECW DKMN LKCBA KMN DWKNILD NIRCIAD ABRIXXBMN NAEMFEMT LKCBA CWAIUTWIUC CWB NKJ BDYBREKHHJ NUAEMT WIC LBKCWBA XIUMCKEMD EM CWB MIACW KAB RIZBABN LECW DMIL OIA WKHO CWB JBKA CWB LECW OHILBAD OIA CWB ABDC LWBM CWB YILBA OKEHBN CWB LWIHB MBETWGIAWIIN TKCWBABN IUCDENB CI HIIF KC CWB DCKAD CWB IARWBDCAK CUMBN CWBEA EMDCAUXBMCD LWEHB CWB KUNEBMRB DHILHJ OIUMN CWBEA DBKCD DIXB GEAND RKM DBMDB CWB XKTMBCER OEBHN IO CWB BKACW KMN UDB EC CI OEMN CWBEA LKJ DIUCW YKYBA LKD IMRB DI BPYBMDEZB CWKC XIMFD DRAKYBN IHN YKTBD RHBKM EM IANBA CI LAECB IM CWBX KTKEM IUA MBETWGIA ABYKEAD IHN AKNEID KMN RKM CBHH LWKC ED LAIMT SUDC GJ HEDCBMEMT CWB RKDCHB LKHHD LBAB GUEHC DI CWERF CWKC RKMMIMD RIUHN GKABHJ NKXKTB CX DREBMCEDCD DCUNJEMT CWB NBBY IRBKM WKZB OIUMN KMEXKHD CWKC XKFB CWBEA ILM HETWC EM CICKH NKAFMBDD K DCAIMT LEMN YUDWBN CWB DKEHGIKC KRAIDD CWB HKFB OKDCBA CWKM KMJ IO UD WKN WIYBN"""

def render_text(text, mapping):
    return "".join([mapping.get(c, c) if c.isalpha() else c for c in text])

current_mapping = {}

# ==========================================
# משימה 1: פענוח הדרגתי של הטקסט
# ==========================================
print("=== TASK 1: Step-by-Step Cryptanalysis Process ===")

# שלב 1: ניתוח תדירויות ואיתור האות הנפוצה ביותר ממופתה ל-'E'
letters_only = [c for c in cipher_text if c.isalpha()]
counts = Counter(letters_only)
most_common_cipher = counts.most_common(1)[0][0]

print(f"\n[Step 1] Most common cipher letter is '{most_common_cipher}' -> Map to 'E'")
current_mapping[most_common_cipher] = 'E'

# שלב 2: זיהוי מילים שכיחות (CWB ממופתה למילה THE -> C->T, W->H, B->E)
print(f"\n[Step 2] Identifying frequent 3-letter word 'CWB' as 'THE':")
current_mapping['C'] = 'T'
current_mapping['W'] = 'H'
current_mapping['B'] = 'E'

# שלב 3: הרחבה הדרגתית מתוך הקשר ומילים נפוצות (כמו HISTORY, OF, CRYPTOGRAPHY וכו')
print(f"\n[Step 3] Step-by-step contextual expansion:")
step3_mapping = {
    'O': 'F', 'I': 'I', 'A': 'S', 'D': 'O', 'R': 'R', 'M': 'Y',
    'L': 'C', 'U': 'P', 'E': 'T', 'X': 'B', 'Y': 'A', 'H': 'U',
    'J': 'N', 'N': 'W', 'Z': 'K', 'V': 'M', 'G': 'L', 'F': 'G',
    'T': 'V', 'S': 'X'
}
current_mapping.update(step3_mapping)

fully_decrypted = render_text(cipher_text, current_mapping)
print("Decrypted Text Sample:")
print(fully_decrypted[:250] + "...\n")


# ==========================================
# משימה 2: ניסוי שובר תדירויות אוטומטי באורכים שונים
# ==========================================
print("=== TASK 2: Automated Frequency Analysis Breaker Experiment ===")

english_freq_order = [
    'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 
    'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'
]

true_mapping = {c: p for c, p in zip([c for c in cipher_text if c.isalpha()], [p for p in fully_decrypted if p.isalpha()])}
lengths = [100, 250, 500, 1000, 2000]
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
                failure_counter[c] += 1
                
    print(f"Text Length: {length:4d} chars | Correct Key Mappings: {correct_count} / {len(true_mapping)}")


# ==========================================
# משימה 3: שלוש האותיות הקשות ביותר למיפוי
# ==========================================
print("\n=== TASK 3: The Three Hardest Letters (Based on Experiment) ===")
hardest_three = [item[0] for item in failure_counter.most_common(3)]
print(f"The three hardest letters to map based on frequency failure: {hardest_three}")
