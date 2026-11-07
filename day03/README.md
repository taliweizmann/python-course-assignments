# Day 03 - Longest Common DNA Substring Finder

## Scientific Objective
Sequence alignment and motif discovery: Identifying the Longest Common Substring (LCS) shared between two biological DNA sequences.

## Files
- `sequences.txt`: Input file containing two DNA sequences (one per line).
- `lcs_finder.py`: Script defining the search function and file-handling logic.

## Implementation Details
- `find_longest_common_substring(seq1, seq2)`: Slides across substrings of `seq1` to verify occurrences inside `seq2`, tracking and returning the longest exact contiguous match found.
- `compare_sequences_from_file(filepath)`: Reads the sequence file and prints the sequences, the matched motif, and its base-pair length.

## Prompts Used (VS Code Copilot / AI)
- *"Write a Python function to find the longest common contiguous substring between two DNA sequences."*
- *"Write a function to read two DNA strings from a text file, run the search, and format the output."*

## Execution
Run from the root repository directory:
```bash
python day03/lcs_finder.py
