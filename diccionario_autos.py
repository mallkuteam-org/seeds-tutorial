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

    fun = {'marca': 'Susuki',
     'modelo': 'Fun',
     'year': 2015,
     'asientos': 4,
     'puertas': 3}

    autos = [focus, corsa, fun]

    for auto in autos:
        print(auto['marca'])

if  __name__ == '__main__':
    main()
