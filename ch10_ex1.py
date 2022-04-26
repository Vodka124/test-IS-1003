# This imports the class over yonder
import vinyl

# This saves various info to the class and from, then calls it to print
def get_info():
    one = vinyl.VinylTrackz('Arctic Monkeys','AM',12,17.79,1)
    two = vinyl.VinylTrackz('Lana Del Rey','Born To Die',21,16.62,2)
    thri = vinyl.VinylTrackz('Neutral Milk Hotel','In The Aeroplane Over the Sea',1,14.99,3)
    four = vinyl.VinylTrackz('Bon Iver','For Emma, Forever Ago',5,19.01,4)
    phi = vinyl.VinylTrackz('Pixies','Doolittle',13,23.98,5)
    
    print(f'{one}\n\n{two}\n\n{thri}\n\n{four}\n\n{phi}')

# This thing sets it all in motion!
get_info()
