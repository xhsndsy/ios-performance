from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from utils import getPerfData, getPackageName


app = Flask(__name__)

CORS(app, resources=r'/*')

# def reserveStr(response):
#     res = response.strip('[')
#     res = res.strip(']')
#     res = res.split(',')
#     print(type(res))
#     print(res)


@app.route("/perfdata", methods=["GET", "POST"])
def perfData():
    cpu_data = []
    gpu_data = []
    fps_data = []
    memory_data = []

    pakname = request.values.get('department')

    if pakname is None:
        cpu_data, gpu_data, fps_data, memory_data = getPerfData('./static/')
    else:
        cpu_data, gpu_data, fps_data, memory_data = getPerfData('./static/' + pakname)

    return jsonify({
        "cpu_data" : cpu_data,
        "gpu_data" : gpu_data,
        "fps_data" : fps_data,
        "memory_data" : memory_data
    })


@app.route("/upload", methods=["POST"])
def uploadData():
    file = request.files['file']
    # print(file)
    file.save('./static/' + secure_filename(file.filename))
    return jsonify('OK')


if __name__ == '__main__':
    app.run(debug=True)