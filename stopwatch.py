# Introduction to Interactive Programming in Python
# Week 3 Mini-Project: "Stopwatch: The Game"

import simplegui

# define global variables
count = 0
number_wins = 0
number_stops = 0
tenths = 0
timer_running = False

# define helper function format to convert time to A:BC.D
def format(count):
    global tenths
    minutes = (count / 600) 
    tens = (count / 100) % 6
    ones = (count / 10) % 10
    tenths = (count % 10)
    return str(minutes) + ":" + str(tens) + str(ones) + ":" + str(tenths)
    
# define event handlers for buttons
def start():
    timer.start()
    global timer_running
    timer_running = True
    return

def stop():
    timer.stop()
    global number_stops
    global tenths
    global timer_running
    if ((tenths == 0) and (timer_running == True)):
        number_stops += 1
        global number_wins
        number_wins += 1
        return
    elif (timer_running == True):
        number_stops += 1
        return
    timer_running = False
    return

def reset():
    timer.stop()
    global count
    global number_wins
    global number_stops
    global timer_running
    count = 0
    number_wins = 0
    number_stops = 0
    timer_running = False
    return

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1
    print(count)
    return

# define draw handler
def draw(canvas):
    canvas.draw_text(format(count), [175, 200], 50, "White")
    canvas.draw_text(str(number_wins) + "/" + str(number_stops), [300, 50], 50, "Blue")
    return

# create frame (and timer?)
frame = simplegui.create_frame("Stopwatch", 400, 400)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame
frame.start()
