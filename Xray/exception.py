import os
import sys
def error_messege_details(error:Exception , error_details:sys)->str:
    """
    Function to format error message and details.
    Args:
        error_messege (str): The error message.
        error_details (str): The error details.
    Returns:
        str: Formatted error message and details.
    """
    _,_,exe_tb = error_details.execution_info()
    
    file_split:str = os.path.split(exe_tb.tb_frame.f_code.co_filename)[1] 
    error_messege:str = f"Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_split, exe_tb.tb_lineno, str(error)
    )

    return f"Error: {error_messege}\nDetails: {error_details}"
    

class XRayException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)

        self.error_message: str = error_messege_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message