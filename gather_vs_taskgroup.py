import asyncio 

async def square_number(n): 
	for i in range(1,n+1): 
		print("Square of ",i, "is ", i**2) 
		await asyncio.sleep(0.001) 

async def square_root(n): 
	print("Square root of ",n," rounded to nearest integer is ", 
		round(n**.5)) 

async  def divide(num1, num2):
	if num2 == 0:
		raise ZeroDivisionError
	else:
		print(num1/num2)

async def task_grp_main(): 
	async with asyncio.TaskGroup() as task_group: 
		task_group.create_task(square_number(5)) 
		task_group.create_task(square_root(25)) 
		task_group.create_task(square_root(18)) 
		task_group.create_task(square_root("gayu")) #exception
		task_group.create_task(square_number("gayu"))#exception
		task_group.create_task(divide(23,0))#exception
	
	print("All different tasks of task_group has executed successfully!!") 


#asyncio.run(task_grp_main())


"""
Square of  1 is  1
Square root of  25  rounded to nearest integer is  5
Square root of  18  rounded to nearest integer is  4
  + Exception Group Traceback (most recent call last):
  |   File "D:\HCO\Program\gather_vs_taskgroup.py", line 30, in <module>
  |     asyncio.run(main())
  |   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1776.0_x64__qbz5n2kfra8p0\Lib\asyncio\runners.py", line 190, in run
  |     return runner.run(main)
  |            ^^^^^^^^^^^^^^^^
  |   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1776.0_x64__qbz5n2kfra8p0\Lib\asyncio\runners.py", line 118, in run
  |     return self._loop.run_until_complete(task)
  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1776.0_x64__qbz5n2kfra8p0\Lib\asyncio\base_events.py", line 653, in run_until_complete
  |     return future.result()
  |            ^^^^^^^^^^^^^^^
  |   File "D:\HCO\Program\gather_vs_taskgroup.py", line 19, in main
  |     async with asyncio.TaskGroup() as task_group: 
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1776.0_x64__qbz5n2kfra8p0\Lib\asyncio\taskgroups.py", line 147, in __aexit__
  |     raise me from None
  | ExceptionGroup: unhandled errors in a TaskGroup (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "D:\HCO\Program\gather_vs_taskgroup.py", line 10, in square_root
    |     round(n**.5))
    |           ~^^~~
    | TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "D:\HCO\Program\gather_vs_taskgroup.py", line 4, in square_number
    |     for i in range(1,n+1):
    |                      ~^~
    | TypeError: can only concatenate str (not "int") to str
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "D:\HCO\Program\gather_vs_taskgroup.py", line 14, in divide
    |     raise ZeroDivisionError
    | ZeroDivisionError
    +------------------------------------
"""


async def gather_main(): 
	asyncio.gather(square_number(5),square_root(25), square_root(18), square_root("gayu") , square_number("gayu"), divide(23,0))
	print("All different tasks of task_group has executed successfully!!") 

asyncio.run(gather_main())

"""
All different tasks of task_group has executed successfully!!
Square of  1 is  1
Square root of  25  rounded to nearest integer is  5
Square root of  18  rounded to nearest integer is  4
_GatheringFuture exception was never retrieved
future: <_GatheringFuture finished exception=TypeError("unsupported operand type(s) for ** or pow(): 'str' and 'float'")>
Traceback (most recent call last):
  File "D:\HCO\Program\gather_vs_taskgroup.py", line 10, in square_root
    round(n**.5))
         ~^^~~
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
"""