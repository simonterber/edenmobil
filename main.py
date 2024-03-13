#!/usr/bin/env pybricks-micropython


# E D E N M O B I L
#
# Entwicklung: Simon Terber, Paul Truger, Lukas Mertz
#
# Ziele:
# - Linien fahren und Farben zum Abbiegen nutzen
# - Treppen fahren bei Ankunft an Zielfarbe
# - Ziele werden per Sprache ausgegeben
# - Roboter informiert über Probleme, Sprachausgabe


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, TouchSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait, DataLog, StopWatch
# Bei den pybricks.tools gibt es eine Möglichkeit zum Daten-Logging
# Dies wird hier importiert und im Programm werden die Sensordaten von
# Abstandssensor (falls installiert) und ColorSensor mitgeloggt, um den
# Weg zurückzuverfolgen
# Hier anzuknüpfen ist eine Aufgabe für die Zukunft des Projekts
from pybricks.media.ev3dev import Font, SoundFile

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialisieren des DataLog
data = DataLog('richtung', 'zeit')
watch = StopWatch() # Stopuhr für die gefahrene Zeit in einer Richtung


# FRONTMOTOREN
# Hier wird mit einer Drivebase gearbeitet
# Die DriveBase ermöglicht eine einfache Lenkung
# Evtl. muss die Lenkung zu einer Differentiallenkung umgebaut werden, wenn
# der Roboter mehr ins Gelände fährt.

# Motoren aus Klasse Motor erstellen
LinkerMotor = Motor(Port.D)
RechterMotor = Motor(Port.A)

# Fahrgestell/ Drivebase
robot = DriveBase(LinkerMotor, RechterMotor, wheel_diameter=55.5, axle_track=104)


# HECKMOTOR EINSTELLUNGEN
# direction to counterclockwise, so that positive speed values make the
# robot move forward.
HeckMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Configure the lift motor, which lifts the rear structure.  It has an
# 8-tooth, a 24-tooth, and a 40-tooth gear connected to it.  Set the
# motor direction to counterclockwise, so that positive speed values
# make the rear structure move upward.
LiftMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 24, 40])


# DER GYROSENSOR WURDE FÜR DIESES MODELL AUSGEPLANT
# Set up the Gyro Sensor.  It is used to measure the angle of the robot.
# Keep the Gyro Sensor and EV3 steady when connecting the cable and
# during start-up of the EV3.
# gyro_sensor = GyroSensor(Port.S2)

# Set up the Touch Sensor.  It is used to detect when the rear
# structure has moved to its maximum position.
BeruehrungsSensor = TouchSensor(Port.S1)

# Einstellungen zum Display
big_font = Font(size=24)
ev3.screen.set_font(big_font)

# Initialize the rear structure.  In order to move the structure both
# the rear motor and lift motor must run in sync.  First, the rear
# motor moves the robot backward while the lift motor moves the rear
# structure up until the Touch Sensor is pressed.  Second, the rear
# motor moves the robot forward while the lift motor moves the rear
# structure down for a set amount of degrees to move to its starting
# position.  Finally, the lift motor resets the angle to "0."  This
# means that when it moves to "0" later on, it returns to this starting
# position.

# Hier werden Heck und Lift-Motoren kurz betätigt

HeckMotor.dc(-20)
LiftMotor.dc(100)
while not BeruehrungsSensor.pressed():
    wait(10)
LiftMotor.dc(-100)
HeckMotor.dc(40)
wait(50)
LiftMotor.run_angle(-145, 510)
HeckMotor.hold()
LiftMotor.run_angle(-30, 44)
LiftMotor.reset_angle(0)
# gyro_sensor.reset_angle(0)

# Initialize the steps variable to 0.
steps = 0



# TREPPE HOCHFAHREN

def TreppeFahren():
    robot.stop()




# HAUPTPROGRAMM

while True:
    
    # LINIE FAHREN MIT REAKTION AUF FARBEN
    
    # Hier Änderungen von Paul Truger
    
    # DIES LOGGT ZEIT UND RICHTUNG IN EINER CSV Datei auf dem BRICK
    #richtung = 'rechts'
    #zeit = watch.time()
    #data.log(richtung, zeit)
    
    
    
    
    
    
    # Display the steps variable on the screen.
    #ev3.screen.clear()
    #ev3.screen.draw_text(70, 50, steps)
    #wait(200)

    # Wait until any Brick Button is pressed.
    #while not any(ev3.buttons.pressed()):
        #wait(10)

    # Check whether Up Button is pressed, and increase the steps
    # variable by 1 if it is.
    #if Button.UP in ev3.buttons.pressed():
        #steps += 1

    # Check whether Down Button is pressed, and decrease the steps
    # variable by 1 if it is.
    #elif Button.DOWN in ev3.buttons.pressed():
       # steps -= 1
        # Make sure the steps variable is not a negative number.
        #if steps < 0:
        #    steps = 0

    # If the Center Button is pressed, break out of the loop.
    #elif Button.CENTER in ev3.buttons.pressed():
    #    break

# This loop climbs the stairs for the amount of steps specified in the
# steps variable.  It repeats until the steps variable is 0.
#while steps > 0:

    # Run the front and rear motors so the robot moves forward.
    #robot.straight(100)
    #HeckMotor.dc(90)

    # Keep moving until the robot is at an angle of at least 10 degrees.
    #while gyro_sensor.angle() < 10:
    #    wait(10)

    # Run the lift motor to move the rear structure up, while
    # simultaneously running the front and rear motors.
    #LiftMotor.dc(90)
    #robot.straight(30)
    #HeckMotor.dc(15)

    # Keep moving the rear structure up until the Touch Sensor is
    # pressed, or the robot is at an angle of less than -3 degrees.
    #while not touch_sensor.pressed():
    #    if gyro_sensor.angle() < -3:
    #        break
    #    wait(10)
    #LiftMotor.hold()

    # Move the robot forward for some time using the front and rear
    # motors.
    #robot.straight(60)
    #HeckMotor.dc(100)
    #wait(1300)

    # Play a sound and pull the rear structure up so it gets back to
    # its starting position.  Keep moving forward slowly by
    # simultaneously running the front and rear motors.
    #ev3.speaker.play_file(SoundFile.AIR_RELEASE)
    #robot.straight(30)
    #HeckMotor.dc(30)
    #LiftMotor.run_target(160, 0)

    # Update the "steps" variable and display it on the screen.
    #steps -= 1
    #ev3.screen.clear()
    #ev3.screen.draw_text(70, 50, steps)

# Settle the robot at the top of a step and end the program.
#robot.straight(100)
#HeckMotor.dc(90)
#wait(2000)
#robot.stop()
#HeckMotor.hold()
#wait(5000)
