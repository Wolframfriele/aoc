use aoc::year_2015::{day_01, day_02, day_03, day_04};
use clap::Parser;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// The AOC day to run
    #[arg(short, long, default_value = None)]
    day: Option<u8>,

    /// If all day's need to be run
    #[arg(short, long)]
    all: bool,
}

fn run_single_day(day: Option<u8>) {
    match day {
        None => {
            println!("Run last day");
            day_04::run_day();
        }
        Some(num) => match num {
            1 => day_01::run_day(),
            2 => day_02::run_day(),
            3 => day_03::run_day(),
            4 => day_04::run_day(),
            _ => println!("Day not implemented."),
        },
    }
}

fn main() {
    let args = Args::parse();

    if args.all {
        println!("All day's will be run");
        day_01::run_day();
        day_02::run_day();
        day_03::run_day();
        day_04::run_day();
    } else {
        run_single_day(args.day);
    }
}
