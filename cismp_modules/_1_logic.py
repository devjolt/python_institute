from random import randint, shuffle



def example():
    question=[
        {'text':'How much is that doggy in the window (system test question)?'}
    ]
    
    items=[
        {'item':'the one with the waggly tail?', 'indicator':'correct', 'id':f'item1'},
        {'item':'the one with one ear?', 'indicator':'inorrect', 'id':f'item2'},
        {'item':'the one without a head?', 'indicator':'incorrect', 'id':f'item3'},
        {'item':'the one which looks like a cat?', 'indicator':'incorrect', 'id':f'item4'},
        
        ]
    return  question, items

