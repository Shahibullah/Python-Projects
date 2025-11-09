
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

# --- Window size ---
width, height = 800, 600

# --- Rain settings ---
num_drops = 300
rain = []
rain_angle = 0.0  # 0 = straight down; negative = left; positive = right

# --- Background transition control ---
transition = 0.0  # 0 = night, 1 = day

# --- Color definitions ---
night_color = [0.0, 0.0, 0.2]         # dark blue night
day_color = [0.678, 0.847, 0.902]     # light sky blue day

# --- Initialize rain positions ---
def init_rain():
    global rain
    rain = []
    for _ in range(num_drops):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        rain.append([x, y])

# --- Draw the house ---
def draw_house():
    # Roof
    glColor3f(0.7, 0.4, 0.2)
    glBegin(GL_TRIANGLES)
    glVertex2f(250, 300)
    glVertex2f(400, 350)
    glVertex2f(550, 300)
    glEnd()

    # Body
    glColor3f(0.8, 0.5, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(270,300)
    glVertex2f(530,300)
    glVertex2f(530,200)
    glVertex2f(270,200)
    glEnd()

    #Door
    glColor3f(0.4, 0.2, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(380,270)
    glVertex2f(380,200)
    glVertex2f(420,200)
    glVertex2f(420,270)
    glEnd()

    #door lock
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(411,220)
    glVertex2f(408,220)
    glVertex2f(408,217)
    glVertex2f(411,220)
    glEnd()
#each window has four window door
       # === Left Window ===
    # Outer frame (black)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(290, 270)
    glVertex2f(350, 270)
    glVertex2f(350, 230)
    glVertex2f(290, 230)
    glEnd()

    # Glass (light blue)
    glColor3f(0.678, 0.847, 0.902)
    glBegin(GL_QUADS)
    glVertex2f(295, 265)
    glVertex2f(345, 265)
    glVertex2f(345, 235)
    glVertex2f(295, 235)
    glEnd()

    # Cross lines (black)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(320, 235)
    glVertex2f(320, 265)
    glVertex2f(295, 250)
    glVertex2f(345, 250)
    glEnd()

    # === Right Window ===
    # Outer frame (black)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(450, 270)
    glVertex2f(510, 270)
    glVertex2f(510, 230)
    glVertex2f(450, 230)
    glEnd()

    # Glass (light blue)
    glColor3f(0.678, 0.847, 0.902)
    glBegin(GL_QUADS)
    glVertex2f(455, 265)
    glVertex2f(505, 265)
    glVertex2f(505, 235)
    glVertex2f(455, 235)
    glEnd()

    # Cross lines (black)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(480, 235)
    glVertex2f(480, 265)
    glVertex2f(455, 250)
    glVertex2f(505, 250)
    glEnd()
#========================================================#
    glColor3f(0.55, 0.40, 0.25)
    glBegin(GL_QUADS)
    glVertex2f(0,300)
    glVertex2f(270, 300)
    glVertex2f(270, 0)
    glVertex2f(0, 0)
    glEnd()

    glColor3f(0.55, 0.40, 0.25)
    glBegin(GL_QUADS)
    glVertex2f(270,200)
    glVertex2f(270, 0)
    glVertex2f(800, 0)
    glVertex2f(800, 200)
    glEnd()

    glColor3f(0.55, 0.40, 0.25)
    glBegin(GL_QUADS)
    glVertex2f(530,300)
    glVertex2f(530,200)
    glVertex2f(800, 200)
    glVertex2f(800, 300)
    glEnd()
#################################################################
    glColor3f(0.55, 0.40, 0.25)
    glBegin(GL_TRIANGLES)
    
    glVertex2f(0,450)
    glVertex2d(45,450)
    glVertex2d(0,300)

    glVertex2d(135,450)
    glVertex2d(90,300)
    glVertex2d(45,450)

    glVertex2d(135,450)
    glVertex2f(225,450)
    glVertex2f(180,300)
    glEnd()

    glColor3f(0.55, 0.40, 0.25)
    glBegin(GL_QUADS)
    glVertex2f(225,450)
    glVertex2f(250,300)
    glVertex2f(400,350)
    glVertex2f(400,450)

    glVertex2f(250,450)
    glVertex2f(400,350)
    glVertex2f(550,300)
    glVertex2f(595,450)
    glEnd()
#==========================left tree==============================#
    glColor3f(0.0, 0.29, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(45,450)
    glVertex2f(0,300)
    glVertex2f(90,300)
    glEnd()

    glColor3f(0.0, 0.29, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(90,300)
    glVertex2f(135,450)
    glVertex2f(180,300)
    glEnd()

    glColor3f(0.0, 0.29, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(180,300)
    glVertex2f(225,450)
    glVertex2f(250,300)
    glEnd()
    #===================
    glColor3f(0.55, 0.40, 0.25)
    glBegin(GL_TRIANGLES)
    
    glVertex2f(595,450)
    glVertex2d(685,450)
    glVertex2d(640,300)

    glVertex2d(685,450)
    glVertex2d(773,450)
    glVertex2d(730,300)

    glVertex2d(773,450)
    glVertex2f(818,450)
    glVertex2f(820,300)
    glEnd()
#==========================right tree==============================#
    glColor3f(0.0, 0.29, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(550,300)
    glVertex2f(595,450)
    glVertex2f(640,300)
    glEnd()
    glColor3f(0.0, 0.29, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(640,300)
    glVertex2f(685,450)
    glVertex2f(730,300)
    glEnd()
    glColor3f(0.0, 0.29, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(730,300)
    glVertex2f(775,450)
    glVertex2f(820,300)
    glEnd()





 
# --- Draw rain ---
def draw_rain():
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_LINES)
    for drop in rain:
        x, y = drop
        glVertex2f(x, y)
        glVertex2f(x + rain_angle * 10, y - 15)
    glEnd()

# --- Update rain animation ---
def update_rain(value):
    global rain
    for drop in rain:
        drop[0] += rain_angle * 2
        drop[1] -= 8
        if drop[1] < 0 or drop[0] < 0 or drop[0] > width:
            drop[0] = random.uniform(0, width)
            drop[1] = height + random.uniform(0, 100)
    glutPostRedisplay()
    glutTimerFunc(33, update_rain, 0)

# --- Display callback ---
def display():
    # Interpolate between night and day colors
    r = night_color[0] * (1 - transition) + day_color[0] * transition
    g = night_color[1] * (1 - transition) + day_color[1] * transition
    b = night_color[2] * (1 - transition) + day_color[2] * transition
    glClearColor(r, g, b, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_house()
    draw_rain()
    glutSwapBuffers()

# --- Keyboard input for gradual day/night ---
def keyboard(key, x, y):
    global transition
    # key = key.decode("utf-8")

    if key == b'd':  # Move toward day
        transition = min(1.0, transition + 0.1)
    elif key == b'n':  # Move toward night
        transition = max(0.0, transition - 0.1)

    glutPostRedisplay()

# --- Arrow keys for rain bending ---
def special_keys(key, x, y):
    global rain_angle
    if key == GLUT_KEY_LEFT:
        rain_angle = max(rain_angle - 0.1, -1.0)
    elif key == GLUT_KEY_RIGHT:
        rain_angle = min(rain_angle + 0.1, 1.0)
    glutPostRedisplay()

# --- Projection setup ---
def setup_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)

# --- Main ---
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"22301025_Task01")
    setup_projection()
    init_rain()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutTimerFunc(0, update_rain, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
