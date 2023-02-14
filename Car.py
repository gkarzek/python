#This is a comment
print("Gozde Karzek 02/13/2023")

class Car:
    def __init__(self, name):
        self.name = name

    def go(self):
        print("The " +self.name + " is moving.")

    def stop(self):
        print("The " + self.name + " is stoping.")
   
    def fly(self):
        print("The " +self.name + " is flying.")
        

def main():
    car1 = Car("Chevy")
    car1.go()
    car1.stop()
    car2 = Car("Kia")
    car2.go()
    car2.stop()
    car3= Car("BMW")
    car3.fly()
    car3.stop()
    

if __name__ == "__main__":
  main()