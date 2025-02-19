import sys


def error_message_details(error, error_detail:sys): # error is the message that will be displayed if there is any error. Error_detail is the details of the error that is coming from the sys
    _,_,exc_tb = error_detail.exc_info() # exc_info is the exceution information which is represented by three variables of which 2 are not important
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python Script name[{0}] line number [{1}] error_message [{2}]".format(
        file_name. exc_tb.tb_lineno, str(error))
        
    return error_message
    


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail= error_detail )
    
    def __str__(self):
        return self.error_message