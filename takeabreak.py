# Program will prompt user to take a break every two hours by opening webbrowser and playing a song.
import time
import webbrowser
# There will be three breaks throughout the day (total_breaks).
total_breaks = 3
# break_count variable to keep track of number of breaks and break loop after satisfied.
break_count = 0
# Show the time when the program started running.
print("This program started on "+time.ctime())
# Add while loop to make program run three times, once the stetement is falce, loop will stop.
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=-OqrcUvrbRY")
    break_count = break_count + 1

