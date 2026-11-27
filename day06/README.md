# Day 06 – FASTA & DNA LCS Web Analyzer

## New Features Added (Extending Day 05)
Building on the Day 04/05 Flask LCS application, I added file handling and sequence analysis features:
1. **FASTA File Upload & Parsing:** Users can upload `.fasta` / `.fa` / `.txt` files directly (or paste FASTA-formatted text with `>` headers). The app extracts sequence names and cleans multi-line sequences automatically.
2. **Downloadable Sample FASTA Files:** Added `/download-sample/1` and `/download-sample/2` endpoints so anyone visiting the site can download two ready-to-use `.fasta` files and test the upload workflow immediately.
3. **Reverse Complement & %GC Analysis:** Users can optionally search the reverse complement (`3' → 5'`) of Sequence 2 and view the GC percentage and matched strand of the longest common motif.
4. **Expanded Unit Tests (`test_lcs.py`) & `requirements.txt`:** Added `pytest` coverage for FASTA parsing, reverse complement, GC content, and full sequence comparison.

## How to Run
```bash
pip install -r requirements.txt
pytest
python app.py
