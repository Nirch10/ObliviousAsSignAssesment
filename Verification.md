Algorithm Verification : 

 
 Intuitively, we can see straight from the start, that the c parameter will not affect our result.
 Then, we want to find out when z = d, and the only difference between the two equations is a and y' -x -> and in order to make them equal we need that small part to be equal.
 The only way for that is when y is equal to x

Math proof : 

d = (a - b)* c % p
y' = y + a % p
z = (y' - x - b)*c % p 
 we want z to be equal to d = > z =d =>
 d = (a - b)* c % p = z = (y' - x - b)*c % p  => (a - b)* c % p = (y' - x - b)*c % p 
 since both sides of the equation are multiplied by c and moduloed by p, we can remove them from both sides => 
 (a - b) = (y' - x - b) => we know y' = y + a % p =>
 a - b = (y + a % p - x -b) => we can remove the b's from both sides =>
 a = y + a % p - x => w move the a's to the left side of the equation =>
 a  a % p = y -x => a(1 - 1 % p) = y -x => 1%p will always be 1 (p is prime) => 
 0 = y - x => y = x;
 therefore,  the only case where our client will connect successfuly to our server is when the random value X that the client chooses is equal to the random value Y the server picks.
