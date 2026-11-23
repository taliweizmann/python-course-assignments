# Day 05 – Unit Testing for the LCS Finder

For this assignment, unit tests were written for the core business logic (`find_longest_common_substring` in `lcs_finder.py`) from the Day 04 Flask web application.

## Location of the Tests
Following the assignment guidelines, the test file is located inside the `day04` directory alongside the module it tests:
* **Test File:** [`../day04/test_lcs.py`](../day04/test_lcs.py)
* **Tested Logic:** [`../day04/lcs_finder.py`](../day04/lcs_finder.py)

## What the Tests Cover
The test suite in `test_lcs.py` uses `pytest` to verify 6 different scenarios:
1. **Standard DNA Match (`test_standard_dna_match`):** Checks that the function accurately identifies the longest contiguous shared motif between two overlapping DNA sequences.
2. **Identical Sequences (`test_identical_sequences`):** Verifies that two identical input sequences return the full sequence.
3. **No Common Substring (`test_no_common_substring`):** Ensures that completely disjoint sequences (e.g., `"AAAA"` and `"TTTT"`) return an empty string (`""`).
4. **Case Insensitivity & Whitespace (`test_case_insensitivity_and_whitespace`):** Confirms that lowercase letters and leading/trailing spaces are properly cleaned and normalized before comparison.
5. **Empty Sequences (`test_empty_sequences`):** Tests edge cases where one or both input sequences are empty strings.
6. **Single-Base Match (`test_single_base_match`):** Verifies behavior when the longest shared overlap consists of only a single nucleotide.

## How to Run the Tests

1. Install `pytest` (if not already installed):
   ```bash
   pip install pytest
2. Run 'pytest':
   pytest 
