#[derive(Debug)]
struct Race {
    time: u32,
    distance: u32
}
fn main() {
    part1();
    part2();
}

fn part1() {
    let data = include_str!("../input.txt").lines().collect::<Vec<&str>>();
    let mut newdata = Vec::new();

    for time in data[0].split(" ") {
        if time.is_empty() || time.starts_with("Time") {
            continue;
        }
        let time = time.parse::<u32>().unwrap();
        newdata.push(Race {
            time: time,
            distance: 0
        });
    }
    let mut newdataiter = newdata.iter_mut();

    for distance in data[1].split(" ").collect::<Vec<&str>>() {
        if distance.is_empty() || distance.starts_with("Distance") {
            continue;
        }

        let distance = distance.parse::<u32>().unwrap();
        newdataiter.next().unwrap().distance = distance;
    }



    let mut nums_to_multiply = Vec::new();

    for race in newdata {
        let mut times_in_race = 0;
        for ms in 0..race.time {
            if ms*(race.time-ms) > race.distance {
                times_in_race += 1;
            }
        }
        nums_to_multiply.push(times_in_race)
    }

    println!("part 1:{:?}", nums_to_multiply.iter().product::<u32>());
}
// alternative: You can also just find the first and the last timepoint where you can release the button as everything in between should give the same result
fn part2() {
    let data = include_str!("../input.txt").lines().collect::<Vec<&str>>();


    let mut nums = Vec::new();

    for line in data.iter() {
        let raw = line.replace(" ", "").replace("Time:", "").replace("Distance:", "").parse::<u64>().unwrap();
        nums.push(raw);
    }
    println!("{:?}", nums);

    let mut counter = 0;
    for time in 0..nums[0] {
        if time * (nums[0] - time) > nums[1] {
            counter += 1;
        }
    }



    println!("part 2: {}", counter);

    // better versions

    let mut counter = 0;
    let mut firsttime = 0;
    for time in 0..nums[0] {
        if time * (nums[0] - time) > nums[1] {
            counter += 1;
            firsttime = time;
            break;
        }
    }

    let mut lasttime = 0;
    for time in (firsttime..nums[0]).rev() {
        if time * (nums[0] - time) > nums[1] {
            lasttime = time;
            break;
        }
    }
    counter += lasttime - firsttime;

    println!("part 2 better: {}", counter);

}