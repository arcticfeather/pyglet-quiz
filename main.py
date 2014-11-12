import pyglet
from pyglet.window import key
import random
import quiz_resources

####### Classes #############

class Player():

    def __init__(self, buttons, controller_number, player_number,):
        self.buzzer = buttons[0];
        self.answer_buttons = buttons[1:]
        self.player_number = player_number
        self.controller_number = controller_number
        self.name = "Player "+str(player_number)

    def set_avatar(self,avatar):
        self.avatar = avatar

class PlayerSelect():

    def __init__(self):
        self.players= [] 
        self.state = "activate_players"
        self.player_batch = pyglet.graphics.Batch()
        self.avatar_batch = pyglet.graphics.Batch()

    def is_player_active(self, player_number):
        found = False
        for player in self.players:
            if player.player_number == player_number:
                found = True
                break
        return found

    def get_player(self, player_number):
        found_player = False
        for player in self.players:
            if player.player_number == player_number:
                found_player = player
        return found_player       

    def clear_player_batch(self):
        self.player_batch = pyglet.graphics.Batch()

    def player_entry_key_press(self, symbol, modifiers):
        if self.state == "activate_players":
            if symbol == key._1:
                if self.is_player_active(1) == False:
                    player = Player([key._1, key.Q, key.W, key.E, key.R], 1, len(players.players)+1)
                    label = pyglet.text.Label(player.name,
                              font_name='Calibri',
                              font_size=20,
                              x=game_window.width*(0.33), y=game_window.height*(0.66),
                              color=(0,0,0,255),batch=self.player_batch)
                    self.players.append(player)
                    print "player 1 active"
            elif symbol == key._2:
                if self.is_player_active(2) == False:
                    player = Player([key._2, key.A, key.S, key.D, key.F], 2, len(players.players)+1)
                    label = pyglet.text.Label(player.name,
                              font_name='Calibri',
                              font_size=20,
                              x=game_window.width*(0.66), y=game_window.height*(0.66),
                              color=(0,0,0,255),batch=self.player_batch)
                    self.players.append(player)
                    print "player 2 active"
            elif symbol == key._3:
                if self.is_player_active(3) == False:
                    player = Player([key._3, key.T, key.Y, key.U, key.I], 3, len(players.players)+1)
                    label = pyglet.text.Label(player.name,
                              font_name='Calibri',
                              font_size=20,
                              x=game_window.width*(0.33), y=game_window.height*(0.33),
                              color=(0,0,0,255),batch=self.player_batch)
                    self.players.append(player)
                    print "player 3 active"
            elif symbol == key._4:
                if self.is_player_active(4) == False:
                    player = Player([key._4, key.G, key.H, key.J, key.K], 4, len(players.players)+1)
                    label = pyglet.text.Label(player.name,
                              font_name='Calibri',
                              font_size=20,
                              x=game_window.width*(0.66), y=game_window.height*(0.33),
                              color=(0,0,0,255),batch=self.player_batch)
                    self.players.append( player)
                    print "player 4 active"
            elif symbol == key.SPACE:
                self.state = "avatar_select"
        elif self.state.startswith("waiting"):
            if symbol == key.SPACE:
                self.state = self.state[8:]

    def game_draw(self):
        self.player_batch.draw()
        self.avatar_batch.draw()

    def control_draw(self):
        if self.state == "activate_players":
            pass

    def update(self):
        global control_window_state
        if self.state == "activate_players":
            if len(self.players) >= 4:
                print "4 players"
                self.state = "waiting_avatar_select"
        elif self.state == "avatar_select":
            control_window_state = "avatar_select"
            for player in players.players:
                avatar_select.append(AvatarSelect(player.player_number))
            self.state = "finished"

class AvatarSelect():    

    def __init__(self,player):
        global frame_width
        self.avatar_sprites = []        # container for avatar sprites
        self.chosen_avatar = None       # chosen_avatar
        # currently selected avatar - start on random number
        self.active_avatar = random.randint(0, len(quiz_resources.characters)-1)   
        self.moving = False             # currently being animated?
        self.player_number = player     # player number
        self.avatar_batch = pyglet.graphics.Batch()
        self.ui_batch = pyglet.graphics.Batch()
        self.x1 = (game_window.width/(len(players.players)+1))*(self.player_number)-(frame_width/2)
        self.x2 = self.x1+frame_width

        # set keys
        if player == 1:
            self.up_key = key.R
            self.down_key = key.Q
            self.buzzer = key._1
        elif player == 2:
            self.up_key = key.F
            self.down_key = key.A
            self.buzzer = key._2
        elif player == 3:
            self.up_key = key.I
            self.down_key = key.T
            self.buzzer = key._3
        elif player == 4:
            self.up_key = key.K
            self.down_key = key.G
            self.buzzer = key._4
        for counter, character in enumerate(quiz_resources.characters): 
            sprite=pyglet.sprite.Sprite(character, x=self.x1, y=(counter*(avatar_height+avatar_spacing)+180+(frame_width-avatar_height)/2)-(self.active_avatar*(avatar_spacing+avatar_height)), batch=self.avatar_batch, group=background)
            sprite.vx=0
            sprite.vy=0
            sprite.target_y=sprite.y
            self.avatar_sprites.append(sprite)
         
        # add background elements
        # avatar frame
        self.frame = pyglet.sprite.Sprite(quiz_resources.frame, x=self.x1, y=180, group=foreground)
        # bottom white box
        vertex_list = self.ui_batch.add(4, pyglet.gl.GL_QUADS, middle,
                ('v2i', [self.x1, 0, self.x2, 0, self.x2, 125, self.x1, 125]),  #('v2i', [x1, y1, x2, y1, x2, y2, x1, y2]),
                ('c4B', [255, 255, 255, 255] * 4),
            )
        # top white box
        vertex_list = self.ui_batch.add(4, pyglet.gl.GL_QUADS, middle,
                ('v2i', [self.x1, 340, self.x2, 340, self.x2, 600, self.x1, 600]), #('v2i', [x1, y1, x2, y1, x2, y2, x1, y2]),
                ('c4B', [255, 255, 255, 255] * 4),
            )

        self.arrow_up = pyglet.sprite.Sprite(quiz_resources.arrow_up, x=self.x1+27, y=350, group=foreground)
        self.arrow_down = pyglet.sprite.Sprite(quiz_resources.arrow_down, x=self.x1+27, y=50, group=foreground)
        print "arrow up: {0}".format(self.x1+27)
        print "arrow down: {0}".format(self.x1+27)

    def game_draw(self):
        if self.chosen_avatar == None:
            self.avatar_batch.draw()
            self.frame.draw()
            self.ui_batch.draw()
            if self.active_avatar > 0:
                self.arrow_down.draw()
            if self.active_avatar < 9:
                self.arrow_up.draw()
        else:
            players.get_player(self.player_number).set_avatar(self.chosen_avatar)
            self.avatar_sprites[self.chosen_avatar].draw()
            self.frame = pyglet.sprite.Sprite(quiz_resources.selected_frame, x=self.x1, y=180, group=foreground)
            self.frame.draw()

    def control_draw(self):
        pass

    def on_key_press(self,symbol, modifiers):
        if self.chosen_avatar == None:
            if symbol == self.up_key:
                if self.active_avatar>0 and self.moving == False:
                    self.moving = True
                    self.active_avatar-=1
                    print "Player {0}: {1}".format(self.player_number, self.active_avatar)
                    for avatar in self.avatar_sprites:
                        avatar.vy = 300
                        avatar.target_y = avatar.y+avatar_height+20
            elif symbol == self.down_key:
                if self.active_avatar<9 and self.moving == False:
                    self.moving = True
                    self.active_avatar+=1
                    print "Player {0}: {1}".format(self.player_number, self.active_avatar)
                    for avatar in self.avatar_sprites:
                        avatar.vy = -300
                        avatar.target_y = avatar.y-avatar_height-20
            elif symbol == self.buzzer:
                print "Player {0} has chosen avatar {1}".format(self.player_number, self.active_avatar)
                self.chosen_avatar = self.active_avatar

    def update(self,dt):
        for avatar in self.avatar_sprites:
            if (avatar.vy >=0) and (avatar.y >= avatar.target_y): 
                avatar.vy = 0
                avatar.y = avatar.target_y
                self.moving = False
            elif (avatar.vy <=0) and (avatar.y <= avatar.target_y): 
                avatar.vy = 0
                avatar.y = avatar.target_y
                self.moving = False
            elif avatar.vy != 0:
                avatar.y += avatar.vy * dt


####### Global variables ####

# windows
control_window = pyglet.window.Window(width=300, height=300)
control_window.set_location(800, 100)  # set window to right side of screen
game_window = pyglet.window.Window()
pyglet.gl.glClearColor(1, 1, 1, 1)

# Current state
control_window_state = "player_select"    # Possible states are: player_select, in_question

# Items used in game
players = PlayerSelect()
avatar_select = []

# Background layers
background = pyglet.graphics.OrderedGroup(0)
middle = pyglet.graphics.OrderedGroup(1)
foreground = pyglet.graphics.OrderedGroup(2)

# Values for avatar sprites
avatar_height = 117
avatar_spacing = 20
avatar_width = 117
frame_width = 125


####### Functions ##########
@game_window.event
def on_close():
    control_window.close()

@control_window.event
def on_close():
    game_window.close()

@control_window.event
@game_window.event
def on_key_press(symbol, modifiers):
    global control_window_state
    if control_window_state.startswith("waiting"):
        if symbol == key.SPACE:
            control_window_state = control_window_state[8:]
            print control_window_state
    elif control_window_state == "player_select":
        players.player_entry_key_press(symbol, modifiers)
    elif control_window_state == "avatar_select":
        for player in avatar_select:
            player.on_key_press(symbol, modifiers)
        if all(player.chosen_avatar is not None for player in avatar_select):
            control_window_state == "waiting_questions"
            print "waiting_questions"


@control_window.event
def on_draw():
    if control_window_state == "player_select":
        control_window.clear()
        players.control_draw()
    elif control_window_state == "avatar_select":
        for player in avatar_select:
            player.control_draw() 

@game_window.event
def on_draw():
    game_window.clear()
    if control_window_state == "player_select":
        players.game_draw()
    elif control_window_state == "avatar_select":
        for player in avatar_select:
            player.game_draw() 

def update(dt):
    if control_window_state == "player_select":
        players.update()
    elif control_window_state == "avatar_select":
        for player in avatar_select:
            player.update(dt)


####### Main app ###########
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
