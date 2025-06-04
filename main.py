import turtle as t
import random



# extracted_colors = []
# colors= colorgram.extract('download.jpeg',8)
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
color_list = [(248, 247, 244), (243, 250, 247), (250, 244, 248), (241, 244, 248), (5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119),(221,130,89),(210,110,34),(250,111,21)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dots in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dots%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# for i in colors :
#     r= i.rgb.r
#     g=i.rgb.g
#     b = i.rgb.b
#     random_color =(r,g,b,)
#     extracted_colors.append(random_color)
#
# print(extracted_colors)
screen = t.Screen()
screen.exitonclick()
