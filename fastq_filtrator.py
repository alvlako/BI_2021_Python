# Here is fastq filtrator


# GC-filtering
def filter_gc(input_list, gc_bounds, save_filtered):
    input_list_1 = list()
    output_list_failed_1 = list()
    for n in range(0, len(input_list)):
        if n % 4 == 1:
            gc = 100*2*input_list[n].count('G')/len(input_list[n])
            if gc > int(gc_bounds[0]) and gc < int(gc_bounds[1]):
                input_list_1.append(input_list[n-1])
                input_list_1.append(input_list[n])
                input_list_1.append(input_list[n+1])
                input_list_1.append(input_list[n+2])
            else:
                if save_filtered is True:
                    output_list_failed_1.append(input_list[n-1])
                    output_list_failed_1.append(input_list[n])
                    output_list_failed_1.append(input_list[n+1])
                    output_list_failed_1.append(input_list[n+2])
    return(input_list_1, output_list_failed_1)


# length filtering
def filter_length(input_list, length_bounds, save_filtered, gc_bounds):
    input_list, _ = filter_gc(input_list, gc_bounds, save_filtered)
    input_list_2 = list()
    output_list_failed_2 = list()
    _, output_from_1 = filter_gc(input_list, gc_bounds, save_filtered)
    for n in range(0, len(input_list)):
        if n % 4 == 1:
            length = len(input_list[n])
            if length > int(length_bounds[0]) and length < int(length_bounds[1]):
                input_list_2.append(input_list[n-1])
                input_list_2.append(input_list[n])
                input_list_2.append(input_list[n+1])
                input_list_2.append(input_list[n+2])
            else:
                if save_filtered is True:
                    output_list_failed_2.append(input_list[n-1])
                    output_list_failed_2.append(input_list[n])
                    output_list_failed_2.append(input_list[n+1])
                    output_list_failed_2.append(input_list[n+2])
    return(input_list_2, output_list_failed_2 + output_from_1)


# quality filtering
def filter_quality(input_list, quality_threshold, save_filtered, length_bounds, gc_bounds):
    input_list_final, _ = filter_length(input_list, length_bounds, save_filtered, gc_bounds)
    output_passed_final = list()
    output_list_failed_3 = list()
    _, output_from_2 = filter_length(input_list, length_bounds, save_filtered, gc_bounds)
    for n in range(0, len(input_list)):
        recoded = list()
        if n % 4 == 3:
            for i in input_list[n]:
                recoded.append(int(ord(i)) - 33)
            mean = sum(recoded) / len(recoded)
            if mean > int(quality_threshold):
                output_passed_final.append(input_list_final[n-3] + '\n')
                output_passed_final.append(input_list_final[n-2] + '\n')
                output_passed_final.append(input_list_final[n-1] + '\n')
                output_passed_final.append(input_list_final[n] + '\n')
            else:
                if save_filtered is True:
                    output_list_failed_3.append(input_list[n-3])
                    output_list_failed_3.append(input_list[n-2])
                    output_list_failed_3.append(input_list[n-1])
                    output_list_failed_3.append(input_list[n])
    # merging failed reads
    output_failed = output_from_2 + output_list_failed_3
    return(output_passed_final, output_failed)


print('Hello, you are about to run fastq filtrator')
# reading and checking the validity of input file format
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
            print('Wrong file format, must be fastq')
            input_fastq = input()
            
# reading and checking the validity of output file format
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
            print('Wrong file format, must be fastq')
            output_file_passed = input()
                
# asking whether failed reads are needed to be saved and checking for the validity of answer
print('Would you like to save filtered results (filtration failed)? Type y/n')
y = str(input())
while True:
    if y == 'y':
        save_filtered = True
        break
    else:
        if y == 'n':
            save_filtered = False
            break 
        else:
            print('Sorry, wrong format of answer')
# reading and checking the validity of output file format for failed reads
if y == 'y':
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
                print('Wrong file format, must be fastq')
                output_file_failed = input()
                
# reading and checking the validity of gc content bounds input
print('Please, specify your desired gc content bounds. You can type 2 thresholds or only one which will be considered as a higher one.')
print('The default options are 0, 100. Please enter your values as following (in one string) 0 100')
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
            
# reading and checking the validity of length content bounds input
print('Please, specify your desired length bounds. You can type 2 thresholds or only one which will be considered as a higher one.')
print('The default options are 0, 2**32. Please enter your values as following (in one string) 0 100')
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

# reading and checking the validity of quality threshold input
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
# opening files and processing of lines in input file
input_fastq = open(input_fastq)
output_file_passed = open(output_file_passed, 'w')
if y== 'y':
    output_file_failed = open(output_file_failed, 'w')
input_list = input_fastq.readlines()


# main function
def main(input_list, quality_threshold, save_filtered, length_bounds, gc_bounds):
    # little functions running, this function will call others and merge the lists to the final files
    return filter_quality(input_list, quality_threshold, save_filtered, length_bounds, gc_bounds)


# call of main function and writing results to files
passed_reads, failed_reads = main(input_list, quality_threshold, save_filtered, length_bounds, gc_bounds)
for p in passed_reads:
    output_file_passed.write(p+'\n')
for f in failed_reads:
    output_file_failed.write(f+'\n')
