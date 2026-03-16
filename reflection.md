# 💭 Reflection: Game Glitch Investigator - Anh Nhu 3/4/2026 

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
First time I ran it, I submitted 50 it told me to "Go HIHGER" for my guess. The answer was 3.
Hints didn't match my guess.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  It says that I have 8 attemps, but before I even start my first guess it already said in the main
  window: "Attemps left: 7" (it should be 8).
  But when I have 1 attemp left, the game stopped: "Out of attemps."
  When I started over to a new game, it didn't refresh the page and still had my previous answer.
  I unchecked the button "Show hint", clicked "Submit Guess" and nothing happened - it didn't deduct attempts I have.
  However, I was unable to restart the game. Had to refresh the page to start playing again.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Gemini to guide me breaking down the big picture, and prompted my questions into VSCode's Copilot.   
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
At first, I just thought that the number of attempts for each level were off. I talked to Copilot and it pointed out to me the range of number for level Normal and Hard should swap. I didn't notice this before so I think AI did a great job helping me.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I asked AI to fix the code where it should deduct the attemps I have after every guess. It fixed most of it, but when I submit my guess for the first time it didn't subtract one. I played the game twice to confirm this error and asked Copilot to fix it again. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed by making Copilot explaining what the code really does, then run the app.py for at least twice to check the error is gone.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I generated pytest and it shows that my code is running perfectly the way I want.
- Did AI help you design or understand any tests? How?
After I asked AI to generate test cases I wanted, it suggested adding another test the simulates the bug behavior I wanted to fix earlier. I'm glad, because I forgot about that case when developed pytest.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because Steamlit runs the Pythons script all over again every time the user interacts, whether by clicking a button or typing a box.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Friend, image every single of your interact with the screen causes the the whole code to restart your process from line 1.
- What change did you make that finally gave the game a stable secret number?
I wrapped the secret generation in an if check: "if "secret" not in st.session_state" so the random number is only generated once every first run. The run after that just reads the saved value. Copilot also suggested treating the same to the other pieces of game state (attemps, score, status, history) to avoid resetting all of them.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I worked on this project the first day being assigned and today, the day before the deadline. I recommend myself not doing this, because it definitely took me a while to get into the groove again.
For the AI-learning aspect, I think that the next time I approach a project, I will first try to map out all the errors that I observed, instead of just note-taking 3-4 of them, fix them, and continue finding more. 
When I wrote test cases for the code, Copilot asked me if I wanted to add a test for a bug I fixed earlier, and I was surprised that it was smart enough to go beyond just responding to my prompts.
From the next time, I will ask AI to explain why the code was written that way to understand how the developer wrote the code, instead of jumping straight into asking AI to fix the bugs.
