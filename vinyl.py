# This class saves set parameters and prints out the results upon call
class VinylTrackz():
    
    # This categorizes the data
    def __init__(self, artist, tit, stock, pric, itemer):
        self.artist = artist
        self.title = tit
        self.stock = stock
        self.price = pric
        self.itemNum = itemer
    
    # This prints stuff 
    def __str__(self):
        return (f'Record Store Item {self.itemNum}:\nArtist: {self.artist}\nTitle: {self.title}'
                + f'\nStock: {self.stock}\nPrice: ${self.price}')
