# Pygame-OpenGL-Poly-Shape-Renderer
# by CtrlAltWiz
# https://github.com/CtrlAltWiz

import sys
import subprocess
import math

# Check if Pygame and PyOpenGL are installed, and install them if missing
try:
    subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'pygame'])
except subprocess.CalledProcessError:
    print("Installing Pygame...")
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'pygame'])

try:
    subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'PyOpenGL'])
except subprocess.CalledProcessError:
    print("Installing PyOpenGL...")
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'PyOpenGL'])

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

# Define the vertices and edges for a poly shape
vertices = [
    [0, 1, 1.618],
    [0, 1, -1.618],
    [0, -1, 1.618],
    [0, -1, -1.618],
    [1, 1.618, 0],
    [1, -1.618, 0],
    [-1, 1.618, 0],
    [-1, -1.618, 0],
    [1.618, 0, 1],
    [1.618, 0, -1],
    [-1.618, 0, 1],
    [-1.618, 0, -1]
]

edges = [
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5), (2, 3),
    (2, 6), (3, 7), (4, 5),
    (4, 6), (5, 7), (6, 7),
    (8, 9), (8, 10), (8, 11),
    (9, 10), (10, 11), (11, 9)
]

def draw_poly():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(angle, 1, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_poly()
        pygame.display.flip()
        pygame.time.wait(10)
        angle += 1

if __name__ == "__main__":
    main()
