# jerkbot-matrix

Jerkbot is an OpenAI chatbot for the [Matrix](https://matrix.org/) chat protocol.  It is named for the sarcastic jerk personality I use for my instance.  You can set any default personality you would like.  It can be changed at any time, and each user has their own separate chat history with their chosen personality setting.  Users can interact with each others chat histories for collaboration if they would like, but otherwise, conversations are separated.

## Installation

```
pip3 install matrix_client openai
```

Get an [OpenAI API](https://platform.openai.com/signup) key 

Set up a [Matrix account](https://app.element.io/#/welcome) for your bot.  You'll need the username, password, and access token.  The access token is located at the bottom of the Help & About section of the settings.

Plug those into the appropriate variables in the MatrixBotLauncher.py.

To use the solo version, just swap jerkbot with jerkbot_solo in MatrixBotLauncher.py.

```
python3 MatrixBotLauncher.py
```


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

## Screenshots

### Default personality
![image](https://user-images.githubusercontent.com/127710567/234451304-c9997a73-c3ec-43c7-a5c2-f3e40d9b1283.png)

### Persona function
![image](https://user-images.githubusercontent.com/127710567/234452164-3a21889d-c801-41e2-8879-a122c7add623.png)
![image](https://user-images.githubusercontent.com/127710567/234451144-b780ee8e-9dfa-4bd0-9471-1ea5da07e4d2.png)

