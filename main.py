import time
import requests
import tidevice
from tidevice._perf import DataType
import pandas as pd
import matplotlib.pyplot as plt
import os

file = open('./static/cpu.txt', 'w', encoding='utf-8')
file.close()
file = open('./static/fps.txt', 'w', encoding='utf-8')
file.close()
file = open('./static/gpu.txt', 'w', encoding='utf-8')
file.close()
file = open('./static/memory.txt', 'w', encoding='utf-8')
file.close()

t = tidevice.Device()
perf = tidevice.Performance(t, [DataType.CPU, DataType.MEMORY, DataType.FPS, DataType.GPU])
#  tidevice version <= 0.4.16:
#  perf = tidevice.Performance(t)

cpu_list = []
memory_list = []
gpu_list = []
fps_list = []
network_list = []

memoryData = []
memoryTime = []
fpsData = []
fpsTime = []
gpuData = []
gpuTime = []
cpuData = []
cpuTime = []
networkData = []
networkTime = []

# 将dict数据存储到字典里
def getList(getdata:list ,outdata:list, datetime, value='value'):
    for res in getdata:
        outdata.append(res[value])
        datetime.append(res['timestamp'])


# 时间戳格式化为时间
def exTimestamp(timestamp:list) -> list:
    res = []
    for tm in timestamp:
        localtime = time.localtime(tm/1000)
        otherStyleTime = time.strftime("%H:%M:%S", localtime)
        res.append(otherStyleTime)
    return res


# 把抓取到的性能数据写入文件
def writePerfData(path, data:dict, value='value'):
    with open(path, mode='a') as filename:
        filename.write("%s, %s"%(data[value], data['timestamp']))
        filename.write('\n')


# python连接远程服务器，发送文件
def uploadData(url, file_path):
    data = {'file': open(file_path, 'rb')}
    respoonse = requests.post(url, files=data)
    print(respoonse.status_code)


# 性能数据的回调获取
def callback(_type: tidevice.DataType, value: dict):
    print(_type.value, value)
    if _type.value == 'memory':
        memory_list.append(value)
        writePerfData('./static/memory.txt', value)
    if _type.value == "cpu":
        cpu_list.append(value)
        writePerfData('./static/cpu.txt', value, value='sys_value')
    if _type.value == "fps":
        fps_list.append(value)
        writePerfData('./static/fps.txt', value)
    if _type.value == "gpu":
        gpu_list.append(value)
        writePerfData('./static/gpu.txt', value)


# 在这里修改需要跑的包名以及性能数据
perf.start("com.netflix.NGP.SamuraiShowdownNETFLIX", callback=callback)
time.sleep(3000)
perf.stop()


print(memory_list, cpu_list, fps_list, gpu_list)
# 格式化写入文件
getList(memory_list, memoryData, memoryTime)
getList(cpu_list, cpuData, cpuTime, 'sys_value')
getList(gpu_list, gpuData, gpuTime)
getList(fps_list, fpsData, fpsTime)

# 将性能测试数据发送至服务器
url = 'http://xhsndsy.top/upload'
for path in os.listdir('./static'):
    file_path = './static/' + path
    uploadData(url, file_path)


#se
# print(cpuData)
# print(gpuData)
# print(fpsData)
# print(memoryData)

colors = ['red', 'green', 'blue', 'yellow']
line_style = ['-', '-', '-', '-']
y_labels = ["cpu Usage", "gpu Sys", "fps", "memory Usage"]


# 画图
y_data = [cpuData, gpuData, fpsData, memoryData]
x_data = [exTimestamp(cpuTime), exTimestamp(gpuTime), exTimestamp(fpsTime), exTimestamp(memoryTime)]
for i in range(4):
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(20, 12), dpi=100)
    axs.plot(x_data[i], y_data[i], c=colors[i], label=y_labels[i], linestyle=line_style[i])
    # axs.scatter(x_data[i], y_data[i], c=colors[i])
    axs.legend(loc='best')
    axs.set_yticks(range(0, 130, 5))
    # axs.grid(True, linestyle='--', alpha=0.5)
    axs.set_xlabel("time", fontdict={'size': 16})
    axs.set_ylabel(y_labels[i], fontdict={'size': 16}, rotation=0)
    axs.set_title("performance".format(y_labels[i]), fontdict={'size': 20})
    fig.autofmt_xdate()

    plt.savefig(y_labels[i]+".png",dpi=300)
    # plt.show()

