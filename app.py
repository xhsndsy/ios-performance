from flask import Flask, jsonify
from flask import render_template
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources=r'/*')

# def reserveStr(response):
#     res = response.strip('[')
#     res = res.strip(']')
#     res = res.split(',')
#     print(type(res))
#     print(res)


@app.route("/perfdata", methods=["GET", "POST"])
def perfDara():
    cpu_data = []
    gpu_data = []
    fps_data = []
    memory_data = []


    with open('./static/cpu.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-2]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            cpu_data.append(res)
        print(cpu_data)
    with open('./static/gpu.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-2]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            gpu_data.append(res)
        print(gpu_data)

    with open('./static/fps.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-2]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            fps_data.append(res)
        print(fps_data)

    with open('./static/memory.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-2]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            memory_data.append(res)
        print(memory_data)

    return jsonify({
        "cpu_data" : cpu_data,
        "gpu_data" : gpu_data,
        "fps_data" : fps_data,
        "memory_data" : memory_data
    })

if __name__ == '__main__':
    app.run(debug=True)