The article is out!!
Here is the link:

https://www.sif.it/riviste/sif/ncc/econtents/2018/041/05/article/33

I think I'll later upload the poster.

Just some personal testing for multifragmentation stuff. Before
running make sure you have python-numpy, python-matplotlib and
python-termcolor installed.

$ python helium6Example.py 

Runs a simple example involving 6He

The table that can be contructed (I'll automate it later) is:

|p angle |	p |	t1	| t2 |	sum-Q |
|--------|------|-------|----|------|
|-29.44	 | 8.70	| 9.95 | 28.81 |67.28 |
|-38.55	 | 3.91	| 13.38 | 30.16 |67.28|
|23.32	 | 10.81 |	28.04 |	8.60 |67.27 |
|36.76	 | 2.08	 | 30.45 |14.91 |67.26 |

energies are in MeV, Q=-19.81.

The method still needs extensive testing but at least it is conserving
energy. More updates will be made but probably in a fork or another
repo.

#Some important clarifications:

The article explicitly refers to the Ex=18.3 in 6He and the peak
associated with it in their plot is the 18.6 peak. If the program is
run using the Ex=18.3 instead of the 18.9, as it was done in the
previous table, then we get the following table:

|p angle |	p |	t1	| t2 |	sum-Q |
|--------|------|-------|----|------|
|-23.40	 | 12.19| 9.04 | 26.23 |67.29 |
|-38.89	 | 1.24	| 18.6  | 28.58 |67.24|
|19.32	 | 13.31 |	25.83 |	8.31 |67.27 |
|26.84	 | 0.69	 | 27.38 | 19.34 |67.22 |

An we can see, indeed that the 18 value appears as part of the t1
spectrum. Also there is a contribution to the first peak around 9 this
might be the reason the first peak looks so large, there are various
contributions from various channels (at least the mentioned 2).

I decided not to use the excitation in 6He of 18.3 in the article
mainly for 2 reasons:

1) Some previous version of the program was buggy and energy was not
being conserved properly. There was a 10% error and this was enough
for me to interpret the 18.6 peak in the t1 spectrum differently.

2) I was expecting 4 solutions and making the comparison from the
calculated values to the peaks values in the t1 spectrum 2 fitted
nicely but the rest didn't.

Once the program was corrected (got 0.1% error), reason 2)
remained. Bear in mind that I only have the published images of the
used spectra, the 2 dimensional spectrums from the article seemed to
fit nicely with the Ex=18.9 so I decided to use that level as the
studied one.

After some discussion with the team (mainly with Dr. Cardella) it was
pointed out that even though those are the "regions" where the peaks
should be, we aren't saying anything about the probabilities (other
than 0 if it is energetically forbidden or !=0 in case it wasn't). The
height of those peaks (if any) might be under the background and
therefore not clearly visible in the spectrum.
