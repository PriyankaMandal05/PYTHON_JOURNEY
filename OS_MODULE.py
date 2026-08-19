import os
# Source - https://stackoverflow.com/a/57122532
# Posted by Swadhikar
# Retrieved 2026-08-19, License - CC BY-SA 4.0



os.getcwd()
# os.chdir('c :\\')  # this doesnot change anything, as we are on c drive itself on our laptop.
# os.getcwd()

# os.mkdir("newfolder")
# os.makedirs("one/two")

# os.remove("two")
# os.rmdir("two")
# os.rmdir("one/two")
# os.makedirs("one/two")
# os.removedirs("one/two")
# print(os.listdir())

x = os.walk(os.getcwd())
# print(x)
# for i in x :
#     print (i)
for curr_dir ,list_dir, list_files in x:
    print(curr_dir)
    print(list_dir)
    print(list_files)
