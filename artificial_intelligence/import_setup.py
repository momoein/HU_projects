# import setup
def add_nth_parent_dir_to_syspath(n=0, display=False):
    import os
    import sys
    def nth_parent_dir(n):
        """default n=0 means current directory"""
        path = os.path.dirname(os.path.realpath(__file__))
        for _ in range(n):
            path = os.path.dirname(path)
        return path
    
    dir = nth_parent_dir(n)
    print(dir) if display else None
        
    if dir not in sys.path:
        sys.path.append(dir)

add_nth_parent_dir_to_syspath(n=0)