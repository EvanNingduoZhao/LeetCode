class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sen = ' '.join(sentence)+" "
        index = -1
        for _ in range(rows):
            index += cols
            if index%len(sen)<len(sen)-1 and sen[index%len(sen)+1]==" ":
                index+=1
            elif sen[index%len(sen)]==" ":
                continue
            else:
                while sen[index%len(sen)]!=" " or index%len(sen)==-1:
                    index-=1
        return (index+1)//(len(sen))