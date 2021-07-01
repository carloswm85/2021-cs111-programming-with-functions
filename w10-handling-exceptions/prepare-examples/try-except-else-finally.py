try:
    # Write normal code here. This block must include
    # code that falls into two groups:
    # 1. Code that may cause an exception to be raised
    # 2. Code that depends on the results from the code
    #    in the first group
	pass
except ZeroDivisionError as zero_div_err:
    # Code that the computer executes if the code in the
    # try block caused a ZeroDivisionError to be raised.
	pass
except ValueError as val_err:
    # Code that the computer executes if the code in
    # the try block caused a ValueError to be raised.
	pass
except (TypeError, KeyError, IndexError) as error:
    # Code that the computer executes if the code in the try
    # block raised a TypeError, KeyError, or IndexError.
	pass
except Exception as excep:
    # Code that the computer executes if the code in the
    # try block caused ANY exception to be raised that was
    # not handled by one of the previous except blocks.
	pass
except:
    # Code that the computer executes if the code in the
    # try block caused ANYTHING to be raised that was
    # not handled by one of the previous except blocks.
	pass
else:
    # Code that the computer executes after the code
    # in the try block if the code in the try block
    # did not raise any exceptions.
	pass
finally:
    # Code that is executed after all the other code in
    # try, except, and else blocks regardless of whether
    # an exception was raised or not.
	#  The code in the finally block usually contains
	# "clean up" code that frees resources that the code
	# in the try block used.
	pass

"""
The Python programming language requires us to order except blocks from most specific at the top to least specific (most general) at the bottom. However, in most programs, it is a bad idea to write except blocks that are very general, including an except block that handles all possible exception types and a bare except block.

It is a bad idea to write an except block that handles all types of exceptions because such a block will handle SyntaxError. We don't want to handle SyntaxError. Instead, we want our program to crash for a syntax error and print the line number where the syntax error occurred so that a programmer can find and fix the syntax error. Syntax errors are caused by a programmer mistyping code and not by bad user input or missing files. We want a programmer to find and fix all the syntax errors in a program long before the program is given to users.
"""
