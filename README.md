Hey guys!

Welcome to the README file for the DNA Sequence Analysis Program.
This program analyzes DNA sequences and detects biologically relevant patterns,
mutations, and structural abnormalities in codon organization.

SET-UP:

1. Compile your DNA sequence into a continuous string format:
   Example: ATGCTGTAG

2. Place your sequence inside the input.txt file.


   Core Functionality — Version 1.0

  The program performs the following analyses:

Start Codon Validation

Verifies that the sequence begins with ATG.

If not, a mutation warning is displayed.

Stop Codon Detection

   Checks for valid stop codons: TAA, TAG, TGA.

Warns if no stop codon is present.

Premature Stop Codon Detection

Detects stop codons appearing before the final codon position.

Indicates potential truncated protein synthesis.

Codon Frame Integrity

   Warns if total nucleotide count is not divisible by 3.

Detects incomplete final codons.

Ensures correct reading frame structure.

Internal Start Codon Detection

   Detects additional ATG codons within the sequence.

May indicate alternative initiation sites.

Codon Frequency Analysis

Counts occurrences of each codon.

Displays codon usage statistics.

Codon Repetition Detection

Detects abnormal consecutive repetition of identical codons.

May indicate replication slippage.

Symmetrical Codon Detection

Detects codons where the first and last nucleotide are identical.

Examples: ATA, GCG, TAT.

These patterns may represent symmetry-related motifs.

CAG Trinucleotide Repeat Expansion Detection

Detects consecutive CAG repeats.


Classifies repeat count:
10-20 repears → high cancer risks
27–35 repeats → Intermediate range
36–39 repeats → Reduced penetrance range
40 or more repeats → Disease-associated range



Mimics pathological mechanisms observed in trinucleotide expansion disorders.





   Update — Version 1.2

Version 1.2 introduces extended structural and molecular analysis features.

Reverse-Complement Palindrome Detection

Detects reverse-complement palindromic regions.

Such sequences may represent restriction enzyme sites or regulatory motifs.

GC-Content Analysis

Calculates overall GC percentage.

Evaluates GC distribution across the sequence.

High GC content may indicate structural stability.

Low GC content may indicate AT-rich regulatory zones.

Poly-Nucleotide Run Detection

Detects homopolymer stretches (AAAAAA, TTTTTT, GGGGGG, CCCCCC).

Long runs may indicate replication instability or sequencing artifacts.

Frame-Specific CAG Expansion Verification

Confirms that CAG repeats occur within the correct reading frame.

Distinguishes random occurrence from tandem pathological expansion.

Reports exact repeat length.

Structural Risk Summary

Generates a final analysis summary.

Classifies detected abnormalities into severity levels.

Provides structural stability assessment.

Enhanced Diagnostic Output

Warnings are categorized as:
Structural Warning
Frame Warning
Mutation Alert
High-Risk Expansion Alert
