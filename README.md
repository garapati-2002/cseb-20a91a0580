# cseb-20a91a0580
lab experiments
1) CPU scheduling algorithms 
1.a) Simulate the FCFS CPU scheduling algorithm.
Program:-
#include<stdio.h>
struct fcfs
 {
	int at,st,str,ft,tat,wt;
}p[50];
main()
 {
	int i,j,n;
	float atrt=0,awt=0;
	printf("Enter the number of process:");
	scanf("%d",&n);
	printf("Enter the arrival time for process:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i].at);
	}
	printf("Enter the service time for process:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i].st);
	}
	a[0].str=a[0].at;
	for(j=0;j<n;j++)
  {
	a[j].ft=a[j].str+a[j].st;
	a[j+1].str=a[j].ft;
  }
for(i=0;i<n;i++)
  {
	a[i].tat=a[i].ft-a[i].at;
	atrt=atrt+a[i].tat;
	a[i].wt=a[i].str-a[i].at;
	awt=awt+a[i].wt;
  }
printf("Process\tAT\tST\tSTR\tFT\tTAT\tWT\n");
for(i=0;i<n;i++) {
printf("a%d\t%d\t%d\t%d\t%d\t%d\t%d\n",i,a[i].at,a[i].st,a[i].str,a[i].ft,a[i].tat,a[i].wt);
  }
atrt=atrt/n;
awt=awt/n;
printf("Average turn around time=%f",atrt);
printf("Average waiting time=%f",awt);
}
output:
![image](https://user-images.githubusercontent.com/84447482/168740607-a23d669e-2887-4215-8259-0bc8880d0971.png)

 

