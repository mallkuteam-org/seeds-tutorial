def main():
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

    camioneta = {'marca': 'Ford',
     'modelo': 'F100',
     'year': 2018,
     'asientos': 2,
     'puertas': 2}

    autos = [focus, corsa, camioneta]

    for auto in autos:
        print(auto['marca'])

if  __name__ == '__main__':
    main()
