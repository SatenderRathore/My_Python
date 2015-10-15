import time
import webbrowser

total_breaks = 3
break_count = 0

print("This programme started on"+time.ctime())
while(break_count<total_breaks):
    time.sleep(50)
    webbrowser.open("https://youtu.be/v0k5eSI-pK0")
    break_count = break_count +1
    
