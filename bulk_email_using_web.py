from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        recipients = request.form.getlist("recipients")
        message = request.form["message"]
        # Simulate sending the email to each recipient
        for recipient in recipients:
            print(f"Email sent to {recipient}: {message}")
        return "Email(s) sent successfully!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
