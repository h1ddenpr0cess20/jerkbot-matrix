# jerkbot-matrix

Jerkbot is an OpenAI chatbot for the Matrix chat protocol.  It is named for the sarcastic jerk personality I use for my instance.  You can set any default personality you would like.  It can be changed at any time, and each user has their own separate chat history with their chosen personality setting.  Users can interact with each others chat histories for collaboration if they would like, but otherwise, conversations are separated.

## Installation

Install the dependencies matrix_client and openai

Get an OpenAI API key

Set up a Matrix account for your bot.  You'll need the username, password, and access token.

Plug those into the appropriate variables in the MatrixBotLauncher.py and run it.

To use the solo version, just swap jerkbot with jerkbot_solo in MatrixBotLauncher.py


## Use

**.ai _message_ or botname: _message_**
    Basic usage.
    Personality is preset by bot operator.
    In jerkbot-solo, just chat like normal instead of using this.
  
**.x _user message_**
    This allows you to talk to another user's chat history.
    _user_ is the display name of the user whose history you want to use
    (Not available in jerkbot-solo)
      
**.persona _personality_**
    Changes the personality.  It can be a character, personality type, object, idea.
    Don't use a custom prompt here.
    If you want to use a custom prompt, use .stock then use .ai _custom prompt_
        
**.reset**
    Reset to preset personality
    
**.stock**
    Remove personality and reset to standard GPT settings
    
**.prompt help**
    Lists custom prompts available for functions not easily set with .persona.
    
**.prompt _prompt_**
    Use special prompt from list of prompts
