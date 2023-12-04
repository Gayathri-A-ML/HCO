
def nestedExceptionGroup():
    excp_grp = ExceptionGroup("Userdefined exception",
                   [FileExistsError("File is missing"), ModuleNotFoundError("module is missing"), SyntaxError("syntax error") ,
                    ExceptionGroup("nested exception",
                   [PermissionError("permission error"), LookupError("lookup error")
                    ])])
    raise excp_grp


def exceptionGroup():
    excp_grp = ExceptionGroup("Userdefined exception",
                   [FileExistsError("File is missing"), ModuleNotFoundError("module is missing"), SyntaxError("syntax error")])
    raise excp_grp

#exceptionGroup()
"""
ExceptionGroup: Userdefined exception (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | FileExistsError: File is missing
    +---------------- 2 ----------------
    | ModuleNotFoundError: module is missing
    +---------------- 3 ----------------
    | SyntaxError: syntax error
    +------------------------------------
"""
# try:
#     exceptionGroup()
# except ExceptionGroup as err:
#     print(err.exceptions)

"""
(FileExistsError('File is missing'), ModuleNotFoundError('module is missing'), SyntaxError('syntax error'))
"""

# try: 
#     exceptionGroup() 
# except* FileExistsError as fnf: 
#     print(fnf.exceptions) 
# except* ModuleNotFoundError as ve: 
#     print(ve.exceptions) 
# except* SyntaxError as zde: 
#     print(zde.exceptions) 

"""
    (FileExistsError('File is missing'),)
(ModuleNotFoundError('module is missing'),)
(SyntaxError('syntax error'),)
 """


# try: 
#     exceptionGroup() 
# except* FileExistsError as fnf: 
#     for err in fnf.exceptions:
#         print(err) 
"""
File is missing
  + Exception Group Traceback (most recent call last):
  |   File "D:\HCO\Program\exceptiongroup.py", line 44, in <module>
  |     exceptionGroup()
  |     ^^^^^^^^^^^^^^^^
  |   File "D:\HCO\Program\exceptiongroup.py", line 5, in exceptionGroup
  |     raise excp_grp
  | ExceptionGroup: Userdefined exception (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | ModuleNotFoundError: module is missing
    +---------------- 2 ----------------
    | SyntaxError: syntax error
    +------------------------------------
"""



nestedExceptionGroup()

"""
ExceptionGroup: Userdefined exception (4 sub-exceptions)
  +-+---------------- 1 ----------------
    | FileExistsError: File is missing
    +---------------- 2 ----------------
    | ModuleNotFoundError: module is missing
    +---------------- 3 ----------------
    | SyntaxError: syntax error
    +---------------- 4 ----------------
    | ExceptionGroup: nested exception (2 sub-exceptions)
    +-+---------------- 1 ----------------
      | PermissionError: permission error
      +---------------- 2 ----------------
      | LookupError: lookup error
      +------------------------------------
"""