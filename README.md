# bootstrap_to_csv
converts a bootstrap.dat file into a CSV file.  Currently set up for btc .dat file, but you can change the variable names if you use a different chain


To run, just use the command line function:
python /python/sight.py /python/bootstrap.dat > bootstrap.csv

where bootstrap.dat is your block file (just all of your blocks concatenated (ie: cat blk000*.dat > bootstrap.dat), you may have to change some settings on your full node to get it to keep all of the blocks)

And shout out to Alex Gorale, who did all the hard work of mapping out the bootstrap.dat file
