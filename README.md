Hey guys!

Welcome to the README file for the DNA Sequence Analysis Program.
This program analyzes DNA sequences and detects biologically relevant patterns,
mutations, and structural abnormalities in codon organization.

SET-UP:

1. Compile your DNA sequence into a continuous string format:
   Example: ATGCTGTAG

2. Place your sequence inside the input.txt file.


Core Functionality (Version 1.0)

The program checks:

1. Start Codon Validation
   - Verifies that the sequence begins with ATG.
   - If not, a mutation warning is displayed.

2. Stop Codon Detection
   - Checks for presence of valid stop codons (TAA, TAG, TGA).
   - Warns if no stop codon is found.

3. Premature Stop Codon Detection
   - Detects stop codons appearing before the final codon position.

4. Codon Frame Integrity
   - Warns if nucleotide count is not divisible by 3.
   - Detects incomplete final codons.

5. Internal Start Codon Detection
   - Detects additional ATG codons within the sequence.

6. Codon Frequency Analysis
   - Counts occurrences of each codon.
   - Displays codon frequency statistics.

7. Codon Repetition Detection
   - Detects abnormal consecutive repetition of identical codons.
  
8. Symmetrical Codon Detection
   - Detects codons where the first and last nucleotide are identical.
   - Example: ATA, GCG, TAT.
   - These structural patterns may indicate symmetry-related motifs.

9. CAG Trinucleotide Repeat Expansion Detection
   - Detects consecutive CAG repeats.
   - Classifies repeat count:

     • 27–35 repeats → Intermediate range
     • 36–39 repeats → Reduced penetrance range
     • ≥40 repeats → Disease-associated range

   This mimics the pathological mechanism observed in Huntington-like expansions.
