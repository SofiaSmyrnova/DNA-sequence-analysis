endcodons = {"TAA", "TAG", "TGA"}

def is_nucleotide(c: str) -> bool:
    if not isinstance(c, str) or len(c) != 1:
        return False
    c = c.upper()
    return c in {"A", "T", "G", "C"}

def extract_codons(line: str) -> list[str]:
    if not line:
        return []

    cleaned = "".join(
        c.upper() for c in line
        if c.upper() in {"A", "T", "G", "C"}
    )

    if not cleaned:
        return []

    codons = [
        cleaned[i:i + 3]
        for i in range(0, len(cleaned), 3)
        if i + 3 <= len(cleaned)
    ]

    if len(cleaned) % 3 != 0:
        print(f"Warning: Incomplete codon found ({len(cleaned) % 3} nucleotides remaining)")

    return codons

def is_validcodon(codon: str) -> bool:
    if not codon or not isinstance(codon, str):
        return False
    return len(codon) == 3 and codon not in endcodons

def results(result: list, frequency: dict):
    print("ANALYSIS RESULTS")

    print("\nPalindrome codons found:")
    if not result:
        print("  No palindrome codons found.")
    else:
        for i, word in enumerate(result, 1):
            print(f"  {i}. {word} - nucleotides: {len(word)}")

    print(f"\nTotal palindrome codons: {len(result)}")

    print("Codon frequency in sequence:")

    if not frequency:
        print("  No codons to display.")
    else:
        freqvec = sorted(
            frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for codon, count in freqvec:
            print(f"  {codon} → {count} time(s)")

def load_file_safely(filename: str, file_type: str) -> list:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        print(f"Loaded {filename}: {len(lines)} lines")
        return lines
    except FileNotFoundError:
        print(f"Warning: {filename} was not found. {file_type} will be empty.")
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

def main():
    print("DNA SEQUENCE ANALYZER")

    result = []
    frequency = {}
    descriptions = {}

    desc_lines = load_file_safely("descriptions.txt", "Descriptions")
    for line in desc_lines:
        pos = line.find(":")
        if pos != -1:
            codon = line[:pos].strip()
            desc = line[pos + 1:].strip()
            descriptions[codon] = desc

    mut_lines = load_file_safely("mutations.txt", "Mutations")
    known_mutations = set(mut_lines)

    seq_lines = load_file_safely("input.txt", "Sequences")

    if not seq_lines:
        print("\nError: no sequences to analyze")
        print("Please create input.txt with DNA sequences.")
        return

    print("SEQUENCE ANALYSIS")

    for seq_num, line in enumerate(seq_lines, 1):
        print(f"Analyzing sequence #{seq_num}:")
        codons = extract_codons(line)

        if not codons:
            print(f"No valid codons found in sequence #{seq_num}")
            continue

        if codons[0] == "ATG":
            print(f"Valid start codon ATG found")
        else:
            print(f"Mutation! Expected ATG but found: {codons[0]}")

        internal_start = "ATG" in codons[1:]

        if internal_start:
            print("Warning! Internal start codon ATG found.")

        stop_count = sum(1 for c in codons if c in endcodons)

        if stop_count == 0:
            print("Mutation! No stop codon found (TAA/TAG/TGA).")
        else:
            print(f"Stop codons found: {stop_count}")


        max_run = 1
        current_run = 1
        for i in range(1, len(codons)):
            if codons[i] == codons[i - 1]:
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 1

        if max_run >= 10:
            print("Warning! High codon repetition detected.")
        if max_run >= 20:
            print("Severe mutation pattern detected! Extreme repetition.")


        for codon in codons:
            frequency[codon] = frequency.get(codon, 0) + 1

            if not is_validcodon(codon):
                print(f"Invalid/stop codon found: {codon}")

            if codon in known_mutations:
                print(f"Known mutation found: {codon}")
                if codon in descriptions:
                    print(f"     → {descriptions[codon]}")

            if len(codon) == 3 and codon[0] == codon[-1]:
                result.append(codon)

        print()

    results(result, frequency)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram has been interrupted by user")
    except Exception as e:
        print(f"\nError has happened {e}")
        import traceback

        traceback.print_exc()