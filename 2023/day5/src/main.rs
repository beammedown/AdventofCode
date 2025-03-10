#[derive(Debug, Clone)]
struct Converter {
    kind: String,
    values: Vec<Vec<u64>>,
}

fn main() {
    let data = include_str!("../input.txt")
        .split("\n")
        .collect::<Vec<&str>>();

    let mut seeds = Vec::new();
    let mut convers: Vec<Converter> = Vec::new();

    //initialization
    for (index, line) in data.iter().enumerate() {
        if line.is_empty() {
            convers.push(Converter {
                kind: String::new(),
                values: Vec::new(),
            });
            continue;
        }
        if index == 0 {
            let some = line.split(" ").collect::<Vec<&str>>();

            for item in some.iter() {
                if !item.contains("seeds") {
                    seeds.push(item.parse::<u64>().unwrap())
                }
            }
        } else if !line.chars().next().unwrap().is_numeric() {
            convers.last_mut().unwrap().kind = line.replace(":", "");
        } else {
            let newvals = line
                .split(" ")
                .collect::<Vec<&str>>()
                .iter()
                .map(|x| x.parse::<u64>().unwrap())
                .collect::<Vec<u64>>();
            convers.last_mut().unwrap().values.push(newvals);
        }
    }

    println!("arrived");
    let mut newseeds = Vec::new();
    let mut skipper = false;
    let mut smallest = Vec::new();
    
    println!("round 1: {:?}", part2(&mut seeds.clone(), convers.clone()));


    for item in 0..seeds.iter().len() {
        if skipper {
            skipper = false;
            continue;
        }
        println!("{}/{}", item/2, seeds.iter().len()/2);
        for num in seeds[item]..(seeds[item] + seeds[item + 1]) {
            newseeds.push(num.clone());
        }
        println!("newseeds.len(): {:?}", newseeds.iter().len());
        let newsmall = part2(&mut newseeds, convers.clone());
        smallest.push(newsmall.clone());
        newseeds.clear();
        skipper = true;
    }
    println!("smallest: {:?}", smallest.iter().min().unwrap());

}

fn part2(association: &mut Vec<u64>, convers: Vec<Converter>) -> &u64 {

    let mut skipper = false;
    for item in convers.iter() {
        for seed in association.iter_mut() {
            skipper = false;
            for song in item.values.iter() {
                if skipper {
                    skipper = false;
                    break;
                }
                if *seed >= *song.iter().nth(1).unwrap()
                    && *seed <= *song.iter().nth(1).unwrap() + song.iter().nth(2).unwrap()
                {
                    for num in *song.iter().nth(1).unwrap()
                        ..song.iter().nth(1).unwrap() + song.iter().nth(2).unwrap()
                    {
                        if num == *seed {
                            let newval = &(song.iter().nth(0).unwrap()
                                + (num - song.iter().nth(1).unwrap()));
                            *seed = *newval;
                            skipper = true;
                            break;
                        }
                    }
                } else {
                    //println!("{} is not in range", seed);
                    continue;
                }
            }
        }
        //println!("{:?}", association);
    }

    //println!("{:?}", association);
    let smallest = association.iter().min().unwrap();
    return smallest;
}
