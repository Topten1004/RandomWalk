# random_walk
Random walk
Lecture and lab combo

Please submit all visuals as a figure per slide in a Powerpoint slide deck, arranged in a logical manner.

Random walk:

A.	Pick a region of interest that effectively bounds the ecological features you are interested in observing. Start with the central latitude and longitude within the region (what is the center point of your boundary box)? Using 10,000 points. From there, create a random walk that generates new latitude and longitude coordinates at a resolution that covers approximately 50% of a quadrant of your region. You may have to experiment with different changes in latitude and longitude to see the type of spatial coverage you are able to generate.

B.	Next, plot the point you generated on a map that is again bounded by your region of interest (provided the maximum and minimum latitude and longitude values). Produce the markers in a size that provides enough spatial awareness (i.e., can see enough of the basemap to orient ourselves) while also seeing the markers well. Finally, color the markers using a colorscale that is related to the physical properties of your parameter (i.e. what color is intuitive for your variable?). Complete your plot by adding all necessary labels (e.g. axes, title).

C.	The visuals for your random walk should be a) a plot of your generated random walk, and b) your random walk colored and superimposed on a basemap for your region of interest.

<<See coordinates file.>>

{
  •	Boundary box (latitude/longitude) coordinates at each corner.
  •	Central (latitude/longitude) coordinates are in the center of the box.
  •	Region of interest: coastal central CA from Santa Barbara south to Paradise Beach.
  •	Parameter of interest (physical properties): surface kelp canopy beds off of the coast, so a green for vegetation but to define the beds from the surrounding water.
  •	Land is to be used for points of reference if addressed at all.
  •	Degree/minute/second format for coordinates are in blue.
 
 
Region of interest: central coast of CA from Santa Cruz to Paradise Beach, focusing on kelp forest canopies.
}


Hawai’ian spectra:

D.	Using the ‘hawaii_svc.py’ as an example, you will randomly select 10 of the 90 files. Each file represents a station which, under ideal conditions, has a column of wavelength data (Var1), 
and 5 remotely-sensed reflectance (Rrs) spectra (Var2_1, Var2_2, etc.). In some cases, less Rrs data will be present due to outliers or user “issues”, or more spectra may be present due to an 
over-ambitious investigator. The spectra have been corrected by Phillipp Groetsch’s three component (3C) model, and thus have the majority of effects due to glint and skylight removed from the 
above-water spectra to calculate Rrs. Thus, the variability across these spectra is not due to sky or illumination variability.

Plot 10 different Hawaii spectra – pick random files by using a random generator to 	generate indices over the number of files present. Plot the mean of a solid line, and 	distribution as a 
shaded region, color of your choice.

•	The visuals for the Hawai'i SVC data can either be all figures on a single slide, or individual slides for each figure.

•	Focus on area marked with arrow. Section C is more of background info. The Hawaii spectra data is from the 10 csv files.

