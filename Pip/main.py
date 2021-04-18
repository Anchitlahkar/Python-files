class Cars(object):
    def __init__(this, name, model, color, company, speed=None):
        this.name = name
        this.model = model
        this.color = color
        this.company = company
        this.speed = speed or {}

    def start(this):
        print("\n\n"+this.name + ": Started")
        speed = this.speed["Started"]
        print('Speed mi/h: ', speed, '\n\n')

    def stop(this):
        print("\n\n"+this.name + ": Stoped")
        speed = this.speed["Stop"]
        print('Speed mi/h: ', speed, '\n\n')

    def accelarate(this):
        print("\n\n"+this.name + ": accelarating...")
        speed = this.speed["minSpeed"]
        print('Speed mi/h: ', speed, '\n\n')

    def fullAccelarate(this):
        print("\n\n"+this.name + ": Max accelarating...")
        speed = this.speed["maxSpeed"]
        print('Speed mi/h: ', speed, '\n\n')

    def changeGear(this, gear):
        print("\n\n"+this.name + ": Gear Changing...")
        gear = gear + 2
        str(gear)
        print("Gear: " + gear)


BugattiChiron = Cars("BugattiChiron", "Chiron", "Black-Blue", "Bugatti",
                     {"Started": 1, "minSpeed": 12, "maxSpeed": 418, "Stop": 0})

BatMobile = Cars("BatMobile", "GX8", "Black",
                 "Wayn", {"Started": 1, "minSpeed": 30, "maxSpeed": 450, "Stop": 0})



car = input("Please Enter You Car Name\n")
command = input("\nPlease enter Commands\n")



if car == 'BugattiChiron':
        if command == "start":
            print(BugattiChiron.start())

        if command == "end":
            print(BugattiChiron.stop())

        if command == "increaseSpeed":
            print(BugattiChiron.accelarate())

        if command == "maxSpeed":
            print(BugattiChiron.fullAccelarate())

        if command == "changeGear":
            print(BugattiChiron.changeGear(1))

        if command == "color":
            print("\nColor: "+ BugattiChiron.color)

        if command == "model":
            print("\nModel: "+ BugattiChiron.model)

        if command == "Company":
            print("\nCompany: "+ BugattiChiron.company)

        if command == "speed":
            print("\nSpeed: "+ BugattiChiron.speed)

        if command == "exit":
            exit()



if car == 'BatMobile':
    while True:
        if command == "start":
            print(BatMobile.start())

        if command == "end":
            print(BatMobile.stop())

        if command == "increaseSpeed":
            print(BatMobile.accelarate())

        if command == "maxSpeed":
            print(BatMobile.fullAccelarate())

        if command == "changeGear":
            print(BatMobile.changeGear(1))

        if command == "color":
            print("\nColor: "+ BatMobile.color)

        if command == "model":
            print("\nModel: "+ BatMobile.model)

        if command == "Company":
            print("\nCompany: "+ BatMobile.company)

        if command == "speed":
            print("\nSpeed: "+ BatMobile.speed)

        if command == "exit":
            exit()
