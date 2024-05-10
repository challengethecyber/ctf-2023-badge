uf2 created from
 - circuitpython base
 - duckyfs files added on top of it
 - filesystem renamed (in windows) to DUCKY

then ran:
# sudo picotool save -a -f -t uf2 ducky.uf2

to load it onto another ducky:
# sudo picotool load ducky.uf2 
