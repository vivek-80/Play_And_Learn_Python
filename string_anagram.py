def string_anagram(in_1,in_2):
    lst_1=list(in_1.lower())
    lst_1.sort()
    lst_2=list(in_2.lower())
    lst_2.sort()
    if lst_1==lst_2:
        print(in_1 +" "+ 'and' +" "+in_2+ ' are anagram :)')
    else:
        print('Both are not anagram :(')
if __name__== "__main__":
    str_1='heart'
    str_2='Earth'
    string_anagram(str_1,str_2)
