import random
import os
import glob

file = glob.glob('/home/roy/ASCII-Art-Splash-Screen/art/*.txt')
word = glob.glob('/home/roy/ASCII-Art-Splash-Screen/word/*.txt')
i = random.randrange(len(file)) 
os.system("cat " +  file[i])
os.system("cat " +  word[0])
