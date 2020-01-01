package queue

import "errors"

// Queue is a generic FIFO data structure
type Queue struct {
	items []interface{}
}

// NewQueue creates a new new queue and returns a pointer to it
func NewQueue() *Queue {
	return &Queue{}
}

// Put inserts n... items into the queue, returning # of items in queue
func (q *Queue) Put(items ...interface{}) int {
	q.items = append(q.items, items...)
	return q.Len()
}

// Get retrieves the first item from the queue, error if empty queue
func (q *Queue) Get() (interface{}, error) {
	if q.IsEmpty() {
		return nil, errors.New("queue: Get() from empty queue")
	}

	item := q.items[0]
	q.items = q.items[1:]
	return item, nil
}

// Peek looks at the first item in the queue, returning false if no items
func (q *Queue) Peek() (interface{}, bool) {
	if q.IsEmpty() {
		return nil, false
	}

	return q.items[0], true
}

// IsEmpty checks to see if the queue is empty
func (q *Queue) IsEmpty() bool {
	return q.Len() == 0
}

// Len gets the length of the queue
func (q *Queue) Len() int {
	return len(q.items)
}
