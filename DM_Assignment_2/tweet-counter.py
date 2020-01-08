import sequential_map_reduce as smr
import parallel_map_reduce as pmr

def runSequential():
    smr.sequentialMapReduce()

def runParallel():
    pmr.parallelMapReduce()


def exitProgram():
    print("\n\t\t\t\t\t  Thank you for using Tweet Counter!\n")  
    exit()


def default():
    print("\nInvalid Input\n")    


def programManage(path):
    switched = {
        1: runSequential,
        2: runParallel,
        3: exitProgram   
    }
    switched.get(path, default)()

def main():

    print("\n\t\t\t\t\t\tWELCOME TO TWEET COUNTER\n")
    print("\nThis program will read a csv file that contains tweets and print out the top.")
    print("There will be two ways that the program counts the words: Sequentially or Parallel.")
    print("Note that parallel would be faster since it uses multiple cores.")

    while(1):
        print("\nChoose the method of counting the words in the tweets\n")
        print("  1) Sequential Method")
        print("  2) Parallel Method")
        print("  3) Exit")  
        option = int(input("\nEnter Counting Method: "))

        programManage(option)                


if __name__ == "__main__":
    main()









