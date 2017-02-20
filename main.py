from tasks import cowrks_task

if __name__ == '__main__':
    for i in range (1,6):
        val = cowrks_task.delay(i)
        print val
