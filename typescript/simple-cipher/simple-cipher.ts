class SimpleCipher {

    public key: string;
    
    private readonly startIndex: number = 97;
    private readonly finishIndex: number = 122;

    constructor(cipherKey?: string) {
        if (cipherKey) {
            this.key = cipherKey
        } else {
            const intArray: number[] = []
            for(let i = 0; i < 101; i++) intArray.push(this.getRandomFromInterval(97,122))
            this.key = String.fromCharCode(...intArray);
        }
    }

    encode(plainText: string): string {
        let encodedText: string = '';
        for (let i = 0; i < plainText.length; i++) {
            let transformedChar: number = (this.key.charCodeAt(i)) + (plainText.charCodeAt(i) - this.startIndex);
            if (transformedChar > this.finishIndex) {
                transformedChar = (transformedChar - (this.finishIndex + 1)) + this.startIndex;
            }
            encodedText+=String.fromCharCode(transformedChar)
        }
        return encodedText
    }

    decode(cipherText: string) {
        let decodedText: string = '';
        for (let i = 0; i < cipherText.length; i++) {
            let transformedChar: number = (cipherText.charCodeAt(i) - this.key.charCodeAt(i));
            transformedChar < 0 ? transformedChar += (this.finishIndex + 1) : transformedChar += this.startIndex
            decodedText += String.fromCharCode(transformedChar)
        }
        return decodedText;
    }
    
    private getRandomFromInterval(min: number, max: number) {
        return Math.floor(Math.random() * (max-min+1) + min);
    }

}

export default SimpleCipher
