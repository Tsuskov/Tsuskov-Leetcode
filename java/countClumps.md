public int countClumps(int[] nums) {
    if (nums.length < 2) {
        return 0;
    }
    int clumps = 0;
    boolean inclump = false;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] == nums[i - 1]) {
            if (!inclump) {
                clumps++;
                inclump = true;
            }
        } else {
            inclump = false;
        }
    }
    
    return clumps;
}