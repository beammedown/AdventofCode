fn main() {
    let mut sum = 0;
    let punctuations = [
        '*', '#', '=', '$', '&', '@', '%', '+', '-', '/'
    ];
    let data = include_str!("../daythree.txt")
        .lines()
        .collect::<Vec<_>>()
        .iter()
        .map(|x| x.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();
    for (line, item) in data.iter().enumerate() {
        let mut num = 0;
        let mut counts = false;
        let mut firstnum_index = 0;
        let mut lastnum_index = item.len();

        for (index, char) in item.iter().enumerate() {
            if char.is_numeric() {
                if num == 0 {
                    firstnum_index = index;
                    lastnum_index = index;
                    num = char.to_digit(10).unwrap();
                } else {
                    lastnum_index = index;
                    num = num * 10 + char.to_digit(10).unwrap();
                }
                if punctuations.iter().any(|x| 
                    if index < item.len()-1 {*x==item[index + 1]} else {false} || 
                    if index > 0 {*x==item[index - 1]} else {false} || 
                    if line > 0 { data[line - 1][index] == *x} else {false} || 
                    if line < data.len()-1 {data[line + 1][index] == *x} else {false} ||

                    if firstnum_index > 0 && line < data.len()-1 && line > 0 {data[line+1][firstnum_index-1] == *x || data[line-1][firstnum_index-1] == *x} else {false} ||
                    if firstnum_index > 0 && line == 0 {data[line+1][firstnum_index-1]==*x} else {false} ||
                    if firstnum_index > 0 && line == data.len()-1 {data[line-1][firstnum_index-1]==*x} else {false} ||

                    if lastnum_index < item.len()-1 && line > 0 && line < data.len()-1 {data[line-1][lastnum_index+1]==*x || data[line+1][lastnum_index+1] == *x } else {false} ||
                    if lastnum_index < item.len()-1 && line == 0 {data[line+1][lastnum_index+1]==*x} else {false} ||
                    if lastnum_index < item.len()-1 && line == data.len()-1 {data[line-1][lastnum_index+1]==*x} else {false}
                ) {
                    counts = true;
                }
            } else {
                if counts {
                    sum += num;
                }
                num = 0;
                counts = false;

            }
        }
        if counts {
            sum += num;
        }
        num = 0;
        counts = false;
    }
    println!("part one: {}", sum);
    two();
}

fn two() {
    let data = include_str!("../daythree.txt")
        .lines()
        .collect::<Vec<_>>()
        .iter()
        .map(|x| x.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let mut numbers: Vec<Number> = Vec::new();
    let mut newnum = Number{num: 0, firstchar: (data.len()+1, 0), lastchar: (0, 0)};
    for (line_index, line) in data.iter().enumerate() {
        for (cindex, cha) in line.iter().enumerate() {
            if cha.is_numeric() {
                newnum.num = newnum.num*10 + cha.to_digit(10).unwrap();
                if newnum.firstchar.0 == data.len()+1 {
                    newnum.firstchar = (line_index, cindex);
                }
                newnum.lastchar = (line_index, cindex);
            } else {

                if newnum.num != 0 {
                    numbers.push(newnum);
                    newnum = Number{num: 0, firstchar: (data.len()+1, 0), lastchar: (0, 0)};
                }
            }
        }
    }

    let mut summe = 0;
    let pos: [(i32, i32); 8] = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1,- 1)];
    for (line_index, line) in data.iter().enumerate() {
        for (cindex, cha) in line.iter().enumerate() {
            if cha == &'*' {
                let mut nums = Vec::new();
                let mut counter = 0;
                for number in numbers.iter() {
                    for changed_pos in pos {
                        if line_index as i32 + changed_pos.0 == number.firstchar.0 as i32 && (cindex as i32+changed_pos.1 >= number.firstchar.1 as i32 && cindex as i32+changed_pos.1 <= number.lastchar.1 as i32) {
                            //println!("{:?}", line_index);
                            nums.push(number.num);
                            counter += 1;
                            break;
                        }
                }
                if counter == 2 {
                    summe += nums[0]*nums[1];
                    counter = 0;
                    nums.clear();
                }
            }
        }
    }
}
    println!("part two: {:?}", summe);
}

#[derive(Debug)]
struct Number {
    num: u32,
    firstchar: (usize, usize),
    lastchar: (usize, usize)
}
