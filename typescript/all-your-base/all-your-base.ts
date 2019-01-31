class Converter {
    convert(toConvert: number[], sourceBase: number, resultBase: number): number[] {
        // (1 * 2^5) + (1 * 2^3) + (1 * 2^1)
        const a = resultBase;
        console.log(a);
        return toConvert
        .map( (digit: number, index: number) => (digit * Math.pow(sourceBase,  ((toConvert.length - 1 ) - index))))

        // Falta unir las unidades si es menor que la base resultante;

    }
}
export default Converter