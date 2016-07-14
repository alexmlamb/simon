# simon
Simple Experiment Manager

Simon is designed to be a super lightweight and nearly invisible tool for helping to organize experiment results and configuration.  

Currently it works like this: 

1.  Every time you start an experiment, Simon creates a results directory for that experiment.   
2.  Simon looks up and saves the current commit of the git repository.  
3.  Simon makes it so that "print" statements are printed to standard out and also saved to a log file.  
4.  Simon lets you write to the log file without printing to standard out.  

I made this package because I usually end up rewriting these pieces of code for every machine learning project that I do.  
