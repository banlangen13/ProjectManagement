import tkinter as tk
from tkinter import ttk
from window.content import create_content_frame

def create_menu(menu_frame, content_frame):
    # 创建菜单选项
    menu_items = [
        ("首页", "home"),
        ("项目管理", "projects"),
        ("客户管理", "clients"),
        ("设备管理", "devices"),
        ("问题管理", "issues"),
        ("资料管理", "docs"),
        ("系统管理", "system")
    ]

    # 创建一个用于存储子菜单的字典
    sub_menus = {}
    # 获取右侧显示的更新方法
    on_select_menu = create_content_frame(content_frame)

    
    # 创建主菜单项
    for item in menu_items:
        menu_name = item[0]
        menu_key = item[1]
        button = tk.Button(menu_frame, text=menu_name, anchor="w", command=lambda key=menu_key: on_select_menu(key))
        button.pack(fill="x", padx=10, pady=5)

        # 如果有子菜单
        if len(item) > 2:
            submenu_frame = tk.Frame(menu_frame, bg="lightgray")
            submenu_frame.pack(fill="x")
            for sub_item in item[2]:
                sub_menu_name = sub_item[0]
                sub_menu_key = sub_item[1]
                sub_button = tk.Button(submenu_frame, text=sub_menu_name, anchor="w", command=lambda key=sub_menu_key: on_select_menu(key))
                sub_button.pack(fill="x", padx=20, pady=5)
            sub_menus[menu_key] = submenu_frame
        else:
            sub_menus[menu_key] = None



