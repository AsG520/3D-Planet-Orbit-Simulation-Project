# Import Packages
from ursina import color, Entity, Ursina, window, EditorCamera, camera, Vec3, held_keys, load_texture
from ursina.shaders import lit_with_shadows_shader, unlit_shader
# Math Import
import math

# Reference/Citation: https://www.youtube.com/watch?v=w2gu9Ah95l0&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i
# Ursina Engine
app = Ursina(title='3D Planet Orbit Simulation')

# Reference/Citation: https://www.youtube.com/watch?v=pDTdZGxlkLo
# Window Border
window.borderless = True
# Window Exit Button
window.exit_button.enabled = True
# Window Cog Button
window.cog_button.enabled = True
# Window Cog Button Color
window.cog_button.color = color.white
# Window Entity Counter
window.entity_counter.enabled = False
# Window Collider Counter
window.collider_counter.enabled = False

# Window Dimensions
window.size = (800, 600)

# Window Background Color
window.color = color.black

# Planet Class
class Planet:
    # Customizer Constructor
    def __init__(self, color, scale_x, scale_y, scale_z, position, texture, shader, rotation = Vec3(0, 0, 0)):
        # Color
        self.color = color 
        # Scale X
        self.scale_x = scale_x
        # Scale Y
        self.scale_y = scale_y
        # Scale Z
        self.scale_z = scale_z
        # Position (x, y, z)
        self.position = position
        # Shader
        #Reference/Citation: https://www.youtube.com/watch?v=jD7cdr6-b34&t=3s
        self.shader = shader
        # Texture
        self.texture = texture
        # Rotation
        self.rotation = rotation
           
    # Accessor
    def getPlanet(self):
        # Entity 
        self.planet = Entity(
            # Model
            model = "sphere",
            # Color
            color = self.color,
            # Position (x, y, z)
            position = self.position,
            # Shader
            shader = self.shader,
            # Texture
            texture = self.texture,
            # Rotation
            rotation = self.rotation,
            # Scale X
            scale_x = self.scale_x,
            # Scale Y
            scale_y = self.scale_y,
            # Scale Z
            scale_z = self.scale_z
        ) 
        
# Time
t = 0

# Moon
moon = Planet(color.white, 1, 1, 1, (65, 0, 0), load_texture('moon.png'), unlit_shader, rotation = Vec3(0, 0, 6.68))
moon.getPlanet()

# Sun        
sun = Planet(color.white, 15, 15, 15, (0, 0, 0), load_texture('sun.png'), lit_with_shadows_shader, rotation = Vec3(0, 0, 7.25))
sun.getPlanet()
    
# Mercury   
mercury = Planet(color.white, 3, 3, 3, (20, 0, 0), load_texture('mercury.png'), unlit_shader, rotation = Vec3(0, 0, 0.034))
mercury.getPlanet()

# Venus
venus = Planet(color.white, 4, 4, 4, (40, 0, 0), load_texture('venus.png'), unlit_shader,rotation = Vec3(0, 0, 177.4))
venus.getPlanet()

# Earth
earth = Planet(color.white, 5, 5, 5, (60, 0, 0), load_texture('earth.png'),  unlit_shader, rotation = Vec3(0, 0, 23.4))
earth.getPlanet()

# Mars
mars = Planet(color.white, 4.5, 4.5, 4.5, (80, 0, 0), load_texture('mars.png'),  unlit_shader, rotation = Vec3(0, 0, 25.19))
mars.getPlanet()

# Jupiter
jupiter = Planet(color.white, 8, 8, 8, (100, 0, 0), load_texture('jupiter.png'),  unlit_shader, rotation = Vec3(0, 0, 3.13))
jupiter.getPlanet()

# Saturn
saturn = Planet(color.white, 7, 7 , 7, (120, 0, 0), load_texture('saturn.png'),  unlit_shader, rotation = Vec3(0, 0, 26.73))
saturn.getPlanet()

# Uranus
uranus = Planet(color.white, 6, 6, 6, (140, 0, 0), load_texture('uranus.png'),  unlit_shader, rotation = Vec3(0, 0, 97.77))
uranus.getPlanet()

# Neptune
neptune = Planet(color.white, 6.5, 6.5, 6.5, (160, 0, 0), load_texture('neptune.png'),  unlit_shader, rotation = Vec3(0, 0, 28.32))
neptune.getPlanet()

# Pluto
pluto = Planet(color.white, 2, 2, 2, (180, 0, 0), load_texture('pluto.png'),  unlit_shader, rotation = Vec3(0, 0, 120))
pluto.getPlanet()

# Saturn Rings
saturn_rings = Entity(model = 'quad', texture = load_texture('saturns_ring.png'), scale = (22, 22), thickness = 10, rotation = Vec3(297, 90, 97.77), double_sided = True)

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

# Camera
camera = EditorCamera()

# Launch Application
app.run()
