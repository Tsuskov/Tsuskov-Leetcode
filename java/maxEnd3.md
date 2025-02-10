public int[] maxEnd3(int[] nums) {
  if (nums[0] > nums[nums.length -1]){
    return new int[] {nums[0],nums[0],nums[0]};
  }
  else {
    return new int[] {nums[nums.length -1],nums[nums.length -1],nums[nums.length -1]};
  }
}
