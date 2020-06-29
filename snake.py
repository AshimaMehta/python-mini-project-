
import curses
import random
import time 
# to initialize windows 
window=curses.initscr()
#to check visibiltiy
curses.curs_set(0)
win_height, win_width=window.getmaxyx()
new_window=curses.newwin(win_height , win_width,0,0)
new_win.keypad(true)
new_win.timeout(200)
For i in range(win_width-1):
	new_win.addch(0,i,curses.ACS_BOARD)
	new_win.addch(win_height-1,i,curses.ACS_BOARD)
	For i in range (win_height-1):
		new_win.addch(i,0,curses.ACS_BOARD)
		new_win.addch(i,win_width-1,curses.ACS_BOARD)
		snake_x=win_width//4
		snake_y=win_width//2
		snake=[
		[snake_y,snake_x] ,
		[snake_y,snake_x-1],
		[snake_y,snake_x-2]
		]
	Food=[win_height//2,win_width//2]
	new_win.addch(Food[0],Food[1],curses.ACS_DIAMOND)
	key=curses.KEY_RIGHT
	while true:
		new_key=new_win.getch()
		key=key if new_key==-1 else new_key
	if snake[0][0] in [1,win_height-1] or snake[0][1] int[1,win_width-1] or snake[0] in snake[1: ]:
		curses.beep()
		time.sleep(2)
		curses.endwin()
		print.('end game')
		quit()
		
		if key==curses.KEY_RIGHT:
			new_head=[snake[0][0],snake[0][1]+1]
		if key==curses.KEY_LEFT:
			new_head=[snake[0][0],snake[0][1]-1]
		if key==curses.KEY_UP:
			new_head=[snake[0][0]-1,snake[0][1]]
		if key==curses.KEY_DOWN:
			new_head=[snake[0][0]+1,snake[0][1]]
			
		snake.insert(0,new_head)
		
		if snake[0]==Food:
			Food=None
			while Food is None:
				new_Food=[
				random.randint(1,win_height-2)
				random.randint(1,win_width-2)
				]
		Food=new_Food if new_Food not in snake else None
		
		new_win.addch(Food[0],Food[1],curses.ACS_DIAMOND)
		
		else:
			tail=snake.pop()
			new_win.addch(int(tail[0]), int(tail[1]),' ')
	
	new_win.addch(int(snake[0][0]),int(snake[0][1]),curses.ACS_LANTERN)
			
	
			
	
	
			
	
