from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template('index.html')

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        role = request.form["role"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = User(username=username, email=email, role=role, password_hash=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Berhasul Registrasi!", "success")
            return redirect(url_for("main.login"))
        except Exception as e:
            db.session.rollback()
            flash("Username atau email sudah ada.", "danger")
    return render_template("register.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            # Menyimpan data pengguna ke session
            session["user_id"] = user.id
            session["username"] = user.username
            session["role"] = user.role
            flash("Login successful!", "success")
            return redirect(url_for("main.dashboard"))  # Pastikan untuk menggunakan nama blueprint di sini
        else:
            flash("Email atau password salah!", "danger")

    return render_template("login.html")


@main.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Anda perlu login.", "warning")
        return redirect(url_for("main.login"))
    
    users = User.query.all()
    total_users = User.query.count()  # Hitung total pengguna
    return render_template("dashboard.html", users=users, total_users=total_users)

@main.route("/add_user", methods=["GET", "POST"])
def add_user():
    if "user_id" not in session or session.get("role") != "admin":
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        role = request.form["role"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = User(username=username, email=email, role=role, password_hash=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("User berhasil ditambahkan!", "success")
            return redirect(url_for("main.dashboard"))
        except Exception as e:
            db.session.rollback()
            flash("Error add user.", "danger")
    return render_template("add_user.html")

@main.route("/edit_user/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    # Cek apakah pengguna sudah login
    if "user_id" not in session:
        flash("You need to login first.", "warning")
        return redirect(url_for("main.login"))
    
    user = User.query.get_or_404(id)
    
    # Admin bisa mengedit pengguna lain, user hanya bisa mengedit dirinya sendiri
    if session.get("role") != "admin" and session.get("user_id") != user.id:
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))
    
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        
        # Hanya admin yang bisa mengubah role
        if session.get("role") == "admin":
            user.role = request.form["role"]
        
        if request.form["password"]:
            user.password_hash = generate_password_hash(request.form["password"], method="pbkdf2:sha256")
        
        try:
            db.session.commit()
            flash("User updated successfully!", "success")
            return redirect(url_for("main.dashboard"))
        except Exception as e:
            db.session.rollback()
            flash("Error updating user.", "danger")
    
    return render_template("edit_user.html", user=user)


@main.route("/delete_user/<int:id>", methods=["POST"])
def delete_user(id):
    # Cek apakah pengguna sudah login
    if "user_id" not in session:
        flash("You need to login first.", "warning")
        return redirect(url_for("main.login"))
    
    user = User.query.get_or_404(id)
    
    # Admin bisa menghapus pengguna lain, user hanya bisa menghapus dirinya sendiri
    if session.get("role") != "admin" and session.get("user_id") != user.id:
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))
    
    try:
        db.session.delete(user)
        db.session.commit()
        flash("User successfully deleted!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Error deleting user.", "danger")
    
    return redirect(url_for("main.dashboard"))


@main.route("/logout")
def logout():
    session.clear()
    flash("Berhasil Logout.", "success")
    return redirect(url_for("main.home"))
