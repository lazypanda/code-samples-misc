###########################################################
#This is my code for the Airtime recruitment challenge.
#The challenge started at a given url
#http://challenge.airtime.com/?email=ehyuan@berkeley.edu
#which contained sets of instructions function(number).function(number)...
#where function was one of add, sub, mult, div
#and number could be any positive or negative integer
#This number would be used to redirect to the next page with a new set of instructions
#under the url: http://challenge.airtime.com/NUMBER?email=ehyuan@berkeley.edu
#
#After reaching the final page, I was to find the longest increasing subsequence
#of the set of numbers and sum its elements
###########################################################




#written for python 2.6,
#python 3.0 incompatible, as urllib is replaced by urllib2 in 3.0

import urllib

values = list()
digits = ['0','1','2','3','4','5','6','7','8','9','-']


def download(url):
        webfile = urllib.urlopen(url)
        string = webfile.read()
        return string

def makeurl(value):
        url = "http://challenge.airtime.com/" + str(value) +"?email=ehyuan@berkeley.edu"
        print url
        return url

def parsestring(string):
        #my first implementation of this code was done in C,
        #then I remembered the convenient split function in python
        functions = string.split('.')
        value = int(functions[0])
        functions = functions[1:len(functions)]
        for function in functions:
                func_val = function.split('(')
                func = func_val[0]
                val = int(func_val[1][0:len(func_val[1])-1])
                if func == "add":
                          value = value + val
                if func == "sub":
                          value = value - val
                if func == "mult":
                          value = value * val
                #division in python is conveniently floored
                if func == "div":
                          value = value / val
        return value

def subsequence(values):
        #this is a naive solution that runs in O(n^2) time
        #a O(n log n) time solution exists(found on wiki!),
        #but I did not fully understand it after reading the article,
        #(particularly about M), so I went with a solution that I fully understood
        length = len(values)
        ss_len = [1] * length
        prev_index = [None] * length
        max_len = 1
        best_end = 0

        for index in range(1,length):
                #reversing this order would give smaller sum
                #that is "for i in range(index-1,-1,-1):"
                for i in range(0,index):
                        if (ss_len[i] + 1 > ss_len[index]) & (values[index] > values[i]):
                                ss_len[index] = ss_len[i] + 1
                                prev_index[index] = i
                if ss_len[index] > max_len:
                        best_end = index
                        max_len = ss_len[index]
        path = list()
        index = best_end
        while index != None:
                path.append(values[index])
                index = prev_index[index]
        path.reverse()
        return path


url = "http://challenge.airtime.com/?email=ehyuan@berkeley.edu"
string = download(url)
#stopping point was made after the fact, originally ran until error
#which was sufficient for reaching the -6 page
while string[0] in digits:
        value = parsestring(string)
        values.append(value)
        url = makeurl(value)
        string = download(url)

best_seq = subsequence(values)
best_sum = sum(best_seq)

print best_seq
print best_sum



