class Game:
    all = []
    def __init__(self, title):
        self.title = title

        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise Exception("Title must be a string")
        elif len(new_title) <= 0:
            raise Exception("Title must be longer than 0 characters")
        elif hasattr(self, "title"):
            raise Exception("Title already exists and cannot be changed")
        else:
            self._title = new_title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        player_results = [result.score for result in Result.all
                    if result.player == player]
        return sum(player_results)/len(player_results)

########################

class Player:
    all = []
    def __init__(self, username):
        self.username = username

        type(self).all.append(self)

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise Exception("Username must be a string")
        elif not 2 <= len(new_username) <= 16:
            raise Exception("Username must be between 2 and 16 in characters")
        else:
            self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player == self ]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        if self.games_played().count(game):
            return True
        else:
            return False

    def num_times_played(self, game):
        if self.played_game(game):
            return len([result for result in self.results()
                        if result.game == game])
        else:
            return 0

########################

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        type(self).all.append(self)

    ##player property
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, new_player):
        if not isinstance(new_player, Player):
            raise Exception("Must be of type Player class")
        else:
            self._player = new_player

    ##game property
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, new_game):
        if not isinstance(new_game, Game):
            raise Exception("Must be of type Game class")
        else:
            self._game = new_game

    ##score property
    # @property
    # def score(self):
    #     return self._score
    # @score.setter
    # def score(self, new_score):
    #     if not isinstance(new_score, int):
    #         raise Exception("Score must be an integer")
    #     elif hasattr(self, "score"):
    #         raise Exception("Score already exists and can't be reset")
    #     elif not 1<= new_score <= 5000:
    #         raise Exception("Score must be between 1 and 5000")
    #     else:
    #         self._score = new_score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
        # else:
        #     raise Exception
