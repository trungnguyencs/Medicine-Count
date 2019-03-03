import sys  
import os
import functools

def main():  
    f_in, f_out = get_file_path()
    drug_dict = {}

    with open(f_in) as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            line = lines[i].strip().split(',')
            try:
                drug_name, cost, pres_name = extract_info(line)
                sum_total_cost(pres_name, drug_name, cost, drug_dict)    
            except: 
                print('Line %d is corrupt!' %(i))
        sorted_lst = sort_drug(drug_dict)

    with open(f_out, 'w') as file:  
        file.write('drug_name,num_prescriber,total_cost\n')
        for drug in sorted_lst:
            drug_name = drug[0]
            pres_count = drug[1]
            total_cost = drug[2]
            file.write(str(drug_name) + ',' + str(pres_count) + ',' + str(total_cost) + '\n')

def get_file_path(): 

    """Get input and output file names, and check for their validity"""

    if len (sys.argv) != 3:                # check if correct number of arguments is provided  
        print('Usage:\npython3 input_path output_path')
        sys.exit()    
    f_in = sys.argv[1]
    f_out = sys.argv[2]
    if not os.path.isfile(f_in):           # check if input file exists
        print("File path %s does not exist. Exiting..." %(f_in))
        sys.exit()
    return f_in, f_out

def extract_info(line):

    """Get drug_name, cost, and pres_name from each line of the txt file"""

    drug_name = line[3].upper()
    cost = int(round(float(line[4]))) 
    pres_name = str(line[1]) + ' ' + str(line[2])
    return drug_name, cost, pres_name

def sum_total_cost(pres_name, drug_name, cost, drug_dict):

    """Create a dictionary of drugs, where each drug_name key has a value is a list 
    which contains its total_cost a dictionary of its pres_name"""

    if drug_name in drug_dict:
        drug_dict[drug_name][1] += cost 
        drug_dict[drug_name][0][pres_name] = None 
    else: 
        drug_dict[drug_name] = [{pres_name: None}, cost]

def sort_drug(drug_dict):  

    """Sort the drugs by total_cost (desc) and if total_cost are then sort by name (asc)"""

    drug_lst = [(drug_name, len(pres_dict), total_cost) for drug_name, [pres_dict, total_cost] in drug_dict.items()]
    # Sort drug_lst by total cost then by drug name 
    return sorted(drug_lst, key=functools.cmp_to_key(cost_name_compare))

def cost_name_compare(drug1, drug2):

    """Compare 2 drugs by total_cost, if they have equal total_cost
    then compare their drug_name
    """

    cost1, drug_name1 = drug1[2], drug1[0]
    cost2, drug_name2 = drug2[2], drug2[0]

    # drug1 is "smaller" than drug2 if it has a larger total_cost,
    # or if their costs are equal and drug1 has a earlier dictionary name order

    if cost1 != cost2:
        return cost2 - cost1
    if drug_name1 < drug_name2:
        return -1
    elif drug_name1 < drug_name2:
        return 1
    else:
        return 0

if __name__ == '__main__':  
    main()