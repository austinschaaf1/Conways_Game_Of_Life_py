def writeTimeToF(totalTime,timeCount):   
    print(str(totalTime / timeCount))
    f = open("timeTable.txt", "a")
    f.write(str(totalTime / timeCount) + "\n")
    f.close()
    print(str(totalTime / timeCount))