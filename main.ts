basic.forever(function on_forever() {
    maqueen.servoRun(maqueen.Servos.S1, 0)
    basic.pause(2000)
    maqueen.servoRun(maqueen.Servos.S1, 150)
    basic.pause(2000)
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
})
