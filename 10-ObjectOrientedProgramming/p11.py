class TV():
    def __init__(self,is_on):
        self.is_on = is_on
    def off(self):
        self.is_on = False
    def on(self):
        self.is_on = True
    def show_status(self):
        if self.is_on == True:
            return 'TV jest on'
        elif self.is_on == False:
            return 'TV is off'
tv = TV(False)

print(tv.show_status())
tv.on()
print(tv.show_status())
tv.off()
print(tv.show_status())
