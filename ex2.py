import re
#regex
s = 'A message from csev@umich.edu to cwen@iupui.edi'
lst = re.findall('\\S+@\\S+', s)
print(lst)

#using regex to filter the email-s
