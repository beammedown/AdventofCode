fn roundone(data: &str) {
    // This is in the RGB Format
    let max_cubes = (12, 13, 14);

    let mut sum = 0;

    for line in data.lines() {
        let mut is_ok = true;
        let takes = line.split(":").last().unwrap();
        let id = line.split(":").next().unwrap().split(" ").last().unwrap().parse::<i32>().unwrap();

        for take in takes.split(";") {
            for item in take.split(",") {
                match item.split(" ").last().unwrap() {
                    "red" => {if item.split(" ").nth(1).unwrap().parse::<i32>().unwrap() > max_cubes.0 {is_ok = false}},
                    "green" => {if item.split(" ").nth(1).unwrap().parse::<i32>().unwrap() > max_cubes.1 {is_ok = false}},
                    "blue" => {if item.split(" ").nth(1).unwrap().parse::<i32>().unwrap() > max_cubes.2 {is_ok = false}},
                    _ => {}
                }
            }
        }
        if is_ok {
           sum += id;  
        }
    }
    println!("{}", sum);
}

fn roundtwo(data: &str) {
    let mut sum = 0;

    for line in data.lines() {
        let mut max_cubes = (0, 0, 0);

        

        let takes = line.split(":").last().unwrap();
//        let id = line.split(":").next().unwrap().split(" ").last().unwrap().parse::<i32>().unwrap();

        for take in takes.split(";") {
            for item in take.split(",") {
                match item.split(" ").last().unwrap() {
                    "red" => { if item.split(" ").nth(1).unwrap().parse::<i32>().unwrap() > max_cubes.0 {max_cubes.0 = item.split(" ").nth(1).unwrap().parse::<i32>().unwrap()} },
                    "green" => { if item.split(" ").nth(1).unwrap().parse::<i32>().unwrap() > max_cubes.1 {max_cubes.1 = item.split(" ").nth(1).unwrap().parse::<i32>().unwrap()} },
                    "blue" => { if item.split(" ").nth(1).unwrap().parse::<i32>().unwrap() > max_cubes.2 {max_cubes.2 = item.split(" ").nth(1).unwrap().parse::<i32>().unwrap()} },
                    _ => {}
                }
            }
        }
        sum += max_cubes.0 * max_cubes.1 * max_cubes.2;

    }
    println!("{}", sum);
}

fn main() {
    let data = include_str!("../../daytwo.txt").trim();

    roundone(data);

    roundtwo(data);

}