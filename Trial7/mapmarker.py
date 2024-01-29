from kivy_garden.mapview import MapMarkerPopup
from locationpopup import LocationPopUp

class MapMarker(MapMarkerPopup):
   
    def on_release(self):
        menu=LocationPopUp(self.market_data)
        menu.open()
        
