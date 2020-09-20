#Description of my work

From what I understood, my mission was to create a triple program files - one to act as Https Server (Receiver according to the pdf), one as Https Client (Sender acc to the pdf) and one to generate paramteres for keys calculations in the first two .

I was not sure what the meaning of X and Y in the server's and the client's formulas, I assumed they were private ints which initialized on the creation of each object - based on the fact that each of them will be a randomized  number between (0, p-1) where p is a prime number.

In order to implement my work, I created 2 main abstract files - 
*AbstractSign - this file includes the abstract class 'SignatureCreator' and 3 derived classes ['ServerSignatureCreator', 'ClientSignatureCreator', 'ProxySignatureCreator'].
                each out those 3 classes implements the sign function according to the given formula.
*HttspConnector- this file includes 2 abstract classes : ['HttpsServer', 'HttpsClient'] - they of course represent https server and client abstract classes

Then, I created 3 packages, with the thinking that each component should be isolated and should be able to run on it's on (even when the client has nothing to do with the server down), as i might want to run each component on a differnet server, they shouldnt be coupled to each other.
Inside each package I implemented the needed funcionality according to the assesment, using flask to run Https server and client.

I used postman + unittests to check weather my servers are running correctly.

Use ReadMe.md to run the project correctly.

Thank you.
