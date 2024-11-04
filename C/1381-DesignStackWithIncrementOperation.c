typedef struct{
    int *values;
    int top;
    int size;
} CustomStack;

//function declarations
CustomStack* customStackCreate(int);
void customStackPush(CustomStack *, int);
int customStackPop(CustomStack *);
int isEmpty(CustomStack *);
void customStackIncrement(CustomStack *, int, int);
void customStackFree(CustomStack*);


CustomStack* customStackCreate(int maxsize){
    CustomStack* stack = (CustomStack*)malloc(sizeof(CustomStack));
    stack->size = maxsize;
    stack->top = -1;
    stack->values = (int*)malloc(sizeof(int)*maxsize);
    return stack;
}


//push operation
void customStackPush(CustomStack *stack, int val){
    if(stack->top < stack->size - 1){
        stack->values[++stack->top] = val;
    }
}


//pop operation
int customStackPop(CustomStack *stack){
    int val;
    if(isEmpty(stack)){
        return -1;
    }
    else{
        val = stack->values[stack->top];
        stack->top--;
    }
    return val;
}


//check if stack is empty
int isEmpty(CustomStack *stack){
    return stack->top == -1;
}


//increment elements of stack array
void customStackIncrement(CustomStack *stack, int k, int val){
    for(int i = 0; i < k; i++){
        if(i < stack->size){
            stack->values[i]+=val;
        }
    }
}

void customStackFree(CustomStack *stack){
    free(stack);
}