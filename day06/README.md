# Day 06 – FASTA & DNA LCS Web Analyzer

## New Features Added (Extending Day 05)
Building on the Day 04/05 Flask LCS application, I added file handling and sequence analysis features:
1. **FASTA File Upload & Parsing:** Users can upload `.fasta` / `.fa` / `.txt` files directly (or paste FASTA-formatted text with `>` headers). The app extracts sequence names and cleans multi-line sequences automatically.
2. **Downloadable Sample FASTA Files:** Added `/download-sample/1` and `/download-sample/2` endpoints so anyone visiting the site can download two ready-to-use `.fasta` files and test the upload workflow immediately.
3. **Reverse Complement & %GC Analysis:** Users can optionally search the reverse complement (`3' → 5'`) of Sequence 2 and view the GC percentage and matched strand of the longest common motif.
4. **Expanded Unit Tests (`test_lcs.py`) & `requirements.txt`:** Added `pytest` coverage for FASTA parsing, reverse complement, GC content, and full sequence comparison.
5. **Non-Standard DNA Character Warning (Peer Review Improvement):** Based on feedback received in a GitHub issue from Nila Theo (https://github.com/taliweizmann/python-course-assignments/issues/1), I added validation (`find_invalid_bases`) that alerts users with a clear warning banner when sequences contain characters outside standard DNA bases (`A`, `C`, `G`, `T`, `N`) to help catch typos while still completing the analysis.

## How to Run
```bash
pip install -r requirements.txt
pytest
python app.py

## Interaction with AI
I used an AI assistant to help design the parse_fasta_content() parser, add in-memory file upload handling and sample FASTA download routes in Flask (compatible with Render hosting), implement the non-DNA base warning alert following peer feedback, update the HTML template, and extend the pytest suite.
