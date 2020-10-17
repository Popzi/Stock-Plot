# Stock plot

This was written in the course Business Intelligence.
The task was to analyze a dataset and fix data errors to get a nice plot of a stock.


I must warn that this script is not the best example of following standard naming conventions but I will blame it on being a student and not knowing better :-)

### Run the script
Steps to get this Lab up and running:


1) 
   - Extract the textfiles to a subdirectory called "Data"

2)
   - Run the stock.py python file (in visual code or cmd)
	*NOTE*: Required python modules; os, pandas and matplotlib

3)
   - The python file should drop a file called NordeaNordenfond.csv in the scripts folder and display a plot while running.
	(You can save this image from the plot window)


-> After this if the stock.py is run again it will use existing data from NordeaNordenfond.csv instead of collecting it again.



In the datasets one quarter seems to be missing Nordea nordenfond, in the stock.py there is a if 
statement checking if we recieve the specific date then we just skip that collection step in 
the dataset (the dataset 2014-06-30 is missing Nordea nordenfonden).

# Remember

  - This was a school assignment during my time studying IT-Security and Software testing - this is not guaranteed to work 100%.
  - Do not copy and use this in your school assignments, instead learn from it and improve it.
  - This will not be maintained by me, this is uploaded for safekeeping online.

License
----

MIT


**Free Software, Hell Yeah!**
