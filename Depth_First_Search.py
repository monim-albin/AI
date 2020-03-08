__author__ = 'AMA'

queue = []                                                                                
visited = []                                                                            
found = False
queue.append(first_node)
visited.append(first_node) 

while len(que) > 0:                                                                     
    current_node = queue.pop()
    neighbor_list = find_neighbors(current_node)                                  
    for neighbor in neighbor_list:                                                      
        if neighbor not in visited:                                                     
             if neighbor == target_node:
                    found = True
            que.append(neighbor)
	   visited.append(neighbor)
        if found == True:                    
          print("the target is found")
