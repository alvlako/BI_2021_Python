while True:
    print('Hello,Enter command')
    command=str(input())
    if command == 'exit':
        break
    error_collector=1
    while error_collector == 1:
        print('Enter sequence')
        user_seq=str(input())
        for letter in user_seq:
            if letter in ['A','T','G','C','U','a','t','g','c','u']:
                error_collector=0
            else:
                print('Invalid alphabet. Try again!')
                error_collector=1
    transcription_table={'A':'U','T':'A','G':'C','C':'G','a':'u','t':'a',
'g':'c','c':'g'}
    complement_table_DNA={'A':'T','T':'A','G':'C','C':'G','a':'t','t':'a',
'g':'c','c':'g'}
    complement_table_RNA={'A':'U','U':'A','G':'C','C':'G','a':'u','u':'a',
'g':'c','c':'g'}
    def transcribe (user_seq):
        transcribed_seq=user_seq
        for letter in transcribed_seq:
            transcribed_seq=transcribed_seq.replace(letter,transcription_table[letter])
        print(transcribed_seq)
    def reverse (user_seq):
        print(user_seq[::-1])
    def complement(user_seq):
        print('Print D for DNA, R for RNA')
        nucleic_acid_type=str(input())
        complement_seq=user_seq
        for letter in complement_seq:
            if nucleic_acid_type =='D':
                complement_seq=complement_seq.replace(letter,complement_table_DNA[letter])
            if nucleic_acid_type =='R':
                complement_seq=complement_seq.replace(letter,complement_table_RNA[letter])
            else:
                print('Wrong nucleic acid type. Try again!')
        print(transcribed_seq)
    def reverse_complement(user_seq):
        print(complement(user_seq)[::-1])
    function_table={'transcribe':transcribe, 'reverse':reverse,'complement':
    complement,'reverse complement':reverse_complement}
    result=function_table[command](user_seq)



