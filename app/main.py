"""
Flask app that powers the three financial calculators
"""
from flask import Flask, render_template, request, jsonify
from app.calculators import mortgage_payment, retirement_401k, tax_liability

app = Flask(__name__)

#Pages
@app.route("/")
def show_mortgage():
    """ The mortgage calculator form """
    return render_template("mortgage.html")
@app.route("/401k-page")
def show_401k():
    """ The 401(k) calculator form """
    return render_template("retirement.html")
@app.route("/tax-page")
def show_tax():
    """ The tax calculator form """
    return render_template("tax.html")

#API endpoints
@app.post("/mortgage")
def api_mortgage():
    """ Return monthly mortgage payment as JSON"""
    data = request.get_json()
    payment = mortgage_payment(
        float(data["principal"]),
        float(data["rate"]),
        int(data["years"]),
    )
    return jsonify({"payment": round(payment, 2)})

@app.post("/401k")
def api_401k():
    """ Return the future 401k balance as JSON."""
    data = request.get_json()
    future_val = retirement_401k(
        float(data["balance"]),
        float(data["contribution"]),
        float(data["return"]),
        int(data["years"]),
    )
    return jsonify({"future_value": round(future_val, 2)})

@app.post("/tax")
def api_tax():
    """ Return estimated federal tax as JSON."""
    data = request.get_json()
    tax = tax_liability(
        float(data["income"]),
        data.get("status", "single"),
    )
    return jsonify({"tax": round(tax, 2)})

if __name__ == "__main__":
    #Run locally with: python main.py
    app.run(host="0.0.0.0", port=8080, debug=True)
