"""Funciones para la creacion de la escena"""
from OpenGL.GL import glUseProgram, glUniformMatrix4fv, glGetUniformLocation,\
    GL_TRUE, glUniform3f, glUniform1ui, glUniform1f
from OpenGL.GL import *
import numpy as np
import sys
import os.path
import libs.transformations as tr
import libs.basic_shapes as bs
import libs.easy_shaders as es
import libs.scene_graph as sg
from libs.assets_path import getAssetPath
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

def createPrisma1():

    # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions         texture coordinates
        # Z+: 
        0.5,  0.5,  0.5, 1/4, 2/3,
        0.5, -0.5,  0.5, 0, 2/3,
        -0.5, -0.5,  0.5, 0, 1/3,
        -0.5,  0.5,  0.5, 1/4, 1/3,

        # Z-: 
        -0.5, -0.5, -0.5, 3/4, 1/3,
        0.5, -0.5, -0.5, 3/4, 2/3,
        0.5,  0.5, -0.5, 2/4, 2/3,
        -0.5,  0.5, -0.5, 2/4, 1/3,

        # X+: 
        0.5, -0.5, -0.5, 2/4, 1,
        0.5,  0.5, -0.5, 2/4, 2/3,
        0.5,  0.5,  0.5, 1/4, 2/3,
        0.5, -0.5,  0.5, 1/4, 1,

        # X-: 
        -0.5, -0.5, -0.5, 3/4, 2/3,
        -0.5,  0.5, -0.5, 2/4, 2/3,
        -0.5,  0.5,  0.5, 2/4, 1/3,
        -0.5, -0.5,  0.5, 3/4, 1/3,

        # Y+: 
        -0.5,  0.5, -0.5, 2/4, 1/3,
        0.5,  0.5, -0.5, 2/4, 2/3,
        0.5,  0.5,  0.5, 1/4, 2/3,
        -0.5,  0.5,  0.5, 1/4, 1/3,

        # Y-: 
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

def createPrisma2():

        # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions         texture coordinates
        # Z+:
        0.5,  0.5,  0.5, 1,0,
        0.5, -0.5,  0.5, 1, 1,
        -0.5, -0.5,  0.5, 0, 1,
        -0.5,  0.5,  0.5, 0, 0,

        # Z-:
        -0.5, -0.5, -0.5, 1, 1,
        0.5, -0.5, -0.5, 0, 1,
        0.5,  0.5, -0.5, 0, 0,
        -0.5,  0.5, -0.5, 1, 0,

        # X+:
        0.5, -0.5, -0.5, 1,  1,
        0.5,  0.5, -0.5, 1, 0,
        0.5,  0.5,  0.5, 0, 0,
        0.5, -0.5,  0.5, 0, 1,

        # X-: 
        -0.5, -0.5, -0.5, 0, 1,
        -0.5,  0.5, -0.5, 0, 0,
        -0.5,  0.5,  0.5, 1, 0,
        -0.5, -0.5,  0.5, 1, 1,

        # Y+: 
        -0.5,  0.5, -0.5, 0, 0,
        0.5,  0.5, -0.5, 1, 0,
        0.5,  0.5,  0.5, 1, 1,
        -0.5,  0.5,  0.5, 0, 1,

        # Y-: 
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

def createPrismaTriangular():

    # Defining locations and texture coordinates for each vertex of the shape
    vertices = [
        #   positions         texture coordinates
        # Z+: 
        0.0,  0.5,  0.5, 1/2, 1,
        0.5*2, -0.5,  0.5, 1, 0,
        -0.5*2, -0.5,  0.5, 0, 0,

        # Z-: 
        0.0,  0.5,  -0.5, 1/2, 1,
        -0.5*2, -0.5, -0.5, 0, 0,
        0.5*2, -0.5, -0.5, 0, 1,

        # X+:
        0.0,  0.5,  -0.5, 0, 1,
        0.0,  0.5,  0.5, 1, 1,
        0.5*2, -0.5, -0.5, 0, 0,
        0.5*2, -0.5,  0.5, 1, 0,

        # X-: 
        0.0,  0.5,  -0.5, 1, 0,
        0.0,  0.5,  0.5, 1, 1,
        -0.5*2, -0.5, -0.5, 0, 0,
        -0.5*2, -0.5,  0.5, 0, 1,

        # Y-: 
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


def createHouse(pipeline):
    # Creacion de primitivas
    shapePared = createPrisma2()
    gpuPared = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuPared)
    gpuPared.fillBuffers(
        shapePared.vertices, shapePared.indices, GL_STATIC_DRAW)
    gpuPared.texture = es.textureSimpleSetup(
        getAssetPath("paredwena2.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeTecho = createPrisma2()
    gpuTecho = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuTecho)
    gpuTecho.fillBuffers(
        shapeTecho.vertices, shapeTecho.indices, GL_STATIC_DRAW)
    gpuTecho.texture = es.textureSimpleSetup(
        getAssetPath("tejas negras.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    
    shapePuerta = createPrisma2()
    gpuPuerta = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuPuerta)
    gpuPuerta.fillBuffers(
        shapePuerta.vertices, shapePuerta.indices, GL_STATIC_DRAW)
    gpuPuerta.texture = es.textureSimpleSetup(
        getAssetPath("puerta.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    
    shapeVentana = createPrisma2()
    gpuVentana = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuVentana)
    gpuVentana.fillBuffers(
        shapeVentana.vertices, shapeVentana.indices, GL_STATIC_DRAW)
    gpuVentana.texture = es.textureSimpleSetup(
        getAssetPath("ventanacafe.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeExtra = createPrismaTriangular()
    gpuExtra = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuExtra)
    gpuExtra.fillBuffers(
        shapeExtra.vertices, shapeExtra.indices, GL_STATIC_DRAW)
    gpuExtra.texture = es.textureSimpleSetup(
        getAssetPath("tejas negras.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    # Nodo de Paredes
    wall1Node = sg.SceneGraphNode('wall1')
    wall1Node.transform = tr.matmul([tr.translate(0.0, 0.75, -2.45) , tr.scale(5.0, 3.0, 0.1)])
    wall1Node.childs += [gpuPared]

    wall2Node = sg.SceneGraphNode('wall2')
    wall2Node.transform = tr.matmul([tr.translate(2.45, 0.75, 0.0) , tr.scale(0.1, 3.0, 5.0)])
    wall2Node.childs += [gpuPared]

    wall3Node = sg.SceneGraphNode('wall3')
    wall3Node.transform = tr.matmul([tr.translate(-2.45, 0.75, 0.0) , tr.scale(0.1, 3.0, 5.0)])
    wall3Node.childs += [gpuPared]

    wall4Node = sg.SceneGraphNode('wall4')
    wall4Node.transform = tr.matmul([tr.translate(0.0, 0.75, 2.45) , tr.scale(5.0, 3.0, 0.1)])
    wall4Node.childs += [gpuPared]

    # Nodo de la pendientes del techo
    roof1Node = sg.SceneGraphNode('roof1')
    roof1Node.transform = tr.matmul([tr.translate(0.0, 2.8, 1.4) , tr.rotationX(np.pi/8), tr.scale(5.0, 0.05, 3.1)])
    roof1Node.childs += [gpuTecho]

    roof2Node = sg.SceneGraphNode('roof2')
    roof2Node.transform = tr.matmul([tr.translate(0.0, 2.8, -1.4) , tr.rotationX(-np.pi/8), tr.scale(5.0, 0.05, 3.1)])
    roof2Node.childs += [gpuTecho]

    # Nodo de la puerta
    doorNode = sg.SceneGraphNode('door')
    doorNode.transform = tr.matmul([tr.translate(-2.5, 0.2, 0.0) , tr.scale(0.1, 1.8, 1.0)])
    doorNode.childs += [gpuPuerta]

    # Nodo de la ventana
    wind1Node = sg.SceneGraphNode('wind1')
    wind1Node.transform = tr.matmul([tr.translate(-2.5, 0.9, 1.5) , tr.scale(0.01, 1.0, 1.0)])
    wind1Node.childs += [gpuVentana]

    wind2Node = sg.SceneGraphNode('wind2')
    wind2Node.transform = tr.matmul([tr.translate(-2.5, 0.9, -1.5) , tr.scale(0.01, 1.0, 1.0)])
    wind2Node.childs += [gpuVentana]

    triNode = sg.SceneGraphNode('tri1')
    triNode.transform = tr.matmul([tr.translate(-2.5, 2.8, 0.0) , tr.scale(0.1, 1.1, 2.8), tr.rotationY(np.pi/2)])
    triNode.childs += [gpuExtra]

    tri2Node = sg.SceneGraphNode('tri2')
    tri2Node.transform = tr.matmul([tr.translate(2.5, 2.8, 0.0) , tr.scale(0.1, 1.1, 2.8), tr.rotationY(np.pi/2)])
    tri2Node.childs += [gpuExtra]

    # Nodo de la casa
    houseNode = sg.SceneGraphNode('house1')
    houseNode.transform = tr.matmul([tr.translate(0.0, 0.5, 0.0) , tr.scale(1.0, 1.0, 1.0)])
    houseNode.childs += [wall1Node, wall2Node, wall3Node, wall4Node, roof1Node, roof2Node, doorNode, wind1Node, wind2Node, triNode, tri2Node]

    return houseNode
  
def createHouse2(pipeline):
    # Creacion de primitivas
    shapePared = createPrisma2()
    gpuPared = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuPared)
    gpuPared.fillBuffers(
        shapePared.vertices, shapePared.indices, GL_STATIC_DRAW)
    gpuPared.texture = es.textureSimpleSetup(
        getAssetPath("paredwena2.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeTecho = createPrisma2()
    gpuTecho = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuTecho)
    gpuTecho.fillBuffers(
        shapeTecho.vertices, shapeTecho.indices, GL_STATIC_DRAW)
    gpuTecho.texture = es.textureSimpleSetup(
        getAssetPath("tejas negras.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
     
    shapeVentana = createPrisma2()
    gpuVentana = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuVentana)
    gpuVentana.fillBuffers(
        shapeVentana.vertices, shapeVentana.indices, GL_STATIC_DRAW)
    gpuVentana.texture = es.textureSimpleSetup(
        getAssetPath("ventanacafe.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeExtra = createPrismaTriangular()
    gpuExtra = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuExtra)
    gpuExtra.fillBuffers(
        shapeExtra.vertices, shapeExtra.indices, GL_STATIC_DRAW)
    gpuExtra.texture = es.textureSimpleSetup(
        getAssetPath("tejas negras.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    # Nodo de Paredes
    wall1Node = sg.SceneGraphNode('wall1')
    wall1Node.transform = tr.matmul([tr.translate(0.0, 0.75, -2.45) , tr.scale(5.0, 3.0, 0.1)])
    wall1Node.childs += [gpuPared]

    wall2Node = sg.SceneGraphNode('wall2')
    wall2Node.transform = tr.matmul([tr.translate(2.45, 0.75, 0.0) , tr.scale(0.1, 3.0, 5.0)])
    wall2Node.childs += [gpuPared]

    wall3Node = sg.SceneGraphNode('wall3')
    wall3Node.transform = tr.matmul([tr.translate(-2.45, 0.75, 0.0) , tr.scale(0.1, 3.0, 5.0)])
    wall3Node.childs += [gpuPared]

    wall4Node = sg.SceneGraphNode('wall4')
    wall4Node.transform = tr.matmul([tr.translate(0.0, 0.75, 2.45) , tr.scale(5.0, 3.0, 0.1)])
    wall4Node.childs += [gpuPared]

    # Nodo de la pendientes del techo
    roof1Node = sg.SceneGraphNode('roof1')
    roof1Node.transform = tr.matmul([tr.translate(0.0, 2.8, 1.4) , tr.rotationX(np.pi/8), tr.scale(5.0, 0.05, 3.1)])
    roof1Node.childs += [gpuTecho]

    roof2Node = sg.SceneGraphNode('roof2')
    roof2Node.transform = tr.matmul([tr.translate(0.0, 2.8, -1.4) , tr.rotationX(-np.pi/8), tr.scale(5.0, 0.05, 3.1)])
    roof2Node.childs += [gpuTecho]

    # Nodo de la ventana
    wind1Node = sg.SceneGraphNode('wind1')
    wind1Node.transform = tr.matmul([tr.translate(-2.5, 0.9, 1.5) , tr.scale(0.1, 1.0, 1.0)])
    wind1Node.childs += [gpuVentana]

    wind2Node = sg.SceneGraphNode('wind2')
    wind2Node.transform = tr.matmul([tr.translate(-2.5, 0.9, -1.5) , tr.scale(0.1, 1.0, 1.0)])
    wind2Node.childs += [gpuVentana]

    triNode = sg.SceneGraphNode('tri1')
    triNode.transform = tr.matmul([tr.translate(-2.5, 2.8, 0.0) , tr.scale(0.1, 1.1, 2.8), tr.rotationY(np.pi/2)])
    triNode.childs += [gpuExtra]

    tri2Node = sg.SceneGraphNode('tri2')
    tri2Node.transform = tr.matmul([tr.translate(2.5, 2.8, 0.0) , tr.scale(0.1, 1.1, 2.8), tr.rotationY(np.pi/2)])
    tri2Node.childs += [gpuExtra]

    # Nodo de la casa
    houseNode = sg.SceneGraphNode('house1')
    houseNode.transform = tr.matmul([tr.translate(0.0, 0.5, 0.0) , tr.scale(1.0, 1.0, 1.0)])
    houseNode.childs += [wall1Node, wall2Node, wall3Node, wall4Node, roof1Node, roof2Node, wind1Node, wind2Node, triNode, tri2Node]

    return houseNode
 
def createHouse3(pipeline):
    # Creacion de primitivas
    shapePared = createPrisma2()
    gpuPared = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuPared)
    gpuPared.fillBuffers(
        shapePared.vertices, shapePared.indices, GL_STATIC_DRAW)
    gpuPared.texture = es.textureSimpleSetup(
        getAssetPath("paredwena2.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeTecho = createPrisma2()
    gpuTecho = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuTecho)
    gpuTecho.fillBuffers(
        shapeTecho.vertices, shapeTecho.indices, GL_STATIC_DRAW)
    gpuTecho.texture = es.textureSimpleSetup(
        getAssetPath("tejas negras.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    
    shapePuerta = createPrisma2()
    gpuPuerta = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuPuerta)
    gpuPuerta.fillBuffers(
        shapePuerta.vertices, shapePuerta.indices, GL_STATIC_DRAW)
    gpuPuerta.texture = es.textureSimpleSetup(
        getAssetPath("puerta.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    
    shapeVentana = createPrisma2()
    gpuVentana = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuVentana)
    gpuVentana.fillBuffers(
        shapeVentana.vertices, shapeVentana.indices, GL_STATIC_DRAW)
    gpuVentana.texture = es.textureSimpleSetup(
        getAssetPath("ventanacafe.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeExtra = createPrismaTriangular()
    gpuExtra = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuExtra)
    gpuExtra.fillBuffers(
        shapeExtra.vertices, shapeExtra.indices, GL_STATIC_DRAW)
    gpuExtra.texture = es.textureSimpleSetup(
        getAssetPath("tejas negras.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    # Nodo de Paredes
    wall1Node = sg.SceneGraphNode('wall1')
    wall1Node.transform = tr.matmul([tr.translate(0.0, 0.75, -2.45) , tr.scale(5.0, 6.0, 0.1)])
    wall1Node.childs += [gpuPared]

    wall2Node = sg.SceneGraphNode('wall2')
    wall2Node.transform = tr.matmul([tr.translate(2.45, 0.75, 0.0) , tr.scale(0.1, 6.0, 5.0)])
    wall2Node.childs += [gpuPared]

    wall3Node = sg.SceneGraphNode('wall3')
    wall3Node.transform = tr.matmul([tr.translate(-2.45, 0.75, 0.0) , tr.scale(0.1, 6.0, 5.0)])
    wall3Node.childs += [gpuPared]

    wall4Node = sg.SceneGraphNode('wall4')
    wall4Node.transform = tr.matmul([tr.translate(0.0, 0.75, 2.45) , tr.scale(5.0, 6.0, 0.1)])
    wall4Node.childs += [gpuPared]

    # Nodo de la pendientes del techo
    roof1Node = sg.SceneGraphNode('roof1')
    roof1Node.transform = tr.matmul([tr.translate(0.0, 4.2, 1.4) , tr.rotationX(np.pi/8), tr.scale(5.0, 0.05, 3.1)])
    roof1Node.childs += [gpuTecho]

    roof2Node = sg.SceneGraphNode('roof2')
    roof2Node.transform = tr.matmul([tr.translate(0.0, 4.2, -1.4) , tr.rotationX(-np.pi/8), tr.scale(5.0, 0.05, 3.1)])
    roof2Node.childs += [gpuTecho]

    # Nodo de la puerta
    doorNode = sg.SceneGraphNode('door')
    doorNode.transform = tr.matmul([tr.translate(-2.5, -1.3, 0.0) , tr.scale(0.1, 1.8, 1.0)])
    doorNode.childs += [gpuPuerta]

    # Nodo de la ventana
    wind1Node = sg.SceneGraphNode('wind1')
    wind1Node.transform = tr.matmul([tr.translate(-2.5, 0.9, 1.5) , tr.scale(0.1, 1.0, 1.0)])
    wind1Node.childs += [gpuVentana]

    wind2Node = sg.SceneGraphNode('wind2')
    wind2Node.transform = tr.matmul([tr.translate(-2.5, 0.9, -1.5) , tr.scale(0.1, 1.0, 1.0)])
    wind2Node.childs += [gpuVentana]

    wind3Node = sg.SceneGraphNode('wind1')
    wind3Node.transform = tr.matmul([tr.translate(-2.5, 2.9, 1.5) , tr.scale(0.1, 1.0, 1.0)])
    wind3Node.childs += [gpuVentana]

    wind4Node = sg.SceneGraphNode('wind2')
    wind4Node.transform = tr.matmul([tr.translate(-2.5, 2.9, -1.5) , tr.scale(0.1, 1.0, 1.0)])
    wind4Node.childs += [gpuVentana]

    triNode = sg.SceneGraphNode('tri1')
    triNode.transform = tr.matmul([tr.translate(-2.5, 4.2, 0.0) , tr.scale(0.1, 1.1, 2.8), tr.rotationY(np.pi/2)])
    triNode.childs += [gpuExtra]

    tri2Node = sg.SceneGraphNode('tri2')
    tri2Node.transform = tr.matmul([tr.translate(2.5, 4.2, 0.0) , tr.scale(0.1, 1.1, 2.8), tr.rotationY(np.pi/2)])
    tri2Node.childs += [gpuExtra]

    # Nodo de la casa
    houseNode = sg.SceneGraphNode('house1')
    houseNode.transform = tr.matmul([tr.translate(0.0, 2.0, 0.0) , tr.scale(1.0, 1.0, 1.0)])
    houseNode.childs += [wall1Node, wall2Node, wall3Node, wall4Node, roof1Node, roof2Node, doorNode, wind1Node, wind2Node, wind3Node, wind4Node, triNode, tri2Node]

    return houseNode
  

def createTree(pipeline):
    # Creacion de primitivas
    shapeTronco = createPrisma2()
    gpuTronco = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuTronco)
    gpuTronco.fillBuffers(
        shapeTronco.vertices, shapeTronco.indices, GL_STATIC_DRAW)
    gpuTronco.texture = es.textureSimpleSetup(
        getAssetPath("troncofinal2.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeHojas = createPrisma1()
    gpuHojas = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuHojas)
    gpuHojas.fillBuffers(
        shapeHojas.vertices, shapeHojas.indices, GL_STATIC_DRAW)
    gpuHojas.texture = es.textureSimpleSetup(
        getAssetPath("hojas2.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    # Nodo del tronco
    trunkNode = sg.SceneGraphNode('trunk')
    trunkNode.transform = tr.matmul([tr.translate(0.0, 0.2, 0.0) , tr.scale(0.2, 1.1, 0.2)])
    trunkNode.childs += [gpuTronco]

    # Nodo de las ramas
    branchNode = sg.SceneGraphNode('branch1')
    branchNode.transform = tr.matmul([tr.translate(0.0, 0.4, 0.1) , tr.scale(0.1, 0.1, 0.1), tr.shearing(0,0,0,0,0,2)])
    branchNode.childs += [gpuTronco]

    branchNode2 = sg.SceneGraphNode('branch1')
    branchNode2.transform = tr.matmul([tr.translate(0.0, 0.4, -0.1) , tr.scale(0.1, 0.1, 0.1), tr.shearing(0,0,0,0,0,-2)])
    branchNode2.childs += [gpuTronco]

    branchNode3 = sg.SceneGraphNode('branch1')
    branchNode3.transform = tr.matmul([tr.translate(0.1, 0.4, 0.0) , tr.scale(0.1, 0.1, 0.1), tr.shearing(2,0,0,0,0,0)])
    branchNode3.childs += [gpuTronco]

    branchNode4 = sg.SceneGraphNode('branch1')
    branchNode4.transform = tr.matmul([tr.translate(-0.1, 0.4, 0.0) , tr.scale(0.1, 0.1, 0.1), tr.shearing(-2,0,0,0,0,0)])
    branchNode4.childs += [gpuTronco]

    # Nodo de las hojas
    leafNode = sg.SceneGraphNode('leaf')
    leafNode.transform = tr.matmul([tr.translate(0.0, 0.6, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leafNode.childs += [gpuHojas]

    leaf2Node = sg.SceneGraphNode('leaf2')
    leaf2Node.transform = tr.matmul([tr.translate(0.3, 0.6, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf2Node.childs += [gpuHojas]   

    leaf3Node = sg.SceneGraphNode('leaf3')
    leaf3Node.transform = tr.matmul([tr.translate(-0.3, 0.6, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf3Node.childs += [gpuHojas] 

    leaf4Node = sg.SceneGraphNode('leaf4')
    leaf4Node.transform = tr.matmul([tr.translate(0.0, 0.6, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf4Node.childs += [gpuHojas]  

    leaf5Node = sg.SceneGraphNode('leaf5')
    leaf5Node.transform = tr.matmul([tr.translate(0.3, 0.9, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf5Node.childs += [gpuHojas]  

    leaf6Node = sg.SceneGraphNode('leaf5')
    leaf6Node.transform = tr.matmul([tr.translate(0.3, 0.9, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf6Node.childs += [gpuHojas]  

    leaf7Node = sg.SceneGraphNode('leaf5')
    leaf7Node.transform = tr.matmul([tr.translate(-0.3, 0.9, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf7Node.childs += [gpuHojas]  

    leaf8Node = sg.SceneGraphNode('leaf5')
    leaf8Node.transform = tr.matmul([tr.translate(-0.3, 0.9, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf8Node.childs += [gpuHojas] 

    leaf9Node = sg.SceneGraphNode('leaf')
    leaf9Node.transform = tr.matmul([tr.translate(0.0, 0.9, 0.6) , tr.scale(0.3, 0.3, 0.3)])
    leaf9Node.childs += [gpuHojas]

    leaf10Node = sg.SceneGraphNode('leaf')
    leaf10Node.transform = tr.matmul([tr.translate(0.0, 0.9, -0.6) , tr.scale(0.3, 0.3, 0.3)])
    leaf10Node.childs += [gpuHojas]

    leaf11Node = sg.SceneGraphNode('leaf')
    leaf11Node.transform = tr.matmul([tr.translate(0.6, 0.9, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf11Node.childs += [gpuHojas]

    leaf12Node = sg.SceneGraphNode('leaf')
    leaf12Node.transform = tr.matmul([tr.translate(-0.6, 0.9, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf12Node.childs += [gpuHojas]

    leaf13Node = sg.SceneGraphNode('leaf')
    leaf13Node.transform = tr.matmul([tr.translate(0.0, 1.2, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf13Node.childs += [gpuHojas]

    leaf14Node = sg.SceneGraphNode('leaf')
    leaf14Node.transform = tr.matmul([tr.translate(0.0, 1.2, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf14Node.childs += [gpuHojas]

    leaf15Node = sg.SceneGraphNode('leaf')
    leaf15Node.transform = tr.matmul([tr.translate(0.3, 1.2, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf15Node.childs += [gpuHojas]

    leaf16Node = sg.SceneGraphNode('leaf')
    leaf16Node.transform = tr.matmul([tr.translate(-0.3, 1.2, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf16Node.childs += [gpuHojas]

    leaf17Node = sg.SceneGraphNode('leaf')
    leaf17Node.transform = tr.matmul([tr.translate(0.0, 1.5, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf17Node.childs += [gpuHojas] 

    # Nodo del arbol a retornar
    treeNode = sg.SceneGraphNode('tree')
    treeNode.transform = tr.matmul([tr.translate(0.0, 0.3, 0.0) , tr.scale(1.0, 1.0, 1.0)])
    treeNode.childs += [trunkNode, branchNode, branchNode2, branchNode3, branchNode4, 
                        leafNode, leaf2Node, leaf3Node, leaf4Node, leaf5Node, leaf6Node, leaf7Node, leaf8Node, 
                        leaf9Node, leaf10Node, leaf11Node, leaf12Node, leaf13Node, leaf14Node, leaf15Node, leaf16Node, 
                        leaf17Node]

    return treeNode

def createTree2(pipeline):
    # Creacion de primitivas
    shapeTronco = createPrisma2()
    gpuTronco = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuTronco)
    gpuTronco.fillBuffers(
        shapeTronco.vertices, shapeTronco.indices, GL_STATIC_DRAW)
    gpuTronco.texture = es.textureSimpleSetup(
        getAssetPath("troncofinal2.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeHojas = createPrisma1()
    gpuHojas = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuHojas)
    gpuHojas.fillBuffers(
        shapeHojas.vertices, shapeHojas.indices, GL_STATIC_DRAW)
    gpuHojas.texture = es.textureSimpleSetup(
        getAssetPath("hojas.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    # Nodo del tronco
    trunkNode = sg.SceneGraphNode('trunk')
    trunkNode.transform = tr.matmul([tr.translate(0.0, 0.2, 0.0) , tr.scale(0.2, 1.1, 0.2)])
    trunkNode.childs += [gpuTronco]

    # Nodo de las ramas
    branchNode = sg.SceneGraphNode('branch1')
    branchNode.transform = tr.matmul([tr.translate(0.0, 0.4, 0.1) , tr.scale(0.1, 0.1, 0.1), tr.shearing(0,0,0,0,0,2)])
    branchNode.childs += [gpuTronco]

    branchNode2 = sg.SceneGraphNode('branch1')
    branchNode2.transform = tr.matmul([tr.translate(0.0, 0.4, -0.1) , tr.scale(0.1, 0.1, 0.1), tr.shearing(0,0,0,0,0,-2)])
    branchNode2.childs += [gpuTronco]

    branchNode3 = sg.SceneGraphNode('branch1')
    branchNode3.transform = tr.matmul([tr.translate(0.1, 0.4, 0.0) , tr.scale(0.1, 0.1, 0.1), tr.shearing(2,0,0,0,0,0)])
    branchNode3.childs += [gpuTronco]

    branchNode4 = sg.SceneGraphNode('branch1')
    branchNode4.transform = tr.matmul([tr.translate(-0.1, 0.4, 0.0) , tr.scale(0.1, 0.1, 0.1), tr.shearing(-2,0,0,0,0,0)])
    branchNode4.childs += [gpuTronco]

    # Nodo de las hojas
    leafNode = sg.SceneGraphNode('leaf')
    leafNode.transform = tr.matmul([tr.translate(0.0, 0.6, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leafNode.childs += [gpuHojas]

    leaf2Node = sg.SceneGraphNode('leaf2')
    leaf2Node.transform = tr.matmul([tr.translate(0.3, 0.6, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf2Node.childs += [gpuHojas]   

    leaf3Node = sg.SceneGraphNode('leaf3')
    leaf3Node.transform = tr.matmul([tr.translate(-0.3, 0.6, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf3Node.childs += [gpuHojas] 

    leaf4Node = sg.SceneGraphNode('leaf4')
    leaf4Node.transform = tr.matmul([tr.translate(0.0, 0.6, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf4Node.childs += [gpuHojas]  

    leaf5Node = sg.SceneGraphNode('leaf5')
    leaf5Node.transform = tr.matmul([tr.translate(0.3, 0.9, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf5Node.childs += [gpuHojas]  

    leaf6Node = sg.SceneGraphNode('leaf5')
    leaf6Node.transform = tr.matmul([tr.translate(0.3, 0.9, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf6Node.childs += [gpuHojas]  

    leaf7Node = sg.SceneGraphNode('leaf5')
    leaf7Node.transform = tr.matmul([tr.translate(-0.3, 0.9, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf7Node.childs += [gpuHojas]  

    leaf8Node = sg.SceneGraphNode('leaf5')
    leaf8Node.transform = tr.matmul([tr.translate(-0.3, 0.9, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf8Node.childs += [gpuHojas] 

    leaf9Node = sg.SceneGraphNode('leaf')
    leaf9Node.transform = tr.matmul([tr.translate(0.0, 0.9, 0.6) , tr.scale(0.3, 0.3, 0.3)])
    leaf9Node.childs += [gpuHojas]

    leaf10Node = sg.SceneGraphNode('leaf')
    leaf10Node.transform = tr.matmul([tr.translate(0.0, 0.9, -0.6) , tr.scale(0.3, 0.3, 0.3)])
    leaf10Node.childs += [gpuHojas]

    leaf11Node = sg.SceneGraphNode('leaf')
    leaf11Node.transform = tr.matmul([tr.translate(0.6, 0.9, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf11Node.childs += [gpuHojas]

    leaf12Node = sg.SceneGraphNode('leaf')
    leaf12Node.transform = tr.matmul([tr.translate(-0.6, 0.9, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf12Node.childs += [gpuHojas]

    leaf13Node = sg.SceneGraphNode('leaf')
    leaf13Node.transform = tr.matmul([tr.translate(0.0, 1.2, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf13Node.childs += [gpuHojas]

    leaf14Node = sg.SceneGraphNode('leaf')
    leaf14Node.transform = tr.matmul([tr.translate(0.0, 1.2, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf14Node.childs += [gpuHojas]

    leaf15Node = sg.SceneGraphNode('leaf')
    leaf15Node.transform = tr.matmul([tr.translate(0.3, 1.2, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf15Node.childs += [gpuHojas]

    leaf16Node = sg.SceneGraphNode('leaf')
    leaf16Node.transform = tr.matmul([tr.translate(-0.3, 1.2, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf16Node.childs += [gpuHojas]

    leaf17Node = sg.SceneGraphNode('leaf')
    leaf17Node.transform = tr.matmul([tr.translate(0.0, 1.5, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf17Node.childs += [gpuHojas] 

    # Nodo del arbol a retornar
    treeNode = sg.SceneGraphNode('tree')
    treeNode.transform = tr.matmul([tr.translate(0.0, 0.3, 0.0) , tr.scale(1.0, 1.0, 1.0)])
    treeNode.childs += [trunkNode, branchNode, branchNode2, branchNode3, branchNode4, 
                        leafNode, leaf2Node, leaf3Node, leaf4Node, leaf5Node, leaf6Node, leaf7Node, leaf8Node, 
                        leaf9Node, leaf10Node, leaf11Node, leaf12Node, leaf13Node, leaf14Node, leaf15Node, leaf16Node, 
                        leaf17Node]

    return treeNode

def createTree3(pipeline):
    # Creacion de primitivas
    shapeTronco = createPrisma2()
    gpuTronco = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuTronco)
    gpuTronco.fillBuffers(
        shapeTronco.vertices, shapeTronco.indices, GL_STATIC_DRAW)
    gpuTronco.texture = es.textureSimpleSetup(
        getAssetPath("troncofinal2.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeHojas = createPrisma1()
    gpuHojas = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuHojas)
    gpuHojas.fillBuffers(
        shapeHojas.vertices, shapeHojas.indices, GL_STATIC_DRAW)
    gpuHojas.texture = es.textureSimpleSetup(
        getAssetPath("hojas3.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    # Nodo del tronco
    trunkNode = sg.SceneGraphNode('trunk')
    trunkNode.transform = tr.matmul([tr.translate(0.0, 0.2, 0.0) , tr.scale(0.2, 1.1, 0.2)])
    trunkNode.childs += [gpuTronco]

    # Nodo de las ramas
    branchNode = sg.SceneGraphNode('branch1')
    branchNode.transform = tr.matmul([tr.translate(0.0, 0.4, 0.1) , tr.scale(0.1, 0.1, 0.1), tr.shearing(0,0,0,0,0,2)])
    branchNode.childs += [gpuTronco]

    branchNode2 = sg.SceneGraphNode('branch1')
    branchNode2.transform = tr.matmul([tr.translate(0.0, 0.4, -0.1) , tr.scale(0.1, 0.1, 0.1), tr.shearing(0,0,0,0,0,-2)])
    branchNode2.childs += [gpuTronco]

    branchNode3 = sg.SceneGraphNode('branch1')
    branchNode3.transform = tr.matmul([tr.translate(0.1, 0.4, 0.0) , tr.scale(0.1, 0.1, 0.1), tr.shearing(2,0,0,0,0,0)])
    branchNode3.childs += [gpuTronco]

    branchNode4 = sg.SceneGraphNode('branch1')
    branchNode4.transform = tr.matmul([tr.translate(-0.1, 0.4, 0.0) , tr.scale(0.1, 0.1, 0.1), tr.shearing(-2,0,0,0,0,0)])
    branchNode4.childs += [gpuTronco]

    # Nodo de las hojas
    leafNode = sg.SceneGraphNode('leaf')
    leafNode.transform = tr.matmul([tr.translate(0.0, 0.6, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leafNode.childs += [gpuHojas]

    leaf2Node = sg.SceneGraphNode('leaf2')
    leaf2Node.transform = tr.matmul([tr.translate(0.3, 0.6, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf2Node.childs += [gpuHojas]   

    leaf3Node = sg.SceneGraphNode('leaf3')
    leaf3Node.transform = tr.matmul([tr.translate(-0.3, 0.6, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf3Node.childs += [gpuHojas] 

    leaf4Node = sg.SceneGraphNode('leaf4')
    leaf4Node.transform = tr.matmul([tr.translate(0.0, 0.6, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf4Node.childs += [gpuHojas]  

    leaf5Node = sg.SceneGraphNode('leaf5')
    leaf5Node.transform = tr.matmul([tr.translate(0.3, 0.9, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf5Node.childs += [gpuHojas]  

    leaf6Node = sg.SceneGraphNode('leaf5')
    leaf6Node.transform = tr.matmul([tr.translate(0.3, 0.9, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf6Node.childs += [gpuHojas]  

    leaf7Node = sg.SceneGraphNode('leaf5')
    leaf7Node.transform = tr.matmul([tr.translate(-0.3, 0.9, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf7Node.childs += [gpuHojas]  

    leaf8Node = sg.SceneGraphNode('leaf5')
    leaf8Node.transform = tr.matmul([tr.translate(-0.3, 0.9, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf8Node.childs += [gpuHojas] 

    leaf9Node = sg.SceneGraphNode('leaf')
    leaf9Node.transform = tr.matmul([tr.translate(0.0, 0.9, 0.6) , tr.scale(0.3, 0.3, 0.3)])
    leaf9Node.childs += [gpuHojas]

    leaf10Node = sg.SceneGraphNode('leaf')
    leaf10Node.transform = tr.matmul([tr.translate(0.0, 0.9, -0.6) , tr.scale(0.3, 0.3, 0.3)])
    leaf10Node.childs += [gpuHojas]

    leaf11Node = sg.SceneGraphNode('leaf')
    leaf11Node.transform = tr.matmul([tr.translate(0.6, 0.9, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf11Node.childs += [gpuHojas]

    leaf12Node = sg.SceneGraphNode('leaf')
    leaf12Node.transform = tr.matmul([tr.translate(-0.6, 0.9, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf12Node.childs += [gpuHojas]

    leaf13Node = sg.SceneGraphNode('leaf')
    leaf13Node.transform = tr.matmul([tr.translate(0.0, 1.2, 0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf13Node.childs += [gpuHojas]

    leaf14Node = sg.SceneGraphNode('leaf')
    leaf14Node.transform = tr.matmul([tr.translate(0.0, 1.2, -0.3) , tr.scale(0.3, 0.3, 0.3)])
    leaf14Node.childs += [gpuHojas]

    leaf15Node = sg.SceneGraphNode('leaf')
    leaf15Node.transform = tr.matmul([tr.translate(0.3, 1.2, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf15Node.childs += [gpuHojas]

    leaf16Node = sg.SceneGraphNode('leaf')
    leaf16Node.transform = tr.matmul([tr.translate(-0.3, 1.2, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf16Node.childs += [gpuHojas]

    leaf17Node = sg.SceneGraphNode('leaf')
    leaf17Node.transform = tr.matmul([tr.translate(0.0, 1.5, 0.0) , tr.scale(0.3, 0.3, 0.3)])
    leaf17Node.childs += [gpuHojas] 

    # Nodo del arbol a retornar
    treeNode = sg.SceneGraphNode('tree')
    treeNode.transform = tr.matmul([tr.translate(0.0, 0.3, 0.0) , tr.scale(1.0, 1.0, 1.0)])
    treeNode.childs += [trunkNode, branchNode, branchNode2, branchNode3, branchNode4, 
                        leafNode, leaf2Node, leaf3Node, leaf4Node, leaf5Node, leaf6Node, leaf7Node, leaf8Node, 
                        leaf9Node, leaf10Node, leaf11Node, leaf12Node, leaf13Node, leaf14Node, leaf15Node, leaf16Node, 
                        leaf17Node]

    return treeNode

def createField(pipeline):
    #creacion de las primitivas
    shapeGrass = createPrisma1()
    gpuGrass = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuGrass)
    gpuGrass.fillBuffers(
        shapeGrass.vertices, shapeGrass.indices, GL_STATIC_DRAW)
    gpuGrass.texture = es.textureSimpleSetup(
        getAssetPath("pastogodgod.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeSteet = createPrisma1()
    gpuStreet = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuStreet)
    gpuStreet.fillBuffers(
        shapeSteet.vertices, shapeSteet.indices, GL_STATIC_DRAW)
    gpuStreet.texture = es.textureSimpleSetup(
        getAssetPath("calle.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeSteet2 = createPrisma2()
    gpuStreet2 = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuStreet2)
    gpuStreet2.fillBuffers(
        shapeSteet2.vertices, shapeSteet2.indices, GL_STATIC_DRAW)
    gpuStreet2.texture = es.textureSimpleSetup(
        getAssetPath("calle.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    # suelo
    grassNode = sg.SceneGraphNode('grass')
    grassNode.transform = tr.matmul([tr.translate(15.0, -0.1, -9.0) , tr.scale(40.0, 0.01, 70.0)])
    grassNode.childs += [gpuGrass]

    # calles
    streetNodea = sg.SceneGraphNode('street1')
    streetNodea.transform = tr.matmul([tr.translate(2.0, -0.08, -2.5) , tr.scale(2.0, 0.01, 15.0)])
    streetNodea.childs += [gpuStreet]

    streetNodeb = sg.SceneGraphNode('street1')
    streetNodeb.transform = tr.matmul([tr.translate(2.0, -0.08, 13.0) , tr.scale(2.0, 0.01, 16.0)])
    streetNodeb.childs += [gpuStreet]

    streetNode2 = sg.SceneGraphNode('street2')
    streetNode2.transform = tr.matmul([tr.translate(15.0, -0.08, 21.5) , tr.scale(28.0, 0.01, 2.0)])
    streetNode2.childs += [gpuStreet2]
    
    streetNode3 = sg.SceneGraphNode('street3')
    streetNode3.transform = tr.matmul([tr.translate(15.0, -0.08, -23.0) , tr.scale(2.0, 0.01, 26.0), tr.shearing(0,0,-13,0,0,0)])
    streetNode3.childs += [gpuStreet]

    streetNode4a = sg.SceneGraphNode('street4')
    streetNode4a.transform = tr.matmul([tr.translate(28.0, -0.08, -29.0) , tr.scale(2.0, 0.01, 14.5)])
    streetNode4a.childs += [gpuStreet]

    streetNode4b = sg.SceneGraphNode('street4')
    streetNode4b.transform = tr.matmul([tr.translate(28.0, -0.08, -14.0) , tr.scale(2.0, 0.01, 15.5)])
    streetNode4b.childs += [gpuStreet]

    streetNode4c = sg.SceneGraphNode('street4')
    streetNode4c.transform = tr.matmul([tr.translate(28.0, -0.08, 0.0) , tr.scale(2.0, 0.01, 15.5)])
    streetNode4c.childs += [gpuStreet]

    streetNode4d = sg.SceneGraphNode('street4')
    streetNode4d.transform = tr.matmul([tr.translate(28.0, -0.08, 15.0) , tr.scale(2.0, 0.01, 14.5)])
    streetNode4d.childs += [gpuStreet]

    streetNode5 = sg.SceneGraphNode('street5')
    streetNode5.transform = tr.matmul([tr.translate(20.0, -0.08, -8.25) , tr.scale(14.0, 0.01, 2.0)])
    streetNode5.childs += [gpuStreet2]

    floorsNode = sg.SceneGraphNode('floors')
    floorsNode.childs += [grassNode, streetNodea, streetNodeb, streetNode2, streetNode3, streetNode4a, streetNode4c, streetNode4d, streetNode4b, streetNode5] 

    return floorsNode
    
def createScene(pipeline):
    # primitivas
    shapePared = createPrisma1()
    gpuPared = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuPared)
    gpuPared.fillBuffers(
        shapePared.vertices, shapePared.indices, GL_STATIC_DRAW)
    gpuPared.texture = es.textureSimpleSetup(
        getAssetPath("base3.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    shapeSteet = createPrisma1()
    gpuStreet = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuStreet)
    gpuStreet.fillBuffers(
        shapeSteet.vertices, shapeSteet.indices, GL_STATIC_DRAW)
    gpuStreet.texture = es.textureSimpleSetup(
        getAssetPath("calle.jpg"), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)

    houseNode = createHouse(pipeline)
    houseNode2 = createHouse2(pipeline)
    houseNode3 = createHouse3(pipeline)

    treeNode1 = createTree(pipeline) 
    treeNode2 = createTree2(pipeline)
    treeNode3 = createTree3(pipeline) 

    floorsNode = createField(pipeline)

    # Nodo de los arboles
    tree1Node = sg.SceneGraphNode('tree1')
    tree1Node.transform = tr.matmul([tr.translate(1.0, 0.0, -37.0) , tr.scale(3.2, 3.2, 3.2)])
    tree1Node.childs += [treeNode2]

    tree2Node = sg.SceneGraphNode('tree2')
    tree2Node.transform = tr.matmul([tr.translate(1.0, 0.0, -12.0) , tr.scale(3.5, 3.5, 3.5)])
    tree2Node.childs += [treeNode1]

    tree3Node = sg.SceneGraphNode('tree2')
    tree3Node.transform = tr.matmul([tr.translate(23.5, 0.0, -34.5) , tr.scale(3.5, 3.5, 3.5)])
    tree3Node.childs += [treeNode2]

    tree4Node = sg.SceneGraphNode('tree2')
    tree4Node.transform = tr.matmul([tr.translate(1.0, 0.0, -17.0) , tr.scale(3.4, 3.4, 3.4)])
    tree4Node.childs += [treeNode3]

    tree5Node = sg.SceneGraphNode('tree2')
    tree5Node.transform = tr.matmul([tr.translate(1.0, 0.0, -23.0) , tr.scale(3.3, 3.3, 3.3)])
    tree5Node.childs += [treeNode1]

    tree6Node = sg.SceneGraphNode('tree2')
    tree6Node.transform = tr.matmul([tr.translate(1.0, 0.0, -28.0) , tr.scale(3.0, 3.0, 3.0)])
    tree6Node.childs += [treeNode2]

    tree7Node = sg.SceneGraphNode('tree2')
    tree7Node.transform = tr.matmul([tr.translate(1.0, 0.0, -32.0) , tr.scale(3.5, 3.5, 3.5)])
    tree7Node.childs += [treeNode3]

    tree8Node = sg.SceneGraphNode('tree2')
    tree8Node.transform = tr.matmul([tr.translate(3.5, 0.0, -14.5) , tr.scale(3.2, 3.2, 3.2)])
    tree8Node.childs += [treeNode2]

    tree9Node = sg.SceneGraphNode('tree2')
    tree9Node.transform = tr.matmul([tr.translate(3.5, 0.0, -19.5) , tr.scale(3.6, 3.6, 3.6)])
    tree9Node.childs += [treeNode1]

    tree10Node = sg.SceneGraphNode('tree2')
    tree10Node.transform = tr.matmul([tr.translate(3.5, 0.0, -24.5) , tr.scale(3.35, 3.35, 3.35)])
    tree10Node.childs += [treeNode3]

    tree11Node = sg.SceneGraphNode('tree2')
    tree11Node.transform = tr.matmul([tr.translate(3.5, 0.0, -29.5) , tr.scale(3.5, 3.5, 3.5)])
    tree11Node.childs += [treeNode2]

    tree12Node = sg.SceneGraphNode('tree2')
    tree12Node.transform = tr.matmul([tr.translate(3.5, 0.0, -34.5) , tr.scale(3.55, 3.55, 3.55)])
    tree12Node.childs += [treeNode2]

    tree13Node = sg.SceneGraphNode('tree2')
    tree13Node.transform = tr.matmul([tr.translate(6.0, 0.0, -17.0) , tr.scale(3.4, 3.4, 3.5)])
    tree13Node.childs += [treeNode3]

    tree14Node = sg.SceneGraphNode('tree2')
    tree14Node.transform = tr.matmul([tr.translate(6.0, 0.0, -22.0) , tr.scale(3.4, 3.4, 3.4)])
    tree14Node.childs += [treeNode1]

    tree15Node = sg.SceneGraphNode('tree2')
    tree15Node.transform = tr.matmul([tr.translate(6.0, 0.0, -27.0) , tr.scale(3.0, 3.0, 3.0)])
    tree15Node.childs += [treeNode2]

    tree16Node = sg.SceneGraphNode('tree2')
    tree16Node.transform = tr.matmul([tr.translate(6.0, 0.0, -32.0) , tr.scale(3.5, 3.5, 3.5)])
    tree16Node.childs += [treeNode3]

    tree17Node = sg.SceneGraphNode('tree2')
    tree17Node.transform = tr.matmul([tr.translate(6.0, 0.0, -37.0) , tr.scale(3.1, 3.1, 3.1)])
    tree17Node.childs += [treeNode1]

    tree18Node = sg.SceneGraphNode('tree2')
    tree18Node.transform = tr.matmul([tr.translate(8.5, 0.0, -19.5) , tr.scale(3.45, 3.45, 3.45)])
    tree18Node.childs += [treeNode3]

    tree19Node = sg.SceneGraphNode('tree2')
    tree19Node.transform = tr.matmul([tr.translate(8.5, 0.0, -24.5) , tr.scale(3.55, 3.55, 3.55)])
    tree19Node.childs += [treeNode2]

    tree20Node = sg.SceneGraphNode('tree2')
    tree20Node.transform = tr.matmul([tr.translate(8.5, 0.0, -29.5) , tr.scale(3.1, 3.1, 3.1)])
    tree20Node.childs += [treeNode2]

    tree21Node = sg.SceneGraphNode('tree2')
    tree21Node.transform = tr.matmul([tr.translate(8.5, 0.0, -34.5) , tr.scale(3.4, 3.4, 3.4)])
    tree21Node.childs += [treeNode3]

    tree22Node = sg.SceneGraphNode('tree2')
    tree22Node.transform = tr.matmul([tr.translate(11.0, 0.0, -22.0) , tr.scale(3.55, 3.55, 3.55)])
    tree22Node.childs += [treeNode1]

    tree23Node = sg.SceneGraphNode('tree2')
    tree23Node.transform = tr.matmul([tr.translate(11.0, 0.0, -27.0) , tr.scale(3.0, 3.0, 3.0)])
    tree23Node.childs += [treeNode2]

    tree24Node = sg.SceneGraphNode('tree2')
    tree24Node.transform = tr.matmul([tr.translate(11.0, 0.0, -32.0) , tr.scale(3.1, 3.1, 3.1)])
    tree24Node.childs += [treeNode3]

    tree25Node = sg.SceneGraphNode('tree2')
    tree25Node.transform = tr.matmul([tr.translate(11.0, 0.0, -37.0) , tr.scale(3.45, 3.45, 3.45)])
    tree25Node.childs += [treeNode3]

    tree26Node = sg.SceneGraphNode('tree2')
    tree26Node.transform = tr.matmul([tr.translate(13.5, 0.0, -24.5) , tr.scale(3.4, 3.4, 3.4)])
    tree26Node.childs += [treeNode2]

    tree27Node = sg.SceneGraphNode('tree2')
    tree27Node.transform = tr.matmul([tr.translate(13.5, 0.0, -29.5) , tr.scale(3.3, 3.3, 3.3)])
    tree27Node.childs += [treeNode2]

    tree28Node = sg.SceneGraphNode('tree2')
    tree28Node.transform = tr.matmul([tr.translate(13.5, 0.0, -34.5) , tr.scale(3.55, 3.55, 3.55)])
    tree28Node.childs += [treeNode3]

    tree29Node = sg.SceneGraphNode('tree2')
    tree29Node.transform = tr.matmul([tr.translate(16.0, 0.0, -32.0) , tr.scale(3.1, 3.1, 3.1)])
    tree29Node.childs += [treeNode1]

    tree30Node = sg.SceneGraphNode('tree2')
    tree30Node.transform = tr.matmul([tr.translate(16.0, 0.0, -37.0) , tr.scale(3.5, 3.5, 3.5)])
    tree30Node.childs += [treeNode2]

    tree31Node = sg.SceneGraphNode('tree2')
    tree31Node.transform = tr.matmul([tr.translate(18.5, 0.0, -29.5) , tr.scale(3.4, 3.4, 3.4)])
    tree31Node.childs += [treeNode1]    

    tree32Node = sg.SceneGraphNode('tree2')
    tree32Node.transform = tr.matmul([tr.translate(18.5, 0.0, -34.5) , tr.scale(3.45, 3.45, 3.45)])
    tree32Node.childs += [treeNode3]    

    tree33Node = sg.SceneGraphNode('tree2')
    tree33Node.transform = tr.matmul([tr.translate(21.0, 0.0, -32.0) , tr.scale(3.5, 3.5, 3.5)])
    tree33Node.childs += [treeNode2]

    tree34Node = sg.SceneGraphNode('tree2')
    tree34Node.transform = tr.matmul([tr.translate(21.0, 0.0, -37.0) , tr.scale(3.5, 3.5, 3.5)])
    tree34Node.childs += [treeNode2]

    #Nodo que contiene los arboles
    forestNode = sg.SceneGraphNode('forest')
    forestNode.childs += [tree1Node, tree2Node, tree3Node, tree4Node, tree5Node, tree6Node, tree7Node, tree8Node, tree9Node, 
                        tree10Node, tree11Node, tree12Node, tree13Node, tree14Node, tree15Node, tree16Node, tree17Node, tree18Node, tree19Node,
                        tree20Node, tree21Node, tree22Node, tree23Node, tree24Node, tree25Node, tree26Node, tree27Node, tree28Node, tree29Node, 
                        tree30Node, tree31Node, tree32Node, tree33Node, tree34Node]

    # nodos de las casas (cx ny -> casa columna x numero y)
    # c1 n1 extra
    house11eNode = sg.SceneGraphNode('house11e')
    house11eNode.transform = tr.matmul([tr.translate(16.0, 0.0, -28.0) , tr.scale(0.6, 0.6, 0.8), tr.rotationY(np.pi/1.4)])
    house11eNode.childs += [houseNode]

    # c1 n1
    house11Node = sg.SceneGraphNode('house11')
    house11Node.transform = tr.matmul([tr.translate(25.0, 0.0, -27.0) , tr.scale(0.8, 0.6, 0.8), tr.rotationY(np.pi)])
    house11Node.childs += [houseNode3]

    # c2 n1
    house21Node = sg.SceneGraphNode('house21')
    house21Node.transform = tr.matmul([tr.translate(21.0, 0.0, -22.0) , tr.scale(0.7, 0.7, 0.7)])
    house21Node.childs += [houseNode3]

    # c2 n2
    house22Node = sg.SceneGraphNode('house22')
    house22Node.transform = tr.matmul([tr.translate(25.0, 0.0, -22.0) , tr.scale(0.5, 0.7, 0.7), tr.rotationY(np.pi)])
    house22Node.childs += [houseNode3]

    # c3 n1
    house31Node = sg.SceneGraphNode('house31')
    house31Node.transform = tr.matmul([tr.translate(24.0, 0.0, -16.0) , tr.scale(0.8, 0.6, 0.4), tr.rotationY(np.pi)])
    house31Node.childs += [houseNode]

    # c3 n2
    house32Node = sg.SceneGraphNode('house32')
    house32Node.transform = tr.matmul([tr.translate(24.0, 0.0, -18.5) , tr.scale(0.8, 0.6, 0.4), tr.rotationY(np.pi)])
    house32Node.childs += [houseNode]

    house322Node = sg.SceneGraphNode('house322')
    house322Node.transform = tr.matmul([tr.translate(24.0, 2.0, -18.5) , tr.scale(0.7, 0.4, 0.4), tr.rotationY(np.pi)])
    house322Node.childs += [houseNode2]

    # c3 n3
    house33Node = sg.SceneGraphNode('house33')
    house33Node.transform = tr.matmul([tr.translate(18.0, 0.0, -17.0) , tr.scale(0.7, 0.6, 0.9)])
    house33Node.childs += [houseNode3]

    # c4 n1
    house41Node = sg.SceneGraphNode('house41')
    house41Node.transform = tr.matmul([tr.translate(20.5, 0.0, -12.0) , tr.scale(0.9, 0.7, 0.9), tr.rotationY(np.pi/2)])
    house41Node.childs += [houseNode3]

    # c4 n2
    house42Node = sg.SceneGraphNode('house42')
    house42Node.transform = tr.matmul([tr.translate(14.0, 0.6, -12.0) , tr.scale(0.8, 0.6, 0.8)])
    house42Node.childs += [houseNode3]

    house42bsNode = sg.SceneGraphNode('house42bs')
    house42bsNode.transform = tr.matmul([tr.translate(14.0, 0.2, -12.0) , tr.scale(4.2, 0.6, 4.2)])
    house42bsNode.childs += [gpuPared]

    # c5 n1
    house51Node = sg.SceneGraphNode('house51')
    house51Node.transform = tr.matmul([tr.translate(8.0, 0.6, -5.1) , tr.scale(1.1, 0.7, 0.7)])
    house51Node.childs += [houseNode]

    house512Node = sg.SceneGraphNode('house512')
    house512Node.transform = tr.matmul([tr.translate(9.0, 0.6, -8.1) , tr.scale(0.7, 0.7, 0.7), tr.rotationY(-np.pi/2)])
    house512Node.childs += [houseNode]

    house513Node = sg.SceneGraphNode('house513')
    house513Node.transform = tr.matmul([tr.translate(9.25, 2.4, -5.1) , tr.scale(0.6, 0.6, 0.6)])
    house513Node.childs += [houseNode2]

    house51bsNode = sg.SceneGraphNode('house51bs')
    house51bsNode.transform = tr.matmul([tr.translate(7.5, 0.2, -5.1) , tr.scale(6.8, 0.6, 3.9)])
    house51bsNode.childs += [gpuPared]

    house51bs2Node = sg.SceneGraphNode('house51bs2')
    house51bs2Node.transform = tr.matmul([tr.translate(9.0, 0.2, -8.1) , tr.scale(3.9, 0.6, 3.9)])
    house51bs2Node.childs += [gpuPared]

    # c5 n2
    house52Node = sg.SceneGraphNode('house52')
    house52Node.transform = tr.matmul([tr.translate(15.0, 0.0, -5.1) , tr.scale(0.8, 0.7, 0.7), tr.rotationY(-np.pi/2)])
    house52Node.childs += [houseNode]

    house522Node = sg.SceneGraphNode('house522')
    house522Node.transform = tr.matmul([tr.translate(15.0, 2.0, -5.1) , tr.scale(0.6, 0.6, 0.6), tr.rotationY(-np.pi/2)])
    house522Node.childs += [houseNode2]

    # c5 n3
    house53Node = sg.SceneGraphNode('house53')
    house53Node.transform = tr.matmul([tr.translate(22.0, 0.0, -5.1) , tr.scale(0.9, 0.7, 0.7), tr.rotationY(-np.pi/2)])
    house53Node.childs += [houseNode3]
    
    # c6 n1
    house61Node = sg.SceneGraphNode('house61')
    house61Node.transform = tr.matmul([tr.translate(15.0, 0.9, 0.0) , tr.scale(0.95, 0.6, 0.95)])
    house61Node.childs += [houseNode]

    house612Node = sg.SceneGraphNode('house612')
    house612Node.transform = tr.matmul([tr.translate(15.0, 2.9, 0.0) , tr.scale(0.7, 0.6, 0.7)])
    house612Node.childs += [houseNode2]

    house61bsNode = sg.SceneGraphNode('house61bs')
    house61bsNode.transform = tr.matmul([tr.translate(14.5, 0.3, 0.0) , tr.scale(6.0, 1.0, 5.0)])
    house61bsNode.childs += [gpuPared]

    house61rNode = sg.SceneGraphNode('house61r')
    house61rNode.transform = tr.matmul([tr.translate(9.5, 0.3, 1.0) , tr.scale(6.0, 0.58, 3.0), tr.shearing(1,0,0,0,0,0)])
    house61rNode.childs += [gpuStreet]

    # c6 n2
    house62Node = sg.SceneGraphNode('house62')
    house62Node.transform = tr.matmul([tr.translate(20.5, 0.0, 0.0) , tr.scale(1.0, 0.7, 0.9), tr.rotationY(np.pi)])
    house62Node.childs += [houseNode3]

    # c7 n1
    house71Node = sg.SceneGraphNode('house71')
    house71Node.transform = tr.matmul([tr.translate(22.7, 0.0, 6.2) , tr.scale(1.0, 0.7, 0.85), tr.rotationY(np.pi)])
    house71Node.childs += [houseNode]

    house712Node = sg.SceneGraphNode('house712')
    house712Node.transform = tr.matmul([tr.translate(23.0, 2.0, 6.2) , tr.scale(0.6, 0.6, 0.6), tr.rotationY(np.pi)])
    house712Node.childs += [houseNode2]

    # c7 n2
    house72Node = sg.SceneGraphNode('house72')
    house72Node.transform = tr.matmul([tr.translate(15.0, 0.0, 6.0) , tr.scale(0.9, 0.7, 0.7), tr.rotationY(-np.pi/2)])
    house72Node.childs += [houseNode]

    house722Node = sg.SceneGraphNode('house722')
    house722Node.transform = tr.matmul([tr.translate(15.0, 2.0, 6.0) , tr.scale(0.7, 0.6, 0.5), tr.rotationY(-np.pi/2)])
    house722Node.childs += [houseNode2]

    # c7 n3
    house73Node = sg.SceneGraphNode('house73')
    house73Node.transform = tr.matmul([tr.translate(8.5, 0.6, 6.0) , tr.scale(0.9, 0.6, 0.9)])
    house73Node.childs += [houseNode]

    house732Node = sg.SceneGraphNode('house732')
    house732Node.transform = tr.matmul([tr.translate(8.5, 2.4, 6.0) , tr.scale(0.8, 0.6, 0.8)])
    house732Node.childs += [houseNode2]

    house73bsNode = sg.SceneGraphNode('house73bs')
    house73bsNode.transform = tr.matmul([tr.translate(8.5, 0.2, 6.0) , tr.scale(4.6, 0.8, 4.6)])
    house73bsNode.childs += [gpuPared]

    # c8 n1
    house81Node = sg.SceneGraphNode('house81')
    house81Node.transform = tr.matmul([tr.translate(21.0, 0.0, 12.0) , tr.scale(1.2, 0.7, 0.8), tr.rotationY(np.pi)])
    house81Node.childs += [houseNode]

    house812Node = sg.SceneGraphNode('house812')
    house812Node.transform = tr.matmul([tr.translate(21.0, 2.0, 12.0) , tr.scale(0.8, 0.6, 0.6), tr.rotationY(np.pi)])
    house812Node.childs += [houseNode2]

    # c8 n2
    house82Node = sg.SceneGraphNode('house82')
    house82Node.transform = tr.matmul([tr.translate(13.0, 0.0, 12.0) , tr.scale(0.8, 0.7, 1.2)])
    house82Node.childs += [houseNode]
    
    house822Node = sg.SceneGraphNode('house822')
    house822Node.transform = tr.matmul([tr.translate(13.0, 2.0, 12.0) , tr.scale(0.6, 0.7, 1.0)])
    house822Node.childs += [houseNode2]

    # c8 n3
    house83Node = sg.SceneGraphNode('house83')
    house83Node.transform = tr.matmul([tr.translate(7.0, 0.0, 11.0) , tr.scale(0.8, 0.7, 0.8)])
    house83Node.childs += [houseNode3]

    # c9 n1
    house91Node = sg.SceneGraphNode('house91')
    house91Node.transform = tr.matmul([tr.translate(24.0, 0.0, 18.) , tr.scale(0.8, 0.7, 0.8), tr.rotationY(np.pi/2)])
    house91Node.childs += [houseNode]

    house912Node = sg.SceneGraphNode('house912')
    house912Node.transform = tr.matmul([tr.translate(24.0, 2.0, 18.2) , tr.scale(0.7, 0.7, 0.7), tr.rotationY(np.pi/2)])
    house912Node.childs += [houseNode2]

    # c9 n2
    house92Node = sg.SceneGraphNode('house92')
    house92Node.transform = tr.matmul([tr.translate(19.0, 0.0, 17.7) , tr.scale(0.7, 0.7, 0.5), tr.rotationY(np.pi/2)])
    house92Node.childs += [houseNode3]
    
    # c9 n3
    house93Node = sg.SceneGraphNode('house93')
    house93Node.transform = tr.matmul([tr.translate(14.0, 0.0, 18.2) , tr.scale(0.7, 0.7, 0.7), tr.rotationY(np.pi/2)])
    house93Node.childs += [houseNode3]

    # c9 n4
    house94Node = sg.SceneGraphNode('house94')
    house94Node.transform = tr.matmul([tr.translate(8.0, 0.0, 18.0) , tr.scale(0.9, 0.7, 0.9)])
    house94Node.childs += [houseNode]

    house942Node = sg.SceneGraphNode('house942')
    house942Node.transform = tr.matmul([tr.translate(8.0, 2.0, 18.0) , tr.scale(0.8, 0.7, 0.8)])
    house942Node.childs += [houseNode2]


    #Nodo que contiene las casas
    allhousesNode = sg.SceneGraphNode('allhouses')
    allhousesNode.childs += [house11Node, house11eNode, 
                            house21Node, house22Node, 
                            house31Node, house32Node, house322Node, house33Node, 
                            house41Node, house42Node, house42bsNode, 
                            house51Node, house512Node, house513Node, house52Node, house522Node, house53Node, house51bsNode, house51bs2Node,
                            house61Node, house612Node, house61bsNode, house61rNode, house62Node, 
                            house71Node, house712Node, house72Node, house722Node, house73Node, house732Node, house73bsNode,
                            house81Node, house812Node, house82Node, house822Node, house83Node, 
                            house91Node, house912Node, house92Node, house93Node, house94Node, house942Node]

    scene = sg.SceneGraphNode('system')
    scene.childs+=[forestNode]
    scene.childs+=[allhousesNode]
    scene.childs+=[floorsNode]



    return scene


