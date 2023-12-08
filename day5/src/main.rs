struct Converter {
    kind: String,
    values: Vec<Vec<i32>>
}

fn main() {
    let data = include_str!("../example.txt").split("\n").collect::<Vec<&str>>();
    
    let mut seeds = Vec::new();
    
    for (index, line) in data.iter().enumerate() {
        if index == 0 {
            let some = line.split(" ").collect::<Vec<&str>>();

            for item in some.iter() {
                if !item.contains("seeds") {
                    seeds.push(item.parse::<i32>().unwrap())
                } 
            }
        }
    }

    println!("{:?}", seeds);
}
