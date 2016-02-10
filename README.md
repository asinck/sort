The two programs here are my implementation of a couple sorting algorithms (merge and quicksort), along with ten data files that these programs were run on. The data files are just lists of random integers.

The purpose of this program was to collect stats on the time it took each algorithm to sort random data (in this case, integers), for my stats class. This is why the data files are included; my team needs consistent data files for the statistics, although in the end the times were taken by one computer.


I used the following code in a python interpreter to generate the files, and just called `generate(1000000)` to generate the files.

```
import sys, random

def rn(a,b):
    return r.randint(a,b)

def generate(length):
    for file in range(1,11):
        s = ""
        f = open(str(file) + ".txt", "w+")
        percent = 1
        print "progress:",
        for i in range(length):
            s += str(rn(1,length*10)) + '\n'
            if i%(length/10) == 0:
                print ".",
                sys.stdout.flush()
        f.write(s)
        f.close()
        print "\nfile %d done." %file
```


The results (in seconds):

________________________________________
| file # |  merge sort  |  quick sort  |
_______________________________________
|   1    |    6.491     |    4.588     |
|   2    |    6.512     |    4.573     |
|   3    |    6.476     |    4.537     |
|   4    |    6.484     |    4.648     |
|   5    |    6.638     |    4.614     |
|   6    |    6.542     |    4.564     |
|   7    |    6.415     |    4.541     |
|   8    |    6.491     |    4.714     |
|   9    |    6.475     |    4.512     |
|   10   |    6.591     |    4.576     |
_______________________________________