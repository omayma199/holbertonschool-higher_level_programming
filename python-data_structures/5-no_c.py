#!/usr/bin/python3
def no_c(my_string)
import re
my_new_string = re.sub('[cC]',"",my_string)
print(my_new_string)
