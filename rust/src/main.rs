use clap::Parser;
mod day_01;
mod day_02;
mod day_03;

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

fn main() {
    let args = Args::parse();

    if args.all {
        println!("All day's will be run")
    } else {
        match args.day {
            None => println!("Run last day"),
            Some(num) => match num {
                1 => day_01::run_day(),
                2 => day_02::run_day(),
                3 => day_03::run_day(),
                _ => println!("Day not implemented."),
            },
        }
    }
}
