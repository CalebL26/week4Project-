import random
import time

def generate_powerball_numbers():
    # Generate five random numbers for white balls
    white_balls = [random.randint(1, 69) for _ in range(5)]
    # Generate one random number for the red ball
    red_ball = random.randint(1, 26)
    return white_balls, red_ball

def main():
    play = input("Would you like to play PowerBall? (yes/no): ")
    if play.lower() == 'yes':
        print("Generating PowerBall numbers...")
        time.sleep(2)  # Add a delay of 2 seconds to simulate number selection
        white_balls, red_ball = generate_powerball_numbers()
        print("Your PowerBall Numbers:")
        print("White Balls:", white_balls)
        print("Red Ball:", red_ball)
    else:
        print("Maybe next time!")

if __name__ == "__main__":
    main()
