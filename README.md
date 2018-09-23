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

energies in MeV, Q=19.81MeV.

The method still needs extensive testing but at least it is conserving
energy. More updates will be made but probably in a fork or another
repo.
