#!/usr/bin/python3
import cgi

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1> Hello programs! </h1>")

form = cgi.FieldStorage()
if form.getvalue("name"):
	name = form.getvalue("name")
	print("<h1>Hello " + name + "! Thanks for using my script!</h1><br/>")
if form.getvalue("happy"):
	print("<p> Yay! I am happy too! </p>")
if form.getvalue("sad"):
        print("<p> Oh no, why are you sad ? </p>")

print("<form method='get' action='hello.py'>")
print("<p>Name: <input type='text' name='name'/></p>")
print("<input type='checkbox' name='happy' /> Happy")
print("<input type='checkbox' name='sad' /> Sad")
print("<input type='submit' value='Submit' />")
print("</form>")
print ("</body></html>")

