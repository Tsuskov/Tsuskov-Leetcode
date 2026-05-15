impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        
        let mut x = n;
        while x % 3 == 0 {
            x /= 3;
        }
        
        x == 1
    }
}