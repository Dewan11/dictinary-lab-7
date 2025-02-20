#Create a dictionary with dept no. , employee roll no. , and salary. Find the department wise min and max of salary
def dic():
    emp_data = {(1,40): 50000, (1,33):200000, (2,80): 100000, (2,79): 75000}
    dept_data = {}

    for k,v in emp_data. items():
        print(k[0], k[1],v)
        if k[0] not in dept_data:
            dept_data[k[0]] = {'Max':v, 'Min':v, 'Total':v}
        else:
            if v> dept_data[k[0]]['Max']:
                dept_data[k[0]]['Max'] = v
            elif v< dept_data[k[0]]['Min']:
                dept_data[k[0]]['Min'] = v
            dept_data[k[0]]['Total'] += v
    print(dept_data)
dic()        
