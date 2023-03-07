import sys

def error_message_details(error,errordetail:sys):
    _,_,exec_tb=errordetail.exc_info()
    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message="Error occured script name[{0}] line number [{1}] error message [{2}]".format(
     file_name,exec_tb.tb_lineno,str(error)
     )
    
    return error_message
    
    
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(erro,errordetail=error_details)

    def __str__(self):
        return self.error_message