class Romb:
    def __setattr__(self, name, value):
        if name == "side_a":
            if value > 0:
                self.__dict__["side_a"] = value
            else:
                print("Error: side must be > 0")

        if name == "angle_a":
            if value > 0 and value < 180:
                self.__dict__["angle_a"] = value
                self.__dict__["angle_b"] = 180 - value
            else:
                print("Error: angle must be 0 - 180")


romb = Romb()
romb.side_a = 5
romb.angle_a = 60

print("side_a:", romb.side_a)
print("angle_a:", romb.angle_a)
print("angle_b:", romb.angle_b)