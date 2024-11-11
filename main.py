import sys
import threading
import keyboard
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from Ui_kaihezi import Ui_widget  # 确保正确导入生成的 Ui_Form 类
from kaihezi import convert_to_absolute, send_click, bring_window_to_front, load_relative_coords
import win32gui
import time
import os
import ctypes

# 设置 DPI 感知，确保在高 DPI 环境下鼠标点击位置正确
try:
    ctypes.windll.user32.SetProcessDpiAwarenessContext(-4)  # 每个显示器 DPI 感知 (Per Monitor v2)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDpiAwareness(2)  # 每个显示器 DPI 感知 (Per Monitor)
    except Exception:
        ctypes.windll.user32.SetProcessDPIAware()  # 系统 DPI 感知
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

class ClickerApp(QWidget):
    def __init__(self):
        super(ClickerApp, self).__init__()
        self.ui = Ui_widget()  # 创建 Ui_Form 实例
        self.ui.setupUi(self)  # 将 QWidget 实例传递给 setupUi 方法
        self.json_file = None
        self.stop_flag = False

        # 绑定按钮和下拉框事件
        self.ui.pushButton.clicked.connect(self.start_clicking)
        self.ui.comboBox.currentIndexChanged.connect(self.select_box_type)
        # 初始化时手动调用一次 select_box_type
        self.select_box_type()
        # 启动热键监听线程
        threading.Thread(target=self.listen_for_hotkey, daemon=True).start()

    def resource_path(self, relative_path):
        """ 获取打包后的文件路径 """
        try:
            base_path = sys._MEIPASS  # PyInstaller 打包后的临时目录
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def select_box_type(self):

        box_type = self.ui.comboBox.currentText().strip()
        print(f"选择的盒子类型: '{box_type}'")
        if box_type == "自定义盒子/3词条固定盒子-开上衣":
            self.json_file = "relative_coords_zidingyi_16_9_1280x720.json"
        elif box_type == "万象固定盒子-开巨剑":
            self.json_file = "relative_coords_miwu_16_9_1280x720.json"
        else:
            self.json_file = None

        # 检查是否正确加载了 JSON 文件
        if self.json_file and os.path.exists(self.json_file):
            print(f"已加载文件: {self.json_file}")

    def start_clicking(self):
        if not self.json_file:
            QMessageBox.warning(self, "错误", "请选择有效的盒子类型")
            return

        iterations = int(self.ui.lineEdit.text())
        self.stop_flag = False
        threading.Thread(target=self.perform_actions, args=(iterations,), daemon=True).start()

    def stop_clicking(self):
        self.stop_flag = True

    def perform_actions(self, iterations):
        """
        执行鼠标点击操作
        """
        coords = load_relative_coords(self.json_file)
        window_title = "地下城与勇士：创新世纪"
        hwnd = win32gui.FindWindow(None, window_title)

        if hwnd == 0:
            QMessageBox.warning(self, "错误", "未找到游戏窗口")
            return

        bring_window_to_front(hwnd)
        
        for i in range(iterations):
            if self.stop_flag:
                break
            for rel_x, rel_y, right_click in coords:
                abs_coords = convert_to_absolute(window_title, rel_x, rel_y)
                if abs_coords:
                    abs_x, abs_y = abs_coords
                    send_click(abs_x, abs_y,right_click)
                    time.sleep(0.5)
        self.ui.label_7.setText("操作完成")

    def listen_for_hotkey(self):
        """
        监听 F10 热键以停止操作
        """
        keyboard.add_hotkey("F10", self.stop_clicking)
        keyboard.wait()

if __name__ == "__main__":
    if not is_admin():
        QMessageBox.warning(None, "权限不足", "请以管理员身份运行程序")
        sys.exit()
    app = QApplication(sys.argv)
    window = ClickerApp()
    window.show()
    sys.exit(app.exec())
