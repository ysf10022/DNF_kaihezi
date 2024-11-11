import ctypes
from ctypes import wintypes
import win32gui
import time
import win32con
import os
import json

# 启用 DPI 感知，以防止 DPI 缩放影响坐标
ctypes.windll.user32.SetProcessDpiAwarenessContext(-4)

# 定义 SendInput 所需常量
INPUT_MOUSE = 0
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("mi", MOUSEINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", wintypes.DWORD), ("_input", _INPUT)]

SendInput = ctypes.windll.user32.SendInput

def load_relative_coords(filename):
    """
    从 JSON 文件加载相对坐标
    """
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(exe_dir, filename)
    with open(file_path, 'r') as file:
        return json.load(file)

def save_relative_coords(filename, relative_coords):
    """
    保存相对坐标到 JSON 文件
    """
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(exe_dir, filename)
    with open(file_path, 'w') as file:
        json.dump(relative_coords, file)
    print(f"相对坐标已保存到 {file_path}")

def get_window_rect(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print(f"未找到窗口: {window_title}")
        return None
    rect = wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect.left, rect.top, rect.right, rect.bottom

def get_window_dpi(hwnd):
    """
    获取窗口的 DPI 缩放比例
    """
    try:
        dpi = ctypes.windll.user32.GetDpiForWindow(hwnd)
        return dpi / 96.0  # 96 是标准 DPI
    except:
        return 1.0

def convert_to_relative(window_title, abs_coords):
    """
    将屏幕绝对坐标转换为相对客户区坐标
    """
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print(f"未找到窗口: {window_title}")
        return None

    # 获取客户区（内容区域）的尺寸
    client_rect = wintypes.RECT()
    ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(client_rect))
    client_width = client_rect.right - client_rect.left
    client_height = client_rect.bottom - client_rect.top

    # 获取客户区左上角的屏幕坐标
    screen_point = wintypes.POINT(0, 0)
    ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(screen_point))
    left, top = screen_point.x, screen_point.y

    # 将绝对坐标转换为相对坐标
    relative_coords = []
    for (abs_x, abs_y, right_click) in abs_coords:
        # 转换为相对于客户区的坐标
        rel_x = (abs_x - left) / client_width
        rel_y = (abs_y - top) / client_height
        relative_coords.append((rel_x, rel_y, right_click))
    
    return relative_coords


def convert_to_absolute(window_title, rel_x, rel_y):
    """
    将相对坐标转换为屏幕绝对坐标，基于客户区坐标
    """
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print(f"未找到窗口: {window_title}")
        return None

    # 获取客户区（内容区域）的尺寸
    client_rect = wintypes.RECT()
    ctypes.windll.user32.GetClientRect(hwnd, ctypes.byref(client_rect))
    client_width = client_rect.right - client_rect.left
    client_height = client_rect.bottom - client_rect.top

    # 将客户区的左上角转换为屏幕坐标
    screen_point = wintypes.POINT(0, 0)
    ctypes.windll.user32.ClientToScreen(hwnd, ctypes.byref(screen_point))
    left, top = screen_point.x, screen_point.y

    # 基于客户区尺寸和位置计算绝对坐标
    abs_x = int(left + rel_x * client_width)
    abs_y = int(top + rel_y * client_height)
    return abs_x, abs_y


def send_click(x, y, right_click=False):
    """
    使用 SendInput 模拟鼠标点击
    """
    ctypes.windll.user32.SetCursorPos(x, y)
    if right_click:
        mouse_down = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(0, 0, 0, MOUSEEVENTF_RIGHTDOWN, 0, None))
        mouse_up = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(0, 0, 0, MOUSEEVENTF_RIGHTUP, 0, None))
    else:
        mouse_down = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(0, 0, 0, MOUSEEVENTF_LEFTDOWN, 0, None))
        mouse_up = INPUT(type=INPUT_MOUSE, mi=MOUSEINPUT(0, 0, 0, MOUSEEVENTF_LEFTUP, 0, None))
    SendInput(1, ctypes.byref(mouse_down), ctypes.sizeof(mouse_down))
    time.sleep(0.05)
    SendInput(1, ctypes.byref(mouse_up), ctypes.sizeof(mouse_up))

def bring_window_to_front(hwnd):
    """
    将窗口置于前台
    """
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    time.sleep(0.1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.1)

def perform_actions(window_title, iterations, coords):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print("未找到游戏窗口")
        return

    bring_window_to_front(hwnd)

    for i in range(iterations):
        print(f"执行第 {i + 1} 次循环")
        for rel_x, rel_y, right_click in coords:
            abs_coords = convert_to_absolute(window_title, rel_x, rel_y)
            if abs_coords:
                abs_x, abs_y = abs_coords
                send_click(abs_x, abs_y, right_click)
                time.sleep(0.1)
    print("操作完成")

# if __name__ == "__main__":
#     #原始绝对坐标
#     coords1 = [
#         (737, 512, True),
#         (655, 359, False),
#         (643,378, False),
#         (658,378, False),
#         (627,395, False),
#         (642,559, False),
#         (525,644, False),
#         (610, 561, False),
#         (610, 561, False),
#         (642, 565, False)
#     ]
    # coords2=[        
    #     (739, 474, True),   # 右键点击
    #     (659, 323, False),  # 左键点击
    #     (622,339, False),  # 左键点击
    #     (641,371,False),
    #     (526,578,False),
    #     (614,522,False),
    #     (614,522,False),
    #     (637,529,False)

    # ]

#     # 将绝对坐标转换为相对坐标
    window_title = "地下城与勇士：创新世纪"


#     #
#     # try:
#     #     relative_coords = load_relative_coords("relative_coords.json")
#     #     print("相对坐标加载成功:", relative_coords)
#     #     iterations = 2
#     #     perform_actions(window_title, iterations, relative_coords)
#     # except FileNotFoundError:
#     #     print("相对坐标文件未找到")

    # relative_coords = convert_to_relative(window_title, coords2)
    # if relative_coords:
    #     save_relative_coords("relative_coords_zidingyi_16_9_1280x720.json", relative_coords)
    # else:
    #     print("转换相对坐标失败")
    


    '''
    coords2=[        
        (739, 474, True),   # 右键点击
        (659, 323, False),  # 左键点击
        (622,339, False),  # 左键点击
        (641,371,False),
        (526,578,False),
        (614,522,False),
        (614,522,False),
        (637,529,False)

    ]
    window_title = "地下城与勇士：创新世纪"  # 请替换为你的游戏窗口标题
    hwnd = win32gui.FindWindow(None, window_title)
    bring_window_to_front(hwnd)

    

    iterations = 2  # 设置循环次数
    perform_actions(window_title, iterations,coords2)
    print("操作完成")
    '''