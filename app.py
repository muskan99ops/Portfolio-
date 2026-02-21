from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey"

# -----------------------------
# Create Database and Table
# -----------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Home Page
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )

        conn.commit()
        conn.close()

        flash("Message Sent Successfully!")
        return redirect("/#contact")

    return render_template("index.html")

# -----------------------------
# Admin Page (View Messages)
# -----------------------------
@app.route("/admin")
def admin():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()

    conn.close()
    return render_template("admin.html", messages=data)

# -----------------------------
# Delete Message
# -----------------------------
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM messages WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/admin")

# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)