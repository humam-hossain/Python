Think about Dhaka city’s garbage collection system and its inefficiencies and the sufferings we
have to endure. What if we have a digital garbage collection system to bypass all the sufferings
and improve our city life?
Let’s consider the sources of the city's garbage.
1. Household garbage
2. SME (Small and medium-sized enterprises) garbage
3. Industrial garbage
4. GO (Government Office) / NGO (Non Government Office) garbage
5. Transportation garbage

Let’s consider the types of garbage.
1. Biodegradable garbage
2. Non-biodegradable garbage
   1. Recyclable garbage
   2. Non-recyclable garbage

Now, we know what sorts of garbage we produce and types of that garbage.
Let’s design a smart garbage collection system. The system has installed a bin in every source
(source-bin) mentioned above (1 to 5). Those bins are connected to the city-corporation's
garbage management plant bins (GMP-bin) by underground tunnels. A suction mechanism
transports the garbage from the source-bin to the GMP-bin. After collecting the garbage,
GMP-bin allocates them to 2 separate bins (Biodegradable/ B-bin and Non-biodegradable/
NB-bin). Non-biodegradable bin (NB-bin) further separates them to 2 separate bins (Recyclable/
R-bin and Non-recyclable/ NR-bin). Contents of the bins are then dumped to the plant for
processing.
Now, write a python program to design a smart garbage collection system that has the following
objects and properties.

User:
+ Name
+ Address
+ Can receive warning message and display it
+ Can check the total bill and display it

Billing-info:
+ One biodegradable garbage item 0 tk.
+ One recyclable garbage item 2 tk.
+ One non-recyclable garbage item 5 tk.
+ Has a billing catalog

Source-bin:
+ Receives garbage.
+ Has fixed capacity (e.g. can contain 10 garbage items at a time).
+ As the source-bin tends to fill; it sends a warning message to the user - “Reduce garbage production”.
+ Outputs garbage and sends to GMP-bin
+ As soon as one item gets sucked by the tunnel; source-bin updates itself to receive one more new item.
+ Can receive warning messages from other bins.
+ For any warning message it receives; it sends a warning message to the user - “Reduce garbage production”.

GMP-bin:
+ Receives garbage
+ Has fixed capacity (e.g. can contain 10 garbage items at a time).
+ As the GMP-bin tends to fill; it sends a warning message to source-bin - “Warning from GMP-bin”.
- Outputs garbage and allocates them 2 other bins based on their type
- As soon as one item gets passed to the following bins; GMP-bin updates itself to receive one more new item.
- Can receive warning messages from other bins.
- For any warning message it receives; it sends a warning message to source-bin - “Warning from GMP-bin”.
- For a given user, update the billing catalog according to the billing-info.

B-bin:
- Receives garbage
- Has unlimited capacity
- Sends to plant

NB-bin:
- Receives garbage
- Has fixed capacity (e.g. can contain 10 garbage items at a time).
- Outputs garbage and allocates them 2 other bins based on their type
- As soon as one item gets passed to the following bins; NB-bin updates itself to receive one more new item.
- As the NB-bin tends to fill; it sends a warning message to GMP-bin - “Warning from NB-bin”
- For a given user, update the billing catalog according to the billing-info.

R-bin:
- Receives garbage
- Has unlimited capacity
- Sends to plant

NR-bin:
- Receives garbage
- Has unlimited capacity
- Sends to plant

You should use local, global variables, appropriate data structure, conditionals, loops, methods
and OOP concepts such as objects, inheritance etc. to write the python program for our smart
garbage collection system.

Submission Guideline:
1. Write all codes in “Colab”.
2. Use a single “Colab” file.
3. Use comments as much as you want.
4. Make sure each code segment can communicate with other code segments.
5. Make sure each code segment generates desired output.
6. Submit the “.ipynb” file
7. No other file types are accepted.
8. Bonus points, if you can implement a user login mechanism.
