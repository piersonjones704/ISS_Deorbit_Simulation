initial_altitude = 130
x_initial_velocity = 7800
y_initial_velocity = 0

def unit_converter_initialaltitude(initial_altitude = 130, input_unit = 'km', output_unit = 'm'):
    unit_conversion = initial_altitude_conversion_process(initial_altitude, input_unit, output_unit)
    y0 = unit_conversion
    return(y0) 
    

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
        y = y * 10**(-2)
    return y

if __name__ == '__main__':
    unit_converter_initialaltitude()