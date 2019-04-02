# ToDo-App
For installing xampp run the following commands

$ wget https://www.apachefriends.org/xampp-files/5.6.33/xampp-linux-x64-5.6.33-0-installer.run

$ chmod +x xampp-linux-x64-5.6.33-0-installer.run

$ ./xampp-linux-x64-7.2.2-0-installer.run

$ sudo /opt/lampp/xampp start

Then create open php my admin and create a database name called TODO and a table name called TODO with 5 columns
then
1.date with date format
2.time with time format
3.content with varchar format
4.priority with int format
5.checked with boolean format


After that install mysql for python by running following commands

$ sudo apt-get install python-pip python-dev libmysqlclient-dev

$ pip install MySQL-python

Then to install neccessary packages

$ pip install termcolor

Then enter the following commands

$ chmod +x todo.sh

$ chmod +x todoDriver.sh

Then open ~/.bashrc file and paste the following lines
source ~/ todo.sh
source ~/ todoDriver.sh
print_my_input

everytime u open ur terminal ur remainders will be listed....

Type command "wattodo" in terminal to make changes or edit or update or mark the work as done in your remainders or work
