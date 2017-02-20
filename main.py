from tasks import cowrks_task
import os
import glob

if __name__ == '__main__':
    #directory where the images are stored
    os.chdir("test_images")
    #iterate over files with the .png extension
    for file in glob.glob("*.png"):
        #.delay is used to send the function for processing
        #on celery
        cowrks_task.delay(file)
