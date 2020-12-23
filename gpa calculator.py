### GPA CALCULATOR ###

def gpa(classes = int(input('total number of classes: '))):
    # letter grade to GPA conversion
    grades = {  'A+' : 4.00, 'A' : 4.00, 'A-' : 3.67,
                'B+' : 3.33, 'B' : 3.00, 'B-' : 2.67,
                'C+' : 2.33, 'C' : 2.00, 'C-' : 1.67,
                'D+' : 1.33, 'D' : 1.00, 'D-' : 0.67,
                'F' : 0.00, 'ABS' : 0.00  }
    # empty lists for the gpa*hours and total hours
    total_gpas = []
    total_hours = []
    # get hours and grades, add to lists
    for i in range(classes):
        hours = float(input(f'class {i+1} hours: '))
        total_gpas.append( hours * grades[input(f'class {i+1} grade: ')])
        total_hours.append(hours)
    # calculate gpa, return in a string
    return f'your gpa for this semester is {sum(total_gpas) / sum(total_hours)}'


print(gpa())


    
