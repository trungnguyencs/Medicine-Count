# Table of Contents
1. [Problem](README.md#problem)
1. [Approach](README.md#approach)
1. [Run instruction](README.md#run-instruction)
1. [Repo directory structure](README.md#repo-directory-structure)
1. [Tips on getting an interview](README.md#tips-on-getting-an-interview)
1. [Contact](README.md#contact)


# Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. 

# Approach

Since the output of this problem requires a set of unique drug names, it is appropriate to use a dictionary (hash map) `drug_dict` with key is the `drug_name`. Further more, since we only count the number of UNIQUE prescribers for each drug, it is reasonable to use a dictionary for each `drug_name`. These dictionaries have the tuple `(prescriber_last_name, prescriber_first_name)` as key. 

The program scans through each line of the txt input file. For each line it processes the string to obtain the `prescriber_last_name`, `prescriber_first_name`, `drug_name` and `drug_cost` information and skip . It then checks if `drug_name` is in `drug_dict`. If it's not, add an item with key is `drug_name` and value is a list of 2 elements: first is a dict with `(pres_first, pres_last)` as key, and second is an int variable `cost` (we can do float too, but then there would be issue with the first test file, so I simply round all float values to integers). If `drug_name` is in `drug_dict`, update the total cost by adding `cost`, and add a `(pres_first, pres_last):None` key-value pair to the inner dictionary `pres_dict` if `(pres_first, pres_last)` is not there yet. Since the cost of looking up to see if a key exists in a dictionary is `O(1)`, assume that we have `n` lines in the input txt file, then the cost of this whole block is `O(n)`.

Next, I copy the `drug_name`, `cost` (total cost of a drug), and `len(pres_dict)` (number of distict prescribers for each drug) to a list and sort it twice: first by `drug_name`, then by `cost`. This guarantees that if there is a tie in cost, drug name is in sorted order. The time complexity for this block is `O(klog(k))`, where `k` is the number of distinct values `drug_name`.

I then use the sorted list above to write to output file. This takes `O(k)`, so in general, the runtime of my program is either `O(n)` or `O(klog(k))`, whichever greater, with `n` is the number of lines in the input txt file, and `k` is the number of distinct values `drug_name`

# Run instruction

Either type `run.sh` or `python3 ./src/medicine_count.py ./input/itcont.txt ./output/top_cost_drug.txt` in your Terminal

# Repo directory structure

The directory structure for my submission:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── top_cost_drug.txt

# Contact
trung.n@ucsc.edu
