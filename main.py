import LCD
import multiprocessing as mp

LCD.initialize()

#is a calling function
if __name__ == "__main__":
    f1 = mp.Process(target=LCD.normalTalkingEmotion)
    f2 = mp.Process(target=LCD.normalEmotion)
    # Starting each process
    f1.start()
    f2.start()
    # Joining each process so they end at the same time
    f1.join()
    f2.join()

