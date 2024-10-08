import turtle
from datetime import *


# 抬起画笔，向前运动一段距离放下
def skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()


def mk_hand(name, length):
    # 注册Turtle形状，建立表针Turtle
    turtle.reset()
    skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    turtle.end_poly()
    # 返回最后记录的多边形。
    hand_form = turtle.get_poly()
    turtle.register_shape(name, hand_form)


def init():
    global sec_hand, minHand, hurHand, printer
    # 重置Turtle指向北
    turtle.mode("logo")
    # 建立三个表针Turtle并初始化
    mk_hand("secHand", 135)
    mk_hand("minHand", 125)
    mk_hand("hurHand", 90)
    sec_hand = turtle.Turtle()
    sec_hand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")

    for hand in sec_hand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    # 建立输出文字Turtle
    printer = turtle.Turtle()
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()


def setup_clock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            skip(-radius - 20)

            skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                skip(25)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                skip(-25)
            elif i == 25 or i == 35:
                skip(20)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                skip(-20)
            else:
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
            skip(-radius - 20)
        else:
            turtle.dot(5)
            skip(-radius)
        turtle.right(6)


def set_week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def set_date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s年%d月%d日" % (y, m, d)


def set_tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    sec_hand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)

    turtle.tracer(False)
    printer.forward(65)
    printer.write(set_week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(set_date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    turtle.tracer(True)

    # 100ms后继续调用tick
    turtle.ontimer(set_tick, 100)


def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    turtle.tracer(False)
    init()
    setup_clock(160)
    turtle.tracer(True)
    set_tick()
    turtle.mainloop()


if __name__ == "__main__":
    main()
