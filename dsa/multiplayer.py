import random
class Player:
    def _init_(self,username):
        self.username=username
        self.score=0
class Match:
    def _init_(self,player1,player2,winner):
        self.player1=player1
        self.player2=player2
        self.winner=winner
class Tournamnet:
    def _init_(self):
        self.players={}
        self.matches=[]
    def register_player(self,username):
        if username in self.players:
            print(f"{username}already registeres.")
        else:
            self.players[username]=Player(username)
            print(f"{username} registered.")
    def add_match_result(self,username1,username2,username3,winner_name):
        if winner_name not in [username1,username2]:
            print("Winner must be one of the two players.")
            return
        if username1 not in self.players or username2 not in self.players:
            print("Players(s) not registered.")
            return
        winner=self.players[winner_name]
        winner.scroe +=3
        match=Match(username1,username2,winner_name)
        winner.score+=3
        match=Match(username1,username2,winner_name)
        self.matches.append(match)
        print(f"{username1} vs {username2}=> {winner_name}")
    def display_leaderboard(self):
        sorted_players=(self.players.values(),key=lambda p:(-p.score,p.username))
        for i,player in enumerate (sorted_players,1):
            print(f"{i}.{player.username}-{player.score}")
    def start_tournament(self):
        if len(self.players)<2:
            print("Not enough players to start the tournament.")
            return
        usernames=list(self.players.keys())
        random.shuffle(usernames)
        while len(usernames)>1:
            player1=usernames.pop()
            player2=usernames.pop()
            winner_name=random.choice([player1,player2])
            self.add_match_result(player1,player2,winner_name)
            usernames.append(winner_name)
        print("Tournament completed.")
        self.display_leaderboard()
        
                