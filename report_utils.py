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
