from zipfile import ZipFile

z=ZipFile("Output.zip",'w')

z.write("Assesment.py")
z.write("text.txt")

z.close()
