# Ideas.md

* Output 
  * Be able to split GPX files into multiple runs.
    * For example, split a run into first five minutes, last five minutes to remove walking and the middle is the run itself.

* If the time of a run is near a whole minute, round it to nearest minute for better graphing.
* Analyse times and see where time has changed, but GPS does not. 
  * This will show stale movement
  * Can use this date to determine stopping
  * If this is only for a few seconds, try and work out if the user is changing direction
    * For example, running to a point, and turning 180 degrees and running back to the start.

* Calories burned formula that accurately depics calories burned
  * Get the difference from what the person would normally use in that hour / minute 
    * Get data from person such as TDEE, BMR, other calculators
    * Can calculate the difference between running and BMR to show how much extra the excercise provided in the same amount of time

* Create a distance / unit measurement class
  * Better conversions such as MilesToKM, GPSCoordinates->KM

* Create a wrapper for Strave
  * Can get all runs from a person
  * can analyse data points
  * can graph and otherwise display data
  
* Get weather for the time and day and area the user was running based on their initual GPS starting position
  * Maybe try and see if the user changes city / area, show nultiple weather reports

* Support CSV, JSON, SQLite, etc for data storage, input and output, and not just GPX files.