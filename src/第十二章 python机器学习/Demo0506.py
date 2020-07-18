# AUTHOR lijixin

import turtle

import turtle




turtle.pensize(3)
turtle.pencolor("black")
turtle.fillcolor("blue")
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200)

# 画左眼

turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# 画右眼
turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()


# 画三角形
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.circle(-50, steps=3)



turtle.penup()
turtle.goto(-150, -70)
turtle.pendown()
turtle.goto(0,-170)
turtle.pendown()
turtle.goto(150,-70)
turtle.pendown()
turtle.mainloop()  # 结果如
