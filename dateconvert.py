# By Bobi + Henry

import datetime

# Parse source date
birthday = "1-May-12"
date_format = "%d-%b-%y"
parsed_date = datetime.datetime.strptime(birthday, date_format)

# Convert format and print
print parsed_date.strftime("%-m/%-d/%y") # 01/11/17
