import turtle

# 创建一个乌龟实例
t = turtle.Turtle()

# 设置乌龟的形状为乌龟图标
turtle.shape('turtle')

# 设置乌龟的颜色为绿色
t.color('green')

# 绘制乌龟的身体
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)

# 绘制乌龟的头部
t.right(45)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# 完成绘制，隐藏乌龟
turtle.done()
