fn main() {
    let _numberword = vec!["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    let data = include_str!("../../dayone.txt").trim();
    let mut lines = Vec::new();
    
    for line in data.lines() {
        let mut firstindex: i32 = -1;
        let mut lastindex: i32 = -1;

        for (index, ch) in line.chars().enumerate() {
            if ch.is_numeric() && firstindex == -1 {
                firstindex = ch.to_digit(10).unwrap() as i32; 
            }
            let curr_last = line.chars().nth_back(index).unwrap();
            if curr_last.is_numeric() && lastindex == -1 {
                lastindex = curr_last.to_digit(10).unwrap() as i32;
            }
            if lastindex != -1 && firstindex != -1 {
                lines.push((firstindex*10)+lastindex);
                break;
            }
        }
    }
    let mut sum = 0;
    for item in lines {
        sum += item;
    }
    println!("{}", sum);
}
