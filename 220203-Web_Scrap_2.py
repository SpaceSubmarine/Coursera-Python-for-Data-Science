# !pip install requests==2.26.0
#!mamba install bs4==4.10.0 -y
#!pip install lxml==4.6.4
#!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

table_rows=table_bs.find_all('tr')
table_rows

first_row =table_rows[0]
first_row
print(type(first_row))
first_row.td


#If we iterate through the list, each element 
# corresponds to a row in the table:
for i,row in enumerate(table_rows):
    print("row",i,"is",row)
    

#As row is a cell object, we can apply the method find_all to 
# it and extract table cells in the object cells using the tag td, 
# this is all the children with the name td. The result is a list, 
# each element corresponds to a cell and is a Tag object, 
# we can iterate through this list as well. 
# We can extract the content using the string attribute.
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input=table_bs .find_all(name=["tr", "td"])
list_input

table_bs.find_all(id="flight")

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

#If we set the href attribute to True, 
# regardless of what the value is, 
# the code finds all tags with href value:
table_bs.find_all(href=True)

#we cansearch for strings instead of tags
table_bs.find_all(string="Florida")
