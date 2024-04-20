import pandas as pd
from flask import Flask, render_template, request

# Load your data (assuming a CSV file)
df = pd.read_csv(r"C:\Users\user\Desktop\Internship\Search Engine\final_csv.csv")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_term = request.form.get("search_term")
        results = df[df['ncc'].str.contains(search_term, case=False)]['name'].tolist()
        return render_template("results.html", search_term=search_term, results=results)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)