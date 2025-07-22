from flask import Flask, request, jsonify, render_template,url_for
from services.FileProcessing import FileProcessing
#from flask_cors import CORS
app = Flask(__name__)
# CORS(app)
fileProcess = FileProcessing()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handleFilesSubmission',methods=['POST'])
def handle_files_submission():

    optionSelected  = request.form['option']
    files = request.files.getlist('file')

    #process files
    results = [fileProcess.processFile(f) for f in files]
    print("processed files:", results)

    #return results
    return jsonify({"option":optionSelected,"results": ''.join(results)})





if __name__ == "__main__":
    app.run(debug=False)