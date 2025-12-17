from flask import Flask, render_template, jsonify, session
import requests

app = Flask(__name__)
app.secret_key = "CHANGE_THIS_SECRET_KEY"

TEMP_MAIL_API = "https://api.internal.temp-mail.io/api/v3"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gen", methods=["GET"])
def generate_email():
    try:
        data = {
            "name": "user",
            "domain": "greencafe24.com"
        }
        r = requests.post(f"{TEMP_MAIL_API}/email/new", data=data)
        r.raise_for_status()
        email = r.json()["email"]

        session["email"] = email
        return jsonify({"status": "ok", "email": email})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)})

@app.route("/get", methods=["GET"])
def get_messages():
    email = session.get("email")
    if not email:
        return jsonify({"status": "error", "msg": "لا يوجد ايميل"})

    try:
        r = requests.get(f"{TEMP_MAIL_API}/email/{email}/messages")
        r.raise_for_status()
        return jsonify({"status": "ok", "messages": r.json()})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)})

@app.route("/delete", methods=["GET"])
def delete_account():
    session.clear()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
