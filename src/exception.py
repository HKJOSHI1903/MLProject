import sys
def error_message_details(error,error_detail:sys):
    _,_,error_tb=error_detail.exc_info()
    file_name=error_tb.tb_frame.f_code.co_filename
    error_message="Error Occoured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,error_tb.tb_lineno,str(error)
        )
    return error_message
class Custom_Exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)   
        self.error_message=error_message_details(error_message,error_detail)
    def __str__(self):
        return self.error_message