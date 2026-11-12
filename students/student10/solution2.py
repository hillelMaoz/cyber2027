"""HW2 - student10: substitution cipher breaking and frequency analysis"""
import random
from collections import Counter

CIPHER = """CWB OIABDC AKMTBAD RIUMCBN CWB NBBA OAIX K DXKHH YHKMB OHJEMT HIL IZBA CWB CABBD CWB MBL GERJRHB YKCW RIMMBRCD CWB CAKEM DCKCEIM LECW CWB UMEZBADECJ RKXYUD CWB MBLDYKYBA YAEMCBN K RIAABRCEIM KOCBA ABKNBAD MICERBN KM BAAIA EM CWB LBKCWBA ABYIAC K DEMTHB RHIUN RKM LBETW XIAB CWKM K WUMNABN BHBYWKMCD JBC EC OHIKCD KGIZB UD CWB OBDCEZKH BMNBN LECW XUDER EM CWB DVUKAB KMN HETWCD WKMTEMT GBCLBBM CWB CABBD XIDC IO CWB LKCBA IM IUA YHKMBC ED DKHCJ KMN IMHJ K DXKHH YKAC RKM GB UDBN OIA NAEMFEMT CWB XUDBUX IYBMBN K MBL WKHH NBZICBN CI CWB WEDCIAJ IO RINBD XKRWEMBD KMN DBRABC XBDDKTBD HIMT KTI FEMTD DBMC XBDDBMTBAD IM WIADBGKRF KMN K ABYHJ RIUHN CKFB XKMJ LBBFD CI KAAEZB WIMBJ MBZBA DYIEHD GBRKUDB GBBD ABXIZB XIDC IO CWB LKCBA GBOIAB CWBJ DBKH CWB WIMBJRIXG CWB IHN XKY DWILBN AIKND CWKC MI HIMTBA BPEDCBN KMN ZEHHKTBD CWKC WKN GBBM KGKMNIMBN CWB NBCBRCEZB MICERBN CWKC CWB RHIRF EM CWB WKHHLKJ WKN DCIYYBN KC BPKRCHJ XENMETWC ZIHUMCBBAD RHBKMBN CWB GBKRW KMN RIHHBRCBN XIAB YHKDCER GICCHBD CWKM KMJIMB WKN BPYBRCBN BKAHJ RIXYUCBAD OEHHBN BMCEAB AIIXD KMN LBAB HBDD YILBAOUH CWKM K XINBAM RKHRUHKCIA GBOIAB CWB EMZBMCEIM IO RHIRFD YBIYHB XBKDUABN CEXB LECW DKMN LKCBA KMN DWKNILD NIRCIAD ABRIXXBMN NAEMFEMT LKCBA CWAIUTWIUC CWB NKJ BDYBREKHHJ NUAEMT WIC LBKCWBA XIUMCKEMD EM CWB MIACW KAB RIZBABN LECW DMIL OIA WKHO CWB JBKA KMN LECW OHILBAD OIA CWB ABDC LWBM CWB YILBA OKEHBN CWB LWIHB MBETWGIAWIIN TKCWBABN IUCDENB CI HIIF KC CWB DCKAD CWB IARWBDCAK CUMBN CWBEA EMDCAUXBMCD LWEHB CWB KUNEBMRB DHILHJ OIUMN CWBEA DBKCD DIXB GEAND RKM DBMDB CWB XKTMBCER OEBHN IO CWB BKACW KMN UDB EC CI OEMN CWBEA LKJ DIUCW YKYBA LKD IMRB DI BPYBMDEZB CWKC XIMFD DRAKYBN IHN YKTBD RHBKM EM IANBA CI LAECB IM CWBX KTKEM IUA MBETWGIA ABYKEAD IHN AKNEID KMN RKM CBHH LWKC ED LAIMT SUDC GJ HEDCBMEMT CWB RKDCHB LKHHD LBAB GUEHC DI CWERF CWKC RKMMIMD RIUHN GKABHJ NKXKTB CWBX DREBMCEDCD DCUNJEMT CWB NBBY IRBKM WKZB OIUMN KMEXKHD CWKC XKFB CWBEA ILM HETWC EM CICKH NKAFMBDD K DCAIMT LEMN YUDWBN CWB DKEHGIKC KRAIDD CWB HKFB OKDCBA CWKM KMJ IO UD WKN WIYBN"""
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENG_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# ---------- Part 1: the key (plain -> cipher), found by guided manual decryption ----------
PLAIN2CIPHER = "KGRNBOTWESFHXMIYVADCUZLPJQ"
C2P = {c: p for p, c in zip(ABC, PLAIN2CIPHER)}
DECISIONS = {
    "C->T, W->H, B->E": "CWB opens the text and is the most frequent word: THE",
    "K->A": "K appears as a single-letter word and is very frequent: A",
    "O->F, I->O, A->R, D->S": "OIABDC = FOREST (followed by AKMTBAD = RANGERS)",
    "M->N, T->G": "AKMTBAD = RANGERS, EMDCAUXBMCD = INSTRUMENTS",
    "R->C, U->U, N->D": "RIUMCBN = COUNTED",
    "X->M, H->L, Y->P, J->Y": "DXKHH YHKMB OHJEMT = SMALL PLANE FLYING",
    "E->I, L->W, Z->V, G->B": "LECW = WITH, IZBA = OVER, GBCLBBM = BETWEEN",
    "F->K, P->X": "FEMTD = KINGS, BPKRCHJ = EXACTLY",
    "S->J, V->Q": "SUDC GJ = JUST BY, DVUKAB = SQUARE",
    "Q->Z": "Plain Z does not appear in the text; assigned by elimination "
            "(cipher Q is the only unused letter)",
}


def decrypt(text, c2p):
    return "".join(c2p.get(ch, ch) for ch in text)


PLAINTEXT = decrypt(CIPHER, C2P)
PLAINTEXT_TO_CIPHER = {p: c for c, p in C2P.items()}


# ---------- Part 2: automatic frequency-rank breaker ----------
def freq_break(ct):
    cnt = Counter(ch for ch in ct if ch.isalpha())
    # stable sort: descending frequency, ties broken alphabetically
    ranked = sorted(cnt, key=lambda c: (-cnt[c], c))
    return {c: ENG_ORDER[i] for i, c in enumerate(ranked)}


def score(ct, guess):
    """Return (correctly mapped letters, letters present in segment, fraction of correct characters)."""
    letters = set(ch for ch in ct if ch.isalpha())
    ok = [c for c in letters if guess.get(c) == C2P[c]]
    chars = sum(1 for ch in ct if ch.isalpha() and guess[ch] == C2P[ch])
    total = sum(1 for ch in ct if ch.isalpha())
    return ok, len(letters), chars / total


LENGTHS = [100, 250, 500, 1000, 2000]


def run_experiment():
    res = {}
    for n in LENGTHS:
        seg = CIPHER[:n]
        g = freq_break(seg)
        ok, present, cr = score(seg, g)
        res[n] = (len(ok), present, cr)
    return res


# ---------- Alice's idea: random letters inserted between words ----------
def alice_experiment(trials=30, seed=1):
    rng = random.Random(seed)
    plain_words = PLAINTEXT.split()
    outs = []
    for _ in range(trials):
        noisy = []
        for w in plain_words:
            noisy.append(w)
            # random "noise word" of 1-4 letters between every two words
            noisy.append("".join(rng.choice(ABC) for _ in range(rng.randint(1, 4))))
        noisy_plain = " ".join(noisy)
        ct = "".join(PLAINTEXT_TO_CIPHER.get(ch, ch) for ch in noisy_plain)
        g = freq_break(ct)
        letters = set(ch for ch in ct if ch.isalpha())
        ok = sum(1 for c in letters if g[c] == C2P[c])
        outs.append((ok, len(ct.replace(" ", ""))))
    return sum(o for o, _ in outs) / trials, outs[0][1]


# ---------- Part 3: rank displacement vs. English (to find the hardest letters) ----------
def rank_displacement():
    cnt = Counter(ch for ch in CIPHER if ch.isalpha())
    ranked = sorted(cnt, key=lambda c: (-cnt[c], c))
    g = freq_break(CIPHER)
    rows = []
    for i, c in enumerate(ranked):
        p = C2P[c]
        eng = ENG_ORDER.index(p)
        rows.append((p, i + 1, eng + 1, i - eng, g[c], g[c] == p))
    return rows


if __name__ == "__main__":
    print("KEY plain->cipher:", PLAIN2CIPHER)
    print("\nManual decisions:")
    for k, v in DECISIONS.items():
        print(f"  {k}: {v}")
    print("\nDecrypted text (beginning):\n", PLAINTEXT[:400], "...\n")
    print("Text length (letters + spaces):", len(CIPHER))

    res = run_experiment()
    print("\nLength | correct letters / letters present | % correct characters")
    for n in LENGTHS:
        a, b, c = res[n]
        print(f"{n:6d} | {a:2d} / {b:2d} | {c * 100:5.1f}%")

    print("\nRank displacement (letter, text rank, English rank, diff, guess, correct?):")
    for row in rank_displacement():
        print("  ", row)

    avg, n_letters = alice_experiment()
    print(f"\nAlice: ~{n_letters} letters; average correctly mapped letters: {avg:.1f}/26")
    print("Without noise, 2000 chars:", res[2000][0], "correct")

    cnt = Counter(ch for ch in PLAINTEXT if ch.isalpha())
    print("\nLetter frequencies in the decrypted text:")
    print(" ".join(f"{p}:{cnt[p]}" for p, _ in cnt.most_common()))
