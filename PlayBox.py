import pygame
pygame.init()

red_color_value, green_color_value, blue_color_value = 0, 0, 0

print("Installing Font...")
font = pygame.font.Font('freesansbold.ttf', 32)

print("Creating a window...")
screen = pygame.display.set_mode([800, 800])
screen.fill((255, 255, 255))
print("Drawing a start screen...")

pygame.draw.circle(screen, (0, 0, 0), (400, 200), 64)
pygame.display.set_caption('PlayBox.py')

text = font.render('PlayBox', True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (800 // 2, 800 // 2)

screen.blit(text, textRect)

pygame.display.flip()
pygame.time.wait(1000)
screen.fill((255, 255, 255))
text2 = font.render('Use console to continue', True, (255, 255, 255), (0, 0, 0))
textRect2 = text2.get_rect()
textRect2.center = (800 // 2, 800 // 2)
screen.blit(text2, textRect2)

pygame.display.flip()
screen.fill((255, 255, 255))
while True:
    shape = input("""
        Which shape you want to draw?(Write the # code of it)
        Shape:          # Code:
        Circle          1
    
        Line            2

        Clear canvas    3

        Fill canvas
        with custom
        color           4

        Polygon         5
        """)
    if shape == "1":
        
        red_color_value = int(input("Write how much red you want in a shape(From 0 to 255): "))
        green_color_value = int(input("Write how much green you want in a shape(From 0 to 255): "))
        blue_color_value = int(input("Write how much blue you want in a shape(From 0 to 255)"))
        radius = int(input("What radius you want your circle radius to be?"))
        point_X = int(input("Write the x-axis for your circle"))
        point_Y = int(input("Write the y-axis for your circle(800 is the deepest, 0 is the highest)"))
        pygame.draw.circle(screen, (red_color_value, green_color_value, blue_color_value), (point_X, point_Y), radius)
    elif shape == "2":
        red_color_value = int(input("Write how much red you want in a shape(From 0 to 255)"))
        green_color_value = int(input("Write how much green you want in a shape(From 0 to 255)"))
        blue_color_value = int(input("Write how much blue you want in a shape(From 0 to 255)"))
        thickness = int(input("What thickness you want your line to be?"))
        point_X_1 = int(input("Write the x-axis for your point 1"))
        point_Y_1 = int(input("Write the y-axis for your point 1(800 is the deepest, 0 is the highest)"))
        point_X_2 = int(input("Write the x-axis for your point 2"))
        point_Y_2 = int(input("Write the y-axis for your point 2(800 is the deepest, 0 is the highest)"))
        print("Waiting for a line to be created...")
        pygame.draw.line(screen, (red_color_value, green_color_value, blue_color_value), (point_X_1, point_Y_1), (point_X_2, point_Y_2), thickness)
    elif shape == "3":
        screen.fill((255, 255, 255))
    elif shape == "4":
        red_color_value = int(input("Write how much red you want in a backround(From 0 to 255)"))
        green_color_value = int(input("Write how much green you want in a backround(From 0 to 255)"))
        blue_color_value = int(input("Write how much blue you want in a backround(From 0 to 255)"))
        screen.fill((red_color_value, green_color_value, blue_color_value))
    elif shape == "5":
        red_color_value = int(input("Write how much red you want in a shape(From 0 to 255)"))
        green_color_value = int(input("Write how much green you want in a shape(From 0 to 255)"))
        blue_color_value = int(input("Write how much blue you want in a shape(From 0 to 255)"))
        num_of_points = int(input("How many point do you want to have?(min. 3)"))
        point_list = []
        num_of_points -= 1
        for i in range(num_of_points):
            point_X = int(input("Write the X axis of the point"))
            point_Y = int(input("Write the Y axis of the point(800 is the deepest, 0 is the highest)"))
            tupl = (point_X, point_Y)
            point_list.append(tupl)

    pygame.display.flip()
    pygame.event.get()
    end = input("End program?(yes/no)")
    if end == "yes":
        pygame.quit()
        break