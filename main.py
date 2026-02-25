endcodons = {"TAA", "TAG", "TGA"}


def is_nucleotide(c: str) -> bool:
    if not isinstance(c, str) or len(c) != 1:
        return False
    c = c.upper()
    return c in {"A", "T", "G", "C"}


def extract_codons(line: str):
#This step returns codons and remainder, where remainder is count how many nucleotides remain (less than 3(<3)) after full codons.
    if not line:
        return [], 0

    cleaned = "".join(
        c.upper() for c in line
        if c.upper() in {"A", "T", "G", "C"}
    )

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
#Valid codon is an ordinary codon, it is not a STOP codon (TAA, TAG, TGA)
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

 #Here we load info from the descriptions.txt, it is attached, please check and comment if you have any questions
    desc_lines = load_file_safely("descriptions.txt", "Descriptions")
    for line in desc_lines:
        pos = line.find(":")
        if pos != -1:
            codon = line[:pos].strip().upper()
            desc = line[pos + 1:].strip()
            descriptions[codon] = desc

    #Here we load info from the mutations.txt, it is attached, please check and comment if you have any questions
    mut_lines = load_file_safely("mutations.txt", "Mutations")
    known_mutations = set(m.strip().upper() for m in mut_lines if m.strip())

    #Here we load DNA sequences! The format is "ATGCAGTAA"
    seq_lines = load_file_safely("input.txt", "Sequences")

    if not seq_lines:
        print("\nError: no sequences to analyze")
        print("Please create input.txt with DNA sequences.")
        return

    print("SEQUENCE ANALYSIS")

    for seq_num, line in enumerate(seq_lines, 1):
        print(f"\nAnalyzing sequence #{seq_num}:")

        codons, remainder = extract_codons(line)

        if not codons:
            print(f"No valid codons found in sequence #{seq_num}")
            continue

    #Starting the codon check
        if codons[0] == "ATG":
            print("Valid start codon ATG found")
        else:
            print(f"Mutation! Expected ATG but found: {codons[0]}")

    #Stopping the codon check
        last_index = len(codons) - 1

        stop_positions = []
        for i in range(len(codons)):
            if codons[i] in endcodons:
                stop_positions.append(i)

        premature_positions = [i for i in stop_positions if i != last_index]

        if not stop_positions:
            print("Mutation! No stop codon found (TAA/TAG/TGA).")
        else:
            if premature_positions:
                print(f"Mutation! Premature stop codon found at codon index(es): {premature_positions}")

            if codons[last_index] in endcodons:
                if remainder == 0:
                    print("Valid stop codon at the end.")
                else:
                    print("Stop codon is last full codon, BUT extra nucleotides remain after it (incomplete codon).")
            else:
                print("Mutation! Sequence does not end with a stop codon.")

            print(f"Stop codons found: {len(stop_positions)}")

    #Starting the internal START check
        internal_start = "ATG" in codons[1:]
        if internal_start:
            print("Warning! Internal start codon ATG found.")

    #Starting the repetition check
        max_run = 1
        current_run = 1
        for i in range(1, len(codons)):
            if codons[i] == codons[i - 1]:
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 1

        if max_run >= 10:
            print("Warning! Medium codon repetition detected. Cancer risks for men.")
        if max_run >= 20:
            print("Severe mutation pattern detected! Extreme repetition.")

    #Prepare - which stop codons are truly premature by their position
        premature_stop_codons = set(codons[i] for i in premature_positions)

    #We COUNT, we look for MUTATIONS, we check for PALINDROMES
        for idx, codon in enumerate(codons):
            frequency[codon] = frequency.get(codon, 0) + 1

    #Invalid codons
            if codon not in endcodons and not is_validcodon(codon):
                print(f"Invalid codon found: {codon}")

        # OUR KNOWN MUTATIONS and their logic.
            #for stop codons: we print only if premature
            #for non-stop codons: print always if in "known_mutations"
            if codon in known_mutations:
                if codon in endcodons:
                    if codon in premature_stop_codons:
                        print(f"Known mutation found: {codon}")
                        if codon in descriptions:
                            print(f"     → {descriptions[codon]}")
                else:
                    print(f"Known mutation found: {codon}")
                    if codon in descriptions:
                        print(f"     → {descriptions[codon]}")

    #Our palindrome check: first letter IS SIMILAR to last letter
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
