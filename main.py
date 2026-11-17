# Ursina Import
from ursina import color, Entity, Ursina, window, EditorCamera, camera, Vec3, held_keys, load_texture, Grid, Text, Audio
# Shader Import
from ursina.shaders import lit_with_shadows_shader, unlit_shader
# TrailRenderer Import
from ursina.prefabs.trail_renderer import TrailRenderer
# Math Import
import math
# Random Import 
import random

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
    # Customize Constructor
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

# Reference/Citation of Text: https://www.ursinaengine.org/api_reference.html#Text

# Initializing Audio
a = Audio('space_sound', loop = True, autoplay = True)

# Trail Renderer List
trail_renderers = []

# Time
t = 0

# Moon
moon = Planet(color.white, 1, 1, 1, (68, 0, 0), load_texture('moon.png'), unlit_shader, rotation = Vec3(0, 0, 6.68))
moon.getPlanet()

# Sun        
sun = Planet(color.white, 15, 15, 15, (0, 3, 0), load_texture('sun.png'), lit_with_shadows_shader, rotation = Vec3(0, 0, 7.25))
sun.getPlanet()
    
# Mercury   
mercury = Planet(color.white, 3, 3, 3, (20, 0, 0), load_texture('mercury.png'),  unlit_shader, rotation = Vec3(0, 0, 0.034))
mercury.getPlanet()

# Mercury Trail
tr_mercury = TrailRenderer(size = (mercury.planet.scale_x, mercury.planet.scale_y), segments = 50, fade_speed = 1, parent = mercury.planet, color_gradient=[color.gray, color.gray.tint(-0.5), color.clear])
trail_renderers.append(tr_mercury)

# Mercury Text
mercury_text = Text(text = "Mercury", position = (0, 1, 0), parent = mercury.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)
    
# Venus
venus = Planet(color.white, 4, 4, 4, (40, 0, 0), load_texture('venus.png'), unlit_shader,rotation = Vec3(0, 0, 177.4))
venus.getPlanet()

# Venus Trail
tr_venus = TrailRenderer(size = (venus.planet.scale_x, venus.planet.scale_y), segments = 50, fade_speed = 1, parent = venus.planet, color_gradient=[color.orange, color.orange.tint(-0.5), color.clear])
trail_renderers.append(tr_venus)

# Venus Text
venus_text = Text(text = "Venus", position = (0, 1, 0), parent = venus.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Earth
earth = Planet(color.white, 5, 5, 5, (60, 0, 0), load_texture('earth.png'),  unlit_shader, rotation = Vec3(0, 0, 23.4))
earth.getPlanet()

# Earth Trail
tr_earth = TrailRenderer(size = (earth.planet.scale_x, earth.planet.scale_y), segments = 50, fade_speed = 1, parent = earth.planet, color_gradient=[color.blue, color.blue.tint(-0.5), color.clear])
trail_renderers.append(tr_earth)

# Earth Text
earth_text = Text(text = "Earth", position = (0, 1, 0), parent = earth.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Mars
mars = Planet(color.white, 4.5, 4.5, 4.5, (80, 0, 0), load_texture('mars.png'),  unlit_shader, rotation = Vec3(0, 0, 25.19))
mars.getPlanet()

# Mars Trail
tr_mars = TrailRenderer(size = (mars.planet.scale_x, mars.planet.scale_y), segments = 50, fade_speed = 1, parent = mars.planet, color_gradient=[color.red, color.red.tint(-0.5), color.clear])
trail_renderers.append(tr_mars)

# Mars Text
mars_text = Text(text = "Mars", position = (0, 1, 0), parent = mars.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Phobos (Moon of mars)
phobos = Planet(color.white, 1.5, 1.5, 1.5, (84, 0, 0), load_texture('phobos.png'), unlit_shader, rotation = Vec3(0, 0, 0))
phobos.getPlanet()

# Deimos (Moon of mars)
deimos = Planet(color.white, 1, 1, 1, (88, 0, 0), load_texture('deimos.png'), unlit_shader, rotation = Vec3(0, 0, 0))
deimos.getPlanet()

# Jupiter
jupiter = Planet(color.white, 8, 8, 8, (100, 0, 0), load_texture('jupiter.png'),  unlit_shader, rotation = Vec3(0, 0, 3.13))
jupiter.getPlanet()

# Jupiter Trail
tr_jupiter = TrailRenderer(size = (jupiter.planet.scale_x, jupiter.planet.scale_y), segments = 50, fade_speed = 1, parent = jupiter.planet, color_gradient=[color.brown, color.brown.tint(-0.5), color.clear])
trail_renderers.append(tr_jupiter)

# Jupiter Text
jupiter_text = Text(text = "Jupiter", position = (0, 1, 0), parent = jupiter.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Io (Moon of Jupiter)
io = Planet(color.white, 2, 2, 2, (100, 0, 0), load_texture('io.png'), unlit_shader, rotation=Vec3(0, 0, 3.13))
io.getPlanet()

# Europa (Moon of Jupiter)
europa = Planet(color.white, 1.8, 1.8, 1.8, (100, 0, 0), load_texture('europa.png'), unlit_shader, rotation=Vec3(0, 0, 3.13))
europa.getPlanet()

# Ganymede (Moon of Jupiter)
ganymede = Planet(color.white, 2.5, 2.5, 2.5, (100, 0, 0), load_texture('ganymede.png'), unlit_shader, rotation=Vec3(0, 0, 3.13))
ganymede.getPlanet()

# Callisto (Moon of Jupiter)
callisto = Planet(color.white, 2.3, 2.3, 2.3, (100, 0, 0), load_texture('callisto.png'), unlit_shader, rotation=Vec3(0, 0, 3.13))
callisto.getPlanet()

# Amalthea (Moon of Jupiter)
amalthea = Planet(color.white, 1, 1, 1, (100, 0, 0), load_texture('amalthea.png'), unlit_shader, rotation=Vec3(0, 0, 3.13))
amalthea.getPlanet()

# Himalia (Moon of Jupiter)
himalia = Planet(color.white, 1, 1, 1, (100, 0, 0), load_texture('himalia.png'), unlit_shader, rotation=Vec3(0, 0, 3.13))
himalia.getPlanet()

# Saturn
saturn = Planet(color.white, 7, 7 , 7, (120, 0, 0), load_texture('saturn.png'),  unlit_shader, rotation = Vec3(0, 0, 26.73))
saturn.getPlanet()

# Saturn Trail
tr_saturn = TrailRenderer(size = (saturn.planet.scale_x, saturn.planet.scale_y), segments = 50, fade_speed = 1, parent = saturn.planet, color_gradient = [color.brown, color.brown.tint(-0.5), color.clear])
trail_renderers.append(tr_saturn)

# Saturn Text
saturn_text = Text(text = "Saturn", position = (0, 1, 0), parent = saturn.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Titan (Moon of Saturn)
titan = Planet(color.white, 2, 2, 2, (130, 0, 0), load_texture('titan.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
titan.getPlanet()

# Rhea (Moon of Saturn)
rhea = Planet(color.white, 1.6, 1.6, 1.6, (130, 0, 0), load_texture('rhea.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
rhea.getPlanet()

# Iapetus (Moon of Saturn)
iapetus = Planet(color.white, 1.55, 1.55, 1.55, (130, 0, 0), load_texture('iapetus.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
iapetus.getPlanet()

# Dione (Moon of Saturn)
dione = Planet(color.white, 1.4, 1.4, 1.4, (130, 0, 0), load_texture('dione.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
dione.getPlanet()

# Tethys (Moon of Saturn)
tethys = Planet(color.white, 1.35, 1.35, 1.35, (130, 0, 0), load_texture('tethys.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
tethys.getPlanet()

# Enceladus (Moon of Saturn)
enceladus = Planet(color.white, 1.2, 1.2, 1.2, (130, 0, 0), load_texture('enceladus.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
enceladus.getPlanet()

# Mimas (Moon of Saturn)
mimas = Planet(color.white, 1.15, 1.15, 1.15, (130, 0, 0), load_texture('mimas.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
mimas.getPlanet()

# Hyperion (Moon of Saturn)
hyperion = Planet(color.white, 1, 1, 1, (130, 0, 0), load_texture('hyperion.png'), unlit_shader, rotation=Vec3(0, 0, 26.73))
hyperion.getPlanet()

# Uranus
uranus = Planet(color.white, 6, 6, 6, (140, 0, 0), load_texture('uranus.png'),  unlit_shader, rotation = Vec3(0, 0, 97.77))
uranus.getPlanet()

# Uranus Trail
tr_uranus = TrailRenderer(size = (uranus.planet.scale_x, uranus.planet.scale_y), segments = 50, fade_speed = 1, parent = uranus.planet, color_gradient=[color.cyan, color.cyan.tint(-0.5), color.clear])
trail_renderers.append(tr_uranus)

# Uranus Text
uranus_text = Text(text = "Uranus", position = (0, 1, 0), parent = uranus.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Ariel (Moon of Uranus)
ariel = Planet(color.white, 1.8, 1.8, 1.8, (140, 0, 0), load_texture('ariel.png'), unlit_shader, rotation=Vec3(0, 0, 97.77))
ariel.getPlanet()

# Umbriel (Moon of Uranus)
umbriel = Planet(color.white, 1.8, 1.8, 1.8, (140, 0, 0), load_texture('umbriel.png'), unlit_shader, rotation=Vec3(0, 0, 97.77))
umbriel.getPlanet()

# Titania (Moon of Uranus)
titania = Planet(color.white, 2.4, 2.4, 2.4, (140, 0, 0), load_texture('titania.png'), unlit_shader, rotation=Vec3(0, 0, 97.77))
titania.getPlanet()

# Oberon (Moon of Uranus)
oberon = Planet(color.white, 2.3, 2.3, 2.3, (140, 0, 0), load_texture('oberon.png'), unlit_shader, rotation=Vec3(0, 0, 97.77))
oberon.getPlanet()

# Neptune
neptune = Planet(color.white, 6.5, 6.5, 6.5, (160, 0, 0), load_texture('neptune.png'),  unlit_shader, rotation = Vec3(0, 0, 28.32))
neptune.getPlanet()

# Neptune Trail
tr_neptune = TrailRenderer(size = (neptune.planet.scale_x, neptune.planet.scale_y), segments = 50, fade_speed = 1, parent = neptune.planet, color_gradient=[color.azure, color.azure.tint(-0.5), color.clear])
trail_renderers.append(tr_neptune)

# Neptune Text
neptune_text = Text(text = "Neptune", position = (0, 1, 0), parent = neptune.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Triton (Moon of Neptune)
triton = Planet(color.white, 2.5, 2.5, 2.5, (160, 0, 0), load_texture('triton.png'), unlit_shader, rotation=Vec3(0, 0, 28.32))
triton.getPlanet()

# Nereid (Moon of Neptune)
nereid = Planet(color.white, 1, 1, 1, (160, 0, 0), load_texture('nereid.png'), unlit_shader, rotation=Vec3(0, 0, 28.32))
nereid.getPlanet()

# Proteus (Moon of Neptune)
proteus = Planet(color.white, 1.2, 1.2, 1.2, (160, 0, 0), load_texture('proteus.png'), unlit_shader, rotation=Vec3(0, 0, 28.32))
proteus.getPlanet()

# Pluto
pluto = Planet(color.white, 2, 2, 2, (180, 0, 0), load_texture('pluto.png'),  unlit_shader, rotation = Vec3(0, 0, 120))
pluto.getPlanet()

# Saturn Rings
saturn_rings = Entity(model = 'quad', texture = load_texture('saturn_rings.png'), scale = (22, 22), thickness = 10, rotation = Vec3(297, 90, 97.77), double_sided = True)

# Jupiter Rings
jupiter_rings = Entity(model = 'quad', texture = load_texture('jupiter_rings.png'), scale = (15, 15), thickness = 10, rotation = Vec3(273, 90, 97.77), double_sided = True)

# Uranus Rings
uranus_rings = Entity(model = 'quad', texture = load_texture('uranus_rings.png'), scale = (12, 12), thickness = 10, rotation = Vec3(370, 90, 97.77), double_sided = True)

# Neptune Rings
neptune_rings = Entity(model = 'quad', texture = load_texture('neptune_rings.png'), scale = (10, 10), thickness = 10, rotation = Vec3(299, 90, 97.77), double_sided = True)

# Grid
grid = Entity(
    model = Grid(100, 200),
    scale = 350,
    position = Vec3(5, -5, 0),
    rotation = Vec3(90, 0, 0),
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

# Camera
camera = EditorCamera()

# Launch Application
app.run()
