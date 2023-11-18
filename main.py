from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grassTexture = load_texture('imgs/grass_block.png')
stoneTexture = load_texture('imgs/stone_block.png')
brickTexture = load_texture('imgs/brick_block.png')
dirtTexture = load_texture('imgs/dirt_block.png')
skyTexture = load_texture('imgs/skybox.png')
armTexture = load_texture('imgs/arm_texture.png')
punchSound = Audio('imgs/punch_sound',loop = False, autoplay=False)
blockPick = 1

window.fps_counter.enabled = False
window.exit_button.visible = False


def update():
    global blockPick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else: 
        hand.passive()

    if held_keys['1']: 
        blockPick = 1
    if held_keys['2']: 
        blockPick = 2
    if held_keys['3']: 
        blockPick = 3
    if held_keys['4']: 
        blockPick = 4


class Cube(Button):
    def __init__(self, position = (0,0,0),texture = grassTexture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'imgs/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            #highlight_color = color.lime,
            scale = 0.5
        
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                punchSound.play()
                if blockPick == 1: cube = Cube(position=self.position+mouse.normal,texture=grassTexture)
                if blockPick == 2: cube = Cube(position=self.position+mouse.normal,texture=stoneTexture)
                if blockPick == 3: cube = Cube(position=self.position+mouse.normal,texture=brickTexture)
                if blockPick == 4: cube = Cube(position=self.position+mouse.normal,texture=dirtTexture)

            if key == "right mouse down":
                punchSound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self,texture = skyTexture):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self,texture=armTexture):
        super().__init__(
            parent = camera.ui,
            model = 'imgs/arm',
            texture = texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)

for i in range(30):
    for j in range(30):
        voxel = Cube(position=(j,0,i))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()