fn main() {
    one();
    two();
}

fn one() {
    let data = include_str!("../input.txt").lines().collect::<Vec<&str>>();

    let mut conclusion = 0;

    for line in data {
        let winnings: Vec<i32> = line
            .split(":")
            .collect::<Vec<&str>>()[1]
            .split("|")
            .collect::<Vec<&str>>()[0]
            .split(" ")
            .collect::<Vec<&str>>()
            .iter()
            .filter_map(|s| s.parse::<i32>().ok())
            .collect();


        let customs: Vec<i32> = line.split(":")
            .collect::<Vec<&str>>()[1]
            .split("|")
            .collect::<Vec<&str>>()[1]
            .split(" ")
            .collect::<Vec<&str>>()
            .iter()
            .filter_map(|item| item.parse::<i32>().ok())
            .collect();

        let mut summe = 0;

        for num in customs.iter() {
            if winnings.iter().any(|w| w==num) {
                if summe == 0 {
                    summe = 1;
                } else {
                    summe *= 2;
                }
            }
        }
        conclusion += summe;
    }
    println!("{:?}", conclusion);
}

struct Card {
    winning_nums: Vec<i32>,
    custom_nums: Vec<i32>,
    weight: u32,
}


fn two() {
    let data = include_str!("../example.txt").lines().collect::<Vec<&str>>();

    let mut conclusion = 0;

    let mut cards = Vec::new();

    for line in data {
        let winnings: Vec<i32> = line
            .split(":")
            .collect::<Vec<&str>>()[1]
            .split("|")
            .collect::<Vec<&str>>()[0]
            .split(" ")
            .collect::<Vec<&str>>()
            .iter()
            .filter_map(|s| s.parse::<i32>().ok())
            .collect();


        let customs: Vec<i32> = line.split(":")
            .collect::<Vec<&str>>()[1]
            .split("|")
            .collect::<Vec<&str>>()[1]
            .split(" ")
            .collect::<Vec<&str>>()
            .iter()
            .filter_map(|item| item.parse::<i32>().ok())
            .collect();

        

        cards.push(Card{
            winning_nums: winnings,
            custom_nums: customs,
            weight: 1
        });
    }

    let mut counter = 0;
    let mut counter2 = Vec::new();

    let cardslen = cards.len();

    for (index, card) in cards.iter_mut().enumerate() {
        if counter2.len() > 0 {
            card.weight += counter2[0];
            counter2.remove(0);
        }

        counter = 0;
        for num in card.custom_nums.iter() {
            if card.winning_nums.iter().any(|x| x==num) {
                counter += 1;
            }
        }

        for s in 1..counter+1 {
            if index+s >= cardslen {
                continue;
            }
            if s >= counter2.len() {
                counter2.push(card.weight);
            } else {
                counter2[s] += card.weight;
            }
        }
    }

    println!("{:?}", counter2);


    for card in cards.iter() {
        println!("{}", card.weight);
        conclusion += card.weight;
    }

    println!("{:?}", conclusion);
}