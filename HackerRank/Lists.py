if __name__ == '__main__':
    N = int(input())
    List = []  

    for _ in range(N):
        command = input().split() 
        action = command[0]  

        if action == 'insert':
            index, value = map(int, command[1:])  
            List.insert(index, value)
        elif action == 'print':
            print(List)
        elif action == 'remove':
            value = int(command[1])  
            List.remove(value)
        elif action == 'append':
            value = int(command[1]) 
            List.append(value)
        elif action == 'sort':
            List.sort()
        elif action == 'pop':
            List.pop()
        elif action == 'reverse':
            List.reverse()
