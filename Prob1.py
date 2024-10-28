from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    histogram=[0]*10
    #counting how often each number appears
    for number in data:
        if 0 <= number <10: #making sure number is a useable digit
            histogram[number]+=1
    return histogram


#1b
def print_histogram(hist:list[int]) -> None:
    for index in range(len(hist)):
        count=hist[index]
        print (f"{index}: {'*' * count}")

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    gw=GWindow(width, height)
    max_value=max(hist) if hist else 0 #determines the max value in hist
    bar_width=width//len(hist)
    height_per_unit=height/(max_value+1) if max_value > 0 else 1
    def my_rect(x,y,w,h,color): #creates my rectangle
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    for index in range(len(hist)):
        bar_height=hist[index]*height_per_unit#calculates the height of the rectangle
        x=index * bar_width
        y=height-bar_height #starts from bottom of the window
        my_rect(x, y, bar_width, bar_height, "red")

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test

