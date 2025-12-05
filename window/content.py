import tkinter as tk
from window.home_ui import create_home_ui  # 导入新的首页UI模块
from window.projects import create_projects_ui  # 导入新的项目UI模块
def create_content_frame(content_frame):
    
    # 选择首页菜单，显示首页的UI
    def display_home():

        # 调用 home_ui.py 中的 create_home_ui 方法
        create_home_ui(content_frame)

    def display_projects():
        # 调用 projects_ui.py 中的 create_projects_ui 方法
        create_projects_ui(content_frame)

    def display_clients():
        frame = tk.Frame(content_frame)
        frame.pack(padx=10, pady=10)
        label = tk.Label(frame, text="这里是客户管理", font=("Arial", 20))
        label.pack(padx=10, pady=10)
        # 客户管理专用UI
        button = tk.Button(frame, text="添加客户", command=lambda: print("客户添加"))
        button.pack(pady=5)

    def display_system():
        frame = tk.Frame(content_frame)
        frame.pack(padx=10, pady=10)
        label = tk.Label(frame, text="这里是系统管理", font=("Arial", 20))
        label.pack(padx=10, pady=10)
        # 系统管理专用UI
        button = tk.Button(frame, text="查看日志", command=lambda: print("查看日志"))
        button.pack(pady=5)

    # 根据菜单选择显示不同的UI
    def on_select_menu(menu_name):
        if menu_name == "home":
            display_home()
        elif menu_name == "projects":
            display_projects()
        elif menu_name == "clients":
            display_clients()
        elif menu_name == "system":
            display_system()
        # 其他菜单的UI
        else:
            label = tk.Label(content_frame, text="请选择一个功能", font=("Arial", 18))
            label.pack(padx=10, pady=10)
    
    return on_select_menu
