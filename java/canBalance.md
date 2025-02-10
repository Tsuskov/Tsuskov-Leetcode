public boolean canBalance(int[] nums) {
  int sum = 0;
  for ( int num : nums){
    sum += num;
  }
  if (sum % 2 != 0){
    return false;
  }
  int half = sum / 2;
  int asum = 0;
  for ( int num : nums){
    asum += num;
    if (asum == half){
      return true;
    }
  }
  return false;
}
