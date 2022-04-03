class clockTime:
    #Constructor
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    #Function to set Hours
    def setHours(self, hours):
        self.hours = hours
    #Function to set Minutes
    def setMinutes(self,minutes):
        self.minutes = minutes
    #Function to set Seconds
    def setSeconds(self,seconds):
        self.seconds = seconds
    #Function to set Time
    def setTime(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    #Function to display Time
    def showTime(self):
        print("Time: " + str(self.hours) + ":" +str(self.minutes) + ":" + str(self.seconds))

hours = int(input("Enter hours value: "))
minutes = int(input("Enter minutes value: "))
seconds = int(input("Enter seconds value: "))
objectclockTime = clockTime()
objectclockTime.setTime(hours, minutes, seconds)
objectclockTime.showTime()
    
    