import requests
import time
import QuestionName
import DockerImagesName

# 可变信息======================================
# 定义ip地址、端口、域名等
url_ip_port = ""
# 定义比赛的id
competition_id1=1
competition_id2=str(competition_id1)
# 定义管理员cookie
admin_cookie=""
# 可变信息======================================




# 批量添加题目+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 定义URL
url = f"http://{url_ip_port}/api/edit/games/{competition_id2}/challenges"
# 定义头信息
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": f"http://{url_ip_port}",
    "Referer": f"http://{url_ip_port}/admin/games/{competition_id2}/challenges",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": f"GZCTF_Token={admin_cookie}",
    "Connection": "close"
}
for i in range(1,350):
    j=str(i)
    # 定义数据
    data = {
        "title": f"{j}",
        "tag": "Web",
        "type": "DynamicContainer"
    }
    # 发送POST请求
    response = requests.post(url, headers=headers, json=data)
    # 输出响应
    print(response)
    time.sleep(0.1)
# 批量添加题目+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





# 批量更改题目分数和类型以及题目名称和DockerImages+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

for question_id in range(1,350):# 这里的question_id是题目id
    question_id_int=int(question_id)
    question_id_str=str(question_id)
    # 处理题目和dockerimages
    question_name_x=QuestionName.question_name[question_id-1]
    docker_images_name_x=DockerImagesName.docker_images_name[question_id-1]
    
    # 目标URL
    url = f"http://{url_ip_port}/api/edit/games/{competition_id2}/challenges/{question_id_str}"
    
    # 请求头
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
        "Content-Type": "application/json",
        "Origin": f"http://{url_ip_port}",
        "Referer": f"http://{url_ip_port}/admin/games/{competition_id2}/challenges/{question_id_str}",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": f"GZCTF_Token={admin_cookie}",
        "Connection": "close"
    }
    # 通过题目id判断题目类型
    if 1 <= question_id <= 4:
        question_type="Blockchain"
    if 5 <= question_id <= 210:
        question_type="Web"
    if 211 <= question_id <= 308:
        question_type="Hardware"
    if 309 <= question_id <= 341:
        question_type="Mobile"
    if 342 <= question_id <= 349:
        question_type="PPC"
    # 请求体
    data = {
        "id": question_id_int,
        "title": f"{question_name_x}",
        "content": "",
        "tag": f"{question_type}",
        "type": "DynamicContainer",
        "hints": [],
        "flagTemplate": None,
        "acceptedCount": 0,
        "fileName": "attachment",
        "attachment": None,
        "testContainer": None,
        "flags": [],
        "containerImage": f"{docker_images_name_x}",
        "memoryLimit": 64,
        "cpuCount": 1,
        "storageLimit": 256,
        "containerExposePort": 80,
        "enableTrafficCapture": False,
        "originalScore": 100,
        "minScoreRate": 0.17,
        "difficulty": 1
    }

    # 发送PUT请求
    response = requests.put(url, headers=headers, json=data)

    # 打印响应内容
    print(response)
    time.sleep(0.1)
# 批量更改题目分数和类型以及题目名称和DockerImages+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++