print("""     @@@@@@@@@@@@@@                                            
            @@@ @@@   @@@@ @@@@                                        
         @@@@@              @@@@@                                      
        @@@                    @@@                                     
       @@@@@                  @@@@@                                   
       @@@@@@                 @@@@@@                                   
       @@@@@@                 @@@@@@                                   
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                    
        @@@@@@@   @@@@@@   @@@@@@@                                     
          @@@     @@@@@@     @@@                                      
@@@       @@@    @@@@@@@@    @@@@     @@@                             
@@@@     @@@@@@#@@@@@@@@@@@@@@@@      @@@@                             
 @@ @@@@    @@@@   @@@@@@@@   @@@@    @@@@ @@                            
@@@@@@@@@@@@   @@@@@@ @@ @@@@@@  @@@@@@@@@@@                           
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                  
        @@@@@@@@@@@@@@@@@@@@@@@@                                      
             @@@@@@@@@@@@@@@@                                          
            @@@@@@@@@@@@@@@@@@                                         
        @@@@@@@@@@@@@@@@@@@@@@@@@@                                     
@@@@@@@@@@@  @@@@@@  @@@@  @@@ @@@@@@@@                              
 @@@@@@@@                      @@@@@@@@@                               
 @@@@                            @@@@                                
 @@                              @@ """)
print("welcome to my island!\nThere are two door in front of you.🚪a red door and 🚪a blue door")
the_door=input("Which door do you want to open?").lower()
if the_door=="red":
    print("Great! now you entered a room.")
    the_doorcolor=input("you found three boxes:🎁 white ,🎁 black ,🎁 green\nwhich box do you open?").lower()
    if the_doorcolor=="white":
        print("Opps! you opend a box filled with snakes🐍 🐍 🐍 ")
    elif the_doorcolor =="green":
        print("Congratutations! you found the treasure!💰💰💰")
    elif the_doorcolor=="black":
        print("Opps! you opend a box filled with spiders💣💣💣")
    else :
        print("Invalid choice!🤷‍♂️🤷‍♂️🤷‍♂️")
elif the_door=="blue": 
     print("Opss! you chose the crocodile door.")  
     print("Game over!🐊 🐊 🐊")
else:
    print("Invalid choice!🤷‍♂️🤷‍♂️🤷‍♂️")