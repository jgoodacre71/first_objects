class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
            print ""
            
class Bassist(Musician):
    def __init__(self):
        super(Bassist,self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super(Guitarist,self).__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        super(Drummer,self).__init__(["1...2...3...4", "Combusting"])
        
class Band:
    def __init__(self):
        self.names = []
    
    def hire(self,Musician):
        self.names.append(Musician)
    
    def fire(self,Musician):
        if Musician in self.names:
            self.names.remove(Musician)
                   
    def play(self):
        for Musician in self.names:
                if Musician.__class__.__name__=="Drummer":
                    Musician.solo(1)
                    is_drummer = True
                    break
        if is_drummer:
            for Musician in self.names:
                Musician.solo(3)

nigel = Guitarist()
nara = Guitarist()
dave = Drummer()
johan = Guitarist()

brass = Band()
brass.hire(nara)
brass.hire(dave)
brass.hire(nigel)
brass.fire(nara)
brass.hire(johan)
brass.play()