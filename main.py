def first_non_repeating_letter(s):
    lower_s = list(s.lower())
    l = [ord(el) for el in lower_s]
    answer = ''
    for i in range(0, len(l)):
        if l.count(l[i]) == 1:
            answer = s[i]
            break
    return answer
            
            
        
