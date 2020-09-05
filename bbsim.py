import subprocess
import re
from statistics import mean, stdev
import sys

'''
BigBoard Simulation Python Script
version 1.0, 2020-09-05

by SethHu#2508, special thanks to by gfred#6558


Usage: python bbsim.py

command = for each run, the script will run the command once and reads from an
output file "ch.nd.txt", commands should have a format of:

    ./speller texts/aca.txt > ch.nd.txt

for multiline command (30 lines in total for CS50 BigBoard config), all commands
can be stored in a seperate file and run:

    bash [filename]

Make sure all output are appended into "ch.nd.txt", by default the command is set
to "bash batchscript", batchscript is available in the end of the script.

runs = how many runs are used to average out data, mean and standard deviation are
calculated

padding = just a value for output formatting
'''


command = "bash batchscript".split()  # default is bash batchscript, make sure the file is available

runs = 15  # Number of runs
p = padding = 7  # output formatting use

# Results is a 2d list
results = list()


# first row
print("run".ljust(p), "load".ljust(p), "check".ljust(p), "size".ljust(p), "unload".ljust(p), "TOTAL".ljust(p), "|")

for run in range(runs):

    # run command
    subprocess.run(command)
    r = open("ch.nd.txt", "r").read() # read output file with name ch.nd.txt

    # read using regex
    load   = sum(map(float, re.findall(r"TIME IN load: *([\d\.]+)", r)))
    check  = sum(map(float, re.findall(r"TIME IN check: *([\d\.]+)", r)))
    size   = sum(map(float, re.findall(r"TIME IN size: *([\d\.]+)", r)))
    unload = sum(map(float, re.findall(r"TIME IN unload: *([\d\.]+)", r)))
    total  = sum(map(float, re.findall(r"TIME IN TOTAL: *([\d\.]+)", r)))

    results.append((load, check, size, unload, total)) # append to final result

    print(str(run).ljust(p), # print formatting
          '{:.4}'.format(load).ljust(p),
          '{:.4}'.format(check).ljust(p),
          '{:.4}'.format(size).ljust(p),
          '{:.4}'.format(unload).ljust(p),
          '{:.4}'.format(total).ljust(p), "|")

if len(results) == 1: results.append(results[0])  # fail-safe for stdev in case of only 1 run

# print results
print("\nmean:".ljust(p+1),
      str(round(mean(res[0] for res in results), 4)).ljust(p),
      str(round(mean(res[1] for res in results), 4)).ljust(p),
      str(round(mean(res[2] for res in results), 4)).ljust(p),
      str(round(mean(res[3] for res in results), 4)).ljust(p),
      str(round(mean(res[4] for res in results), 4)).ljust(p),
      "\nstdev:".ljust(p+1),
      str(round(stdev(res[0] for res in results), 4)).ljust(p),
      str(round(stdev(res[1] for res in results), 4)).ljust(p),
      str(round(stdev(res[2] for res in results), 4)).ljust(p),
      str(round(stdev(res[3] for res in results), 4)).ljust(p),
      str(round(stdev(res[4] for res in results), 4)).ljust(p)
      )

''' batchscript for CS50 BigBoard below
./speller texts/aca.txt>ch.nd.txt
./speller texts/austen.txt>>ch.nd.txt
./speller texts/bible.txt>>ch.nd.txt
./speller texts/birdman.txt>>ch.nd.txt
./speller texts/burnett.txt>>ch.nd.txt
./speller texts/carroll.txt>>ch.nd.txt
./speller texts/cat.txt>>ch.nd.txt
./speller texts/constitution.txt>>ch.nd.txt
./speller texts/federalist.txt>>ch.nd.txt
./speller texts/frankenstein.txt>>ch.nd.txt
./speller texts/grimm.txt>>ch.nd.txt
./speller texts/her.txt>>ch.nd.txt
./speller texts/holmes.txt>>ch.nd.txt
./speller texts/homer.txt>>ch.nd.txt
./speller texts/koran.txt>>ch.nd.txt
./speller texts/lalaland.txt>>ch.nd.txt
./speller texts/mansfield.txt>>ch.nd.txt
./speller texts/pneumonoultramicroscopicsilicovolcanoconiosis.txt>>ch.nd.txt
./speller texts/revenant.txt>>ch.nd.txt
./speller texts/rinehart.txt>>ch.nd.txt
./speller texts/shakespeare.txt>>ch.nd.txt
./speller texts/stein.txt>>ch.nd.txt
./speller texts/stoker.txt>>ch.nd.txt
./speller texts/surgery.txt>>ch.nd.txt
./speller texts/tolstoy.txt>>ch.nd.txt
./speller texts/wells.txt>>ch.nd.txt
./speller texts/whittier.txt>>ch.nd.txt
./speller texts/wordsworth.txt>>ch.nd.txt
./speller texts/xueqin1.txt>>ch.nd.txt
./speller texts/xueqin2.txt>>ch.nd.txt
'''
