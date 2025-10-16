
initial_altitude = 130
x_initial_velocity = 7800
y_initial_velocity = 0

def unit_converter_initialaltitude(initial_altitude = 130, input_unit = 'km', output_unit = 'm'):
    unit_conversion = initial_altitude_conversion_process(initial_altitude, input_unit, output_unit)
    return(unit_conversion)

def initial_altitude_conversion_process(initial_altitude, input_unit, output_unit):
    y = initial_altitude
    if input_unit == 'km' and output_unit == 'm':
        y = y * 10**3
    elif input_unit == 'm' and output_unit == 'm':
        y = y
    elif input_unit == 'miles' and output_unit == 'm':
        y = y * 1609.344
    elif input_unit == 'ft' and output_unit == 'm':
        y = y * 0.3048
    elif input_unit == 'cm' and output_unit == 'm':
        y = y * 10*(-2)

def unit_converter_x_initial_velocity(x_initial_velocity = 7800, input_unit = 'km', output_unit = 'm'):
    unit_conversion = x_initial_velocity_conversion_process(x_initial_velocity, input_unit, output_unit)
    return(unit_conversion)

def x_initial_velocity_conversion_process(x_initial_velocity, input_unit, output_unit):
    vx = x_initial_velocity
    if input_unit == 'km' and output_unit == 'm':
        vx = vx * 10**3
    elif input_unit == 'm' and output_unit == 'm':
        vx = vx
    elif input_unit == 'miles' and output_unit == 'm':
        vx = vx * 1609.344
    elif input_unit == 'ft' and output_unit == 'm':
        vx = vx * 0.3048
    elif input_unit == 'cm' and output_unit == 'm':
        vx = vx * 10*(-2)