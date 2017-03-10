def find_max_min(mylist):
  
    if type(mylist) == list:
        minimum = min(mylist)
        maximum = max(mylist)
            
        
        if minimum == maximum:
            new_list = len(mylist)
            
            return ([new_list])
            
        else:
          return ([minimum, maximum])
    
    else:
        pass
        
find_max_min([1, 2, 3, 4])
find_max_min([6,4])
find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])
find_max_min([4, 4, 4, 4])
find_max_min([1, 2, 3, 4])