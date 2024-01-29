from kivymd.uix.dialog import MDDialog



class LocationPopUp(MDDialog):
    def __init__(self,market_data):
        super(). __init__()
        self.name=str(market_data[1])
        self.y=str(market_data[4])
        self.x=str(market_data[5])
        self.title="Reference Marks"
        
        self.text='Name:{}\nY:{}\nX:{}'.format(self.name,self.y,self.x)

        
     
