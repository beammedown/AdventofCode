fn main() {
    let numberword = vec!["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    let data = include_str!("../../dayone.txt").trim();

    for line in data.lines() {
        let firstindex = -1;
        let lastindex = -1;

        for (index, ch) in line.chars().enumerate() {
            if ch.is_numeric() {
                
            }
        }
    }
}
