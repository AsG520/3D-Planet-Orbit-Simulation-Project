# Import Packages
from ursina import color, Entity, Ursina, window, EditorCamera, camera, Vec3, held_keys, load_texture
from ursina.shaders import lit_with_shadows_shader

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

# Launch Application
app.run()
