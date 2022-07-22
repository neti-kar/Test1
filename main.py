class Car:
    wheels = 4
    doors = 4
    engine = 1
    color = 'white'

    def exclaim(self):
        return 'I am a car!'


audi = Car()
bmw = Car()
vw = Car()
vw.color = 'black'
bmw.color = 'red'

print(audi.exclaim())
print(f'I have {audi.engine} engine, {bmw.wheels} wheels and {vw.doors} doors' )
print(audi.color, vw.color, bmw.color)