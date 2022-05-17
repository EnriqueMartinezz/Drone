from djitellopy import tello
from time import sleep

drone = tello.Tello()

drone.connect()
print(drone.get_battery())

# take off to the height of 200cm
 drone.takeoff()
 drone.move_up(120)

#Move forward 480 and rotate counter_clockwise 90
 drone.move_forward(480)
 sleep(.5)

drone.rotate_counter_clockwise(90)
sleep(.5)

#Move forward 280 and rotate counter_clockwise 90
drone.move_forward(280)
sleep(.5)

drone.rotate_counter_clockwise(90)
sleep(.5)

#Move forward 480 and rotate counter_clockwise 90
drone.move_forward(480)
sleep(.5)

drone.rotate_counter_clockwise(90)
sleep(.5)

#Move forward 280 and rotate counter_clockwise 90
drone.move_forward(280)
sleep(.5)

drone.rotate_counter_clockwise(90)
sleep(.5)

#land
drone.land()
