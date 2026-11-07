def find_longest_common_substring(seq1, seq2):
    """
    Finds the longest contiguous common DNA substring between two sequences.
    """
    seq1 = seq1.strip().upper()
    seq2 = seq2.strip().upper()
    longest = ""

    for i in range(len(seq1)):
        for j in range(i + 1, len(seq1) + 1):
            sub = seq1[i:j]
            if sub in seq2 and len(sub) > len(longest):
                longest = sub
    return longest

def compare_sequences_from_file(filepath):
    """
    Reads two DNA sequences from a text file and computes their LCS.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if len(lines) < 2:
        print("Error: The file must contain at least two DNA sequences.")
        return

    seq1, seq2 = lines[0], lines[1]
    common = find_longest_common_substring(seq1, seq2)

    print("--- Longest Common DNA Substring Finder ---")
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"Longest Common Match: {common}")
    print(f"Match Length: {len(common)} bp")

if __name__ == "__main__":
    compare_sequences_from_file("day03/sequences.txt")
