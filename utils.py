import config


# 获取性能测试数据
def getPerfData(path):
    cpu_data = []
    gpu_data = []
    fps_data = []
    memory_data = []

    with open(path + '/cpu.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-1]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            cpu_data.append(res)
        # print(cpu_data)
    with open(path + '/gpu.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-1]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            gpu_data.append(res)
        # print(gpu_data)

    with open(path + '/fps.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-1]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            fps_data.append(res)
        # print(fps_data)

    with open(path + '/memory.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmpstr = line[:-1]
            res = tmpstr.split(', ')
            res = list(map(int, map(float, res)))
            res.reverse()
            memory_data.append(res)
        # print(memory_data)

    return cpu_data, gpu_data, fps_data, memory_data


# 获取包名切片创建文件夹
def getPackageName():
    pak_name = config.PackageName
    pak_list = pak_name.split('.')

    return pak_list[-1]

#
# cpu_data, gpu_data, fps_data, memory_data = getPerfData('./static')
#
# print(cpu_data)
