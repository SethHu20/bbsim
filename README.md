# bbsim
CS50 BigBoard Speller Simulation Python Script

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
