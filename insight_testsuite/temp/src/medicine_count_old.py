import sys  
import os

def main():  
    f_in, f_out = get_file_path()
    drug_dict = {}
    with open(f_in) as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            line = lines[i].strip().split(',')
            try:
                drug_name, cost = line[3], int(round(float(line[4]),0)) # name is in the 3rd, cost if in the 4th column
                sum_total_cost(drug_name.upper(), cost, drug_dict)    
            except: 
                print('Line %d is corrupt!' %(i))
        ord_dict = ord_cost(drug_dict)
    with open(f_out, 'w') as file:  
        file.write('drug_name,num_prescriber,total_cost\n')
        for k,v in ord_dict:
            file.write(str(k) + ',' + str(v[0]) + ',' + str(v[1]) + '\n')

def get_file_path(): 
    if len (sys.argv) != 3: # check if correct number of arguments is provided  
        print('Usage:\npython3 input_path output_path')
        sys.exit()    
    f_in = sys.argv[1]
    f_out = sys.argv[2]
    if not os.path.isfile(f_in): # check if input file exists
        print("File path %s does not exist. Exiting..." %(f_in))
        sys.exit()
    return f_in, f_out

def sum_total_cost(drug_name, cost, drug_dict):
    if drug_name in drug_dict:
        count_cost = drug_dict[drug_name]
        count, total_cost = count_cost[0], count_cost[1]
        drug_dict[drug_name] = [count + 1, total_cost + cost]
    else: 
        drug_dict[drug_name] = [1, cost]
    return 

def ord_cost(drug_dict, desc=True):  
    drug_lst = [(drug, [count, cost]) for drug, [count, cost] in drug_dict.items()]
    return sorted(drug_lst, key=lambda x: x[1][1], reverse=desc)

if __name__ == '__main__':  
    main()