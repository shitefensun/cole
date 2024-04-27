import pygame
from turtle import *
import calendar
from datetime import datetime, timedelta
from tkinter import Tk, simpledialog, messagebox
import tkinter as tk  # 为tkinter设置别名tk


# 添加一个全局变量来追踪闹钟的状态
alarm_on = False

# 在代码的开始部分定义全局变量
alarm_time = None
# 创建一个隐藏的Tkinter主窗口
root = tk.Tk()
root.withdraw()

# 初始化修改时间变量
modi_datetime = datetime.now()

# 定义时钟函数
def clock(modi_y, modi_m, modi_d, modi_hour, modi_minite, modi_second):
    # 创建Tkinter窗口
    root = tk.Tk()
    root.title("用户功能")

    # 创建画布
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    # 创建设置时间按钮
    set_time_button = tk.Button(root, text="设置时间", command=set_time)
    set_time_button.pack(side=tk.LEFT, padx=10, pady=10)

    # 创建设置闹钟按钮
    set_alarm_button = tk.Button(root, text="设置闹钟", command=set_alarm)
    set_alarm_button.pack(side=tk.LEFT, padx=10, pady=10)

    # 创建关闭闹钟按钮
    stop_alarm_button = tk.Button(root, text="关闭闹钟", command=stop_alarm)
    stop_alarm_button.pack(side=tk.LEFT, padx=10, pady=10)


    # 创建指针和钟表框架
    tracer(False)
    handcre(50, 100, 150)
    frame(200)
    tracer(True)
    Tick(modi_y, modi_m, modi_d, modi_hour, modi_minite, modi_second)
    hideturtle()
    mainloop()

# 定义钟表框架绘制函数
def frame(radius):
    reset()
    pensize(7)
    penup()
    goto(radius + 20, 0)
    pendown()
    color('yellow3')
    circle(radius + 20)
    penup()
    goto(0, 0)
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius - 20)
        else:
            dot(5)
            Skip(-radius)
        right(6)

# 定义移动画笔但不绘制的函数
def Skip(step):
    penup()
    forward(step)
    pendown()

# 定义创建时钟指针的函数
def handcre(hourlength, minitelength, secondlength):
    global secHand, minHand, hurHand, printer
    mode("logo")  # 重置Turtle指向北
    # 建立三个表针Turtle并初始化
    mkHand("secHand", secondlength)
    mkHand("minHand", minitelength)
    mkHand("hurHand", hourlength)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()

# 注册Turtle形状，建立表针Turtle
def mkHand(name, length):
    reset()
    Skip(-length * 0.1)
    begin_poly()
    forward(length * 1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)
def handcre(hourlength, minitelength, secondlength):
    global secHand, minHand, hurHand, printer
    mode("logo")  # 重置Turtle指向北
    # 建立三个表针Turtle并初始化
    mkHand("secHand", secondlength)
    mkHand("minHand", minitelength)
    mkHand("hurHand", hourlength)
    secHand = Turtle()
    secHand.shape("secHand")
    secHand.color('green')
    minHand = Turtle()
    minHand.shape("minHand")
    minHand.color("blue")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    hurHand.color('red')
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()




# 定义获取星期的函数
def Week(year, month, day):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return week[calendar.weekday(year, month, day)]

# 定义设置当前时间的函数
run_tick = True  # 控制Tick函数是否继续执行的全局变量

def set_time():
    global modi_datetime, run_tick
    user_input = simpledialog.askstring('设置时间', '请输入当前的时间(格式如12:30:45):')
    if user_input:
        try:
            hour, minute, second = map(int, user_input.split(':'))
            now = datetime.now()
            # 更新全局时间变量
            modi_datetime = datetime(now.year, now.month, now.day, hour, minute, second)
            # 重置Tick函数的计时器
            run_tick = False  # 停止当前的Tick函数执行
            turtle.ontimer(lambda: reset_tick(), 1000)  # 安排重置和重新启动Tick函数
        except ValueError:
            messagebox.showerror("错误", "输入格式不正确，请重新输入。")

def reset_tick():
    global run_tick
    run_tick = True  # 重新允许Tick函数执行
    Tick(0, 0, 0, 0, 0, 0)  # 从新的时间开始执行Tick函数
# 初始化pygame混音器
pygame.mixer.init()

# 设置闹钟的铃声，这里假设铃声文件名为'alarm_sound.wav'，请确保该文件在您的程序目录中
#alarm_sound = pygame.mixer.Sound('D:\\桌面\\编程学习\\Python_study\\pythonProject1\\alarm_sound.mp3')#闹钟铃声文件存放的路径

# 用于存储修改后的时间和闹钟时间
modi_datetime = datetime.now()
alarm_time = None

# 检查闹钟时间并响铃
def check_alarm():
    global alarm_time
    current_time = datetime.now()
    # 如果当前时间达到或超过闹钟时间
    if alarm_time and current_time >= alarm_time:
        alarm_sound.play()  # 播放闹钟声音
        alarm_time = None  # 重置闹钟时间
        messagebox.showinfo("闹钟", "时间到了！")  # 弹出提醒窗口


def set_alarm():
    global alarm_time, alarm_on
    user_input = simpledialog.askstring("设置闹钟", "请输入闹钟时间(格式如7:30):")

    if user_input:
        try:
            hour, minute = map(int, user_input.split(':'))
            now = datetime.now()
            # 设置闹钟时间为今天的用户指定时间
            alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if alarm_time < now:
                # 如果设置的时间已经过去，则设置为第二天的该时间
                alarm_time += timedelta(days=1)
            messagebox.showinfo("闹钟设置", "闹钟已设置为：{}".format(alarm_time.strftime("%H:%M")))
        except ValueError:
            messagebox.showerror("设置错误", "输入格式不正确，请按照 '小时:分钟' 格式重新输入。")



def stop_alarm():
    """停止闹钟并关闭铃声"""
    global alarm_sound
    if alarm_sound:
        alarm_sound.stop()  # 正确停止pygame的Sound对象
        messagebox.showinfo("闹钟", "闹钟已关闭")  # 弹出提醒窗口
    else:
        messagebox.showinfo("闹钟", "没有激活的闹钟")  # 弹出提醒窗口
# 主函数，启动时钟程序
# 定义指针动态显示函数
def Tick(modi_y, modi_m, modi_d, modi_hour, modi_minite, modi_second):
    # 使用全局变量 modi_datetime 来保持时间状态
    global modi_datetime
    modi_datetime += timedelta(seconds=1)  # 每次调用Tick时增加1秒

    t = modi_datetime  # 使用修改的时间
    secHand.setheading(6 * t.second)
    minHand.setheading(6 * t.minute)
    hurHand.setheading(30 * (t.hour % 12))
    tracer(False)
    printer.clear()

    # 显示数字时间
    printer.color("black")
    printer.goto(0, -140)
    printer.write(t.strftime("%H:%M:%S"), align="center", font=("Courier", 20, "bold"))

    # 显示星期和日期
    printer.goto(0, -160)
    printer.write(Week(t.year, t.month, t.day), align="center", font=("Courier", 14, "bold"))
    printer.goto(0, -180)
    printer.write(t.strftime("%Y-%m-%d"), align="center", font=("Courier", 14, "bold"))

    tracer(True)
    check_alarm()  # 检查是否到达设定的闹钟时间

    # 使用捕获异常处理以避免窗口关闭后继续执行引起错误
    try:
        ontimer(lambda: Tick(modi_y, modi_m, modi_d, modi_hour, modi_minite, modi_second), 1000)
    except turtle.Terminator:
        return  # 如果窗口关闭则退出函数

def main():
    global modi_datetime
    modi_datetime = datetime.now()  # 初始化modi_datetime
    clock(0, 0, 0, 0, 0, 0)

if __name__ == '__main__':
    main()
    # 不进行修改