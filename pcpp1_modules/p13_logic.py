from random import randint, choice, shuffle

def tkinter_window_coordinates():
    """
    if your window's size is 200x200 what are the coordinates of the pixel located in top right window corner

    answers
    x= y= 

    in a window which is 200x200, what is the location of the following coordinates:

    alter size of window and top, bottom, right, left corner

    left or right x
    top or botton y
    """
    if randint(0,1) == 0:
        x_value = randint(1,100) * 10
        y_value = x_value
    else: 
        x_value = randint(1,100) * 10
        y_value = randint(1,100) * 10  

    y_description = 'top' if randint(0,1) == 0 else 'bottom'
    x_description = 'left' if randint(0,1) == 0 else 'right'

    y_coordinate = 0 if y_description == 'top' else y_value
    x_coordinate = 0 if x_description == 'left' else x_value
   
    window_size = f"{x_value}x{y_value}"
    description = f"{y_description}-{x_description}"
    coordinates = f"x={x_coordinate}, y={y_coordinate}"

    question_root = f"{choice(['If your window size is', 'In a window which is'])} {window_size}, "

    if randint(0,1):
        #given coordinates, get description
        question = question_root + f'what is the location of the coordinates {coordinates}?'
        all_descriptions = (
            'top-left',
            'top-right',
            'bottom-left',
            'bottom-right'
        )
        incorrect = [item for item in all_descriptions if item != description]
        correct = description
        items = [{'item':correct, 'indicator':'correct', 'id':'item1'}]
        for i, item in enumerate(incorrect):
            items.append({'item':item, 'indicator':'incorrect', 'id':f'item{i+2}'})

    else:
        #given description, get coordinates
        question = question_root + f'what are the coordinates of the pixel at the {description} of the window?'
        all_coordinates = (
            'x=0, y=0',
            f'x={x_value}, y=0',
            f'x=0, y={y_value}',
            f'x={x_value}, y={y_value}',
        )
        incorrect = [item for item in all_coordinates if item != coordinates]
        correct = coordinates
        items = [{'code':correct, 'indicator':'correct', 'id':'item1'}]
        for i, item in enumerate(incorrect):
            items.append({'code':item, 'indicator':'incorrect', 'id':f'item{i+2}'})

    shuffle(items)
    return [{'text':question}], items

def tkinter_create_line():
    """
    """
    size_of_canvas = randint(1,4)*100

    

    line_orientation = {
        "a line from diagonal top left to bottom right":f"\t0, 0,\n\t{size_of_canvas}, {size_of_canvas},\n",
        "a line from diagonal bottom left to top right":f"\t{size_of_canvas}, 0,\n\t0, {size_of_canvas},\n",
        "a line from left to right":f"\t0, {int(size_of_canvas/2)},\n\t{size_of_canvas}, {int(size_of_canvas/2)},\n",
        "a line from top to bottom":f"\t{int(size_of_canvas/2)},0,\n\t{int(size_of_canvas/2)},{size_of_canvas},\n"
    }

    line_description = {
        "thin":"\twidth = 1\n",
        "thick":"\twidth = 40\n",
        "rounded":"\tcapstyle = 'round'\n",
        "arrowhead at the start":"\tarrow = 'first'\n",
        "arrowhead at the end":"\tarrow = 'last'\n",
        "arrowhead at both ends":"\tarrow = 'both'\n",
        "dashed":"\tdash = (1),\n",
        "solid":"\tdash = (),\n"
    }
    
    orientation_key = choice(list(line_orientation.keys()))
    orientation_code = line_orientation[orientation_key]

    line_description_key = choice(list(line_description.keys()))
    line_description_code = line_description[line_description_key]

    description = orientation_key + ', ' + line_description_key

    id = 1
    items = [{'item': description, 'indicator':'correct', 'id':f'item{id}'}]
    id+=1
    used = [description]

    while len(items)!=4:
        if len(items)==3:
            attempt = choice(list(line_orientation.keys())) + ', ' + choice(list(line_description.keys()))
        else:
            attempt = choice(list(line_orientation.keys())) + ', ' + line_description_key
        if attempt not in used:
            items.append({'item': attempt, 'indicator':'incorrect', 'id':f'item{id}'})
            used.append(attempt)
            id+=1

    code = """"""
    code+="from tkinter import *\n"
    code+="w = Tk()\n"
    code+=f"c = Canvas(w, height = {size_of_canvas}, width = {size_of_canvas})\n"
    code+="c.pack()\n"
    code+="c.create_line(\n"
    code+=orientation_code
    code+=line_description_code
    code+=")\n"
    code+="w.mainloop()"

    question = [{'text':'What will be outcome of the following code?'},{'code':code}]
    
    return question, items