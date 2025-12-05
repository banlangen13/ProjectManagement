import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

        # 创建绑定事件
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        if self.tooltip:
            return
        # 创建一个标签显示提示信息
        x = self.widget.winfo_rootx() + event.x
        y = self.widget.winfo_rooty() + event.y + 20  # 设置显示位置

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)  # 去掉窗口边框
        self.tooltip.wm_geometry(f"+{x}+{y}")  # 设置弹出窗口位置

        label = tk.Label(self.tooltip, text=self.text, background="yellow", relief="solid", padx=5, pady=5)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
