#code for python process
import time

def sample_process():
    start_time = time.time()
    while time.time() - start_time<3600:
        pass

    print("process completed")

if __name__=="__main__":
    sample_process()