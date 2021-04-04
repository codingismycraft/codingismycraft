#include <assert.h>
#include <dirent.h>
#include <stdio.h>
#include <string.h>
#include <time.h>


#define FALSE 0
#define TRUE 1
#define MAX_STRING_SIZE 100
#define MAX_HEAP_SIZE 1024
#define SORTED_FILES_PATH "/home/john/repos/codingismycraft/algorithms/sorting_large_file/sorted_files"
#define OUTPUT_FILE "/home/john/repos/codingismycraft/algorithms/sorting_large_file/solution/sorted_using_c.txt"

typedef struct FileWrapper_ {
    FILE *fp;
    char current_line[MAX_STRING_SIZE];
    int reached_end;
} FileWrapper;

FileWrapper FILE_WRAPPER_POOL[MAX_HEAP_SIZE];

FileWrapper *HEAP[MAX_HEAP_SIZE];
int heap_size = 0;

void push(FileWrapper *fw);
int starts_with(const char *a, const char *b);

void file_wrapper_init(FileWrapper *pfw, const char *pszFilename) {
    pfw->fp = fopen(pszFilename, "r");
    assert(pfw->fp != NULL);
    pfw->reached_end = (fgets(pfw->current_line, MAX_STRING_SIZE, pfw->fp) == NULL);
    if (!pfw->reached_end)
        pfw->current_line[strcspn(pfw->current_line, "\n")] = 0;

}

int file_wrapper_read_next_line(FileWrapper *pfw) {
    if (pfw->reached_end)
        return FALSE;
    pfw->reached_end = (fgets(pfw->current_line, MAX_STRING_SIZE, pfw->fp) == NULL);
    if (!pfw->reached_end){
        pfw->current_line[strcspn(pfw->current_line, "\n")] = 0;
        return TRUE;
    }
    return FALSE;
}

void heap_populate() {
    DIR *d;
    struct dirent *dir;
    char buffer[1024];
    d = opendir(SORTED_FILES_PATH);
    heap_size = 0;
    int wrapper_pool_size = 0;
    if (d) {
        while ((dir = readdir(d)) != NULL) {
            if (starts_with(dir->d_name, "sorted_")) {
                strcpy(buffer, SORTED_FILES_PATH);
                strcat(buffer, "/");
                strcat(buffer, dir->d_name);
                FileWrapper *pfw = &FILE_WRAPPER_POOL[wrapper_pool_size++];
                file_wrapper_init(pfw, buffer);
                push(pfw);
            }
        }
        closedir(d);
    }
}

int get_parent_index(int index) {
    if (index <= 0)
        return -1;
    else if (index % 2 == 0) {
        return index / 2 - 1;
    } else {
        return index / 2;
    }
}

inline int get_left_index(int index) {
    return index * 2 + 1;
}

inline int get_right_index(int index) {
    return 2 * (index + 1);
}

void swap(int i1, int i2) {
    FileWrapper *temp = HEAP[i1];
    HEAP[i1] = HEAP[i2];
    HEAP[i2] = temp;
}

FileWrapper *pop() {
    int left_index = 0;
    int right_index = 0;
    int current_index = 0;
    int index_to_check = 0;

    if (heap_size <= 0)
        return NULL;

    FileWrapper *p_return_value = HEAP[0];

    if (heap_size <= 1) {
        --heap_size;
        return p_return_value;
    }
    swap(0, heap_size - 1);

    --heap_size;
    current_index = 0;

    for (;;) {
        left_index = get_left_index(current_index);

        if (left_index >= heap_size)
            return p_return_value;

        right_index = get_right_index(current_index);

        if (right_index >= heap_size) {
            index_to_check = left_index;
        } else {
            if (strcmp(HEAP[left_index]->current_line, HEAP[right_index]->current_line) < 0) {
                index_to_check = left_index;
            } else {
                index_to_check = right_index;
            }
        }
        if (strcmp(HEAP[current_index]->current_line, HEAP[index_to_check]->current_line) < 0) {
            return p_return_value;
        }
        swap(current_index, index_to_check);
        current_index = index_to_check;
    }
}

void push(FileWrapper *p_fw) {
    int this_index, parent_index;
    HEAP[heap_size] = p_fw;
    ++heap_size;
    this_index = heap_size - 1;
    for (;;) {
        parent_index = get_parent_index(this_index);
        if (parent_index < 0)
            return;
        if (strcmp(HEAP[parent_index]->current_line, HEAP[this_index]->current_line) <= 0)
            return;
        swap(parent_index, this_index);
        this_index = parent_index;
    }
}

int starts_with(const char *a, const char *b) {
    if (strncmp(a, b, strlen(b)) == 0)
        return 1;
    return 0;
}

int main() {
    heap_populate();
    FILE* fp = fopen(OUTPUT_FILE, "w");
    FileWrapper *p_fw;
    int counter = 0;
    time_t started = time(0);

    while ((p_fw = pop()) != NULL) {
        fprintf (fp, "%s\n", p_fw->current_line);
        ++counter;
        if (counter % 100000 == 0){
            printf("%d\n", counter);
        }
        if (file_wrapper_read_next_line(p_fw)) {
            push(p_fw);
        }
    }
    time_t finished = time(0);
    double seconds=difftime(finished,started);
    printf("Duration: %f\n" , seconds);

    return 0;
}
