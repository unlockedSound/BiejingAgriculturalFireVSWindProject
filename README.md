# BeijingAgriculturalFireVSWindProject

These files comprise many of the scripts and text files that made up my undergraduate thesis project. More digging and a lot of clean up is needed for this to be fluid and run how I want it to but I thought it better to put up instead of just sitting on my hands.

To slate the basics: the goal was to take fire data from Landsat's Active Fire Data and local weather station data around Beijing. Using Beijing as a center point an area was defined for research. The weather stations were used to create equidistant areas within the research area. The assumption was made that a fire within the weather stations area are effected by said station's weather condition.

Most of the work involved cleaning data and determining methodology for answering the question "Does agricultural biomass burning likely influence Beijing air quality"

The key file for this is windDirectionVSFire.py which takes each individual fire, draws a line to Beijing and compares this angle to the azimuth of the wind in relevent weather zone. If the azimuth is within a certain range of the fire's angle the case is marked as true, fire likely contibutor to air quality, otherwise false, fire not likely contriubutor to air quality.

This project was my senior undergraduate thesis at University of Maryland for the Geography Department. While there is a story behind it special thanks to Dr. Tatiana Loboda for acting as my advisor and teacher and working through this with me. She offered input, thoughts, excitement, and was always happy to chat, meet, and hit her head against the problem right alongside me. It was, without a question, the best experience of a 5.5 year long journey through undergrad.
