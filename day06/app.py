from flask import Flask, Response, render_template, request
from lcs_finder import analyze_sequences

app = Flask(__name__)

SAMPLE_FASTA_1 = (
    ">Sample_Gene_A_Human_Segment\n"
    "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG\n"
    "CGATCGTAGCTAGGACTGATCGTAGCTAGCTAGCATCGA\n"
)

SAMPLE_FASTA_2 = (
    ">Sample_Gene_B_Homolog_Segment\n"
    "TTAGCGCTAGCTAGCATCGATCGTAGCTAGGACTGATCG\n"
    "AATTCCGGATCGATCGTAGCTAGCTAGCATCGATTTTTA\n"
)


def _read_uploaded_file(file_storage) -> str:
    """Read an uploaded text/FASTA file into a UTF-8 string."""
    if not file_storage or not file_storage.filename:
        return ""
    return file_storage.stream.read().decode("utf-8-sig", errors="replace")


@app.route("/download-sample/<int:sample_id>")
def download_sample(sample_id: int):
    """Serve downloadable sample FASTA files so users can test file uploads immediately."""
    if sample_id == 1:
        content = SAMPLE_FASTA_1
        filename = "sample_seq1.fasta"
    elif sample_id == 2:
        content = SAMPLE_FASTA_2
        filename = "sample_seq2.fasta"
    else:
        return "Sample not found", 404

    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@app.route("/", methods=["GET", "POST"])
def index():
    seq1 = ""
    seq2 = ""
    check_rev_comp = False
    result = None
    error = None

    if request.method == "POST":
        # Prefer uploaded FASTA file content if provided; otherwise use pasted text
        uploaded_1 = _read_uploaded_file(request.files.get("file1"))
        uploaded_2 = _read_uploaded_file(request.files.get("file2"))

        seq1 = uploaded_1 if uploaded_1.strip() else request.form.get("seq1", "")
        seq2 = uploaded_2 if uploaded_2.strip() else request.form.get("seq2", "")
        check_rev_comp = request.form.get("rev_comp") == "on"

        name1 = request.files["file1"].filename if uploaded_1.strip() else "Sequence 1"
        name2 = request.files["file2"].filename if uploaded_2.strip() else "Sequence 2"

        if not seq1.strip() or not seq2.strip():
            error = "Please provide both sequences either by uploading FASTA files or pasting text."
        else:
            result = analyze_sequences(
                seq1,
                seq2,
                check_rev_comp=check_rev_comp,
                default_name1=name1,
                default_name2=name2,
            )

    return render_template(
        "index.html",
        seq1=seq1,
        seq2=seq2,
        check_rev_comp=check_rev_comp,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
