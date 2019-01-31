class FlattenArray {
    static flatten(array: any[]): number[] {
        const flattened: number[] = [];
        this.flattenRecursion(array, flattened);
        return flattened
    }

    private static flattenRecursion(array: any[], progress: number[]) {
        array.forEach( elem => {
            if (!Array.isArray(elem)) {
                if (elem != undefined) {
                    progress.push(elem);
                }
            } else {
                this.flattenRecursion(elem, progress);
            }
        })
    }
}

export default FlattenArray;