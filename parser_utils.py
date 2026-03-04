from constants import endcodons

# NEWWW
def clean_dna(s: str) -> str:
    if not s:
        return ""
    s = s.upper()
    return "".join(ch for ch in s if ch in {"A", "T", "G", "C"})
# NEWW

def is_nucleotide(c: str) -> bool:
    if not isinstance(c, str) or len(c) != 1:
        return False
    return c.upper() in {"A", "T", "G", "C"}


def extract_codons(line: str):
    if not line:
        return [], 0

# Also new
    cleaned = clean_dna(line)
#

    if not cleaned:
        return [], 0

    codons = [
        cleaned[i:i + 3]
        for i in range(0, len(cleaned), 3)
        if i + 3 <= len(cleaned)
    ]

    remainder = len(cleaned) % 3

    if remainder != 0:
        print(f"Warning: Incomplete codon found ({remainder} nucleotides remaining)")

    return codons, remainder


def is_validcodon(codon: str) -> bool:
    if not codon or not isinstance(codon, str):
        return False
    return len(codon) == 3 and codon not in endcodons
