# Write a function that calculates and displays the average of its input arguments.
def average(*args):
    try:
        av = sum(args)/len(args)
        return av
    except:
        print("Arguments should be integers")

print(average(3,6,10,39))