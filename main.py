from tasks import cowrks_task
import os
import glob

if __name__ == '__main__':
    os.chdir("test_images")
    for file in glob.glob("*.png"):
        cowrks_task.delay(file)
