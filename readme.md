# Logger

* Logging

> <b>  Logging is a means of tracking events that happen when some software runs.</b>
 >The software’s developer adds logging calls to their code to indicate that certain events have occurred.

> This logger is defined to serve the primary logging<br> 
> Logs are being saved as **UCODE.log** in current directory

###### Requiremts
```commandline
pip install requirements.txt
```

#### Importing Logger
```python
from logger import Logger
```
#### Fetching or declaring 

Valid thresholds

| Acceptable threshold        | When it's used |
| ------------- |:-------------:| 
| DEBUG         |  Detailed information, typically of interest only when diagnosing problems.|
| INFO          |  Confirmation that things are working as expected.|      
| WARNING       |  An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected. |
| ERROR         |  Due to a more serious problem, the software has not been able to perform some function.|      
| CRITICAL      |  A serious error, indicating that the program itself may be unable to continue running. |

```python
UCODE     = 'C-192'
threshold = 'debug'   # Not case-sensitive 
logs = Logger(UCODE,threshold)
```
* Using Logger
```python
logs.info('info log message')
logs.debug('debug log message')
logs.warning('error logs ')
logs.error('error log message')
logs.critical('critical log message')
```

###Example 1
```python
from logger import Logger
logs=Logger('my_logs','Debug')

# Loggings 
logs.info('info log message')
logs.debug('debug log message')
logs.warning('error logs ')
logs.error('error log message')
logs.critical('critical log message')

```
####Output:
Logs are saved in file `my_logs.log`

###Example 2
```python
from logger import Logger
logs=Logger('C192','warning')
try:
    print(1/0)
except ZeroDivisionError as zero:
    logs.warning("Can not divide by zero")
```
Logs are saved in file `C192.log`
![Output]()
```console
WARNING : 2021-01-28 16:30:43,552 : C192 - Can not divide by zero
```

