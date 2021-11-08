

focus = {'marca': 'Ford',
 'modelo': 'Focus',
 'year': 2017,
 'asientos': 4,
 'puertas': 4}

corsa = {'marca': 'Chevrolet',
 'modelo': 'Corsa',
 'year': 2017,
 'asientos': 2,
 'puertas': 2}

autos = [focus, corsa]

for auto in autos:
    print(auto['marca'])
