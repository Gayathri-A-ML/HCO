from multiprocessing import Queue


if __name__=='__main__':

    colours = ['Red', 'Blue', 'Orange', 'Pink']
    queue_obj = Queue()
    print("Pushing item inti queue")
    for colour in colours:
        print("pushing item ", colour)
        queue_obj.put(colour)
    print("poping out the colours")
    while not queue_obj.empty():
        print("poping out the colour", queue_obj.get())


"""
Pushing item inti queue
pushing item  Red
pushing item  Blue
pushing item  Orange
pushing item  Pink
poping out the colours
poping out the colour Red
poping out the colour Blue
poping out the colour Orange
poping out the colour Pink
"""