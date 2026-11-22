# Ursina Import
from ursina import color, Entity, Ursina, window, EditorCamera, camera, Vec3, held_keys, load_texture, Grid, Text, mouse, Audio, ThinSlider
# Shader Import
from ursina.shaders import lit_with_shadows_shader, unlit_shader
# TrailRenderer Import
from ursina.prefabs.trail_renderer import TrailRenderer
# Math Import
import math

# Reference/Citation: https://www.youtube.com/watch?v=w2gu9Ah95l0&list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i
# Ursina Engine
app = Ursina(title = '3D Planet Orbit Simulation')

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

# Reference/Citation: https://docs.python.org/3/tutorial/classes.html
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
        # Reference/Citation: https://www.youtube.com/watch?v=jD7cdr6-b34&t=3s
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

# Reference/Citation: https://www.ursinaengine.org/api_reference.html#Cursor
# Cursor
cursor = Entity(parent = camera.ui, model = 'quad', color = color.red, scale = 0.008, rotation_z = 45)

# Reference/Citation of Text: https://www.ursinaengine.org/api_reference.html#Text

# Reference/Citation: https://www.ursinaengine.org/api_reference.html#Audio
# Initializing Audio
a = Audio('space_sound', loop = True, autoplay = True)

# Reference/Citation: https://www.ursinaengine.org/api_reference.html#TrailRenderer
# Trail Renderer List
trail_renderers = []

# Time
t = 0

# Reference/Citation: https://www.ursinaengine.org/api_reference.html#Slider
# Slider
slider = ThinSlider(max = 100, dynamic = True, position = (-0.25, -0.45))
# Slider Text
slider.knob.text_entity.enabled = False

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
tr_mercury = TrailRenderer(size = (mercury.planet.scale_x, mercury.planet.scale_y), segments = 50, fade_speed = 1, parent = mercury.planet, color_gradient = [color.gray, color.gray.tint(-0.5), color.clear])
trail_renderers.append(tr_mercury)

# Mercury Text
mercury_text = Text(text = "Mercury", position = (0, 1, 0), parent = mercury.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)
    
# Venus
venus = Planet(color.white, 4, 4, 4, (40, 0, 0), load_texture('venus.png'), unlit_shader,rotation = Vec3(0, 0, 177.4))
venus.getPlanet()

# Venus Trail
tr_venus = TrailRenderer(size = (venus.planet.scale_x, venus.planet.scale_y), segments = 50, fade_speed = 1, parent = venus.planet, color_gradient = [color.orange, color.orange.tint(-0.5), color.clear])
trail_renderers.append(tr_venus)

# Venus Text
venus_text = Text(text = "Venus", position = (0, 1, 0), parent = venus.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Earth
earth = Planet(color.white, 5, 5, 5, (60, 0, 0), load_texture('earth.png'), unlit_shader, rotation = Vec3(0, 0, 23.4))
earth.getPlanet()

# Earth Trail
tr_earth = TrailRenderer(size = (earth.planet.scale_x, earth.planet.scale_y), segments = 50, fade_speed = 1, parent = earth.planet, color_gradient = [color.blue, color.blue.tint(-0.5), color.clear])
trail_renderers.append(tr_earth)

# Earth Text
earth_text = Text(text = "Earth", position = (0, 1, 0), parent = earth.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Mars
mars = Planet(color.white, 4.5, 4.5, 4.5, (80, 0, 0), load_texture('mars.png'), unlit_shader, rotation = Vec3(0, 0, 25.19))
mars.getPlanet()

# Mars Trail
tr_mars = TrailRenderer(size = (mars.planet.scale_x, mars.planet.scale_y), segments = 50, fade_speed = 1, parent = mars.planet, color_gradient = [color.red, color.red.tint(-0.5), color.clear])
trail_renderers.append(tr_mars)

# Mars Text
mars_text = Text(text = "Mars", position = (0, 1, 0), parent = mars.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Phobos (Moon of Mars)
phobos = Planet(color.white, 1.5, 1.5, 1.5, (84, 0, 0), load_texture('phobos.png'), unlit_shader, rotation = Vec3(0, 0, 0))
phobos.getPlanet()

# Deimos (Moon of Mars)
deimos = Planet(color.white, 1, 1, 1, (88, 0, 0), load_texture('deimos.png'), unlit_shader, rotation = Vec3(0, 0, 0))
deimos.getPlanet()

# Jupiter
jupiter = Planet(color.white, 8, 8, 8, (100, 0, 0), load_texture('jupiter.png'), unlit_shader, rotation = Vec3(0, 0, 3.13))
jupiter.getPlanet()

# Jupiter Trail
tr_jupiter = TrailRenderer(size = (jupiter.planet.scale_x, jupiter.planet.scale_y), segments = 50, fade_speed = 1, parent = jupiter.planet, color_gradient = [color.brown, color.brown.tint(-0.5), color.clear])
trail_renderers.append(tr_jupiter)

# Jupiter Text
jupiter_text = Text(text = "Jupiter", position = (0, 1, 0), parent = jupiter.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Io (Moon of Jupiter)
io = Planet(color.white, 2, 2, 2, (100, 0, 0), load_texture('io.png'), unlit_shader, rotation = Vec3(0, 0, 3.13))
io.getPlanet()

# Europa (Moon of Jupiter)
europa = Planet(color.white, 1.8, 1.8, 1.8, (100, 0, 0), load_texture('europa.png'), unlit_shader, rotation = Vec3(0, 0, 3.13))
europa.getPlanet()

# Ganymede (Moon of Jupiter)
ganymede = Planet(color.white, 2.5, 2.5, 2.5, (100, 0, 0), load_texture('ganymede.png'), unlit_shader, rotation = Vec3(0, 0, 3.13))
ganymede.getPlanet()

# Callisto (Moon of Jupiter)
callisto = Planet(color.white, 2.3, 2.3, 2.3, (100, 0, 0), load_texture('callisto.png'), unlit_shader, rotation = Vec3(0, 0, 3.13))
callisto.getPlanet()

# Amalthea (Moon of Jupiter)
amalthea = Planet(color.white, 1, 1, 1, (100, 0, 0), load_texture('amalthea.png'), unlit_shader, rotation = Vec3(0, 0, 3.13))
amalthea.getPlanet()

# Himalia (Moon of Jupiter)
himalia = Planet(color.white, 1, 1, 1, (100, 0, 0), load_texture('himalia.png'), unlit_shader, rotation = Vec3(0, 0, 3.13))
himalia.getPlanet()

# Saturn
saturn = Planet(color.white, 7, 7 , 7, (120, 0, 0), load_texture('saturn.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
saturn.getPlanet()

# Saturn Trail
tr_saturn = TrailRenderer(size = (saturn.planet.scale_x, saturn.planet.scale_y), segments = 50, fade_speed = 1, parent = saturn.planet, color_gradient = [color.brown, color.brown.tint(-0.5), color.clear])
trail_renderers.append(tr_saturn)

# Saturn Text
saturn_text = Text(text = "Saturn", position = (0, 1, 0), parent = saturn.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Titan (Moon of Saturn)
titan = Planet(color.white, 2, 2, 2, (130, 0, 0), load_texture('titan.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
titan.getPlanet()

# Rhea (Moon of Saturn)
rhea = Planet(color.white, 1.6, 1.6, 1.6, (130, 0, 0), load_texture('rhea.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
rhea.getPlanet()

# Iapetus (Moon of Saturn)
iapetus = Planet(color.white, 1.55, 1.55, 1.55, (130, 0, 0), load_texture('iapetus.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
iapetus.getPlanet()

# Dione (Moon of Saturn)
dione = Planet(color.white, 1.4, 1.4, 1.4, (130, 0, 0), load_texture('dione.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
dione.getPlanet()

# Tethys (Moon of Saturn)
tethys = Planet(color.white, 1.35, 1.35, 1.35, (130, 0, 0), load_texture('tethys.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
tethys.getPlanet()

# Enceladus (Moon of Saturn)
enceladus = Planet(color.white, 1.2, 1.2, 1.2, (130, 0, 0), load_texture('enceladus.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
enceladus.getPlanet()

# Mimas (Moon of Saturn)
mimas = Planet(color.white, 1.15, 1.15, 1.15, (130, 0, 0), load_texture('mimas.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
mimas.getPlanet()

# Hyperion (Moon of Saturn)
hyperion = Planet(color.white, 1, 1, 1, (130, 0, 0), load_texture('hyperion.png'), unlit_shader, rotation = Vec3(0, 0, 26.73))
hyperion.getPlanet()

# Uranus
uranus = Planet(color.white, 6, 6, 6, (140, 0, 0), load_texture('uranus.png'), unlit_shader, rotation = Vec3(0, 0, 97.77))
uranus.getPlanet()

# Uranus Trail
tr_uranus = TrailRenderer(size = (uranus.planet.scale_x, uranus.planet.scale_y), segments = 50, fade_speed = 1, parent = uranus.planet, color_gradient = [color.cyan, color.cyan.tint(-0.5), color.clear])
trail_renderers.append(tr_uranus)

# Uranus Text
uranus_text = Text(text = "Uranus", position = (0, 1, 0), parent = uranus.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Ariel (Moon of Uranus)
ariel = Planet(color.white, 1.8, 1.8, 1.8, (140, 0, 0), load_texture('ariel.png'), unlit_shader, rotation = Vec3(0, 0, 97.77))
ariel.getPlanet()

# Umbriel (Moon of Uranus)
umbriel = Planet(color.white, 1.8, 1.8, 1.8, (140, 0, 0), load_texture('umbriel.png'), unlit_shader, rotation = Vec3(0, 0, 97.77))
umbriel.getPlanet()

# Titania (Moon of Uranus)
titania = Planet(color.white, 2.4, 2.4, 2.4, (140, 0, 0), load_texture('titania.png'), unlit_shader, rotation = Vec3(0, 0, 97.77))
titania.getPlanet()

# Oberon (Moon of Uranus)
oberon = Planet(color.white, 2.3, 2.3, 2.3, (140, 0, 0), load_texture('oberon.png'), unlit_shader, rotation = Vec3(0, 0, 97.77))
oberon.getPlanet()

# Neptune
neptune = Planet(color.white, 6.5, 6.5, 6.5, (160, 0, 0), load_texture('neptune.png'), unlit_shader, rotation = Vec3(0, 0, 28.32))
neptune.getPlanet()

# Neptune Trail
tr_neptune = TrailRenderer(size = (neptune.planet.scale_x, neptune.planet.scale_y), segments = 50, fade_speed = 1, parent = neptune.planet, color_gradient = [color.azure, color.azure.tint(-0.5), color.clear])
trail_renderers.append(tr_neptune)

# Neptune Text
neptune_text = Text(text = "Neptune", position = (0, 1, 0), parent = neptune.planet, origin = (0, 0), color = color.white, scale = 0.3, billboard = True)

# Triton (Moon of Neptune)
triton = Planet(color.white, 2.5, 2.5, 2.5, (160, 0, 0), load_texture('triton.png'), unlit_shader, rotation = Vec3(0, 0, 28.32))
triton.getPlanet()

# Nereid (Moon of Neptune)
nereid = Planet(color.white, 1, 1, 1, (160, 0, 0), load_texture('nereid.png'), unlit_shader, rotation = Vec3(0, 0, 28.32))
nereid.getPlanet()

# Proteus (Moon of Neptune)
proteus = Planet(color.white, 1.2, 1.2, 1.2, (160, 0, 0), load_texture('proteus.png'), unlit_shader, rotation = Vec3(0, 0, 28.32))
proteus.getPlanet()

# Pluto
pluto = Planet(color.white, 2, 2, 2, (180, 0, 0), load_texture('pluto.png'), unlit_shader, rotation = Vec3(0, 0, 120))
pluto.getPlanet()

# Saturn Rings
saturn_rings = Entity(model = 'quad', texture = load_texture('saturn_rings.png'), scale = (22, 22), thickness = 10, rotation = Vec3(297, 90, 97.77), double_sided = True)

# Jupiter Rings
jupiter_rings = Entity(model = 'quad', texture = load_texture('jupiter_rings.png'), scale = (15, 15), thickness = 10, rotation = Vec3(273, 90, 97.77), double_sided = True)

# Uranus Rings
uranus_rings = Entity(model = 'quad', texture = load_texture('uranus_rings.png'), scale = (12, 12), thickness = 10, rotation = Vec3(370, 90, 97.77), double_sided = True)

# Neptune Rings
neptune_rings = Entity(model = 'quad', texture = load_texture('neptune_rings.png'), scale = (10, 10), thickness = 10, rotation = Vec3(299, 90, 97.77), double_sided = True)

# Reference/Citation: https://www.ursinaengine.org/api_reference.html#Grid
# Cube Grid
cube_grid = Entity()

# Top Base
Entity(parent = cube_grid, model = Grid(20, 20), scale = 350, x = 0, y = 200, rotation = Vec3(90, 90, 0))
# Bottom Base
Entity(parent = cube_grid, model = Grid(20, 20), scale = 350, x = 0, y = -200, rotation = Vec3(90, 90, 0))

# Right Base
Entity(parent = cube_grid, model = Grid(20, 20), scale = 350, x = 200, rotation = Vec3(0, 90, 0))
# Left Base
Entity(parent = cube_grid, model = Grid(20, 20), scale = 350, x = -200, rotation = Vec3(0, 90, 0))

# Back Base
Entity(parent = cube_grid, model = Grid(20, 20), scale = 350, z = -200)
# Front Base
Entity(parent = cube_grid, model = Grid(20, 20), scale = 350, z = 200)

# Join Faces
cube_grid.combine()

# Triangle Connection
cube_grid.model.mode = 'triangle'
# Updating Model
cube_grid.model.generate()

# Cube Grid Opacity
cube_grid.color = color.rgba(255, 255, 255, 0.20)

# Update Function
def update():
    # Time Variable
    global t
    # Increment Time
    t += 0.01

    # Relative Sun
    sun.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = sun.planet)
    
    # Rotation Radius Moon
    radius_moon = 8
    # Relative Moon 
    moon.planet.rotate(Vec3(0, 0, 6.68) * -2, relative_to = moon.planet)
    # Rotate Moon X
    moon.planet.x = math.cos(t / 0.0748) * radius_moon + earth.planet.x
    # Rotate Moon Z
    moon.planet.z = math.sin(t / 0.0748) * radius_moon + earth.planet.z
    
    # Relative Jupiter Rings
    jupiter_rings.rotate(Vec3(0, 0, 1) * 2, relative_to = jupiter_rings)
    # Rotate Jupiter Rings X
    jupiter_rings.x = jupiter.planet.x
    # Rotate Jupiter Rings Z 
    jupiter_rings.z = jupiter.planet.z
    
    # Relative Uranus Rings
    uranus_rings.rotate(Vec3(0, 0, 1) * -2, relative_to = uranus_rings)
    # Rotate Uranus Rings X
    uranus_rings.x = uranus.planet.x
    # Rotate Uranus Rings Z
    uranus_rings.z = uranus.planet.z
    
    # Relative Neptune Rings
    neptune_rings.rotate(Vec3(0, 0, 1) * 2, relative_to = neptune_rings)
    # Rotate Neptune Rings X
    neptune_rings.x = neptune.planet.x
    # Rotate Neptune Rings Z
    neptune_rings.z = neptune.planet.z
        
    # Rotation Radius Mercury
    radius_mercury = 20
    # Rotate Mercury X
    mercury.planet.x = math.cos(t / 0.24) * radius_mercury
    # Rotate Mercury Z
    mercury.planet.z = math.sin(t / 0.24) * radius_mercury
    # Relative Mercury
    mercury.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = mercury.planet)
    
    # Rotation Radius Venus
    radius_venus = 40
    # Rotate Venus X
    venus.planet.x = math.cos(t / 0.62) * radius_venus
    # Rotate Venus Z
    venus.planet.z = math.sin(t / 0.62) * radius_venus
    # Relative Venus
    venus.planet.rotate(Vec3(0, 1, 0) * 2, relative_to = venus.planet)
    
    # Rotation Radius Earth 
    radius_earth = 60
    # Rotate Venus X
    earth.planet.x = math.cos(t) * radius_earth
    # Rotate Venus Z
    earth.planet.z = math.sin(t) * radius_earth
    # Relative Earth
    earth.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = earth.planet)
      
    # Rotation Radius Mars
    radius_mars = 80
    # Rotate Mars X
    mars.planet.x = math.cos(t / 1.88) * radius_mars
    # Rotate Mars Z
    mars.planet.z = math.sin(t / 1.88) * radius_mars
    # Relative Mars
    mars.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = mars.planet)
    
     # Rotation Radius Phobos
    radius_phobos = 4
    # Rotate Phobos X
    phobos.planet.x = math.cos(t / 0.087) * radius_phobos + mars.planet.x
    # Rotate Phobos Z
    phobos.planet.z = math.sin(t / 0.087) * radius_phobos + mars.planet.z
    # Relative Phobos
    phobos.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = phobos.planet)
    
     # Rotation Radius Deimos
    radius_deimos = 8
    # Rotate Deimos X
    deimos.planet.x = math.cos(t / 0.346) * radius_deimos + mars.planet.x
    # Rotate Deimos Z
    deimos.planet.z = math.sin(t / 0.346) * radius_deimos + mars.planet.z
    # Relative Deimos
    deimos.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = deimos.planet)
    
    # Rotation Radius Jupiter
    radius_jupiter = 100
    # Rotate Jupiter X
    jupiter.planet.x = math.cos(t / 11.86) * radius_jupiter
    # Rotate Jupiter Z
    jupiter.planet.z = math.sin(t / 11.86) * radius_jupiter
    # Relative Jupiter
    jupiter.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = jupiter.planet)
    
    # Rotation Radius Amalthea
    radius_amalthea = 4.5
    # Rotate Amalthea X
    amalthea.planet.x = math.cos(t / 0.498) * radius_amalthea + jupiter.planet.x
    # Rotate Amalthea Z
    amalthea.planet.z = math.sin(t / 0.498) * radius_amalthea + jupiter.planet.z
    # Relative Amalthea
    amalthea.planet.rotate(Vec3(0, 1, 0) * -2, relative_to=jupiter.planet)

    # Rotation Radius Io
    radius_io = 6
    # Rotate Io X
    io.planet.x = math.cos(t / 1.769) * radius_io + jupiter.planet.x
    # Rotate Io Z
    io.planet.z = math.sin(t / 1.769) * radius_io + jupiter.planet.z
    # Relative Io
    io.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = jupiter.planet)

    # Rotation Radius Europa
    radius_europa = 8
    # Rotate Europa X
    europa.planet.x = math.cos(t / 3.551) * radius_europa + jupiter.planet.x
    # Rotate Europa Z
    europa.planet.z = math.sin(t / 3.551) * radius_europa + jupiter.planet.z
    # Relative Europa
    europa.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = jupiter.planet)

    # Rotation Radius Ganymede
    radius_ganymede = 11
    # Rotate Ganymede X
    ganymede.planet.x = math.cos(t / 7.155) * radius_ganymede + jupiter.planet.x
    # Rotate Ganymede Z
    ganymede.planet.z = math.sin(t / 7.155) * radius_ganymede + jupiter.planet.z
    # Relative Ganymede
    ganymede.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = jupiter.planet)

    # Rotation Radius Callisto
    radius_callisto = 12
    # Rotate Callisto X
    callisto.planet.x = math.cos(t / 16.689) * radius_callisto + jupiter.planet.x
    # Rotate Callisto Z
    callisto.planet.z = math.sin(t / 16.689) * radius_callisto + jupiter.planet.z
    # Relative Callisto
    callisto.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = jupiter.planet)

    # Rotation Radius Himalia
    radius_himalia = 35
    # Rotate Himalia X
    himalia.planet.x = math.cos(t / 250.566) * radius_himalia + jupiter.planet.x
    # Rotate Himalia Z
    himalia.planet.z = math.sin(t / 250.566) * radius_himalia + jupiter.planet.z
    # Relative Himalia
    himalia.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = jupiter.planet)

    # Rotation Radius Saturn
    radius_saturn = 120
    # Rotate Saturn X
    saturn.planet.x = math.cos(t / 29.46) * radius_saturn
    # Rotate Saturn Z
    saturn.planet.z = math.sin(t / 29.46) * radius_saturn
    # Relative Saturn
    saturn.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Relative Saturn Rings
    saturn_rings.rotate(Vec3(0, 0, 1) * 2, relative_to = saturn_rings)
    # Rotate Saturn Rings X
    saturn_rings.x = saturn.planet.x
    # Rotate Saturn Rings Z
    saturn_rings.z = saturn.planet.z
    
    # Rotation Radius Mimas
    radius_mimas = 4
    # Rotate Mimas X
    mimas.planet.x = math.cos(t / 0.94) * radius_mimas + saturn.planet.x
    # Rotate Mimas Z
    mimas.planet.z = math.sin(t / 0.94) * radius_mimas + saturn.planet.z
    # Relative Mimas
    mimas.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Enceladus
    radius_enceladus = 4.5
    # Rotate Enceladus X
    enceladus.planet.x = math.cos(t / 1.37) * radius_enceladus + saturn.planet.x
    # Rotate Enceladus Z
    enceladus.planet.z = math.sin(t / 1.37) * radius_enceladus + saturn.planet.z
    # Relative Enceladus
    enceladus.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Tethys
    radius_tethys = 5.5
    # Rotate Tethys X
    tethys.planet.x = math.cos(t / 1.89) * radius_tethys + saturn.planet.x
    # Rotate Tethys Z
    tethys.planet.z = math.sin(t / 1.89) * radius_tethys + saturn.planet.z
    # Relative Tethys
    tethys.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Dione
    radius_dione = 6.5
    # Rotate Dione X
    dione.planet.x = math.cos(t / 2.74) * radius_dione + saturn.planet.x
    # Rotate Dione Z
    dione.planet.z = math.sin(t / 2.74) * radius_dione + saturn.planet.z
    # Relative Dione
    dione.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Rhea
    radius_rhea = 9
    # Rotate Rhea X
    rhea.planet.x = math.cos(t / 4.52) * radius_rhea + saturn.planet.x
    # Rotate Rhea Z
    rhea.planet.z = math.sin(t / 4.52) * radius_rhea + saturn.planet.z
    # Relative Rhea
    rhea.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Titan
    radius_titan = 10
    # Rotate Titan X
    titan.planet.x = math.cos(t / 15.95) * radius_titan + saturn.planet.x
    # Rotate Titan Z
    titan.planet.z = math.sin(t / 15.95) * radius_titan + saturn.planet.z
    # Relative Titan
    titan.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Hyperion
    radius_hyperion = 12.03
    # Rotate Hyperion X
    hyperion.planet.x = math.cos(t / 21.28) * radius_hyperion + saturn.planet.x
    # Rotate Hyperion Z
    hyperion.planet.z = math.sin(t / 21.28) * radius_hyperion + saturn.planet.z
    # Relative Hyperion
    hyperion.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Iapetus
    radius_iapetus = 28.95
    # Rotate Iapetus X
    iapetus.planet.x = math.cos(t / 79.33) * radius_iapetus + saturn.planet.x
    # Rotate Iapetus Z
    iapetus.planet.z = math.sin(t / 79.33) * radius_iapetus + saturn.planet.z
    # Relative Iapetus
    iapetus.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = saturn.planet)

    # Rotation Radius Uranus
    radius_uranus = 140
    # Rotate Uranus X
    uranus.planet.x = math.cos(t / 84.01) * radius_uranus
    # Rotate Uranus Z
    uranus.planet.z = math.sin(t / 84.01) * radius_uranus
    # Relative Uranus
    uranus.planet.rotate(Vec3(0, 1, 0) * 2, relative_to = uranus.planet)
    
    # Rotation Radius Ariel
    radius_ariel = 6
    # Rotate Ariel X
    ariel.planet.x = math.cos(t / 2.520379) * radius_ariel + uranus.planet.x
    # Rotate Ariel Z
    ariel.planet.z = math.sin(t / 2.520379) * radius_ariel + uranus.planet.z
    # Relative Ariel
    ariel.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = uranus.planet)

    # Rotation Radius Umbriel
    radius_umbriel = 8
    # Rotate Umbriel X
    umbriel.planet.x = math.cos(t / 4.144176) * radius_umbriel + uranus.planet.x
    # Rotate Umbriel Z
    umbriel.planet.z = math.sin(t / 4.144176) * radius_umbriel + uranus.planet.z
    # Relative Umbriel
    umbriel.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = uranus.planet)

    # Rotation Radius Titania
    radius_titania = 11
    # Rotate Titania X
    titania.planet.x = math.cos(t / 8.705867) * radius_titania + uranus.planet.x
    # Rotate Titania Z
    titania.planet.z = math.sin(t / 8.705867) * radius_titania + uranus.planet.z
    # Relative Titania
    titania.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = uranus.planet)

    # Rotation Radius Oberon
    radius_oberon = 14.5
    # Rotate Oberon X
    oberon.planet.x = math.cos(t / 13.463234) * radius_oberon + uranus.planet.x
    # Rotate Oberon Z
    oberon.planet.z = math.sin(t / 13.463234) * radius_oberon + uranus.planet.z
    # Relative Oberon
    oberon.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = uranus.planet)
    
    # Rotation Radius Neptune
    radius_neptune = 150
    # Rotate Neptune X
    neptune.planet.x = math.cos(t / 164.8) * radius_neptune
    # Rotate Neptune Z
    neptune.planet.z = math.sin(t / 164.8) * radius_neptune
    # Relative Neptune
    neptune.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = neptune.planet)
    
    # Rotation Radius Proteus
    radius_proteus = 5
    # Rotate Proteus X
    proteus.planet.x = math.cos(t / 1.122315) * radius_proteus + neptune.planet.x
    # Rotate Proteus Z
    proteus.planet.z = math.sin(t / 1.122315) * radius_proteus + neptune.planet.z
    # Relative Proteus
    proteus.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = neptune.planet)

    # Rotation Radius Triton
    radius_triton = 9
    # Rotate Triton X
    triton.planet.x = math.cos(t / -5.876854) * radius_triton + neptune.planet.x
    # Rotate Triton Z
    triton.planet.z = math.sin(t / -5.876854) * radius_triton + neptune.planet.z
    # Relative Triton
    triton.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = neptune.planet)

    # Rotation Radius Nereid
    radius_nereid = 35
    # Rotate Nereid X
    nereid.planet.x = math.cos(t / 360.13619) * radius_nereid - 26.3 + neptune.planet.x
    # Rotate Nereid Z
    nereid.planet.z = math.sin(t / 360.13619) * 23.1 + neptune.planet.z
    # Relative Nereid
    nereid.planet.rotate(Vec3(0, 1, 0) * -2, relative_to = neptune.planet)
    
    # Rotation Radius Pluto
    radius_pluto = 180
    # Rotate Pluto X
    pluto.planet.x = math.cos(t / 248.0) * radius_pluto
    # Rotate Pluto Z
    pluto.planet.z = math.sin(t / 248.0) * radius_pluto
    # Relative Pluto
    pluto.planet.rotate(Vec3(0, 1, 0) * 2, relative_to = pluto.planet)

# Reference/Citation: https://stackoverflow.com/questions/68065745/left-click-detection-with-ursina, https://www.ursinaengine.org/faq.html  
# Keyboard Movement 
    # Conditional 'd' Key
    if (held_keys['d']):
        # 1.0 Move Right
        camera.position += Vec3(1.0, 0, 0)
    # Conditional 'w' Key
    elif (held_keys['w']):
        # 1.0 Move Forward
        camera.position += Vec3(0, 0, 1.0)
    # Conditional 's' Key
    elif (held_keys['s']):
        # 1.0 Move Backward
        camera.position += Vec3(0, 0, -1.0)
    # Conditional 'a' Key
    elif (held_keys['a']):
        # 1.0 Move Left
        camera.position += Vec3(-1.0, 0, 0) 

    # Conditional 'e' Key
    elif (held_keys['e']):
        # 1.0 Move Up
        camera.position += Vec3(0, 1.0, 0)
    # Conditional 'q' Key
    elif (held_keys['q']):
        # 1.0 Move Down
        camera.position += Vec3(0, -1.0, 0)
          
    # Conditional 'r' Key 
    elif (held_keys['r']):
        # Origin Position
        camera.position = Vec3(0, 0, 0)
        # Origin Rotation
        camera.rotation = Vec3(0, 0, 0)

    # Conditional 'up arrow' Key 
    elif (held_keys['up arrow']):
        # 1.0 Rotate Up
        camera.rotation += Vec3(1.0, 0, 0)
    # Conditional 'down arrow' Key 
    elif (held_keys['down arrow']):
        # 1.0 Rotate Down
        camera.rotation += Vec3(-1.0, 0, 0)
    # Conditional 'left arrow' Key 
    elif (held_keys['left arrow']):
        # 1.0 Rotate Left
        camera.rotation += Vec3(0, 1.0, 0)
    # Conditional 'right arrow' Key 
    elif (held_keys['right arrow']):
        # 1.0 Rotate Right
        camera.rotation += Vec3(0, -1.0, 0)

    # Conditional 'mouse' Key
    elif (mouse.moving == True):
        # Reference/Citation: https://www.ursinaengine.org/api_reference.html#mouse
        # Delta Mouse Movement 
        camera.rotation += Vec3(mouse.delta.y * 5, mouse.delta.x * 5, 0)

    # Print Camera Rotation Coordinates
    print(camera.rotation)
    # Print Camera Position Coordinates
    print(camera.position)

# Reference/Citation: https://www.ursinaengine.org/api_reference.html#input_handler
# Input Function
def input(key):
    # Conditional 'escape' Key
    if key == 'escape':
        # Iterate in Trail Renderer List
        for e in trail_renderers:
            # Disable Trails
            e.enabled = not e.enabled
    # Conditional 'f' Key
    elif key == 'f':
        # Mute Audio
        a.pause()
    # Conditional 'o' Key
    elif key == 'o':
        # Resume Audio
        a.resume()

# Call Update Function 
update()

# Reference/Citation: https://www.ursinaengine.org/api_reference.html#EditorCamera
# Camera
camera = EditorCamera()

# Launch Application
app.run()
