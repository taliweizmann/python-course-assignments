def parse_fasta_content(raw_text: str, default_name: str = "Sequence") -> tuple[str, str]:
    """Parse raw text or FASTA-formatted text into (sequence_name, cleaned_sequence)."""
    lines = [line.strip() for line in raw_text.strip().splitlines() if line.strip()]
    if not lines:
        return default_name, ""

    if lines[0].startswith(">"):
        header = lines[0][1:].strip() or default_name
        sequence = "".join(lines[1:]).upper().replace(" ", "")
        return header, sequence

    sequence = "".join(lines).upper().replace(" ", "")
    return default_name, sequence


def reverse_complement(seq: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    complement_map = str.maketrans("ACGT", "TGCA")
    cleaned = seq.strip().upper()
    return cleaned.translate(complement_map)[::-1]


def calculate_gc_content(seq: str) -> float:
    """Calculate the GC percentage of a DNA sequence."""
    cleaned = seq.strip().upper()
    if not cleaned:
        return 0.0
    gc_count = cleaned.count("G") + cleaned.count("C")
    return round((gc_count / len(cleaned)) * 100, 2)


def find_longest_common_substring(seq1: str, seq2: str) -> str:
    """Find the longest contiguous common substring between two DNA sequences."""
    s1 = seq1.strip().upper()
    s2 = seq2.strip().upper()

    if not s1 or not s2:
        return ""

    longest = ""
    n = len(s1)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s1[i:j]
            if sub in s2 and len(sub) > len(longest):
                longest = sub

    return longest


def analyze_sequences(
    raw_seq1: str,
    raw_seq2: str,
    check_rev_comp: bool = False,
    default_name1: str = "Sequence 1",
    default_name2: str = "Sequence 2",
) -> dict:
    """Parse two raw/FASTA inputs, find the longest shared motif, and return summary stats."""
    name1, s1 = parse_fasta_content(raw_seq1, default_name=default_name1)
    name2, s2 = parse_fasta_content(raw_seq2, default_name=default_name2)

    forward_match = find_longest_common_substring(s1, s2)
    best_match = forward_match
    strand = "Forward (5' → 3')"

    if check_rev_comp:
        rev_s2 = reverse_complement(s2)
        rev_match = find_longest_common_substring(s1, rev_s2)
        if len(rev_match) > len(forward_match):
            best_match = rev_match
            strand = "Reverse Complement (3' → 5')"

    return {
        "name1": name1,
        "name2": name2,
        "len1": len(s1),
        "len2": len(s2),
        "substring": best_match,
        "length": len(best_match),
        "strand": strand,
        "gc_content": calculate_gc_content(best_match),
    }
