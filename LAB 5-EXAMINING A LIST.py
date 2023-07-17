#In this lab, the task is to read a set of temperature
#data (the monthly high temperatures at Heathrow Airport for 1948 through 2016)
#from a file and then find some basic information: the highest and lowest temperatures,
#the mean (average) temperature, and the median temperature
#(the temperature in the middle if all the temperatures are sorted). 
#The temperature data is in the file lab_05.txt in the source code directory
#for this chapter. Because I haven’t yet discussed reading files,
#here’s the code to read the files into a list:

#You should find the highest and lowest temperature, the average, and the
#median. You will probably want to use the min(), max(), sum(), len(),
#and sort() functions/methods. 

temperatures=[]
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)

temperatures.sort()
median_temp = temperatures[len(temperatures)//2]
print("max = {}".format(max_temp))
print("min = {}".format(min_temp))
print("mean = {}".format(mean_temp))
print("median = {}".format(median_temp))

#BONUS Determine how many unique temperatures are in the list.

unique_temps = len(set(temperatures))

print("number of temps - {}".format(len(temperatures)))
print("number of unique temps - {}".format(unique_temps))
                     
