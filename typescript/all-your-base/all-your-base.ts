class Converter {
    convert(toConvert: number[], sourceBase: number, resultBase: number): number[] {
        // (1 * 2^5) + (1 * 2^3) + (1 * 2^1)
        const a = resultBase;
        console.log(a);
        const result: number[] = toConvert
        .map( (digit: number, index: number) => (digit * Math.pow(sourceBase,  ((toConvert.length - 1 ) - index))))
        const parsedResult = result.reduce( (a: number, b: number) => a + b)
        return [parsedResult]
        
        // Falta unir las unidades si es menor que la base resultante;

    }
}
export default Converter