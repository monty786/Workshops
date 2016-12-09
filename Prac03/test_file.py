__author__ = 'jc437351'

temp_file = open("temp.txt","w")
print("first line", file=temp_file)
print("second line", file=temp_file)
temp_file.close()
print("===")
temp_file= open("temp.txt","r")
for line in temp_file:
    line=line.strip()
    print(line)
temp_file.close()
print("===")
temp_file= open("temp.txt","r")
my_str = temp_file.read()
print(my_str)
temp_file.close()
print("===")
temp_file=open("temp.txt","r")
lines=temp_file.readlines()
print(lines)

temp_file.close()
print("===")
my_list=['first line\n', 'second line\n']
out_file=open("out.txt","w")
out_file.writelines(my_list)
out_file.close()
