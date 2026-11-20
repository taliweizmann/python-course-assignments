from lcs_finder import find_longest_common_substring


def test_standard_dna_match():
    """Verify finding a standard longest common substring between two DNA sequences."""
    seq1 = "ATGCGATCGATCGTAGCTA"
    seq2 = "CGATCGTAGCTAGGACTGA"
    assert find_longest_common_substring(seq1, seq2) == "CGATCGTAGCTA"


def test_identical_sequences():
    """Verify that identical sequences return the full sequence."""
    seq = "GATTACA"
    assert find_longest_common_substring(seq, seq) == "GATTACA"


def test_no_common_substring():
    """Verify that completely disjoint sequences return an empty string."""
    assert find_longest_common_substring("AAAA", "TTTT") == ""


def test_case_insensitivity_and_whitespace():
    """Verify that lowercase inputs and leading/trailing spaces are normalized."""
    seq1 = "  atgcgatc  "
    seq2 = "ttCGATaa"
    assert find_longest_common_substring(seq1, seq2) == "CGAT"


def test_empty_sequences():
    """Verify edge cases where one or both input sequences are empty."""
    assert find_longest_common_substring("", "ACGT") == ""
    assert find_longest_common_substring("ACGT", "") == ""
    assert find_longest_common_substring("", "") == ""


def test_single_base_match():
    """Verify matching when the longest overlap is only a single nucleotide."""
    assert find_longest_common_substring("AC", "TGCA") == "A" or len(
        find_longest_common_substring("AC", "TGCA")
    ) == 1
