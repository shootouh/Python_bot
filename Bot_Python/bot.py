import random
import pyjokes
from lorem_text import lorem

# Function to recommend movies by genre
def recommend_movie(genre):
    movie_list = {
        'comedy': ['Forrest Gump', 'American Pie', 'Shrek'],
        'drama': ['The Green Mile', 'The Pianist', 'The Shawshank Redemption'],
        'science fiction': ['Star Wars', 'The Matrix', 'Interstellar']
    }
    
    if genre in movie_list:
        return random.choice(movie_list[genre])
    else:
        return f"Sorry, I can't find movies for the genre '{genre}'. Available genres: {', '.join(movie_list.keys())}"

# Function to recommend music by genre
def recommend_music(genre):
    music_list = {
        'rock': ['Queen', 'Led Zeppelin', 'Pink Floyd'],
        'pop': ['Michael Jackson', 'Madonna', 'Taylor Swift'],
        'electronic': ['Daft Punk', 'The Chemical Brothers', 'Deadmau5']
    }
    
    if genre in music_list:
        return random.choice(music_list[genre])
    else:
        return f"Sorry, I can't find music for the genre '{genre}'. Available genres: {', '.join(music_list.keys())}"

# Function for playing "Rock-Paper-Scissors"
def play_rock_paper_scissors(user_choice):
    choices = ['rock', 'scissors', 'paper']
    bot_choice = random.choice(choices)
    
    if user_choice in choices:
        if user_choice == bot_choice:
            return f"It's a tie! Both chose {user_choice}."
        elif (
            (user_choice == 'rock' and bot_choice == 'scissors') or
            (user_choice == 'scissors' and bot_choice == 'paper') or
            (user_choice == 'paper' and bot_choice == 'rock')
        ):
            return f"You win! You chose {user_choice}, and the bot chose {bot_choice}."
        else:
            return f"The bot wins! You chose {user_choice}, and the bot chose {bot_choice}."
    else:
        return "Invalid choice. Please try again."

# Function for telling a joke
def tell_joke():
    joke = pyjokes.get_joke()
    return joke

# Function for telling an interesting story
def tell_story():
    stories = lorem.paragraph()
    return stories

# Main function for processing user messages
def chat_bot():
    print("Hello! I'm your entertainment chat bot. I can recommend movies, music, games, tell jokes, share interesting stories, and play a game. For a list of commands, type 'help'.")

    while True:
        user_input = input("Your message: ").lower()

        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'help':
            print("Available commands:")
            print("- To get a movie recommendation: 'movie'. To specify a genre: 'comedy', 'drama', 'science fiction'.")
            print("- To get music recommendations: 'music'. To specify a genre: 'rock', 'pop', 'electronic'.")
            print("- To play 'Rock-Paper-Scissors': 'rps'.")
            print("- For a joke: 'Tell me a joke'.")
            print("- For an interesting story: 'Tell me a story'.")
            print("- To exit: 'Exit'.")
        elif 'movie' in user_input:
            genre = input("What genre of movies are you interested in? (comedy, drama, science fiction) - ")
            recommendation = recommend_movie(genre)
            print(f"Processing... \n'{recommendation}'.")
        elif 'music' in user_input:
            genre = input("What genre of music are you interested in? (rock, pop, electronic) - ")
            recommendation = recommend_music(genre)
            print(f"Processing... \n'{recommendation}'.")
        elif 'rps' in user_input:
            game_choice = input("Choose: 'rock', 'scissors', or 'paper': ")
            result = play_rock_paper_scissors(game_choice)
            print(result)
        elif 'joke' in user_input:
            joke = tell_joke()
            print(joke)
        elif 'story' in user_input:
            story = tell_story()
            print(story)
        else:
            print("I don't understand your request. Please try again.")

if __name__ == "__main__":
    chat_bot()
