impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let n1: u64 = num1.parse().unwrap();
        let n2: u64 = num2.parse().unwrap();
        (n1 + n2).to_string()
    }
}