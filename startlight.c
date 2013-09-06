#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
   setuid(0);
   system("cd /home/pi/raspberrypi-twitter-mood-light/; ./stream.py");

   return 0;
}