queue1 = []
queue2 = []

n = int(input("Enter number of elements in Queue 1: "))

for i in range(n):
    value = int(input("Enter element: "))
    queue1.append(value)

m = int(input("Enter number of elements in Queue 2: "))

for i in range(m):
    value = int(input("Enter element: "))
    queue2.append(value)

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        queue1.append(value)
        print("Element inserted successfully")

    elif choice == 2:
        if len(queue1) == 0:
            print("Queue is empty")
        else:
            print("Deleted element:", queue1.pop(0))

    elif choice == 3:
        print("Queue 1:", queue1)
        print("Queue 2:", queue2)

    elif choice == 4:
        if len(queue1) == 0:
            print("Queue is empty")
        else:
            stack = []

            while len(queue1) > 0:
                stack.append(queue1.pop(0))

            while len(stack) > 0:
                queue1.append(stack.pop())

            print("Reversed Queue:", queue1)

    elif choice == 5:
        merged_queue = queue1 + queue2
        print("Merged Queue:", merged_queue)

    elif choice == 6:
        if queue1 == queue2:
            print("Both queues are identical")
        else:
            print("Queues are not identical")

    elif choice == 7:
        print("Program ended")
        break

    else:
        print("Invalid choice")

        