##Here is fastq filtrator


#GC-filtering
def filter_gc(input_list, gc_bounds, save_filtered):
    input_list_1 = list()
    output_list_failed_1 = list()
    for n in range (0, len(input_list)):
        if n % 4 == 1:
            gc = 100*(input_list[n].count('G') + input_list[n].count('С')) / len(input_list[n])
            if float(gc_bounds[0]) <= gc <= float(gc_bounds[1]):
                input_list_1.append(input_list[n - 1])
                input_list_1.append(input_list[n])
                input_list_1.append(input_list[n + 1])
                input_list_1.append(input_list[n + 2])
            else:
                if save_filtered == True:
                    output_list_failed_1.append(input_list[n - 1])
                    output_list_failed_1.append(input_list[n])
                    output_list_failed_1.append(input_list[n + 1])
                    output_list_failed_1.append(input_list[n + 2])
    return(input_list_1, output_list_failed_1)


#length filtering
def filter_length(input_list, length_bounds, save_filtered, gc_bounds):
    input_list, _ = filter_gc(input_list, gc_bounds, save_filtered) 
    input_list_2 = list()
    output_list_failed_2 = list()
    _, output_from_1 = filter_gc(input_list, gc_bounds, save_filtered)
    if input_list == []:
        return(input_list, output_list_failed_2 + output_from_1)  
    for n in range (0, len(input_list)):
        if n % 4 == 1:
            length = len(input_list[n])
            if float(length_bounds[0]) <= length <= float(length_bounds[1]):
                input_list_2.append(input_list[n - 1])
                input_list_2.append(input_list[n])
                input_list_2.append(input_list[n + 1])
                input_list_2.append(input_list[n + 2])
            else:
                if save_filtered == True:
                    output_list_failed_2.append(input_list[n - 1])
                    output_list_failed_2.append(input_list[n])
                    output_list_failed_2.append(input_list[n + 1])
                    output_list_failed_2.append(input_list[n + 2])
    return(input_list_2, output_list_failed_2 + output_from_1)


#quality filtering
def filter_quality(input_list, quality_threshold, save_filtered, length_bounds, gc_bounds):
    input_list_final, _ = filter_length(input_list, length_bounds, save_filtered, gc_bounds)
    output_passed_final = list()
    output_list_failed_3 = list()
    _, output_from_2 = filter_length(input_list, length_bounds, save_filtered, gc_bounds)
    if input_list_final == []:
        output_failed = output_from_2 + output_list_failed_3
        return(output_passed_final,output_failed) 
    for n in range (0, len(input_list_final)):
        recoded = list()
        if (n + 1) % 4 == 0:
            for i in input_list[n]:
                recoded.append(ord(i) - 33)
            mean = sum(recoded) / len(recoded)
            if mean >= int(quality_threshold):
                output_passed_final.append(input_list_final[n - 3] + '\n')
                output_passed_final.append(input_list_final[n - 2] + '\n')
                output_passed_final.append(input_list_final[n - 1] + '\n')
                output_passed_final.append(input_list_final[n] + '\n')
            else:
                if save_filtered == True:
                    output_list_failed_3.append(input_list[n - 3])
                    output_list_failed_3.append(input_list[n - 2])
                    output_list_failed_3.append(input_list[n - 1])
                    output_list_failed_3.append(input_list[n])
    #merging failed reads
    output_failed = output_from_2 + output_list_failed_3
    return(output_passed_final,output_failed)


print('Hello, you are about to run fastq filtrator')
#reading and checking the validity of input file format
print('Please, specify the path to your input fastq file')
input_fastq = input()
while True:
    try:
        int(input_fastq)
        print('It must be a string, not a number')
        input_fastq = input()
    except ValueError:
        if input_fastq.endswith('fastq'):
            break
        else:
            print('Wrong file format, must be fastq. Do you want to ignore? (y/n)')
            if input() == 'y':
                break
            else:
                input_fastq = input()

#reading prefix
print('Please specify your output file(-s) prefix (absolute). If you want to specify the full path, type False')
prefix = input()

#reading and checking the validity of output file format
if prefix == 'False':
    print('Please, specify the path to the output fastq file with reads passed the filtration step')
    output_file_passed = input()
    while True:
        try:
            int(output_file_passed)
            print('It must be a string, not a number')
            output_file_passed = input()
        except ValueError:
            if output_file_passed.endswith('fastq'):
                break
            else:
                print('Wrong file format, must be fastq. Do you want to ignore? (y/n)')
                if input() == 'y':
                    break
                else:
                    output_file_passed = input()
else:
    output_file_passed = prefix + '_passed.fastq'
               
#asking whether failed reads are needed to be saved and checking for the validity of answer
print('Would you like to save filtered results (filtration failed)? Type y/n')
y = str(input())
while True:
    if y == 'y':
        save_filtered = True
        break
    else:
        if y == 'n':
            save_filtered = False
            output_file_failed = ''
            break 
        else:
            print('Sorry, wrong format of answer')
            if input() == 'y':
                break
            else:
                y = input()

#reading and checking the validity of output file format for failed reads
if save_filtered == True and prefix == 'False':
    print('Please, specify the path to the output fastq file with reads failed the filtration step')
    output_file_failed = input()
    while True:
        try:
            int(output_file_failed)
            print('It must be a string, not a number')
            output_file_failed = input()
        except ValueError:
            if output_file_failed.endswith('fastq'):
                break
            else:
                print('Wrong file format, must be fastq. Do you want to ignore? (y/n)')
                if input() == 'y':
                    break
                else:
                    output_file_failed = input()
elif save_filtered == True and prefix != 'False':
    output_file_failed = prefix + '_failed.fastq'
                
#reading and checking the validity of gc content bounds input
print('Please, specify your desired gc content bounds. You can type 2 thresholds or only one which will be considered as a higher one. The default options are 0, 100. Please enter your values as following (in one string) 0 100')
gc_bounds = str(input()).split(' ')
if gc_bounds == '':
    gc_bounds = [0, 100]
else:
    while True:
        try:
            int(gc_bounds[0])
            int(gc_bounds[1])
            break
        except ValueError:
            print('It must be a number, not a character')
            gc_bounds = str(input()).split(' ')
           
#reading and checking the validity of length content bounds input
print('Please, specify your desired length bounds. You can type 2 thresholds or only one which will be considered as a higher one. The default options are 0, 2**32. Please enter your values as following (in one string) 0 100')
length_bounds = str(input()).split(' ')
if length_bounds == '':
    length_bounds = [0, 2**32]
else:
    while True:
        try:
            str(length_bounds[0])
            str(length_bounds[1])
            break
        except ValueError:
            print('It must be a number, not a character')
            length_bounds = str(input()).split(' ')

#reading and checking the validity of quality threshold input
print('Please specify your quality threshold. Please enter one value. The defauls option is 0')
quality_threshold = str(input())
if quality_threshold == '':
    quality_threshold = 0
else:
    while True:
        try:
            int(quality_threshold)
            break
        except ValueError:
            print('It must be a number, not a character')
            quality_threshold = input()


#main function
def main(input_fastq = input_fastq, quality_threshold = quality_threshold, save_filtered = save_filtered,
length_bounds = length_bounds, gc_bounds = gc_bounds, output_file_passed = output_file_passed, output_file_failed = output_file_failed,
output_file_prefix = prefix):
    with open(input_fastq) as input_fastq:
        input_list = input_fastq.read().splitlines()
    if output_file_prefix == 'False':
        output_file_passed = open(output_file_passed, 'w')
        if save_filtered == True:
            output_file_failed = open(output_file_failed, 'w')
    else:
        output_file_passed = output_file_prefix + '_passed.fastq'
        output_file_passed = open(output_file_passed, 'w')
        if save_filtered == True:
            output_file_failed = output_file_prefix + '_failed.fastq'
            output_file_failed = open(output_file_failed, 'w')
    passed_reads, failed_reads = filter_quality(input_list, quality_threshold, save_filtered, length_bounds, gc_bounds)
    for p in passed_reads:
        output_file_passed.write(p)
    if save_filtered == True:
        for f in failed_reads:
            output_file_failed.write(f + '\n')
        output_file_failed.close()
    output_file_passed.close()

#call of main function
main(input_fastq = input_fastq, quality_threshold = quality_threshold, save_filtered = save_filtered,
length_bounds = length_bounds, gc_bounds = gc_bounds, output_file_passed = output_file_passed, output_file_failed = output_file_failed,
output_file_prefix = prefix)
