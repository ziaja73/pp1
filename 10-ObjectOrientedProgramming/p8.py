class Phone():
    def __init__(self,model,cena,pamiec):
        self.model = model
        self.cena = cena
        self.pamiec = pamiec
        self.state = "on"
        self.current_vol = 5
    def off(self):
        self.state = 'off'
    def on(self):
        self.state = 'on'
    def vol_up(self):
        self.current_vol =+1
    def vol_down(self):
        self.current_vol -=1

phone = Phone('s20', 3000, 128)
print(phone.pamiec)
phone.vol_down()
print(phone.current_vol)
