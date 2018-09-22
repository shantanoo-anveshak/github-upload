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
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)
    result2 = subtract.delay(5,2)
    print ('Subtract Task finished? ', result1.ready())
    print ('Subtract Task result: ', result1.result)

    time.sleep(5)
    print ('Subtract Task finished? ', result1.ready())
    print ('Subtract Task result: ', result1.result)
    result3 = multiply.delay(4,5)
    print('Multiply task finished?', result3.ready())
    print('Multiply Task result: ', result3.result)
