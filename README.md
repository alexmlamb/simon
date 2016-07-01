# simon
Simple Experiment Manager

Ideas: 

0.  Simon is initialized with a base directory.  
1.  For each experiment, creates a new directory, named using both the time of experiment creation and (optionally) an additional name.  
2.  Gives a function for logging.  These logged values are randomly printed at a constant rate, and all stored to a logfile.
3.  User can request the experiment directory name.  
4.  Saving/loading capability?  Should it help with loading model file for past experiment?  Maybe have some capability for this.  

import simon

mysimon = simon("/tmp/", name = "mytest")

for i in range(0,100000):
  mysimon.log(i)
  
print mysimon.dir
#/tmp/20150101_mytest/

