import random

team_ODI_best = ["Gilchrist", "Tendulkar", "Lara", "Kohli", "deVilliers", "Kallis", "Ponting", "Akram", "Warne", "Mulitaran", "McGrath"]
team_T20_best = ["Gayle", "Sharma", "Root", "deKock", "McCulum", "Dhoni", "Afridi", "Bravo", "Khan", "Gul", "Malinga"]

def my_scorecard(give_it_a_dictionary, players_name, players_score):
    the_scorecard = give_it_a_dictionary
    if players_name in [the_scorecard.keys()][0]:
        the_scorecard[players_name] = the_scorecard[players_name] + int(players_score)
    elif players_name not in [the_scorecard.keys()][0]:
        the_scorecard[players_name] = players_score

    return the_scorecard

def get_batsman_total(scorecard, batsman_name):
    if batsman_name in [scorecard.keys()][0]:
        return scorecard[batsman_name]
    elif batsman_name not in [scorecard.keys()]:
        return 0

def bowling_figures(give_it_a_ditionary, players_name, wickets, runs_conceded):
    bowling_card = give_it_a_ditionary
    if players_name in [bowling_card.keys()][0]:
        bowling_card[players_name][0] = bowling_card[players_name][0] + wickets
        bowling_card[players_name][1] = bowling_card[players_name][1] + runs_conceded
    elif players_name not in [bowling_card.keys()][0]:
        bowling_card[players_name] = [wickets, runs_conceded]
    return bowling_card

def check_for_a_winner(score_1, score_2, balls_left, wickets):
    if (score_1 > score_2) and (balls_left == 0) or (wickets == 10):
        return ("Team ODI best wins"), False
    elif (score_2 > score_1):
        return ("Team T20 best wins"), False
    elif (balls_left == 0) or (wickets == 10) and (score_1 == score_2):
        return ("We have a tie!"), False

print("\n\n  Welcome to my cricket game\n")

batting_team = "Team ODI best"
bowling_team = "Team T20 best"
batting = team_ODI_best
bowling = team_T20_best
target_score = 0

for innings in range (1, 3):
    game_on = True
    if (innings == 2):
       target_score = team_total
    while(game_on):

        print("Batting: {}\n".format(batting_team))

        on_strike_batsman = batting[0]
        non_striker_batsman = batting[1]

        batsman_one_total = 0
        bowler_one_wickets = 0
        bowler_runs_conceded = 0
        next_batsmen = 1
        wickets = 0
        team_one_score_card = {}
        team_two_bowling_scorecard = {}
        team_total = 0
        balls_left = 60

        for overs in range(0, 10):
            bowler_name = random.choice(bowling)
            for ball in range(1, 7):
                what_happened = random.randint(0, 6)
                if (what_happened == 5):
                    print("{}.{}: {} to {}: OUT!".format(overs, ball, bowler_name, on_strike_batsman))
                    bowler_one_wickets += 1
                    wickets += 1
                    my_scorecard(team_one_score_card, on_strike_batsman, 0)

                    if (next_batsmen != 10):
                        if (ball < 6):
                            on_strike_batsman = batting[next_batsmen + 1]
                            next_batsmen += 1
                        elif (ball == 6):
                            on_strike_batsman, non_striker_batsman = non_striker_batsman, batting[next_batsmen + 1]
                            bowling_figures(team_two_bowling_scorecard, bowler_name, bowler_one_wickets,
                                            bowler_runs_conceded)
                            next_batsmen += 1
                    elif (wickets == 10):
                        bowling_figures(team_two_bowling_scorecard, bowler_name, bowler_one_wickets, bowler_runs_conceded)
                        print("\nINNINGS OVER: {}.{}: Total: {}: {} {}, {} {} : {} {}: {}".format(overs, ball, team_total,
                                                                         on_strike_batsman,
                                                                        get_batsman_total(team_one_score_card, on_strike_batsman),
                                                                         non_striker_batsman,
                                                                         get_batsman_total(team_one_score_card,
                                                                                                       non_striker_batsman),
                                                                      bowler_name, team_two_bowling_scorecard[bowler_name][0],
                                                                        team_two_bowling_scorecard[bowler_name][1]))
                        if (innings == 2):
                            result, game_on = check_for_a_winner(target_score, team_total, balls_left, wickets)
                            print(result)

                        game_on = False
                        break
                else:
                    team_total = team_total + what_happened
                    bowler_runs_conceded = bowler_runs_conceded + what_happened
                    my_scorecard(team_one_score_card, on_strike_batsman, what_happened)
                    print("{}.{}: {} to {}: {}".format(overs, ball, bowler_name, on_strike_batsman, what_happened))
                    if (what_happened in [1, 3]) or (ball == 6):
                        on_strike_batsman, non_striker_batsman = non_striker_batsman, on_strike_batsman
                        bowling_figures(team_two_bowling_scorecard, bowler_name, bowler_one_wickets, bowler_runs_conceded)
                    if (innings == 2) and (team_total > target_score):
                        result, game_on = check_for_a_winner(target_score, team_total, balls_left, wickets)
                        bowling_figures(team_two_bowling_scorecard, bowler_name, bowler_one_wickets, bowler_runs_conceded)

                        print("\nINNININGS OVER {}.{}: Total: {}/{}: Batsman: {} {}, {} {}; Bowler: {} {}-{}\n***\n".format(
                                        overs, ball, team_total, wickets, on_strike_batsman,
                                        get_batsman_total(team_one_score_card, on_strike_batsman),
                                        non_striker_batsman,
                                        get_batsman_total(team_one_score_card, non_striker_batsman), bowler_name,
                                        team_two_bowling_scorecard[bowler_name][0], team_two_bowling_scorecard[bowler_name][1]))
                        print("\n")
                        print(result)

                        break


            if (game_on == True):
                print("\nEnd of over {}: Total: {}-{}, Batsmen: {} {}, {} {}; Bowler: {} {}-{} \n***\n ".format(overs+1, team_total,
                                                                                                                wickets,
                                                                                                             on_strike_batsman,
                                                                        get_batsman_total(team_one_score_card, on_strike_batsman),
                                                                         non_striker_batsman,
                                                                         get_batsman_total(team_one_score_card,
                                                                           non_striker_batsman),
                                                                           bowler_name,
                                                                         team_two_bowling_scorecard[bowler_name][0],
                                                                        team_two_bowling_scorecard[bowler_name][1]))
            bowler_one_wickets = 0
            bowler_runs_conceded = 0

            if (overs == 9):
                game_on = False
                if (innings == 2):
                    result, game_on = check_for_a_winner(target_score, team_total, balls_left, wickets)
                    print(result)

            if (game_on == False):
                break

    print("\nTeam Batting: {} scorecard".format(batting_team))
    print(team_one_score_card)
    print("\nTeam Bowling: {}  figures".format(bowling_team))
    print(team_two_bowling_scorecard)
    batting = team_T20_best
    bowling = team_ODI_best
    batting_team = "team T20_best"
    bowling_team = "team ODI best"


