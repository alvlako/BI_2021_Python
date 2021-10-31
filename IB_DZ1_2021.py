functions_available = ['transcribe', 'reverse', 'complement', 'reverse_complement']
print('Available functions: ', *functions_available)
while True:
    print('Enter command')
    command = str(input())
    if command == 'exit':
        break
    if command not in functions_available:
        print('Command not available')
        continue
    error_collector = 1
    while error_collector == 1:
        print('Enter sequence')
        user_seq = str(input())
        try:
            if user_seq.lower().find('t') > -1 and user_seq.lower().find('u') > -1:
                error_collector = 1
                print('Mixed U-T sequence')
        except ValueError:
            error_collector = 0
        for letter in user_seq:
            if letter in ['A', 'T', 'G', 'C', 'U', 'a', 't', 'g', 'c', 'u']:
                error_collector = 0
            else:
                print('Invalid alphabet. Try again!')
                error_collector = 1
    transcription_table = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 'u', 't': 'a', 'g': 'c', 'c': 'g'}
    complement_table_DNA = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}
    complement_table_RNA = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G', 'a': 'u', 'u': 'a', 'g': 'c', 'c': 'g'}

    def transcribe(user_seq):
        transcribed_seq = user_seq
        transcribed_seq_final = ''
        try:
            for letter in transcribed_seq:
                transcribed_seq_final = transcribed_seq_final + transcription_table[letter]
        except KeyError:
            print('Unknown nucleotides (did you type RNA sequence?)')
        return transcribed_seq_final

    def reverse(user_seq):
        return user_seq[::-1]

    def complement(user_seq):
        print('Type D for DNA, R for RNA')
        nucleic_acid_type = str(input())
        complement_seq = user_seq
        complement_seq_final = ''
        if nucleic_acid_type != 'D' and nucleic_acid_type != 'R':
            print('Wrong nucleic acid type. Try again!')
        else:
            if nucleic_acid_type == 'D':
                try:
                    for letter in complement_seq:
                        complement_seq_final = complement_seq_final + complement_table_DNA[letter]
                    return complement_seq_final
                except KeyError:
                    print('RNA nucleotides in DNA, try again!')
            if nucleic_acid_type == 'R':
                try:
                    for letter in complement_seq:
                        complement_seq_final = complement_seq_final + complement_table_RNA[letter]
                    return complement_seq_final
                except KeyError:
                    print('DNA nucleotides in RNA, try again!')
        
    def reverse_complement(user_seq):
        reverted_complement = str(complement(user_seq))[::-1]
        return reverted_complement
    function_table = {'transcribe': transcribe, 'reverse': reverse, 'complement': complement, 'reverse_complement': reverse_complement}
    result = function_table[command](user_seq)
    if result is not None:
        print(result)
