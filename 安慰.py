import tkinter as tk
import math
import time
import random

class HeartAnimation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 先隐藏主窗口
        self.windows = []
        
        # 更多不重复的温暖话语
        self.heart_messages = [
            "你很棒哦", "要开心呐", "慢慢来哦", "我在这呢", "别放弃哦", "会好的啦", 
            "有人爱你", "要坚强哦", "深呼吸", "放松点", "会过去呐", "抱紧你哦",
            "不孤单哦", "慢慢走", "你很美", "没关系", "有希望", "笑一笑",
            "你很暖", "有我在", "要加油", "别害怕", "休息下", "慢慢来",
            "值得爱", "歇会叭", "没关系啦", "慢慢说哦", "我懂你哒", "辛苦了",
            "你很特别", "慢慢呼吸", "今天很棒", "你很勇敢", "世界需要你",
            "一切会好", "你很温柔", "慢慢成长", "你很珍贵", "我在倾听",
            "不必着急", "你很独特", "今天辛苦", "允许休息", "慢慢感受",
            "你很好", "我信你", "慢慢来", "你可以的", "我陪你捏"
        ]
        
        # 柔和的颜色组合
        self.colors = [
            '#FFB6C1', '#FFC0CB', '#FFD1DC', '#FFE4E1', '#FFF0F5',
            '#FFE4E6', '#FFD7D9', '#FFCBCF', '#FFBFC5', '#FFB3BB',
            '#E6E6FA', '#F0F8FF', '#F5F5DC', '#FFFACD', '#FFEFD5',
            '#FFE4B5', '#FFDAB9', '#FFDEAD', '#FFF8DC', '#FDF5E6'
        ]
        
        # 获取屏幕尺寸
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # 打乱消息顺序，确保不重复
        random.shuffle(self.heart_messages)
        
    def center_window(self, window, width, height):
        """将窗口居中显示"""
        x = (self.screen_width - width) // 2
        y = (self.screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
        
    def show_initial_window(self):
        """显示初始窗口"""
        self.initial_window = tk.Toplevel()
        self.initial_window.title("温暖的话")
        self.initial_window.configure(bg='#FFF0F5')
        
        # 设置窗口大小并居中
        self.center_window(self.initial_window, 400, 200)
        
        label = tk.Label(self.initial_window, text="不要难过啦", 
                        font=("Microsoft YaHei", 24, "bold"),
                        fg='#FF69B4', bg='#FFF0F5')
        label.pack(expand=True)
        
        # 绑定关闭事件到初始窗口
        self.initial_window.protocol("WM_DELETE_WINDOW", self.close_all_windows)
        
        # 3秒后关闭初始窗口并开始爱心动画
        self.initial_window.after(1000, lambda: [self.initial_window.destroy(), self.create_heart()])
        
    def create_heart(self):
        """创建爱心形状的窗口"""
        # 计算爱心中心点位置（屏幕中心）
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        
        # 生成爱心形状的坐标
        points = []
        for t in range(0, 628, 8):  # 减小步长使爱心更密集
            t = t / 100
            x = 16 * (math.sin(t) ** 3)
            y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
            # 缩放和平移坐标，使爱心居中
            x = x * 10 + center_x
            y = -y * 10 + center_y
            points.append((x, y))
        
        # 逐个创建窗口
        self.create_windows_one_by_one(points)
    
    def create_windows_one_by_one(self, points):
        """逐个创建窗口"""
        for i, (x, y) in enumerate(points):
            # 减慢速度，每个窗口间隔150毫秒
            self.root.after(i * 150, lambda x=x, y=y, idx=i: self.create_single_window(x, y, idx))
    
    def create_single_window(self, x, y, index):
        """创建单个窗口"""
        window = tk.Toplevel()
        window.title("温暖的话")
        
        # 设置窗口大小和位置
        window_width = 120
        window_height = 100
        window.geometry(f"{window_width}x{window_height}+{int(x-window_width/2)}+{int(y-window_height/2)}")
        
        # 设置窗口颜色 - 使用柔和的粉色系
        color_index = index % len(self.colors)
        bg_color = self.colors[color_index]
        window.configure(bg=bg_color)
        
        # 添加文字
        message_index = index % len(self.heart_messages)
        label = tk.Label(window, text=self.heart_messages[message_index],
                        font=("Microsoft YaHei", 14, "bold"),
                        fg='#8B0000', bg=bg_color,  # 使用深红色文字，确保可读性
                        wraplength=100,
                        justify='center')
        label.pack(expand=True)
        
        # 绑定关闭事件 - 使用protocol方法处理窗口关闭按钮
        window.protocol("WM_DELETE_WINDOW", self.close_all_windows)
        
        # 同时绑定鼠标点击事件
        window.bind('<Button-1>', self.close_all_windows)
        label.bind('<Button-1>', self.close_all_windows)
        
        self.windows.append(window)
    
    def close_all_windows(self, event=None):
        """关闭所有窗口"""
        # 关闭所有爱心窗口
        for window in self.windows:
            try:
                window.destroy()
            except:
                pass
        
        # 关闭初始窗口（如果还存在）
        try:
            self.initial_window.destroy()
        except:
            pass
        
        # 关闭主窗口
        self.root.destroy()
    
    def run(self):
        """运行程序"""
        self.root.after(100, self.show_initial_window)
        self.root.mainloop()

if __name__ == "__main__":
    # 设置UTF-8编码
    import sys
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    
    app = HeartAnimation()
    app.run()