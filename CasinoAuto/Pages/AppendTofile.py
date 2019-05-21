
def appendtofile(self,k,string):

    if(k==1):
        with open('bugreport_livecasino.txt', 'a') as wf:
            wf.write('Starting:')