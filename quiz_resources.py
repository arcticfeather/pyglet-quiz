import pyglet
import os

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

characters = []

for file in os.listdir("resources/characters"):
    if file.endswith(".png"):
        characters.append(pyglet.resource.image("characters/"+file))

frame = pyglet.resource.image("frame.png")
selected_frame = pyglet.resource.image("selected_frame.png")
arrow_up = pyglet.resource.image("arrow_up.png")
arrow_down = pyglet.resource.image("arrow_down.png")