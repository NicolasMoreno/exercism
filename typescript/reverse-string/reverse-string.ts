class ReverseString {
    static reverse(word: string): string {
        let reverseWord = '';
        if(word !== '') {
            for(let i = word.length - 1; i >= 0; i--) {
                reverseWord += word.charAt(i);
            }
        }
        return reverseWord;
    }
}

export default ReverseString
