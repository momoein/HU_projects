



def set_attrs(object_, keywords, values):
    for kw, val in zip(keywords, values):
        setattr(object_, kw, val)
    

