# hushhush
no talking. a minimal discord bot

The purpose of this bot is to create a discord server where and attempt at communication is silenced. after a couple seconds. 

This bot will delete messages after a set timeout, and will acknowledge a user command by deleting the command isntantly. if a message sent is not deleted instantly (unless its already deleting messages instantly) then the bot did not recognize the message

test cases:

- change name to hush
  - @hush after 1s | bot starts watching the channel
  - @hush ignore @garyyo
  - @hush watch @garyyo
  - @hush stop | bot stops watching channel

- change name to quiet
  - @quiet after 2min 5sec
  - @quiet ignore @garyyo
  - @quiet watch @garyyo
  - @quiet after -6m | does not recognize
  - @quiet after | does not recognize
  - @quiet after 0 | the bot stops watching the channel

- stretch goals
  - @hush-hush after 1 s 2min
  - @hush-hush delete any text goes here
  - @hush-hush message @usertag messagetext
    - pings a user and instructs them to click reaction (a check mark). upon this the messagetext is revealed (through edit?) to everyone for the default amount of time, or until the same user reacts with an x or unreacts the checkmark

can bot react to own message with controls, and detect when a user also reacts to that message as a way to control it?
