# Import Packages
from ursina import color, Entity, Ursina, window, EditorCamera, camera, Vec3, held_keys, load_texture
from ursina.shaders import lit_with_shadows_shader, unlit_shader

# Reference/Citation: https://www.youtube.com/watch?v=w2gu9Ah95l0&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i
# Ursina Engine
app = Ursina()

# Window Dimensions
window.size = (800, 600)

# Window Background Color
window.color = color.black

# Planet Class
class Planet:
    # Customizer Constructor
    def __init__(self, color, scale, position, texture, shader):
        # Color
        self.color = color 
        # Scale
        self.scale = scale
        # Position (x, y, z)
        self.position = position
        # Shader
        #Reference/Citation: https://www.youtube.com/watch?v=jD7cdr6-b34&t=3s
        self.shader = shader
        # Texture
        self.texture = texture
           
    # Accessor
    def getPlanet(self):
        # Entity 
        planet = Entity(
            # Model
            model = "sphere",
            # Color
            color = self.color,
            # Scale
            scale = self.scale,
            # Position (x, y, z)
            position = self.position,
            # Shader
            shader = self.shader,
            # Texture
            texture = self.texture,
        )

# Keyboard Movement        
# Reference/Citation: https://stackoverflow.com/questions/68065745/left-click-detection-with-ursina, https://www.ursinaengine.org/faq.html  
def update():
    # Conditional 'd' Key
    if (held_keys['d']):
        # 0.5 Right
        camera.position += Vec3(0.5, 0, 0)
        
    # Conditional 'w' Key
    elif (held_keys['w']):
        # 0.5 Forward
        camera.position += Vec3(0, 0, 0.5)
        
    # Conditional 's' Key
    elif (held_keys['s']):
        # 0.5 Backward
        camera.position += Vec3(0, 0, -0.5)
        
    # Conditional 'a' Key
    elif (held_keys['a']):
        # 0.5 Left
        camera.position += Vec3(-0.5, 0, 0)  
        
    # Conditional 'r' Key 
    elif (held_keys['r']):
        # Origin Position 
        camera.position = Vec3(0, 0, 0)
        # Origin Rotation
        camera.rotation = Vec3(0, 0, 0)

# Update Function 
update()

# Camera (color, scale, position, texture, shader)
camera = EditorCamera()

# Sun (color, scale, position, texture, shader)       
sun = Planet(color.white, 15, (0, 0, 0), load_texture('sun.png'), lit_with_shadows_shader)
sun.getPlanet()

# Mercury (color, scale, position, texture, shader) 
mercury = Planet(color.white, 3, (20, 0, 0), load_texture('mercury.png'),  unlit_shader)
mercury.getPlanet()

# Venus (color, scale, position, texture, shader)
venus = Planet(color.white, 4, (40, 0, 0), load_texture('venus.png'), unlit_shader)
venus.getPlanet()

# Earth (color, scale, position, texture, shader)
earth = Planet(color.white, 5, (60, 0, 0), load_texture('earth.png'),  unlit_shader)
earth.getPlanet()

# Mars (color, scale, position, texture, shader)
mars = Planet(color.white, 4.5, (80, 0, 0), load_texture('mars.png'),  unlit_shader)
mars.getPlanet()

# Jupiter (color, scale, position, texture, shader)
jupiter = Planet(color.white, 8, (100, 0, 0), load_texture('jupiter.png'),  unlit_shader)
jupiter.getPlanet()

# Saturn (color, scale, position, texture, shader)
saturn = Planet(color.white, 7, (120, 0, 0), load_texture('saturn.png'),  unlit_shader)
saturn.getPlanet()

# Uranus (color, scale, position, texture, shader)
uranus = Planet(color.white, 6, (140, 0, 0), load_texture('uranus.png'),  unlit_shader)
uranus.getPlanet()

# Neptune (color, scale, position, texture, shader)
neptune = Planet(color.white, 6.5, (160, 0, 0), load_texture('neptune.png'),  unlit_shader)
neptune.getPlanet()

# Launch Application
app.run()
