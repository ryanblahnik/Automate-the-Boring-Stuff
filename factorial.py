import logging 

logging.basicConfig(filename='C:\\f_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.disable(logging.WARNING)

logging.debug('Start of program')


def factorial(n):
    logging.info('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.warning('i is %s, total is %s' % (i, total))
    logging.critical('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
