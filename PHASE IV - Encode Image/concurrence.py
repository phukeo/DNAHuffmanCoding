import time
import scrape as sc
import concurrent.futures


def main(entryList):

    start=time.perf_counter()

    
    resultslist=[]
    minFreeEnergies=[]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        # Below Punches out values but not in order that they were submitted
        
        # futureResults=[executor.submit(sc.freeEnergy,i) for i in totalCombined]
        # for f in concurrent.futures.as_completed(futureResults):
        #     print(f.result())
        
        # Better way is to map the results:
        results=executor.map(sc.freeEnergy,entryList)

        for i in results:
            resultslist.append(i)
            minFreeEnergies.append(min(i))

    finish=time.perf_counter()
    timeTaken=finish-start
    # print("Future Results is :", futureResults)
    print("Results is :", resultslist)
    print("Minimum Values : ", minFreeEnergies)
    print(f"Job completed in {round(timeTaken,2)} seconds")
    return (minFreeEnergies)
# print("The list of free energy outputs is ",a)
# print("The second list of free energy outputs is ", b )

if __name__ == '__main__':
    print("in here")
