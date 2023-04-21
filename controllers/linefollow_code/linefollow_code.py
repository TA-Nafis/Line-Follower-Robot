from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

time_step = 32
max_speed = 5

last_error=I=D=P=error=0

kp=1.4
ki=0
kd=0.1

#motor

wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

#IR sensor

ds = []
dsNames = ['Right','Mid', 'Left']
for i in range(3):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(time_step)

#mainloop

while robot.step(time_step) != -1:
    
    right_ir_val=ds[0].getValue()
    mid_ir_value=ds[1].getValue()
    left_ir_value=ds[2].getValue()
    print("left: {0}, middle: {1}, right: {2}".format(left_ir_value,mid_ir_value,right_ir_val))
    
    if left_ir_value < 425 and right_ir_val < 425 and mid_ir_value >= 835:
        error=0

    elif left_ir_value < 425 and right_ir_val >= 425 and mid_ir_value >= 835:
        error=-1

    elif left_ir_value >= 425 and right_ir_val < 425 and mid_ir_value >= 835:
        error=1

    elif left_ir_value >= 425 and right_ir_val < 425 and mid_ir_value < 835:
        error=2

    elif left_ir_value < 425 and right_ir_val >= 425 and mid_ir_value < 835:
        error=-2


    P=error
    I=error+I
    D=error-last_error
    balance=int((kp*P)+(ki*I)+(kd*D))
    last_error=error   
    
    left_Speed=max_speed-balance
    right_Speed=max_speed+balance
    

    if left_Speed> max_speed :
        wheels[0].setVelocity(left_Speed)
        wheels[1].setVelocity(0)
        wheels[2].setVelocity(left_Speed)
        wheels[3].setVelocity(0)
        
    if right_Speed> max_speed :
        wheels[0].setVelocity(0)
        wheels[1].setVelocity(right_Speed)
        wheels[2].setVelocity(0)
        wheels[3].setVelocity(right_Speed) 
         
    if left_Speed < 0:
        wheels[0].setVelocity(0)
        wheels[1].setVelocity(right_Speed)
        wheels[2].setVelocity(0)
        wheels[3].setVelocity(right_Speed)
        
    if right_Speed < 0:
        wheels[0].setVelocity(left_Speed)
        wheels[1].setVelocity(0)
        wheels[2].setVelocity(left_Speed)
        wheels[3].setVelocity(0)
        
    if left_Speed ==  max_speed:
        wheels[0].setVelocity(left_Speed)
        wheels[1].setVelocity(right_Speed)
        wheels[2].setVelocity(left_Speed)
        wheels[3].setVelocity(right_Speed)
     
    if right_Speed ==  max_speed:
        wheels[0].setVelocity(left_Speed)
        wheels[1].setVelocity(right_Speed)
        wheels[2].setVelocity(left_Speed)
        wheels[3].setVelocity(right_Speed)    
        
    pass