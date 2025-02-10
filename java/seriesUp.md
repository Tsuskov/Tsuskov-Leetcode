public int[] seriesUp(int n) {
    int lang = n * (n + 1) / 2; 
    int[] num = new int[lang]; 
    int index = 0; 

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) { 
            num[index] = j;
            index++; 
        }
    }

    return num;
}