from lcs_finder import (
    analyze_sequences,
    calculate_gc_content,
    find_invalid_bases,
    find_longest_common_substring,
    parse_fasta_content,
    reverse_complement,
)


def test_parse_fasta_with_header():
    fasta_text = ">Human_HBB_fragment\nATGCGATC\nGATCGTAG\n"
    header, seq = parse_fasta_content(fasta_text)
    assert header == "Human_HBB_fragment"
    assert seq == "ATGCGATCGATCGTAG"


def test_parse_raw_sequence_without_header():
    header, seq = parse_fasta_content("  atgc gatc  ", default_name="CustomSeq")
    assert header == "CustomSeq"
    assert seq == "ATGCGATC"


def test_standard_dna_match():
    seq1 = "ATGCGATCGATCGTAGCTA"
    seq2 = "CGATCGTAGCTAGGACTGA"
    assert find_longest_common_substring(seq1, seq2) == "CGATCGTAGCTA"


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_gc_content():
    assert calculate_gc_content("GCGC") == 100.0
    assert calculate_gc_content("ATGC") == 50.0


def test_invalid_bases_detection():
    assert find_invalid_bases("ATGCHX") == ["H", "X"]
    assert find_invalid_bases("ACGTN") == []


def test_analyze_fasta_inputs_with_reverse_complement():
    fasta1 = ">SeqA\nAAACCCGATTACATTT\n"
    fasta2 = ">SeqB\nGGGTAATGTAATCAAA\n"
    res = analyze_sequences(fasta1, fasta2, check_rev_comp=True)
    assert res["name1"] == "SeqA"
    assert res["name2"] == "SeqB"
    assert res["substring"] == "GATTACA"
    assert res["length"] == 7
    assert "Reverse Complement" in res["strand"]
    assert res["warnings"] == []


def test_analyze_warns_on_non_dna_characters():
    res = analyze_sequences("ATGCH", "ATGCG")
    assert len(res["warnings"]) == 1
    assert "H" in res["warnings"][0]
