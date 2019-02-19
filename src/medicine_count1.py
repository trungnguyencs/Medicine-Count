import sys  
import os

def main():  
    f_in, f_out = get_file_path()
    drug_dict = {}
    with open(f_in) as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            line = lines[i].strip().split(',')
            # try:
                # name is in the 3rd, cost if in the 4th column
            pres_last = line[1]
            pres_first = line[2]
            drug_name = line[3].upper()
            cost = int(round(float(line[4]))) 
            sum_total_cost(pres_last, pres_first, drug_name, cost, drug_dict)    
            # except: 
            #     print('Line %d is corrupt!' %(i))
        ord_lst = ord_cost(drug_dict)
    with open(f_out, 'w') as file:  
        file.write('drug_name,num_prescriber,total_cost\n')
        for k,v in ord_lst:
            file.write(str(k) + ',' + str(len(v[0])) + ',' + str(v[1]) + '\n')

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

def sum_total_cost(pres_last, pres_first, drug_name, cost, drug_dict):
    if drug_name in drug_dict:
        drug_dict[drug_name][1] += cost 
        drug_dict[drug_name][0][(pres_first, pres_last)] = None 
    else: 
        drug_dict[drug_name] = [{(pres_first, pres_last): None}, cost]

def ord_cost(drug_dict):  
    drug_lst = [(drug_name, [pres_dict, cost]) for drug_name, [pres_dict, cost] in drug_dict.items()]
    # The next 2 lines guarantee drug_dict is sorted by total cost then by drug name 
    sort_temp = sorted(drug_lst, key=lambda x: (x[0]), reverse=False)
    return sorted(sort_temp, key=lambda x: (x[1][1]), reverse=True)

if __name__ == '__main__':  
    main()