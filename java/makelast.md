public int[] makeLast(int[] nums) {
 int[] last = new int[nums.length * 2]; 
 last[last.length - 1] = nums[nums.length - 1];
 return last;
}
