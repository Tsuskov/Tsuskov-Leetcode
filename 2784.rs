impl Solution {
    pub fn is_good(nums: Vec<i32>) -> bool {
        // The length of the array should be n + 1, where n is the maximum value in the array.
        let n = *nums.iter().max().unwrap_or(&0); // The array should contain all integers from 1 to n exactly once, except for n which should appear exactly twice.
        if n <= 0 || nums.len() != (n as usize + 1) {
            // If the length of the array is not n + 1, or if n is not a positive integer, then the array cannot be good.
            return false;
        }

        let mut freq = vec![0; n as usize + 1]; // Create a frequency array to count the occurrences of each integer from 1 to n.
        for &x in &nums {
            // Iterate through the input array and count the occurrences of each integer.
            if x < 1 || x > n {
                // If any integer is outside the range [1, n], the array cannot be good.
                return false;
            }
            freq[x as usize] += 1; // Increment the frequency count for the integer x.
        }

        for value in 1..n as usize {
            // Check that each integer from 1 to n-1 appears exactly once.
            if freq[value] != 1 {
                // If any integer from 1 to n-1 does not appear exactly once, the array cannot be good.
                return false; // If any integer from 1 to n-1 appears more than once, the array cannot be good.
            }
        }

        freq[n as usize] == 2 // Finally, check that the integer n appears exactly twice. If it does, the array is good; otherwise, it is not.
    }
}
