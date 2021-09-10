# cat
a Cat class so that you can create a cat object and interact with it. Create class Cat. This class should have the following:
 A name attribute that is intialized when a cat is created.
 An energy attribute that has an initial value of 2.
 A stomach capacity attribute that has an initial value of 2.
 A method called play(). If the value of energy is greater than 0, it prints a
message similar to &quot;catname says meow&quot; and then reduces the value of energy
by 1. The message has to contain the name of the cat and the sound meow.
However, if the value of energy is less than or equal to 0, it prints &quot;catname is
tired&quot; instead.
 A method called eat(). If the capacity of stomach is greater than 0, it prints a
message similar to &quot;catname says nom&quot; and then reduces the capacity of
stomach by 1. The message has to contain the name of the cat and the
sound nom. However, if the capacity of stomach is less than or equal to 0, it
prints &quot;catname is full&quot; instead.
In main(), you should have the following:
 The program asks the user to enter a name and then creates a cat object with
that name.
 The program then asks how the user would like to interact with the cat by
entering either &#39;play&#39; or &#39;feed&#39;.
 Once the user enters the option, the program calls the corresponding methods
from the Cat class to perform the interaction.
 Once the interaction is completed, the program should ask if the user would like
to continue. If the user enters &#39;y&#39;, the program will again ask how the user would
like to interact with the cat. If the user enters &#39;n&#39;, the program will end. The user
can enter either a capital letter or a lowercase letter.
