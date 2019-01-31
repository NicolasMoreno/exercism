export function keep<T>(array: T[], callback: (e: T) => boolean): T[] {
    const result: T[] = []
    array.map(callback)
    .forEach( (condition: boolean, index: number) => condition ? result.push(array[index]) : false);
    return result;
}

export function discard<T>(array: T[], callback: (e: T) => boolean): T[] {
    const result: T[] = []
    array.map(callback)
    .forEach( (condition: boolean, index: number) => !condition ? result.push(array[index]) : false);
    return result;
}
