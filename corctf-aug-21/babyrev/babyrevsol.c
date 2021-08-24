#define _GNU_SOURCE
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(){

	char checkStringUTF[] = "_@Z.uEbSuFRC_uPRu_\\O";
	int rotValues[] = {2,5,11,13,17,23,29,29,37,37,41,47,53,
	53,59,61,67,71,73,79,83};
	char * memaddr;
	char final[20];
	for (int i = 0; i<20; i++){
		final[i] = 0;
	}

	printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	printf("This is the UTF output of the\nstored hex
	values: %s\n",checkStringUTF);
	memaddr = memfrob(checkStringUTF,20);

	for(int i = 0; i < 20; i++) {
		if(memaddr[i] >= 65 && memaddr[i] <= 90){
			//Capital Letter
			int calc = memaddr[i]-rotValues[i];
			if(calc < 65){
				while(calc < 65) calc = calc + 26;
			} else if (calc > 90) {
				while(calc > 90) calc = calc - 26;
			}
			final[i] = calc;

		} else if (memaddr[i] >= 97 && memaddr[i] <= 122) {
			//Lowercase
			int calc = memaddr[i]-rotValues[i];
			if(calc < 97){
				while(calc < 97) calc = calc + 26;
			} else if (calc > 122) {
				while(calc > 122) calc = calc - 26;
			}
			final[i] = calc;
		}
	}

	printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	printf("This is what is converts to when\nyou run memfrob():
	%s\n",memaddr);
	printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	printf("This is my final output:");
	for(int i = 0; i<20; i++){
		if(i == 3 || i == 8 || i == 14 || i == 17){
			printf("_");
		}
		printf("%c",final[i]);

	}



	return 1;
}
