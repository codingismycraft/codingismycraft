// build: gcc rll.c -o rll

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct NODE {
    struct NODE* p_next;
    int value;
};

typedef struct NODE node;


struct LINKED_LIST {
    node* p_head;
    node* p_tail;
};

typedef struct LINKED_LIST linked_list;

node node_pool[50000000];
int node_pool_index = 0;


void push_end(linked_list* ll, int value){
    assert(ll != NULL);
    node* p_new_node = &node_pool[node_pool_index++];
    p_new_node->value = value;
    p_new_node->p_next = NULL;

    if (ll->p_head == NULL)
    {
        ll->p_head = p_new_node;
        ll->p_head->p_next = ll->p_tail;
        ll->p_tail = p_new_node;
    }
    else
    {
        ll->p_tail->p_next = p_new_node;
        ll->p_tail = p_new_node;
    }
}


void reverse_ll(linked_list* pp){
    assert(pp != NULL);

    node* n = pp->p_head;
    node* previous = NULL;

    while (n != NULL){
        node* n2 = n->p_next;
        n->p_next = previous;
        previous = n;
        n = n2;
    }

    node* p = pp->p_head;
    pp->p_head = pp->p_tail;
    pp->p_tail = p;
}

void print_ll(linked_list* pp){
    assert(pp != NULL);
    node* p_head = pp->p_head;
    while(p_head){
        printf("%i\n", p_head->value);
        p_head = p_head->p_next;
    }
}

int main() {

    FILE* filePointer;
    linked_list ll;
    ll.p_head = NULL;
    ll.p_tail = NULL;
    int bufferLength = 64;
    char buffer[bufferLength];
    printf("Loading data from file\n");


    clock_t timer1 = clo55ck();
    filePointer = fopen("data.txt", "r");
    while(fgets(buffer, bufferLength, filePointer)) {
        push_end(&ll, atoi(buffer));
    }
    fclose(filePointer);
    timer1 = clock() - timer1;
    printf("reading from file took %f seconds to execute \n\n", ((double)timer1)/CLOCKS_PER_SEC);

    printf("Reversing\n");
    //print_ll(&ll);
    clock_t timer = clock();
    reverse_ll(&ll);
    timer = clock() - timer;
    double time_taken = ((double)timer)/CLOCKS_PER_SEC; // in seconds
    printf("reverse_ll took %f seconds to execute \n", time_taken);

    printf("Done..\n");
}

