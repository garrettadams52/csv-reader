import csv

def main():
    while(True):
        spec = input('Enter the type of animal: cats or dogs. Enter q to end program. \n')
        if str(spec) == 'q': break
        try:
            filename = f'./data/{spec.lower()}.csv' 
            rows = []
            i = 0

            with open(filename, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                
                #make a list of lists
                for j, row in enumerate(csvreader):
                    if j > 0:
                        rows.append(row)

            #print csv info 
            for x in rows:
                print(f"{x[i]} is a{x[i+1]} year old{x[i+2]}")
                i = 0
        except:
            print(f"Sorry, we don\'t have any {spec} here\n")

    

main()