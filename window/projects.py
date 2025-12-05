import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from utils.tooltip import Tooltip  # 导入 Tooltip 类
from tkcalendar import DateEntry

project_list = [
    {"name": "项目 A", "address": "地址 A", "devices": 5, "docs": 2},
    {"name": "项目 B", "address": "地址 B", "devices": 8, "docs": 4},
    {"name": "项目 C", "address": "地址 C", "devices": 10, "docs": 1}
]
    
def create_projects_ui(content_frame):
    # 清空右侧内容区域
    for widget in content_frame.winfo_children():
        widget.destroy()

    # 创建一个框架来放置按钮和项目列表
    frame = tk.Frame(content_frame)
    frame.pack(padx=10, pady=10)



    # 项目名称输入框
    name_label = tk.Label(frame, text="项目名称:")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    project_name_entry = tk.Entry(frame)
    project_name_entry.grid(row=0, column=1, padx=10, pady=10)

    # 项目状态下拉框
    status_label = tk.Label(frame, text="项目状态:")
    status_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")
    status_options = ["请选择", "实施中", "已验收", "实施完成"]
    status_combobox = ttk.Combobox(frame, values=status_options)
    status_combobox.grid(row=0, column=3, padx=10, pady=10)

    # 实施人员下拉框
    personnel_label = tk.Label(frame, text="实施人员:")
    personnel_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    personnel_options = ["请选择", "张三", "李四", "王五"]
    personnel_combobox = ttk.Combobox(frame, values=personnel_options)
    personnel_combobox.grid(row=1, column=1, padx=10, pady=10)

        # 起始日期选择框
    start_date_label = tk.Label(frame, text="开始日期:")
    start_date_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    start_date_entry = DateEntry(frame, width=20, background='darkblue', foreground='white', borderwidth=2)
    start_date_entry.grid(row=2, column=1, padx=10, pady=10)

    # 结束日期选择框
    end_date_label = tk.Label(frame, text="结束日期:")
    end_date_label.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    end_date_entry = DateEntry(frame, width=20, background='darkblue', foreground='white', borderwidth=2)
    end_date_entry.grid(row=2, column=3, padx=10, pady=10)

    # 查询按钮，占两行
    query_button = tk.Button(frame, text="查询", command=lambda: query_projects(project_name_entry.get(), status_combobox.get(), personnel_combobox.get()))
    query_button.grid(row=3, column=0, padx=10, pady=10)

    def query_projects(name, status, personnel):
        print(f"查询项目: {name}, {status}, {personnel}")