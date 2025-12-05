import tkinter as tk
from utils.tooltip import Tooltip  # 导入 Tooltip 类

def create_home_ui(content_frame):
    # 清空右侧内容区域
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # 创建一个框架来放置标签、下拉框和按钮
    frame = tk.Frame(content_frame)
    frame.pack(padx=10, pady=10)
    
    # 文本标签：显示 "请选择项目"
    label = tk.Label(frame, text="请选择项目", font=("Arial", 16), width=10)
    label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # 下拉框：用于显示可选的项目名称
    projects = ["20230710 旗舰版V10.11.4.0预约会议版 席媒终端客户端.exe等2个文件", "项目 B", "项目 C", "项目 D"]
    selected_project = tk.StringVar()
    selected_project.set(projects[0])  # 默认选择第一个项目
    dropdown = tk.OptionMenu(frame, selected_project, *projects)
    dropdown.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    dropdown.config(width=80)

    # 确定按钮：点击后显示选择的项目
    def on_button_click():
        print(f"你选择的项目是: {selected_project.get()}")

    button = tk.Button(frame, text="确定", command=on_button_click)
    button.grid(row=1, column=1, padx=10, pady=10, sticky="w")


    # 项目状态标签
    project_status = "实施中"  # 假设项目状态是“实施中”
    status_label = tk.Label(frame, text=f"项目状态: {project_status}", font=("Arial", 16))
    status_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    # 设备数量标签（蓝色字，鼠标悬停显示设备信息）
    device_count = 20  # 假设设备数量为 20 台
    devices_label = tk.Label(frame, text=f"设备数量: {device_count}台", font=("Arial", 16), fg="blue")
    devices_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    # 鼠标悬停提示设备信息
    device_info = "升降机 10 台, 桌牌 5 台, 其他 5 台"
    Tooltip(devices_label, device_info)

    # 项目地址标签
    project_address = "项目地址: XXXX"
    address_label = tk.Label(frame, text=project_address, font=("Arial", 16))
    address_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # 项目资料状态（红色字，鼠标悬停显示缺少的资料）
    missing_documents = 3  # 假设缺少 3 份资料
    documents_label = tk.Label(frame, text=f"项目资料: {missing_documents} 份资料缺失", font=("Arial", 16), fg="red")
    documents_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    # 鼠标悬停提示缺少的资料
    missing_docs_info = "缺少: 用户手册, 施工报告, 测试文档"
    Tooltip(documents_label, missing_docs_info)

    # 如果资料正常，可以显示“正常”状态
    if missing_documents == 0:
        documents_label.config(text="项目资料: 正常", fg="green")
