from flask import Flask, request, jsonify, render_template,url_for
#from flask_cors import CORS
app = Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    return render_template('index.html')





if __name__ == "__main__":
    app.run(debug=False)