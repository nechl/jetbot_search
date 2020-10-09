from traitlets import HasTraits, Unicode, Bool, observe, Int
from jetbot import Robot
import time
import outsourcing_nechl
from random import randint as rn

class NechlBot(Robot):
    def __init__(self, *args, **kwargs):
        """ Initialize the Emobot class
    
        The settings have been empirically set by executing 10 spins. 
        Be aware that these settings might differ from JetBot to JetBot as no two motors are exactly the same.
        Therefore all units have to be considered as approximations.
        """
        super(NechlBot, self).__init__(*args, **kwargs)
        self.rotation_speed = 0.3
        self.rotation_time_1_degree = 2.39 / 360
        self.max_degrees_sight = 80 # 160 / 2
        #self.right_motor.alpha = self.left_motor.alpha + 0.045

    searching_status = Bool(False)
    item_searching = Unicode()
    item_found = Bool(False)
    round_search = Int(0)
    
    @observe("searching_status")
    def searching_status_watcher(self, change):
        if change["old"] == False and change["new"] == True:
            self.searching_around()
            #self.round_search = self.round_search + 1
            #self.round_search = self.round_search % 130
            pass
        elif change['old'] == True and change['new'] == False:
            self.stop()


    def searching_around(self):
        if self.round_search <= 50:
            self.forward(0.3)
            time.sleep(0.001)
            self.round_search +=1
        elif self.round_search > 50:
            self.rotate_left(degree = 44)
            time.sleep(0.001)
            self.round_search +=1
        self.round_search %=60
        
            


    def rotate_left(self, degree=60):
        """ Rotate to the left by a specified margin 
                
        Input:
            degree: Amount of degrees the JetBot should turn
        """
        self.left(self.rotation_speed)
        time.sleep(self.rotation_time_1_degree * degree)
        self.stop()
    def rotate_right(self, degree=60):
        """ Rotate to the right by a specified margin 
        
        Input:
            degree: Amount of degrees the JetBot should turn
        """
        self.right(self.rotation_speed)
        time.sleep(self.rotation_time_1_degree * degree)
        self.stop()
    def avoid_ob(self):
        self.backward(0.3)
        time.sleep(0.1)
        self.rotate_left(22.5)