import libs.transformations as tr
from OpenGL.GL import glUseProgram, glUniformMatrix4fv, glGetUniformLocation,\
    GL_TRUE, glUniform3f, glUniform1ui, glUniform1f
import numpy as np
import libs.basic_shapes as bs
import math 


def setPlot(pipeline, mvpPipeline, width, height):
    projection = tr.perspective(45, float(width)/float(height), 0.1, 100)

    glUseProgram(mvpPipeline.shaderProgram)
    glUniformMatrix4fv(glGetUniformLocation(
        mvpPipeline.shaderProgram, "projection"), 1, GL_TRUE, projection)

    glUseProgram(pipeline.shaderProgram)
    glUniformMatrix4fv(glGetUniformLocation(
        pipeline.shaderProgram, "projection"), 1, GL_TRUE, projection)

    glUniform3f(glGetUniformLocation(
        pipeline.shaderProgram, "La"), 1.0, 1.0, 1.0)
    glUniform3f(glGetUniformLocation(
        pipeline.shaderProgram, "Ld"), 1.0, 1.0, 1.0)
    glUniform3f(glGetUniformLocation(
        pipeline.shaderProgram, "Ls"), 1.0, 1.0, 1.0)

    glUniform3f(glGetUniformLocation(
        pipeline.shaderProgram, "Ka"), 0.2, 0.2, 0.2)
    glUniform3f(glGetUniformLocation(
        pipeline.shaderProgram, "Kd"), 0.9, 0.9, 0.9)
    glUniform3f(glGetUniformLocation(
        pipeline.shaderProgram, "Ks"), 1.0, 1.0, 1.0)

    glUniform3f(glGetUniformLocation(
        pipeline.shaderProgram, "lightPosition"), 5, 5, 5)

    glUniform1ui(glGetUniformLocation(
        pipeline.shaderProgram, "shininess"), 1000)
    glUniform1f(glGetUniformLocation(
        pipeline.shaderProgram, "constantAttenuation"), 0.1)
    glUniform1f(glGetUniformLocation(
        pipeline.shaderProgram, "linearAttenuation"), 0.1)
    glUniform1f(glGetUniformLocation(
        pipeline.shaderProgram, "quadraticAttenuation"), 0.01)

    # Parametros de la matriz de vista
   # viewPos = camera_pos # tambien llamado eye
    #at = np.array([camera_pos[0] + np.cos(camera_theta) * camera_radius,
     #                   camera_pos[1], 
      #                  camera_pos[2] + np.sin(camera_theta) * camera_radius])
    #up = np.array([0,1,0])
def createsWindowDoor():

    # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions         texture coordinates
        # Z+: block top
        0.5,  0.5,  0.5, 1,0,
        0.5, -0.5,  0.5, 1, 1,
        -0.5, -0.5,  0.5, 0, 1,
        -0.5,  0.5,  0.5, 0, 0,

        # Z-: block bottom
        -0.5, -0.5, -0.5, 1, 1,
        0.5, -0.5, -0.5, 0, 1,
        0.5,  0.5, -0.5, 0, 0,
        -0.5,  0.5, -0.5, 1, 0,

        # X+: block left
        0.5, -0.5, -0.5, 1,  1,
        0.5,  0.5, -0.5, 1, 0,
        0.5,  0.5,  0.5, 0, 0,
        0.5, -0.5,  0.5, 0, 1,

        # X-: block right
        -0.5, -0.5, -0.5, 0, 1,
        -0.5,  0.5, -0.5, 0, 0,
        -0.5,  0.5,  0.5, 1, 0,
        -0.5, -0.5,  0.5, 1, 1,

        # Y+: white face
        -0.5,  0.5, -0.5, 0, 0,
        0.5,  0.5, -0.5, 1, 0,
        0.5,  0.5,  0.5, 1, 1,
        -0.5,  0.5,  0.5, 0, 1,

        # Y-: yellow face
        -0.5, -0.5, -0.5, 0, 0,
        0.5, -0.5, -0.5, 1, 0,
        0.5, -0.5,  0.5, 1, 1,
        -0.5, -0.5,  0.5, 0, 1
    ]

    # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = [
        0, 1, 2, 2, 3, 0,  # Z+
        7, 6, 5, 5, 4, 7,  # Z-
        8, 9, 10, 10, 11, 8,  # X+
        15, 14, 13, 13, 12, 15,  # X-
        19, 18, 17, 17, 16, 19,  # Y+
        20, 21, 22, 22, 23, 20]  # Y-

    return bs.Shape(vertices, indices)
def createBloquesPrismas():

    # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions         texture coordinates
        # Z+: block top
        0.5,  0.5,  0.5, 1/4, 2/3,
        0.5, -0.5,  0.5, 0, 2/3,
        -0.5, -0.5,  0.5, 0, 1/3,
        -0.5,  0.5,  0.5, 1/4, 1/3,

        # Z-: block bottom
        -0.5, -0.5, -0.5, 3/4, 1/3,
        0.5, -0.5, -0.5, 3/4, 2/3,
        0.5,  0.5, -0.5, 2/4, 2/3,
        -0.5,  0.5, -0.5, 2/4, 1/3,

        # X+: block left
        0.5, -0.5, -0.5, 2/4, 1,
        0.5,  0.5, -0.5, 2/4, 2/3,
        0.5,  0.5,  0.5, 1/4, 2/3,
        0.5, -0.5,  0.5, 1/4, 1,

        # X-: block right
        -0.5, -0.5, -0.5, 3/4, 2/3,
        -0.5,  0.5, -0.5, 2/4, 2/3,
        -0.5,  0.5,  0.5, 2/4, 1/3,
        -0.5, -0.5,  0.5, 3/4, 1/3,

        # Y+: white face
        -0.5,  0.5, -0.5, 2/4, 1/3,
        0.5,  0.5, -0.5, 2/4, 2/3,
        0.5,  0.5,  0.5, 1/4, 2/3,
        -0.5,  0.5,  0.5, 1/4, 1/3,

        # Y-: yellow face
        -0.5, -0.5, -0.5, 1, 1/3,
        0.5, -0.5, -0.5, 1, 2/3,
        0.5, -0.5,  0.5, 3/4, 2/3,
        -0.5, -0.5,  0.5, 3/4, 1/3
    ]

    # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = [
        0, 1, 2, 2, 3, 0,  # Z+
        7, 6, 5, 5, 4, 7,  # Z-
        8, 9, 10, 10, 11, 8,  # X+
        15, 14, 13, 13, 12, 15,  # X-
        19, 18, 17, 17, 16, 19,  # Y+
        20, 21, 22, 22, 23, 20]  # Y-

    return bs.Shape(vertices, indices)

def createWindowHouse():
    # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions        texture
        -0.5, -0.5, 0.0,  0, 1,
        0.5, -0.5, 0.0, 1, 1,
        0.5,  0.5, 0.0, 1, 0,
        -0.5,  0.5, 0.0,  0, 0]

    # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = [
        0, 1, 2,
        2, 3, 0]

    return bs.Shape(vertices, indices)


def createPrismaTriangular():

    # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions         texture coordinates
        # Z+: block top
        0.0,  0.5,  0.5, 1/2, 1,
        0.5*2, -0.5,  0.5, 1, 0,
        -0.5*2, -0.5,  0.5, 0, 0,

        # Z-: block bottom
        0.0,  0.5,  -0.5, 1/2, 1,
        -0.5*2, -0.5, -0.5, 0, 0,
        0.5*2, -0.5, -0.5, 0, 1,

        # X+: block left
        0.0,  0.5,  -0.5, 0, 1,
        0.0,  0.5,  0.5, 1, 1,
        0.5*2, -0.5, -0.5, 0, 0,
        0.5*2, -0.5,  0.5, 1, 0,

        # X-: block right
        0.0,  0.5,  -0.5, 1, 0,
        0.0,  0.5,  0.5, 1, 1,
        -0.5*2, -0.5, -0.5, 0, 0,
        -0.5*2, -0.5,  0.5, 0, 1,

        # Y-: yellow face
        -0.5*2, -0.5, -0.5, 1, 0,
        0.5*2, -0.5, -0.5, 1, 1,
        0.5*2, -0.5,  0.5, 0, 1,
        -0.5*2, -0.5,  0.5, 0, 0
    ]

    # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = [
        0, 1, 2,  # Z+
        3, 4, 5,   # Z-
        6, 7, 8, 8, 9, 7,  # X+
        10, 11, 12, 12, 13, 11,  # X-
        14, 15, 16, 16, 17, 14]  # Y-

    return bs.Shape(vertices, indices)


def createTecho2():

    # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions         texture coordinates
        # Z+: block top
        0.0,  0.5,  0.0, 1/2, 1,
        0.5*2, -0.5,  0.5, 1, 0,
        -0.5*2, -0.5,  0.5, 0, 0,

        # Z-: block bottom
        0.0,  0.5,  0.0, 1/2, 1,
        -0.5*2, -0.5, -0.5, 0, 0,
        0.5*2, -0.5, -0.5, 1, 0,

        # X+: block left
        0.0,  0.5,  0.0, 1/2, 1,
        0.5*2, -0.5, -0.5, 0, 0,
        0.5*2, -0.5,  0.5, 1, 0,

        # X-: block right
        0.0,  0.5,  0.0, 1/2, 1,
        -0.5*2, -0.5, -0.5, 0, 0,
        -0.5*2, -0.5,  0.5, 1, 0,

        # Y-: yellow face
        -0.5*2, -0.5, -0.5, 1, 0,
        0.5*2, -0.5, -0.5, 1, 1,
        0.5*2, -0.5,  0.5, 0, 1,
        -0.5*2, -0.5,  0.5, 0, 0
    ]

    # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = [
        0, 1, 2,  # Z+
        3, 4, 5,   # Z-
        6, 7, 8,  # X+
        9, 10, 11,  # X-
        12, 13, 14, 14, 15, 12]  # Y-

    return bs.Shape(vertices, indices)