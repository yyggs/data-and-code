#include <stdio.h>
#include <math.h>


#define N 2187
#define reps 1
#include <omp.h> 

double xx[N][N], yy[N][N], zz;
int len[N];  
int threads[8];

void init1(void);
void init2(void);
void loop1(void);
void loop2(void);
void valid1(void);
void valid2(void);


int main(int argc, char *argv[]) { 

  double start1,start2,end1,end2;
    omp_set_num_threads(8);
  init1(); 

  start1 = omp_get_wtime(); 

  for (int r=0; r<reps; r++){ 
    loop1();
  } 

  end1  = omp_get_wtime();  

  valid1(); 

  //printf("%f,", (float)(end1-start1)); 


  init2(); 

  start2 = omp_get_wtime(); 

  for (int r=0; r<reps; r++){ 
    loop2();
  } 

  end2  = omp_get_wtime(); 

  valid2(); 
    // FILE *file = fopen("threads_data3.txt", "w");
    // if (file == NULL) {
    //     printf("Error opening file!\n");
    //     return 1;
    // }

    // for (int i = 0; i < N; i++) {
    //     fprintf(file, "%d, %d\n", i, threads[i]);
    // }

    // fclose(file);
    int num = 0;
    for(int i = 0; i < 8; i++){
        printf("%d  ", threads[i]);
        num += threads[i];
    }
    printf("%d  ", num);
  //printf("%f\n", (float)(end2-start2)); 
} 

void init1(void){

  for (int i=0; i<N; i++){ 
    for (int j=0; j<N; j++){ 
      xx[i][j] = 0.0; 
      yy[i][j] = 1.618*(i+j); 
    }
  }

}

void init2(void){ 
  int i,j, expr; 

  for (int i=0; i<N; i++){ 
    expr =  i%( 4*(i/70) + 1); 
    if ( expr == 0) { 
      len[i] = N/3;
    }
    else {
      len[i] = 3; 
    }
  }

  for (int i=0; i<N; i++){ 
    for (int j=0; j<N; j++){ 
      yy[i][j] = (double) (i*j+1) / (double) (N*N); 
    }
  }

  zz = 0.0;
 
} 

void loop1(void) { 
 
#pragma omp parallel for default(none) shared(xx,yy) schedule(runtime)
  for (int i=0; i<N; i++){ 
    for (int j=0; j<i; j++){
      xx[i][j] += log(yy[i][j]) / (double) N;
    } 
  }

} 



void loop2(void) {

  double rNN = 1.0 / (double) (N*N);  

#pragma omp parallel for default(none) shared(rNN,yy,len,threads) reduction(+:zz) schedule(static, 64)
  for (int i=0; i<N; i++){ 
    if(len[i] > 3) threads[omp_get_thread_num()]++;
    for (int j=0; j < len[i]; j++){
      for (int k=0; k<j; k++){ 
	    zz += (k+1) * yy[i][j]* yy[i][j] * rNN;
      } 
    }
  }

}

void valid1(void) { 
  
  double sumxx= 0.0; 
  for (int i=0; i<N; i++){ 
    for (int j=0; j<N; j++){ 
      sumxx += xx[i][j];
    }
  }
  //printf("Sum of xx is %lf      ", sumxx);

} 


void valid2(void) { 
  
  //printf("zz is %lf      ", zz);

} 
 

