import turtle

t = turtle.Turtle()
t.pensize(3)
t.shape("turtle")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
t.pencolor("Black")
t.fillcolor("Black")
go(146.75, 61.41)
t.begin_fill()
t.seth(116.22)
t.circle(223.74, 55.25)
t.seth(69.37)
t.circle(70.50, 195.81)
t.seth(264.94)
t.circle(71.50, 46.5)
t.seth(210.88)
t.circle(125.94, 105.88)
t.seth(316.76)
t.circle(326.73, 33.75)
t.seth(350.51)
t.circle(143.90, 69.11)
t.seth(59.62)
t.circle(-9.14, 88.4)
t.seth(331.22)
t.circle(70.07, 129.45)
t.seth(100.67)
t.circle(73.39, 125.37)
t.end_fill()

t.fillcolor("Red")
go(-143.73, -53.76)
t.begin_fill()
t.seth(242.3)
t.forward(80.81)
t.seth(292.77)
t.circle(120.52, 120.33)
t.seth(121.55)
t.forward(33.01)
t.seth(170.51)
t.circle(-326.73, 29.72)
t.end_fill()

go(-43.78, 185.89)
t.begin_fill()
t.seth(148.07)
t.circle(60.99, 90)
t.seth(28.74)
t.circle(-159.63, 31.35)
t.end_fill()

go(151.88, 41.57)
t.begin_fill()
t.seth(298.74)
t.circle(-118.8, 41.6)
t.seth(40.3)
t.circle(50.13, 114.6)
t.end_fill()

go(-87.36, -90.78)
t.begin_fill()
t.seth(152.63)
t.circle(-326.73, 8.65)
t.seth(230.19)
t.circle(46.39, 44.18)
t.seth(274.38)
t.circle(191.01, 20.76)
t.seth(15.37)
t.forward(60.13)
t.seth(99.2)
t.circle(145.01, 24.85)
t.end_fill()

go(-40.21, -110.67)
t.begin_fill()
t.seth(235.38)
t.circle(101.83, 32.48)
t.seth(343.4)
t.forward(48.03)
t.seth(53.77)
t.circle(87.43, 39.27)
t.seth(169.74)
t.circle(-326.73, 8.12)
t.end_fill()

t.fillcolor("Black")
go(-67.36, -199.14)
t.begin_fill()
t.seth(181.34)
t.circle(-120.52, 39.02)
t.seth(291.91)
t.forward(80.35)
t.seth(291.91)
t.circle(30.85, 180.21)
t.seth(112.13)
t.forward(28.39)
t.end_fill()

go(7.85, -170.51)
t.begin_fill()
t.seth(220.35)
t.circle(-120.52, 31.39)
t.seth(302.04)
t.forward(68.19)
t.seth(302.04)
t.circle(31.25, 177.94)
t.seth(119.98)
t.forward(60.97)
t.end_fill()

t.fillcolor("#f5cba7")
go(-76.42, -152.09)
t.begin_fill()
t.seth(195.37)
t.forward(36.27)
t.seth(285.37)
t.circle(18.13, 180)
t.end_fill()

go(-17.33, -176.89)
t.begin_fill()
t.seth(163.4)
t.forward(36.20)
t.seth(253.4)
t.circle(18.03, 180)
t.end_fill()

go(112.48, 42.15)
t.begin_fill()
t.seth(124.34)
t.circle(239.53, 36.71)
t.seth(161.05)
t.circle(152.34, 31.22)
t.seth(192.26)
t.circle(139.94, 24.86)
t.seth(217.12)
t.circle(90.49, 13.36)
t.seth(230.49)
t.circle(96.48, 90.95)
t.seth(321.44)
t.circle(383.96, 24.82)
t.seth(346.26)
t.circle(103.17, 60.96)
t.seth(47.23)
t.circle(98.89, 77.11)
t.end_fill()

t.pensize(5)
go(-35.83, -45.75)
t.seth(247.15)
t.circle(-16.08, 180)
go(99.59, -45.75)
t.seth(171.63)
t.forward(85.77)
go(-88.47, 15.35)
t.seth(138.78)
t.forward(84.45)
go(-65.48, 115.57)
t.seth(137.36)
t.circle(78.33, 54.71)
go(135.99, 15.35)
t.seth(123.84)
t.circle(69.07, 55.73)

t.pencolor("Crimson")
t.fillcolor("Red")
go(122.21, 155.92)
t.begin_fill()
t.seth(355.15)
t.circle(131.59, 30.77)
t.seth(25.92)
t.circle(37.49, 130.38)
t.seth(156.29)
t.circle(30.96, 66.92)
t.seth(88.45)
t.circle(30.96, 66.92)
t.seth(155.37)
t.circle(37.49, 130.38)
t.seth(285.74)
t.circle(131.59, 30.77)
t.end_fill()

t.pensize(3)
t.fillcolor("#ffab91")
t.pencolor("#ffab91")
go(-122.43, -6.65)
t.begin_fill()
t.seth(90)
t.circle(15.5)
go(49.75, -86.10)
t.seth(90)
t.circle(31.96/2)
t.end_fill()

t.hideturtle()
turtle.done()