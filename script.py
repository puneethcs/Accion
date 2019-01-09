import sys

def space(n):
    s=''
    return "".join([" " for i in range(n)])

heandin_line_dict={}
def heading_line_number(star_str,heading_num,r):
    star_str=star_str.replace("*",heading_num,1)
    #print star_str
    if len(star_str) > 2:
        inc = heandin_line_dict[star_str[0:-1]]
    if star_str not in heandin_line_dict:
        heandin_line_dict[star_str] = star_str.replace("*",r,1).replace("*",'.1')
    else:
        sp = heandin_line_dict[star_str].split('.')
        sp[-1] = str(int(sp[-1])+1)
        #print sp
        heandin_line_dict[star_str] = ".".join(sp)
    return heandin_line_dict[star_str]

line_no=0

for line in sys.stdin:
    line = line.rstrip()
    #print (line)
    if len(line.strip()) == 0:
        print(" ")
        continue
    line_star_with=False
    num_star=len(line)-len(line.lstrip('*'))
    if num_star == 1:
        line_star_with=True
        line_nbr=0.0
        a=b=0
        line_no+=1
        print line.replace('*',str(line_no))
    elif num_star > 1:
        if num_star == 2:
            line_nbr +=0.1
            heandin_line_dict={}
        star_str = "".join('*' for i in range(num_star))
        print line.replace(star_str,heading_line_number(star_str,str(line_no),str(line_nbr)[1:]),1)
        continue
    if line_star_with == False:
        #print line
        #print a,b
        if a == 0 and b == 0:
            b=len(line) - len(line.lstrip())
            print(space(b)+"+ "+line.strip())
            a=b
            continue
        else:
            b=len(line) - len(line.lstrip())
        #print a,b
        if a == b:
            a=b
            print(space(a)+"+ "+line.strip())
        elif a != b:
            a=b
            print(space(a)+"- "+line.strip())