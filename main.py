import tkinter as tk
from tkinter import ttk
from window.menu import create_menu
from window.home_ui import create_home_ui  # 导入新的首页UI模块

def create_main_window():
    # 创建主窗口
    root = tk.Tk()
    root.title("功能管理系统")       # 设置窗口标题
    root.geometry("800x600")        # 设置窗口大小800*600
    root.resizable(False, False)    # 禁止水平和垂直拉伸

    # 创建左侧菜单框架
    menu_frame = tk.Frame(root, width=200, bg="lightgray")
    menu_frame.grid(row=0, column=0, sticky="ns")

    # 创建右侧内容框架
    content_frame = tk.Frame(root, width=600, bg="white")
    content_frame.grid(row=0, column=1, sticky="nsew")

    # 创建菜单
    create_menu(menu_frame, content_frame)

    # 使内容框架自适应窗口大小
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    # 默认加载首页
    create_home_ui(content_frame)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
