# coding=utf-8
"""Tarea 2"""

import glfw
from OpenGL.GL import *
import numpy as np
import sys
import os.path
import libs.setup as sp
import libs.transformations as tr
import libs.basic_shapes as bs
import libs.easy_shaders as es
import libs.scene_graph as sg
import libs.performance_monitor as pm
from libs.assets_path import getAssetPath
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
class Controller:
    def __init__(self):
        self.fillPolygon = True
        self.camera=True

controller = Controller()

def on_key(window, key, scancode, action, mods):

    if action != glfw.PRESS:
        return
    
    global controller

    if key == glfw.KEY_SPACE:
        controller.camera = not controller.camera

    elif key == glfw.KEY_LEFT_CONTROL:
        controller.fillPolygon = not controller.fillPolygon

    elif key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)

def main():

    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 1080
    height = 720
    title = "Tarea 2"

    window = glfw.create_window(width, height, title, None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)

    glfw.set_key_callback(window, on_key)

    textureShaderProgram = es.SimpleTextureModelViewProjectionShaderProgram()
    colorShaderProgram = es.SimpleModelViewProjectionShaderProgram()
    
    # color del fondo
    glClearColor(0.529, 0.808, 0.922, 1.0)

    # activamos 3D
    glEnable(GL_DEPTH_TEST)

    cpuAxis = bs.createAxis(2)
    gpuAxis = es.GPUShape().initBuffers()
    colorShaderProgram.setupVAO(gpuAxis)
    gpuAxis.fillBuffers(cpuAxis.vertices, cpuAxis.indices, GL_STATIC_DRAW)

    # creamos la escena 
    dibujo = sp.createScene(textureShaderProgram)

    perfMonitor = pm.PerformanceMonitor(glfw.get_time(), 0.5)

    t0 = glfw.get_time()

    # Parametros de posición de la cámara
    camera_pos = np.array([2.0, 0.7, 0.2])
    camera_radius = 2
    camera_theta = np.pi/2
    camera_phi = -np.pi/4

    while not glfw.window_should_close(window):

        #fps / ms
        perfMonitor.update(glfw.get_time())
        glfw.set_window_title(window, title + str(perfMonitor))

        glfw.poll_events()
       
        projection = tr.perspective(45, 600/600, 0.1, 100)

        # Actualizamos los parametros de vista segun el tipo de camara
        if controller.camera:
            if camera_pos[1] == 30.0:
                camera_pos = np.array([2.0, 0.7, 0.2])
                camera_theta = np.pi/2
                camera_phi = -np.pi/4
            projection = tr.perspective(60, float(width)/float(height), 0.1, 100)
        else:
            camera_pos = np.array([10.0, 30.0, -8.0])
            camera_theta = np.pi - 0.1
            camera_phi = 0
            projection = tr.ortho(-40, 40, -30, 30, 0.1, 100)  

        glUseProgram(colorShaderProgram.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(colorShaderProgram.shaderProgram, "projection"), 1, GL_TRUE, projection)

        glUseProgram(textureShaderProgram.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(textureShaderProgram.shaderProgram, "projection"), 1, GL_TRUE, projection)

        t1 = glfw.get_time()
        dt = t1 - t0
        t0 = t1
  
        if controller.camera:
        # Movimiento de camara y del usuario
            if (glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS):
                camera_theta -= 2 * dt
                if (camera_theta < 0.1):
                    camera_theta = 0.1
            elif (glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS):
                camera_theta += 2* dt
                if (camera_theta > np.pi -0.1):
                    camera_theta = np.pi -0.1
            elif (glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS):
                camera_phi -= 2 * dt
            elif (glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS):
                camera_phi += 2* dt
            elif (glfw.get_key(window, glfw.KEY_W) == glfw.PRESS):
                camera_pos[0] += np.cos(camera_phi) * dt * 3
                camera_pos[2] += np.sin(camera_phi) * dt * 3
            elif (glfw.get_key(window, glfw.KEY_S) == glfw.PRESS):
                camera_pos[0] -= np.cos(camera_phi) * dt * 3
                camera_pos[2] -= np.sin(camera_phi) * dt * 3
            elif (glfw.get_key(window, glfw.KEY_A) == glfw.PRESS):
                camera_pos[0] += np.sin(camera_phi) * dt * 3
                camera_pos[2] -= np.cos(camera_phi) * dt * 3
            elif (glfw.get_key(window, glfw.KEY_D) == glfw.PRESS):
                camera_pos[0] -= np.sin(camera_phi) * dt * 3
                camera_pos[2] += np.cos(camera_phi) * dt * 3
            elif (glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS):
                camera_pos[1] -=  dt * 3
            elif (glfw.get_key(window, glfw.KEY_E) == glfw.PRESS):
                camera_pos[1] +=  dt * 3

            #bordes de la escena
            if camera_pos[0] < -4.5:
                camera_pos[0] = -4.5
            if camera_pos[0] >  34:
                camera_pos[0] = 34
            if camera_pos[2] < -43:
                camera_pos[2] = -43
            if camera_pos[2] > 25:
                camera_pos[2] = 25
                 
        # Parametros de la matriz de vista
        viewPos = camera_pos 
        at = np.array([camera_pos[0] + camera_radius * np.sin(camera_theta) * np.cos(camera_phi),
                        camera_pos[1] + camera_radius * np.cos(camera_theta), 
                        camera_pos[2] + camera_radius * np.sin(camera_theta) * np.sin(camera_phi)])
        up = np.array([0,1,0]) 

        # Actualizar la matriz
        view = tr.lookAt(
            viewPos,
            at,
            up
        )

        glUseProgram( textureShaderProgram.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(textureShaderProgram.shaderProgram, "view"), 1, GL_TRUE, view)

        glUseProgram(colorShaderProgram.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(colorShaderProgram.shaderProgram, "view"), 1, GL_TRUE, view)
        glUniform3f(glGetUniformLocation(colorShaderProgram.shaderProgram, "viewPosition"), viewPos[0], viewPos[1], viewPos[2])
 
        #rellenado de los poligonos
        if (controller.fillPolygon):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


        # Limpiamos la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(textureShaderProgram.shaderProgram)

        sg.drawSceneGraphNode(dibujo, textureShaderProgram, "model")

        glfw.swap_buffers(window)

    # freeing GPU memory
    gpuAxis.clear()
    dibujo.clear()

    glfw.terminate()

    return 0


if __name__ == "__main__":
    main()
   