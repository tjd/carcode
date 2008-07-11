
def onVisit(obj,  col_evt):
    # When the car collisiones with a road part we consider
    # that part visited and disable collision tests for it
    if not obj.visited:
        obj.visited = True
        obj.collisionable = False

def onFinish(obj,  col_evt):
    # Triggered when car reaches finish line
    # check if the player has visited all the 4 road sections
    if road1.visited and road2.visited and road3.visited and road4.visited:
        Console.clear()
        Console.write('Finished!')
    else:
        Console.write('Did not visit all the paths')
        
# Create the road using boxes
road1 = Box((0, 0),  (500,  30), (0.4,0.4,0.4),  True)
road2 = Box((500, 0),  (30,  500), (0.4,0.4,0.4),  True)
road3 = Box((0, 470),  (500,  30), (0.4,0.4,0.4),  True)
road4 = Box((0, 0),  (30,  500), (0.4,0.4,0.4),  True)

# Subscribe callback onVisit to collision event for all boxes
road1.evt_collision.subscribe(onVisit)
road2.evt_collision.subscribe(onVisit)
road3.evt_collision.subscribe(onVisit)
road4.evt_collision.subscribe(onVisit)

# Create a finish line with a box
finish = Box((0,  35), (30,  20),  (0.0,  0.0,  1.0,  0.5),  True)
finish.evt_collision.subscribe(onFinish)

# Set visited to false for all road parts
road1.visited = False
road2.visited = False
road3.visited = False
road4.visited = False

# Add all entities to Arena
Arena.add_entity(road1)
Arena.add_entity(road2)
Arena.add_entity(road3)
Arena.add_entity(road4)
Arena.add_entity(finish)

# Create a pair of sensors to guide the car
blacksensor1 = ColorSensor(24, 12, (0, 0, 0))
blacksensor2 = ColorSensor(24, -12, (0, 0, 0))

# Cet the car object
car = Arena.get_car()

# Add the sensors to the car
car.add_sensor("fl_sensor", blacksensor1)
car.add_sensor("fr_sensor", blacksensor2)
