from .tasks import longtime_add
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    # at this time, our task is not finished, so it will return False
    print ('Add Task finished? ', result.ready())
    print ('Add Task result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print ('Add Task finished? ', result.ready())
    print ('Add Task result: ', result.result)
    result1 = longtime_subtract.delay(5,2)
    print('Subtract task finished?', result1.ready())
    if(result1.ready()):
	print('Subtract task result: ', result1.result)

