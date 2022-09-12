from crypt import methods
from flask import Flask,json, request,make_response,jsonify
from flask_jwt_extended import jwt_manager,JWTManager,jwt_required, create_access_token,create_refresh_token,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///free.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "ddhdhdieieijensksksu8w992"
jwt = JWTManager(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, nullable=False,primary_key=True)
    username = db.Column(db.String(50),nullable=False,unique=True)
    password=db.Column(db.String(20),nullable=False)


@app.route('/')
def home():
    return "hello"

@app.post('/signup')
def signup():
    username = request.json["username"],
    password3 = request.json["password"]
    pwdhash = generate_password_hash(password3)
    
    user = User.query.filter_by(username=request.json["username"]).first()

    if user:
        return make_response(jsonify("username already in use"))
    
    userAccount = User(username=request.json["username"],password=pwdhash)
    db.session.add(userAccount)
    db.session.commit()
    return make_response(jsonify("account created succesfully"))



@app.route("/login", methods=["GET","POST"])
def login():
    data = request.json
    username3 = request.json["username"],
    password3 = request.json["password"]

    user = User.query.filter_by(username=request.json["username"]).first()

    if not user :
        return make_response(jsonify("User not found"))

    if check_password_hash(user.password, password3):
        access_token = create_access_token({
            "id":user.id,
            "username":user.username,
            "password":user.password
        })
        return make_response(jsonify({"accesstoken":access_token}))

    else:
        return make_response(jsonify("Incorrect password!,Please try again"))


if __name__ == "__main__":
    app.run(debug=True)