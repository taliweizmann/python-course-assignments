from flask import Flask, render_template, request
from lcs_finder import find_longest_common_substring

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    common_sub = None
    seq1 = ""
    seq2 = ""
    sub_length = 0

    if request.method == "POST":
        seq1 = request.form.get("seq1", "").strip().upper()
        seq2 = request.form.get("seq2", "").strip().upper()

        if seq1 and seq2:
            common_sub = find_longest_common_substring(seq1, seq2)
            sub_length = len(common_sub)

    return render_template(
        "index.html",
        seq1=seq1,
        seq2=seq2,
        common_sub=common_sub,
        sub_length=sub_length
    )

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
