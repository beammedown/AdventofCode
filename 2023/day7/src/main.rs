#[derive(Debug, Clone, PartialEq)]
struct Hand {
    cards: Vec<Card>,
    bid: u32,
    combination: u8,
}

#[derive(Debug, Clone, PartialEq)]
struct Card {
    name: char,
    value: u32,
}

fn main() {
    let data = include_str!("../input.txt");

    let mut handstack = Vec::new();

    for line in data.lines() {
        let mut tmp = Vec::new();
        for item in line.split_whitespace().collect::<Vec<&str>>().first().unwrap().chars() {

            let val = match item {
                'A' => 14,
                'K' => 13,
                'Q' => 12,
                'J' => 11,
                'T' => 10,
                _ => item.to_digit(10).unwrap(),
            };

            tmp.push(Card {
                name: item,
                value: val,
            });
        }

        let mut get_combination = 0; // HighCard

        let possibilities = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'];

        for card in &tmp {

            for item in possibilities.iter() {
                if tmp.iter().filter(|x| x.name==*item).count() == 5 {
                    get_combination = 6; // FiveofAKind 
                } else if tmp.iter().filter(|x| x.name==*item).count() == 4 {
                    get_combination = 5; // FourOfAKind
                } else if tmp.iter().filter(|x| x.name==*item).count() == 2 && tmp.iter().filter(|&x| x.value == card.value && x.name != *item).count() == 3 {
                    get_combination = 4; // FullHouse
                } else if tmp.iter().filter(|x| x.name==*item).count() == 3 && tmp.iter().filter(|&x| x.value == card.value && x.name != *item).count() <= 1 {
                    get_combination = 3; // ThreeOfAKind
                } else if tmp.iter().filter(|x| x.name==*item).count() == 2 && tmp.iter().filter(|&x| x.value == card.value && x.name != *item).count() == 2 {
                    get_combination = 2; // TwoPairs
                } else if tmp.iter().filter(|x| x.name==*item).count() == 2 && tmp.iter().filter(|&x| x.value == card.value && x.name != *item).count() <= 1{
                    get_combination = 1; // OnePair
                } 
            }

/*            if tmp.iter().filter(|&x| x.value == card.value).count() == 5 {
                get_combination = 6; // FiveofAKind 
            } else if tmp.iter().filter(|&x| x.value == card.value).count() == 4 {
                get_combination = 5; // FourOfAKind
            } else if tmp.iter().filter(|&x| x.value == card.value).count() == 3 && tmp.iter().filter(|&x| x.value == card.value).count() <= 1 {
                get_combination = 3; // ThreeOfAKind
            } else if tmp.iter().filter(|&x| x.value == card.value).count() == 2 && tmp.iter().filter(|&x| x.value == card.value ).count() == 2 {
                get_combination = 2; // TwoPairs
            } else if tmp.iter().filter(|&x| x.value == card.value).count() == 2 && tmp.iter().filter(|&x| x.value == card.value).count() == 3 {
                get_combination = 4; // FullHouse
            } else if tmp.iter().filter(|&x| x.value == card.value).count() == 2 && tmp.iter().filter(|&x| x.value == card.value).count() <= 1{
                get_combination = 1; // OnePair
            } */
        }

        handstack.push(Hand {
            cards: tmp,
            bid: line.split_whitespace().collect::<Vec<&str>>().last().unwrap().parse::<u32>().unwrap(),
            combination: get_combination,
        });
    }

    let mut ranking = Vec::new();

    // Ranking the hands against each othter
    let mut throwout = handstack.clone();

    while throwout.len() > 0 {
        let tmp = throwout.clone();
        let mut highest = tmp.last().unwrap().clone();

        for hand in tmp {
            if hand.combination > highest.combination {
                highest = hand;
            }



            else if hand.combination == highest.combination {
                let mut counter = 0;
                while counter < hand.cards.len() {
                    if hand.cards[counter].value > highest.cards[counter].value {
                        highest = hand.clone();
                        break;
                    } else if hand.cards[counter].value < highest.cards[counter].value {
                        break;
                    } else {
                        counter += 1;
                    }
                }
            }
        }

        ranking.push(highest.clone());
        throwout.retain(|x| x != &highest);
    }
    let mut product = 0;

    for (index, hand) in ranking.iter().enumerate() {
        product += hand.bid * (ranking.len() - index) as u32;
    }

    println!("The product is: {}", product);
}
