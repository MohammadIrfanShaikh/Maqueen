def on_forever():
    maqueen.servo_run(maqueen.Servos.S1, 0)
    basic.pause(2000)
    maqueen.servo_run(maqueen.Servos.S1, 150)
    basic.pause(2000)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
basic.forever(on_forever)
